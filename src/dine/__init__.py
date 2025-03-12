"""
DINE - A Python client for the Spanish National Statistics Institute (INE) API.
"""

import threading
from typing import Any, Dict, List, Optional

from .api import INEClient

# Create a global client instance with thread-local storage
_thread_local = threading.local()


def _get_client() -> INEClient:
    """Get or create a thread-local client instance."""
    if not hasattr(_thread_local, "client"):
        _thread_local.client = INEClient()
    return _thread_local.client


# Expose the client methods at the module level
def get_table_info(table_id: str) -> Dict:
    """Get information about a specific table."""
    return _get_client().get_table_info(table_id)


def list_operations() -> List[Dict]:
    """List all available operations."""
    return _get_client().list_operations()


def get_operation(operation_id: str) -> Dict:
    """Get details for a specific operation."""
    return _get_client().get_operation(operation_id)


def list_tables_by_operation(operation_id: str) -> List[Dict]:
    """List all tables for a specific operation."""
    return _get_client().list_tables_by_operation(operation_id)


def list_all_tables() -> List[Dict]:
    """
    List all available tables in the INE, iterating through all operations.

    Returns:
        List of dictionaries with information about all tables
    """
    return _get_client().list_all_tables()


def download_table(table_id: str, output_path: Optional[str] = None) -> str:
    """
    Download a table from INE by its ID and save it in Parquet format.

    Args:
        table_id: ID of the table to download
        output_path: Output path to save the data. If not provided,
                    it's saved in the current directory with the table ID as name.

    Returns:
        Path where the data was saved
    """
    return _get_client().download_table(table_id, output_path)


# Also expose the client class for advanced usage
__all__ = [
    "INEClient",
    "get_table_info",
    "list_operations",
    "get_operation",
    "list_tables_by_operation",
    "list_all_tables",
    "download_table",
]
