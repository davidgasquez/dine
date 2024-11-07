# DINE 🦕

Exportando todas las tablas del [Instituto Nacional de Estadística](https://www.ine.es/) a un formato más amigable y eficiente.

## 🚀 Instalación

El proyecto require tener instalado `uv` y `aria2`. Una vez instalados, ejecutar el siguiente comando para crear el entorno virtual y descargar las dependencias necesarias.

```bash
make setup
```

## 📦 Uso

Lo único que se necesita hacer es ejecutar el notebook `ine.ipynb`! Este se encargará de descargar todos los archivos necesarios, exportarlos a Parquet y generar un README.md con los metadatos de cada tabla.

Tambien hay una linea de comandos para descargar tablas específicas.

```bash
uv run "https://raw.githubusercontent.com/davidgasquez/dine/refs/heads/main/dine.py" info 2056
uv run "https://raw.githubusercontent.com/davidgasquez/dine/refs/heads/main/dine.py" download 2056 -f parquet
```

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
