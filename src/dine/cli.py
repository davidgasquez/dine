import json
from typing import Optional

import typer

import dine

app = typer.Typer(
    name="dine",
    help="Exportando datos del Instituto Nacional de Estadística de España",
    add_completion=False,
)


operations_app = typer.Typer(help="Gestión de operaciones estadísticas")
app.add_typer(operations_app, name="operations")


@operations_app.command("list")
def list_operations():
    """
    List all available operations.
    """
    operations = dine.list_operations()
    formatted_operations = json.dumps(operations)
    typer.echo(formatted_operations)


@operations_app.command("get")
def get_operation(id: str = typer.Argument(..., help="ID de la operación estadística")):
    """
    Get detailed information about a statistical operation by its ID.
    """
    operation = dine.get_operation(id)
    formatted_operation = json.dumps(operation)
    typer.echo(formatted_operation)


# Add tables section
tables_app = typer.Typer(help="Gestión de tablas estadísticas")
app.add_typer(tables_app, name="tables")


@tables_app.command("list")
def list_tables(
    operation_id: Optional[str] = typer.Option(
        None,
        "--operation",
        "-op",
        help="ID de la operación estadística para filtrar tablas",
    ),
):
    """
    List all available statistical tables.

    By default, lists all tables from all operations.
    If an operation ID is provided, only shows tables from that operation.
    """
    if operation_id:
        tables = dine.list_tables_by_operation(operation_id)
        formatted_tables = json.dumps(tables)
        typer.echo(formatted_tables)
    else:
        tables = dine.list_all_tables()
        formatted_tables = json.dumps(tables)
        typer.echo(formatted_tables)


@tables_app.command("download")
def download_table(
    id: str = typer.Argument(..., help="ID de la tabla a descargar"),
    output: Optional[str] = typer.Option(
        None, "--output", "-o", help="Ruta de salida para guardar los datos"
    ),
):
    """
    Download a table from INE by its ID and save it in Parquet format.
    """
    try:
        output_path = dine.download_table(id, output)
        typer.echo(f"Tabla descargada y guardada en: {output_path}")
    except Exception as e:
        typer.echo(f"Error al descargar la tabla: {str(e)}", err=True)
        raise typer.Exit(code=1)


@tables_app.command("info")
def get_table_info(
    id: str = typer.Argument(..., help="ID de la tabla a obtener información"),
):
    """
    Get detailed information about a table by its ID.
    """
    table_info = dine.get_table_info(id)
    formatted_info = json.dumps(table_info)
    typer.echo(formatted_info)


@app.command()
def operations():
    """
    List all available operations.
    """
    operations = dine.list_operations()
    formatted_operations = json.dumps(operations)
    typer.echo(formatted_operations)


if __name__ == "__main__":
    app()
