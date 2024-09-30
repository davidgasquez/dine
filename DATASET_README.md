---
license: mit
language:
- es
pretty_name: INE
configs:
- config_name: default
  data_files:
    - split: tablas
      path: tablas.jsonl
  default: true
---

# INE

Este repositorio contiene todas las tablas¹ del [Instituto Nacional de Estadística](https://www.ine.es/) exportadas a ficheros Parquet.

Puedes encontrar los datos de las tablas como sus metadatos en la carpeta `tablas`. Cada dataset está identificado un una ID.  Puedes encontrar el ID en la URL de la tabla en la web del INE (es el número que aparece en la URL) or en el archivo `tablas.parquet` de este repositorio.

Por ejemplo, la tabla de [_Índices nacionales de clases_](https://www.ine.es/jaxiT3/Tabla.htm?t=50904&L=0) se corresponde al ID `50904` (en la URL) está en [`tablas/50904/datos.parquet`](https://huggingface.co/datasets/davidgasquez/ine/blob/main/tablas/50904/datos.parquet).

Puedes ejecutar queries SQL en los archivos remotos fácilmente en cualquier shell DuckDB ([demo](https://shell.duckdb.org/#queries=v0,select-*-from-'https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fdavidgasquez%2Fine%2Fresolve%2Fmain%2Ftablas%2F50904%2Fdatos.parquet'-limit-10~)):

```sql
select
  *
from 'https://huggingface.co/datasets/davidgasquez/ine/resolve/main/tablas/50904/datos.parquet' limit 10;
```

¹ [El manual oficial del INE](https://www.ine.es/dyngs/DataLab/manual.html?cid=64) define una tabla como "el resultado del cruce de grupos de valores contenidos en una o varias variables, es decir, son una agrupación de series temporales definidas por estos grupos". Una tabla se puede entender como un DataFrame, una hoja de cálculos, un fichero CSV, ...
