# /// script
# dependencies = [
#   "polars",
#   "httpx",
#   "tqdm",
#   "asyncio"
# ]
# ///

import argparse
import asyncio
import json
import sys
import textwrap
from io import StringIO
from pathlib import Path

import httpx
import polars as pl
from tqdm import tqdm

BASE_URL = "https://servicios.ine.es"
CSV_URL = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/{table_id}.csv"


async def get_table_info(client, table_id):
    """Get metadata about a specific table from INE API"""
    url = f"{BASE_URL}/wstempus/js/ES/DATOS_TABLA/{table_id}?tip=AM"
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching table info: {e}", file=sys.stderr)
        sys.exit(1)


async def download_table(client, table_id, output_path=None, output_format="csv"):
    """Download a table from INE and optionally convert to different formats"""
    url = CSV_URL.format(table_id=table_id)

    try:
        # Download CSV data
        response = await client.get(url)
        response.raise_for_status()

        # If no output path specified, use table_id as filename
        if output_path is None:
            output_path = f"{table_id}.{output_format}"

        # Ensure the output directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        if output_format == "csv":
            # Direct CSV save
            with open(output_path, "wb") as f:
                f.write(response.content)
        else:
            # For other formats, we need to load into Polars first
            csv_data = StringIO(response.content.decode("utf-8"))
            df = pl.read_csv(
                csv_data,
                truncate_ragged_lines=True,
                separator=";",
                infer_schema_length=None,
                ignore_errors=True,
            )

            if output_format == "parquet":
                df.write_parquet(output_path)
            else:
                raise ValueError(f"Unsupported output format: {output_format}")

        print(f"Table {table_id} downloaded to {output_path}")

    except httpx.HTTPError as e:
        print(f"Error downloading table: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing data: {e}", file=sys.stderr)
        sys.exit(1)


async def get_available_operations(client):
    """Get list of all available statistical operations from INE"""
    url = f"{BASE_URL}/wstempus/js/ES/OPERACIONES_DISPONIBLES"
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching operations: {e}", file=sys.stderr)
        sys.exit(1)


async def get_operation_tables(client, operation_id):
    """Get all tables for a given operation"""
    url = f"{BASE_URL}/wstempus/js/ES/TABLAS_OPERACION/{operation_id}"
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        print(
            f"Error fetching tables for operation {operation_id}: {e}", file=sys.stderr
        )
        return []


async def download_table_data(client, table_id, output_dir, skip_existing=False):
    """Download table data and save as parquet"""
    url = CSV_URL.format(table_id=table_id)
    output_path = output_dir / "datos.parquet"

    # Check if file exists and skip if requested
    if skip_existing and output_path.exists():
        return

    try:
        response = await client.get(url)
        response.raise_for_status()

        # Read CSV into Polars DataFrame
        csv_data = StringIO(response.content.decode("utf-8"))
        df = pl.read_csv(
            csv_data,
            separator=";",
            truncate_ragged_lines=True,
            infer_schema_length=None,
            ignore_errors=True,
        )

        # Save as parquet
        df.write_parquet(output_path, compression="zstd")

    except httpx.HTTPError as e:
        print(f"Error downloading table {table_id}: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error processing table {table_id}: {e}", file=sys.stderr)


async def process_tables(client, tables, output_dir, skip_existing):
    """Process tables concurrently"""
    semaphore = asyncio.Semaphore(10)  # Limit concurrent downloads

    async def process_table(table):
        async with semaphore:
            table_id = str(table["Id"])
            table_dir = output_dir / table_id
            table_dir.mkdir(parents=True, exist_ok=True)

            # Save metadata
            metadata_path = table_dir / "metadata.json"
            if not skip_existing or not metadata_path.exists():
                with open(metadata_path, "w", encoding="utf-8") as f:
                    json.dump(table, f, ensure_ascii=False, indent=2)

            # Download and save table data
            await download_table_data(client, table_id, table_dir, skip_existing)

    tasks = [process_table(table) for table in tables]
    for task in tqdm(
        asyncio.as_completed(tasks), total=len(tasks), desc="Downloading tables"
    ):
        await task


async def async_info_command(args):
    """Handle the info subcommand"""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        info = await get_table_info(client, args.table_id)
        print(json.dumps(info, indent=2, ensure_ascii=False))


async def async_download_command(args):
    """Handle the download subcommand"""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        await download_table(client, args.table_id, args.output, args.format)


async def async_export_command(args):
    """Handle the export subcommand"""
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
        print("Fetching available operations...")
        operations = await get_available_operations(client)

        # Get all tables from all operations
        tables = []
        print("Fetching tables from operations...")
        for op in tqdm(operations):
            op_tables = await get_operation_tables(client, op["Id"])
            tables.extend(op_tables)

        print(f"Found {len(tables)} tables")
        await process_tables(client, tables, output_dir, args.skip_existing)


def show_help():
    """Show detailed help information about the tool"""
    help_text = """
    dine - Download datasets from INE (Spanish Statistical Office)

    Commands:
      info TABLE_ID        Get detailed information about a specific table
      download TABLE_ID    Download a specific table
      export              Export all available tables from INE
      help                Show this help message

    Examples:
      # Get information about table 6146
      dine info 6146

      # Download table 6146 as CSV
      dine download 6146

      # Download table 6146 as Parquet
      dine download 6146 -f parquet -o output.parquet

      # Export all tables to a directory
      dine export -o ine_data

    For more information about a specific command, use:
      dine COMMAND --help
    """
    print(textwrap.dedent(help_text))


def main():
    parser = argparse.ArgumentParser(
        description="Download datasets from INE (Spanish Statistical Office)",
        add_help=False,  # Disable default help to use our custom help
    )
    subparsers = parser.add_subparsers(dest="command")

    # Info command
    info_parser = subparsers.add_parser(
        "info", help="Get detailed information about a specific table"
    )
    info_parser.add_argument("table_id", help="INE table identifier")

    # Download command
    download_parser = subparsers.add_parser(
        "download", help="Download a specific table"
    )
    download_parser.add_argument("table_id", help="INE table identifier")
    download_parser.add_argument("-o", "--output", help="Output file path")
    download_parser.add_argument(
        "-f",
        "--format",
        choices=["csv", "parquet"],
        default="csv",
        help="Output format (default: csv)",
    )

    # Export command
    export_parser = subparsers.add_parser(
        "export", help="Export all available tables from INE"
    )
    export_parser.add_argument(
        "-o", "--output-dir", default="ine", help="Output directory (default: ine)"
    )
    export_parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip downloading tables that already exist",
    )

    try:
        args = parser.parse_args()

        if not args.command or args.command == "help":
            show_help()
            return

        if args.command == "info":
            asyncio.run(async_info_command(args))
        elif args.command == "download":
            asyncio.run(async_download_command(args))
        elif args.command == "export":
            asyncio.run(async_export_command(args))
    except Exception as e:
        print(f"\nError: {str(e)}\n", file=sys.stderr)
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
