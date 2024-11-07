# Definición de URLs

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=47

A continuación se describe la construcción de peticiones URL:

**https://servicios.ine.es/wstempus/js/{idioma}/{función}/{input}\[?parámetros\]**

Los campos que aparecen entre llaves, { }, son obligatorios.

Los campos que aparecen entre corchetes, \[ \], son opcionales y cambian en relación a la función considerada.

Descripción de cada uno de ellos.

{idioma}

Puede tomar los siguientes valores:

*   **ES**: español
*   **EN**: inglés

{función}

Funciones implementadas en el sistema para poder realizar diferentes tipos de consulta en función del tipo de fuente, Tempus3 o PcAxis, y del elemento que se quiere obtener. Para más información, consultar las secciones ["Petición de metadatos"](https://www.ine.es/dyngs/DataLab/manual.html?cid=48 "Enlace petición de metadatos") y ["Petición de datos"](https://www.ine.es/dyngs/DataLab/manual.html?cid=49 "Enlace petición de datos").

**Funciones para la obtención de datos de Tempus3**

*   Operaciones: OPERACIONES\_DISPONIBLES, OPERACIÓN...
*   Variables: VARIABLES, VARIABLES\_OPERACION...
*   Valores: VALORES\_VARIABLES, VALORES\_VARIABLEOPERACION...
*   Tablas: TABLAS\_OPERACION, GRUPOS\_TABLA...
*   Series: SERIE, SERIES\_OPERACION...
*   Publicaciones: PUBLICACIONES, PUBLICACIONES\_OPERACION...
*   Datos: DATOS\_SERIE, DATOS\_TABLA...

**Función para la obtención de datos del repositorio de ficheros PcAxis**: Al ser Pc-Axis un formato para difundir tablas estadísticas, la única función implementada es la siguiente:

*   Datos: **DATOS\_TABLA**

{inputs}

Identificadores de los elementos de entrada de las funciones. Estos inputs varían en base a la función utilizada. Algunos ejemplos:

*   **Funciones**: OPERACION, VARIABLES\_OPERACION,TABLAS\_OPERACION... **Parámetro**: código de identificación de una operación estadística.
*   **Funciones**: SERIE, DATOS\_SERIE. **Parámetro**: identificador de la serie.
*   **Función**: DATOS\_TABLA. **Parámetro**: identificador de la tabla.

Para obtener información más detallada de los parámetros empleados en cada función, consultar las secciones consultar las secciones ["Petición de metadatos"](https://www.ine.es/dyngs/DataLab/manual.html?cid=48 "Enlace petición de metadatos") y ["Petición de datos"](https://www.ine.es/dyngs/DataLab/manual.html?cid=49 "Enlace petición de datos").

\[?parámetros\]

Los parámetros en la URL se establecen a partir del símbolo **?**

Cuando haya más de un parámetro, el símbolo **&** se utiliza como separador.

No todas las funciones admiten todos los parámetros posibles. A continuación se detallan los parámetros disponibles según su carácter:

**Parámetros comunes a todas las funciones.**

*   **page**: Debido al gran número de registros que pueden resultar de las consultas, es necesario ofrecer la respuesta paginada. Se ofrece un máximo de 500 elementos por página para no ralentizar la respuesta. Para consultar las páginas siguientes, se utiliza el parámetro page.
    _Ejemplo:_  [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=2](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=2)
*   **download=nombre\_del\_fichero.json**: Cualquier petición puede descargarse en un fichero plano con extensión .json
    _Ejemplo:_ [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?nult=1&download=MiDescarga.json](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=1&download=MiDescarga.json)
    _Ejemplo:_ [https://servicios.ine.es/wstempus/jsstat/ES/DATASET/23256?download=MiDescarga.json](https://servicios.ine.es/wstempus/jsstat/ES/DATASET/23256?download=MiDescarga.json)
*   ****det**** (sólo para Tempus3): Ofrece mayor nivel de detalle de la información mostrada. Da acceso a los atributos de la consulta que son a su vez elementos de la base de datos Tempus3.
    _Ejemplo:_  [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?nult=1&det=1](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=1&det=1)
    _Ejemplo:_  [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?nult=1&det=2](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=1&det=2)
*   ****tip****: Ofrece la posibilidad de obtener la respuesta de las peticiones de modo más amigable y con los metadatos, información adicional que mejora la comprensión de la misma.

    *   **tip=A**: Tipo amigable. Sólo disponible para Tempus3.
    *   **tip=M**: Tipo metadatos. Sólo para peticiones de datos.
    *   **tip=AM:** Tipo amigable y metadatos.

    _Ejemplo:_ [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?tip=AM&date=20110501:](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?tip=AM&date=20110501:)
    _Ejemplo:_ [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t22/p133/cno11/serie/l0/01003.px?tip=M&nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t22/p133/cno11/serie/l0/01003.px?tip=M&nult=1)

**Parámetros para la petición de datos.**

*   ****date****: Permite filtrar datos por fecha según diferentes opciones:
    *   **date=YYYYMMDD**: Fecha concreta.
    *   **date=YYYYMMDD&date=YYYYMMDD**: Lista de fechas concretas:
    *   **date=YYYYMMDD:YYYYMMDD**: Rango de fechas, permite omitir tanto la Fecha Inicio como la Fecha Fin.
        _Ejemplo:_ [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?date=20110501:](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?date=20110501:)
*   ****nult****:  Devuelve los _n_ últimos datos.
    _Ejemplo:_ https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t26/p067/p01/serie/l0/01004a.px?nult=4

**Parámetros para la obtención de datos y metadatos en base al ámbito geográfico.**

*   ****geo****:  para obtener resultados en función del ámbito geográfico.

    *   **geo=1**: Resultados por comunidades autónomas, provincias, municipios y otras desagregaciones.
    *   **geo=0**: Resultados nacionales: geo=0

    _Ejemplo_:  [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES?geo=1](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES?geo=1 "Enlace a OPERACIONES DISPONIBLES con desagregación geográfica. Abre ventana nueva")
    _Ejemplo_:  [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC?geo=0](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC?geo=0 "Enlace a TABLAS POR OPERACIÓN a nivel Nacional. Abre ventana nueva")
