# DINE 🦕

Librería y línea de comandos para explorar y exportar datos del [Instituto Nacional de Estadística](https://www.ine.es/).

## 🔍 Recursos

- [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099) - API JSON de INE
- [Tablas INE](https://www.ine.es/dyngs/INEbase/listaoperaciones.htm) - Listado de operaciones estadísticas
- [Microdatos INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176918&menu=resultados&idp=1254735976595) - Acceso a microdatos de encuestas
- [API INE](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945948443) - Documentación de la API
- [Tempus3](https://www.ine.es/dyngs/IOE/es/operacion.htm?numinv=30714) - Sistema de difusión de información estadística

Puedes explorar la documentación de la API en Markdown en la carpeta [docs](docs).

## 🚀 Instalación

Puedes instalar la librería `dine` usando `uv` o `pip`.

```bash
pip install dine
```

```bash
uv add dine
```

Para instalar `dine` en el sistema de manera aislada, puedes hacerlo con:

```bash
uv tool install dine
```

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
