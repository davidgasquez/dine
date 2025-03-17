# DINE 🦕

Pequeña librería y línea de comandos para explorar y exportar datos del [Instituto Nacional de Estadística](https://www.ine.es/).

## 🚀 Instalación

Puedes instalar la librería `dine` usando `uv` (recomendado) o `pip`.

```bash
# Usando uv
uv pip install dine

# Usando pip
pip install dine
```

Puedes tambien instalar `dine` en el sistema de manera aislada con:

```bash
uv tool install dine
```

O, alternativamente, ejecutar los comandos "sin instalación" usando  `uvx` (e.g: `uvx):

```bash
uvx dine --help
```

Es la forma más fácil de empezar a usar el proyecto!

## 🛠️ Uso

La librería `dine` proporciona una interfaz de línea de comandos para interactuar con los datos del INE.

### Operaciones Estadísticas

Listar todas las operaciones estadísticas disponibles:

```bash
dine operations list
```

Obtener información detallada sobre una operación específica:

```bash
dine operations get <ID_OPERACION>
```

### Tablas Estadísticas

Listar todas las tablas estadísticas disponibles:

```bash
dine tables list
```

Listar tablas de una operación específica:

```bash
dine tables list --operation <ID_OPERACION>
```

Obtener información detallada sobre una tabla específica:

```bash
dine tables info <ID_TABLA>
```

Descargar una tabla y guardarla en formato Parquet:

```bash
dine tables download <ID_TABLA>
```

Especificar una ruta de salida personalizada:

```bash
dine tables download <ID_TABLA> --output ruta/personalizada.parquet
```

### Uso desde Python

También puedes usar DINE directamente desde Python:

```python
import dine

# Listar operaciones
operaciones = dine.list_operations()

# Obtener información de una operación
operacion = dine.get_operation("ID_OPERACION")

# Listar tablas
tablas = dine.list_all_tables()
tablas_por_operacion = dine.list_tables_by_operation("ID_OPERACION")

# Obtener información de una tabla
info_tabla = dine.get_table_info("ID_TABLA")

# Descargar una tabla
ruta_salida = dine.download_table("ID_TABLA", "ruta/salida.parquet")
```

## 🔧 Desarrollo

Para contribuir al proyecto, se puede usar el siguiente comando para instalar las dependencias necesarias y ejecutar el proyecto.

```bash
make install
```

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
