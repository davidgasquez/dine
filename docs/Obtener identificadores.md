# Obtener identificadores de objetos utilizando INEbase

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=1259945947403

Navegando a través de [INEbase](https://www.ine.es/inebmenu/indice.htm "Enlace a INEbase. Abre ventana nueva") se pueden obtener los IDs que identifican de manera única a los elemnto de entrada de las funciones, [{input}](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=47 "Enlace a definición de URLs"):

Obtención del identificador de una tabla utilizando INEbase

Navegando a través de INEbase, se acceden a las tablas estadísticas. Se dintinguen los identificadores en base a la fuente de procedencia de las mismas.

**Tablas Tempus3**

*   **Tabla** [Índices por comunidades autónomas de subgrupos](https://www.ine.es/jaxiT3/Tabla.htm?t=22351 "Enlace a la tabla Índices por comunidades autónomas de subgrupos").
*   **Enlace**: https://www.ine.es/jaxiT3/Tabla.htm?t=22351
*   **Identificador**: el parámetro _t_ de la URL: _**22351**_

[![Image 1: Identificador de una tabla Tempus3](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/tabla_jss_tempus3.jpg)](https://www.ine.es/jaxiT3/Tabla.htm?t=22351)

**Tablas del repositorio de ficheros PC-Axis**

*   **Tabla**: [Población (españoles/extranjeros) por edad (3 grupos de edad), sexo y año](https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01001.px&L=0 "Enlace a la tabla Población (españoles/extranjeros) por edad (3 grupos de edad), sexo y año").
*   **Enlace**: https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01001.px
*   **Identificador**: concatenación de los parámetros _path_ (t20/e245/p08/l0/) y _file_ (01001.px) resultando _**t20/e245/p08/l0/01001.px**_

[![Image 2: Identificador de una tabla del repositorio PC-Axis](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/tabla_jss_pcaxis.jpg)](https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01001.px)

Obtención del identificador de una serie utilizando INEbase (sólo Tempus3)

Sólo se dispone de identificadores de series para aquella información cuya fuente de datos es Tempus3. Por tanto, lo que a continuación se cuenta sólo es aplicable a las tablas de Tempus3.

El identificador de una serie de Tempus3 se obtiene a través de las tablas de INEbase.

*   **Serie**: serie correspondiente a la variación mensual del Índice de Precios de Consumo de Alimentos en Cantabria.
*   **Tabla**: Navegar a la tabla que contiene la serie en la que se tiene interés: "Índices por comunidades autónomas de subgrupos"
*   **Enlace de la tabla**: [https://www.ine.es/jaxiT3/Tabla.htm?t=22351](https://www.ine.es/jaxiT3/Tabla.htm?t=22351)
*   **Procedimiento**: Hacer una selección de valores en la tabla y realizar la consulta.
    *   En la pantalla de tabla de datos, se puede acceder a la información de cada serie haciendo clic en la celda correspondiente. ![Image 3: Identificador de una serie Tempus3](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/ID_serie.jpg)

    *   En la ventana emergente aparece, entre otra información, el identificador de la serie asociada a la celda sobre la que se ha hecho clic.
*   **Identificador de la serie**: _**IPC212317**_. Éste se utilizará como parámetro de las funciones que hagan peticiones de información sobre series.
