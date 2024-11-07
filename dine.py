# /// script
# dependencies = [
#   "polars",
#   "requests",
# ]
# ///

import argparse
import sys
import requests
from pathlib import Path
import json
import polars as pl
from io import StringIO

BASE_URL = "https://servicios.ine.es"
CSV_URL = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/{table_id}.csv"


def get_table_info(table_id):
    """Get metadata about a specific table from INE API"""
    url = f"{BASE_URL}/wstempus/js/ES/DATOS_TABLA/{table_id}?tip=AM"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching table info: {e}", file=sys.stderr)
        sys.exit(1)


def download_table(table_id, output_path=None, output_format="csv"):
    """Download a table from INE and optionally convert to different formats"""
    url = CSV_URL.format(table_id=table_id)

    try:
        # Download CSV data
        response = requests.get(url)
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
            df = pl.read_csv(csv_data, truncate_ragged_lines=True, separator=";")

            if output_format == "parquet":
                df.write_parquet(output_path)
            else:
                raise ValueError(f"Unsupported output format: {output_format}")

        print(f"Table {table_id} downloaded to {output_path}")

    except requests.RequestException as e:
        print(f"Error downloading table: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing data: {e}", file=sys.stderr)
        sys.exit(1)


def info_command(args):
    """Handle the info subcommand"""
    info = get_table_info(args.table_id)
    print(json.dumps(info, indent=2, ensure_ascii=False))


def download_command(args):
    """Handle the download subcommand"""
    download_table(args.table_id, args.output, args.format)


def main():
    parser = argparse.ArgumentParser(
        description="Download datasets from INE (Spanish Statistical Office)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Info command
    info_parser = subparsers.add_parser("info", help="Get information about a table")
    info_parser.add_argument("table_id", help="INE table identifier")

    # Download command
    download_parser = subparsers.add_parser("download", help="Download a table")
    download_parser.add_argument("table_id", help="INE table identifier")
    download_parser.add_argument("-o", "--output", help="Output file path")
    download_parser.add_argument(
        "-f",
        "--format",
        choices=["csv", "parquet"],
        default="csv",
        help="Output format (default: csv)",
    )

    args = parser.parse_args()

    if args.command == "info":
        info_command(args)
    elif args.command == "download":
        download_command(args)


if __name__ == "__main__":
    main()
