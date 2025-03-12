from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
import polars as pl


class INEClient:
    """Client for interacting with the INE (Instituto Nacional de Estadística) API."""

    def __init__(
        self,
        timeout: int = 30,
        base_url: str = "https://servicios.ine.es/wstempus/js/ES",
    ):
        """
        Initialize the INE API client.

        Args:
            timeout: Request timeout in seconds
            base_url: Base URL for the INE API
        """
        self.base_url = base_url
        self.client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={"User-Agent": "dine-python-client/1.0"},
            limits=httpx.Limits(max_keepalive_connections=20),
            transport=httpx.HTTPTransport(retries=3),
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close the underlying HTTP client."""
        self.client.close()

    def _get(self, endpoint: str, paginate: bool = True) -> Any:
        """
        Make a GET request to the INE API.

        Args:
            endpoint: API endpoint to request
            paginate: Whether to paginate results (for endpoints that support it)

        Returns:
            Parsed JSON response
        """
        page = 1
        data = []

        while True:
            params = {"det": 10}

            if paginate:
                params["page"] = page

            url = f"{self.base_url}/{endpoint}"
            response = self.client.get(url, params=params)
            response.raise_for_status()

            response_data = response.json()

            if not response_data:
                break

            data.extend(response_data)

            # Stop if we got less than the max page size or pagination is disabled
            if len(response_data) < 500 or not paginate:
                break

            page += 1

        return data if paginate else response_data

    def get_table_info(self, table_id: str) -> Dict:
        """Get information about a specific table."""
        return self._get(f"DATOS_TABLA/{table_id}?tip=AM")

    def list_operations(self) -> List[Dict]:
        """List all available operations."""
        return self._get("OPERACIONES_DISPONIBLES")

    def get_operation(self, operation_id: str) -> Dict:
        """Get details for a specific operation."""
        return self._get(f"OPERACION/{operation_id}")

    def list_tables_by_operation(self, operation_id: str) -> List[Dict]:
        """List all tables for a specific operation."""
        return self._get(f"TABLAS_OPERACION/{operation_id}")

    def list_all_tables(self) -> List[Dict]:
        """
        List all available tables in the INE, iterating through all operations.

        Returns:
            List of dictionaries with information about all tables
        """
        # Get all operations
        operations = self.list_operations()

        # Initialize empty list for tables
        all_tables = []

        # Loop through operations and get tables for each
        for operation in operations:
            operation_id = operation.get("Id")
            if operation_id:
                try:
                    tables = self.list_tables_by_operation(operation_id)
                    # Add operation name to each table for reference
                    for table in tables:
                        table["operation_name"] = operation.get("Nombre", "")
                        table["operation_id"] = operation_id
                    all_tables.extend(tables)
                except Exception:
                    # Skip operations that fail
                    continue

        return all_tables

    def download_table(self, table_id: str, output_path: Optional[str] = None) -> str:
        """
        Download a table from INE by its ID and save it in Parquet format.

        Args:
            table_id: ID of the table to download
            output_path: Output path to save the data. If not provided,
                        it's saved in the current directory with the table ID as name.

        Returns:
            Path where the data was saved
        """
        # Get table data
        data = self._get(f"DATOS_TABLA/{table_id}")

        # Convert to DataFrame using polars
        df = pl.DataFrame(data)

        # Determine output path
        if output_path is None:
            output_path = f"{table_id}.parquet"
        else:
            # Ensure the path ends with .parquet
            if not output_path.endswith(".parquet"):
                output_path = f"{output_path}.parquet"

        # Create directory if it doesn't exist
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save as parquet
        df.write_parquet(output_path)

        return output_path
