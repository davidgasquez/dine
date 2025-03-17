API JSON / Referencia de la API
===============               

[![Image 1: SIGLAS Instituto Nacional de Estadística](https://www.ine.es/menus/_b/img/LogoINE.svg)](https://www.ine.es/)

*   [English](https://www.ine.es/dyngs/DAB/en/index.htm?cid=1100 "English Page")

   

[](https://www.ine.es/indiceweb.htm "Menú de navegación") ![Image 2: Instituto Nacional de EstadÃ­stica](https://www.ine.es/menus/_b/img/LogoINESiglasMini.svg)

*   [Censo Electoral](https://www.ine.es/dyngs/CEL/index.htm?cid=41)
*   [Sede electrónica](https://sede.ine.gob.es/ss/Satellite?c=Page&cid=1254734719723&pagename=SedeElectronica%2FSELayout&lang=es_ES)
*   [Compartir](javascript:void(0))
    *   [X](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareTwitter "Abre ventana nueva X")
    *   [Facebook](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareFacebook "Abre ventana nueva Facebook")
    *   [Linkedin](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareLinkedin "Abre ventana nueva Linkedin")
    *   [WhatsApp](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareWhatsapp "Abre ventana nueva WhatsApp")
    *   [Correo Electrónico](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareMail "Abre ventana nueva")
    *   [Copiar al portapapeles](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#shareClipboard "Abre ventana nueva")

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   Referencia de la API
    ====================
    

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   [Referencia de la API](https://www.ine.es/dyngs/DAB/index.htm?cid=1100)
*   [Lista de funciones](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128)
*   [Obtener datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102)
*   [Otros casos de uso](https://www.ine.es/dyngs/DAB/index.htm?cid=1103)
*   [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)
*   [Base de datos Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
*   [Generador de URLs](https://www.ine.es/dyngs/DAB/index.htm?cid=1347)
*   [Generador de gráficos](https://www.ine.es/dyngs/DAB/index.htm?cid=1348)

Referencia de la API
--------------------

Se accede a la información disponible en INEbase mediante peticiones URL. Las peticiones URL tienen la siguiente estructura:

**https://servicios.ine.es/wstempus/js/{idioma}/{función}/{input}\[?parámetros\]**

Los campos que aparecen entre llaves, { }, son obligatorios.  Los campos que aparecen entre corchetes, \[ \], son opcionales y cambian en relación a la función considerada.

*   **{idioma}**. Puede tomar los siguientes valores:
    *   ES: español.
    *   EN: inglés.
*   **{función}**. Funciones implementadas en el sistema para poder realizar diferentes tipos de consulta.
*   **{input}**. Identificadores de los elementos de entrada de las funciones. Estos inputs varían en base a la función utilizada.
*   **\[¿parámetros\]**. Los parámetros en la URL se establecen a partir del símbolo ?. Cuando haya más de un parámetro, el símbolo & se utiliza como separador. No todas las funciones admiten todos los parámetros posibles.

Lista de funciones
------------------

*   DATOS\_TABLA
    *   Obtener datos para una tabla específica.
        
    *   ### Input
        
        Código identificativo de la tabla. Para obtener el código de una tabla acceder a [Obtención del identificador de una tabla utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).
        
    *   ### Parámetros
        
        *   **nult**: devolver los n últimos datos o periodos.
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’), incluir metadatos (‘M’) o ambos (‘AM’)¨.
        *   **tv**: parámetro para filtrar, utilizado con el formato _tv=id\_variable:id\_valor_. Más información en [Como filtrar datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102).
    *   ### Salida
        
        Información y datos de las series contenidas en la tabla: nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato).
        
    *   ### Ejemplos
        
        *   Devuelve todos los periodos de la tabla con Id=50902
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902)
            
        *   Devuelve el último periodo de la tabla con Id=50902
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=1)
            
        *   Devuelve los últimos 5 periodos de la tabla con Id=50902
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=5)
            
        *   Devuelve el último periodo de la tabla con Id=50902 más salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=1&tip=A](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=1&tip=A)
            
        *   Devuelve el último periodo de la tabla con Id=50902 junto a los metadatos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=1&tip=M](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=1&tip=M)
            
        *   Devuelve el último periodo de la tabla con Id=50902 con salida amigable y metadatos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=1&tip=AM](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=1&tip=AM)
            
        *   Devuelve el último periodo de la tabla con Id=50902 y nivel de detalle 2
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=1&det=2](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=1&det=2)
            
*   DATOS\_SERIE
    *   Obtener datos para una serie específica.
        
    *   ### Input
        
        Código identificativo de la serie. Para obtener el código de una serie acceder a [Obtención del identificador de una serie utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104#is1131).
        
    *   ### Parámetros
        
        *   **nult**: devolver los n últimos datos o periodos.
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’), incluir metadatos (‘M’) o ambos (‘AM’)¨.
        *   **date**: obtener los datos entre dos fechas. El formato es date=aaaammdd:aaaammdd.
    *   ### Salida
        
        Información de la serie: nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato).
        
    *   ### Ejemplos
        
        *   Devuelve el último periodo de la serie con código IPC251856
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=1)
            
        *   Devuelve los últimos 5 periodos de la serie con código IPC251856
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=5)
            
        *   Devuelve el último periodo de la serie con código IPC251856 con salida amigable y metadatos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=1&tip=AM](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=1&tip=AM)
            
        *   Devuelve el último periodo de la serie con código IPC251856 y nivel de detalle 2
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=1&det=2](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=1&det=2)
            
        *   Devuelve los datos entre el 01/01/2023 y el 31/12/2023
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?date=20230101:20231231&tip=A](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?date=20230101:20231231&tip=A)
            
        *   Devuelve los datos a partir del 01/01/2024
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?date=20240101:&tip=A](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?date=20240101:&tip=A)
            
*   DATOS\_METADATAOPERACION
    *   Obtener datos de series pertenecientes a una operación dada utilizando un filtro.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **p**: id de la periodicidad de las series. Periodicidades comunes: 1 (mensual), 3 (trimestral), 6 (semestral), 12 (anual). Para ver una lista de las periodicidades acceder a [PERIODICIDADES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1158).
        *   **nult**: devolver los n últimos datos o periodos.
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’), incluir metadatos (‘M’) o ambos (‘AM’).
        *   **g1**: primer filtro de variables y valores. El formato es g1=id\_variable\_1:id\_valor\_1. Cuando no se especifica el id\_valor\_1 se devuelven todos los valores de id\_variable\_1 (g1=id\_variable\_1:). Para obtener las variables de una operación dada consultar [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC). Para obtener los valores de una variable específica de una operación data consultar [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/IPC](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/IPC).
        *   **g2**: segundo filtro de variables y valores. El formato es g2=id\_variable\_2:id\_valor\_2. Cuando no se especifica el id\_valor\_2 se devuelven todos los valores de id\_variable\_2 (g2=id\_variable\_2:). Seguiríamos con g3, g4,… según el número de filtros que se utilicen sobre variables.
    *   ### Ejemplos
        
        *   Devuelve el último periodo de las series de la operación del IPC referentes a la provincia de Madrid (g1=115:29) para la variación mensual (g2=3:84) y todos los grupos ECOICOP (g3=762:)
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1)
            
        *   Devuelve los últimos 5 periodos de las series de la operación del IPC referentes a la provincia de Madrid (g1=115:29) para la variación mensual (g2=3:84) y todos los grupos ECOICOP (g3=762:)
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=5)
            
        *   Consulta con salida amigable y metadatos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1&tip=AM](https://servicios.ine.es/wstempus/js/ES/DATOS_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1&tip=AM)
            
        *   Consulta con nivel de detalle 2
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1&det=2](https://servicios.ine.es/wstempus/js/ES/DATOS_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1&det=2)
            
*   OPERACIONES\_DISPONIBLES
    *   Obtener todas las operaciones disponibles.
        
    *   ### Input
        
        Ninguno.
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
        *   **geo**: para obtener resultados en función del ámbito geográfico:
            *   geo=1: resultados por comunidades autónomas, provincias, municipios y otras desagregaciones.
            *   geo=0: resultados nacionales.
        *   **page**: la respuesta está paginada. Se ofrece un máximo de 500 elementos por página para no ralentizar la respuesta. Para consultar las páginas siguientes, se utiliza el parámetro page.
    *   ### Salida
        
        Se obtienen los identificadores del elemento operación estadística. Existen tres códigos para la identificación de la operación estadística "Índice de Precios de Consumo (IPC)":
        
        *   código numérico Tempus3 interno (Id=25).
        *   código de la operación estadística en el Inventario de Operaciones Estadísticas (IOE30138).
        *   código alfabético Tempus3 interno (IPC).
    *   ### Ejemplos
        
        *   Devuelve las operaciones disponibles
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES)
            
        *   Devuelve todas las operaciones disponibles y nivel de detalle 2
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES?det=2](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES?det=2)
            
        *   Devuelve todas las operaciones disponibles que contengan desagregación geográfica (comunidades autónomas, provincias, municipios y otras desagregaciones)
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES?geo=1](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES?geo=1)
            
        *   Devuelve todas las operaciones disponibles que contengan solamente resultados nacionales
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES?geo=0](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES?geo=0)
            
        *   Devuelve las operaciones disponibles (primeros 500 resultados)
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES?page=1](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES?page=1)
            
*   OPERACION
    *   Obtener una operación.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
    *   ### Salida
        
        Información de la operación estadística IPC: identificador Tempus3, código del IOE y nombre de la operación. Existen tres códigos para la identificación de la operación estadística "Índice de Precios de Consumo (IPC)":
        
        *   código numérico Tempus3 interno (Id=25).
        *   código de la operación estadística en el Inventario de Operaciones Estadísticas (IOE30138).
        *   código alfabético Tempus3 interno (IPC).
    *   ### Ejemplos
        
        *   Devuelve la operación IPC utilizando el código alfabético Tempus3 interno (IPC)
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC)
            
        *   Devuelve la operación IPC utilizando el identificador interno Tempus 3 (id=25)
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACION/25](https://servicios.ine.es/wstempus/js/ES/OPERACION/25)
            
        *   Devuelve la operación IPC utilizando el código de la operación estadística en el Inventario de Operaciones Estadísticas (IOE30138)
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACION/IOE30138](https://servicios.ine.es/wstempus/js/ES/OPERACION/IOE30138)
            
        *   Devuelve la operación IPC y nivel de detalle 2
            
            [https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC?det=2](https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC?det=2)
            
*   VARIABLES
    *   Obtener todas las variables disponibles.
        
    *   ### Input
        
        Ninguno.
        
    *   ### Parámetros
        
        *   **page**: la respuesta está paginada. Se ofrece un máximo de 500 elementos por página para no ralentizar la respuesta. Para consultar las páginas siguientes, se utiliza el parámetro page.
    *   ### Salida
        
        Información de todas las variables del Sistema: identificador Tempus3, nombre de la variable y código oficial.
        
    *   ### Ejemplos
        
        *   Devuelve las variables disponibles (primeros 500 resultados)
            
            [https://servicios.ine.es/wstempus/js/ES/VARIABLES](https://servicios.ine.es/wstempus/js/ES/VARIABLES)
            
        *   Devuelve las variables disponibles (segundos 500 resultados)
            
            [https://servicios.ine.es/wstempus/js/ES/VARIABLES?page=2](https://servicios.ine.es/wstempus/js/ES/VARIABLES?page=2)
            
*   VARIABLES\_OPERACION
    *   Obtener todas las variables utilizadas en una operación dada.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **page**: la respuesta está paginada. Se ofrece un máximo de 500 elementos por página para no ralentizar la respuesta. Para consultar las páginas siguientes, se utiliza el parámetro page.
    *   ### Salida
        
        Información de las variables que describen la operación: identificador Tempus3, nombre de la variable y código oficial.
        
    *   ### Ejemplos
        
        *   Devuelve las variables de la operación IPC
            
            [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC)
            
        *   Devuelve las variables de la operación IPC (primeros 500 resultados). Consulta igual a la anterior
            
            [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC?page=1](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC?page=1)
            
*   VALORES\_VARIABLE
    *   Obtener todos los valores para una variable específica.
        
    *   ### Input
        
        Código identificador de la variable. Para consultar las variables disponibles acceder a [VARIABLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1145).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
    *   ### Salida
        
        Información de los valores que puede tomar la variable: identificador Tempus3 del valor, identificador Tempus 3 de la variable a la que pertenece, nombre del valor y código oficial.
        
    *   ### Ejemplos
        
        *   Devuelve los valores de la variable Provincias (Id=115)
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLE/115](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/115)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLE/115?det=2](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/115?det=2)
            
*   VALORES\_VARIABLEOPERACION
    *   Obtener todos los valores para una variable específica de una operación dada.
        
    *   ### Input
        
        Códigos identificadores de la variable y de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143) y para consultar las variables disponibles acceder a [VARIABLES\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1146).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
    *   ### Salida
        
        Información de los valores que puede tomar la variable para describir la operación: identificador Tempus3 del valor, objeto variable Tempus3 a la que pertenece, nombre del valor y código oficial.
        
    *   ### Ejemplos
        
        *   Valores de la variable "Grupos ECOICOP" (Id=762) para la operación IPC (IOE30138 / IPC / 25).
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/25](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/25)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/25?det=2](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/25?det=2)
            
*   TABLAS\_OPERACION
    *   Obtener un listado de todas las tablas de una operación.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
        *   **geo**: para obtener resultados en función del ámbito geográfico.
            *   geo=1: resultados por comunidades autónomas, provincias, municipios y otras desagregaciones.
            *   geo=0: Resultados nacionales.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (\`A’).
    *   ### Salida
        
        Información de las tablas asociadas a la operación: identificador Tempus3 de la tabla, nombre de la tabla, código con información del nivel geográfico y clasificación, objeto Tempus3 periodicidad, objeto Tempus3 publicación, objeto Tempus3 periodo inicio, año inicio, PubFechaAct dentro de la publicación , FechaRef\_fin y última modificación.
        
        FechaRef\_fin: nulo cuando el último periodo publicado coincide con el de la publicación fecha, en otro caso, cuando la tabla está cortada en un periodo anterior al de la publicación fecha, es sustituido por Fk\_perido\_fin/ Anyo\_perido\_fin (fecha del último dato publicado). Consultar [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/33](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/33).
        
        PubFechaAct = contiene la última fecha de actualización de la tabla y el último periodo-año publicado.
        
    *   ### Ejemplos
        
        *   Tablas estadísticas asociadas a la operación estadística IPC (IOE30138 / IPC / 25)
            
            [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC?det=2](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC?det=2)
            
        *   Salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC?det=2&tip=A)
            
        *   Tablas con contenido geográfico
            
            [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC?geo=1](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC?geo=1)
            
*   GRUPOS\_TABLA
    *   Obtener todos los grupos para una tabla específica. Una tabla está definida por diferentes grupos o combos de selección y cada uno de ellos por los valores que toman una o varias variables.
        
    *   ### Input
        
        Código identificativo de la tabla. Para obtener el código de una tabla acceder a [Obtención del identificador de una tabla utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).
        
    *   ### Parámetros
        
        Ninguno.
        
    *   ### Salida
        
        Grupos de valores que definen la tabla: identificador Tempus3 del grupo y nombre del grupo.
        
    *   ### Ejemplos
        
        *   Grupos o combos de selección que definen a la tabla [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913) (Id 50913)
            
            [https://servicios.ine.es/wstempus/js/ES/GRUPOS\_TABLA/50913](https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/50913)
            
*   VALORES\_GRUPOSTABLA
    *   Obtener todos los valores de un grupo específico para una tabla dada. Una tabla está definida por diferentes grupos o combos de selección y cada uno de ellos por los valores que toman una o varias variables.
        
    *   ### Input
        
        Códigos identificativos de la tabla y del grupo. Para consultar los grupos de una tabla acceder a [GRUPOS\_TABLA](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1150).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
    *   ### Salida
        
        Información de los valores pertenecientes al grupo: identificador Tempus3 del valor, identificador Tempus 3 de la variable a la que pertenece, nombre del valor y código oficial.
        
    *   ### Ejemplos
        
        *   Valores del grupo "Comunidades y Ciudades Autónomas" (Id=110924) perteneciente a la tabla tabla [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913) (Id 50913)
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110924](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110924)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110924?det=2](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110924?det=2)
            
*   SERIE
    *   Obtener una serie específica.
        
    *   ### Input
        
        Código identificativo de la serie. Para obtener el código de una serie acceder a [Obtención del identificador de una serie utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (\`A´), incluir metadatos (\`M´) o ambos (\`AM´).
    *   ### Salida
        
        Información de la serie: identificadores Tempus3 de la serie, objeto Tempus3 operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, objeto Tempus3 periodicidad, objeto Tempus3 publicación, PubFechaAct dentro de la publicación, objeto Tempsu3 clasificación, objeto Tempus3 escala y objeto Tempus3 unidad.
        
        PubFechaAct = contiene la última fecha de actualización de la serie y el último periodo-año publicado.
        
        clasificación = nos da información de la versión temporal de la serie, por ejemplo, la clasificación nacional que en algunos casos sigue, marco poblacional, base utilizada en el cálculo de los índices,...
        
    *   ### Ejemplos
        
        *   Consulta de la serie [IPC251852](https://www.ine.es/jaxiT3/Tabla.htm?t=50913) que recoge la variación mensual del Índice de precios de consumo
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2&tip=A)
            
        *   Consulta con metadatos y salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?tip=AM](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?tip=AM)
            
*   SERIES\_OPERACION
    *   Obtener todas las series de una operación.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (\`A´), incluir metadatos (\`M´) o ambos (\`AM´).
        *   **page**: la respuesta está paginada. Se ofrece un máximo de 500 elementos por página para no ralentizar la respuesta. Para consultar las páginas siguientes, se utiliza el parámetro page.
    *   ### Salida
        
        Información de las series: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad.
        
    *   ### Ejemplos
        
        *   Consulta de las primeras 500 series pertenecientes a la operación IPC (IOE30138 / IPC / 25)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1)
            
        *   Consulta de las segundas 500 series pertenecientes a la operación IPC (IOE30138 / IPC / 25)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=2](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=2)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1&det=2](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1&det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1&det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1&det=2&tip=A)
            
        *   Consulta con metadatos y salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1&tip=AM](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1&tip=AM)
            
*   VALORES\_SERIE
    *   Obtener los valores y variables que definen una serie.
        
    *   ### Input
        
        Código identificativo de la serie. Para obtener el código de una serie acceder a [Obtención del identificador de una serie utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
    *   ### Salida
        
        Información de los metadatos que definen a la serie: identificador Tempus3 del valor, identificador Tempus3 de la variable a la que pertenece, nombre del valor y código oficial del valor.
        
    *   ### Ejemplos
        
        *   Consulta de las variables y valores de la serie que recoge los datos del índice general el IPC ([IPC251852](https://www.ine.es/consul/serie.do?s=IPC251852))
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_SERIE/IPC251852](https://servicios.ine.es/wstempus/js/ES/VALORES_SERIE/IPC251852)
            
        *   Consulta con nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_SERIE/IPC251852?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_SERIE/IPC251852?det=1)
            
*   SERIES\_TABLA
    *   Obtener todas las series de una tabla específica.
        
    *   ### Input
        
        Código identificativo de la tabla. Para obtener el código de una tabla acceder a [Obtención del identificador de una tabla utilizando INEbase](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos del parámetro: 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (\`A´), incluir metadatos (\`M´) o ambos (\`AM´).
        *   **tv**: parámetro para filtrar, utilizado con el formato tv=id\_variable:id\_valor. Más información en [Como filtrar datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102).
    *   ### Salida
        
        Información de las series de la tabla: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad.
        
    *   ### Ejemplos
        
        *   Series que aparecen en la tabla [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Datos.htm?t=50913) de la operación IPC (Id 50913)
            
            [https://servicios.ine.es/wstempus/jsCache/ES/SERIES\_TABLA/50913](https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/50913)
            
        *   Consulta con nivel de detalle máximo
            
            [https://servicios.ine.es/wstempus/jsCache/ES/SERIES\_TABLA/50913?det=2](https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/50913?det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/jsCache/ES/SERIES\_TABLA/50913?det=2&tip=A](https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/50913?det=2&tip=A)
            
        *   Consulta de metadatos y salida amigable
            
            [https://servicios.ine.es/wstempus/jsCache/ES/SERIES\_TABLA/50913?tip=AM](https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/50913?tip=AM)
            
*   SERIE\_METADATAOPERACION
    *   Obtener series pertenecientes a una operación dada utilizando un filtro.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **p**: id de la periodicidad de las series. Periodicidades comunes: 1 (mensual), 3 (trimestral), 6 (semestral), 12 (anual). Para ver una lista de las periodicidades acceder a [PERIODICIDADES](https://servicios.ine.es/wstempus/js/ES/).
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’), incluir metadatos (‘M’) o ambos (‘AM’).
        *   **g1**: primer filtro de variables y valores. El formato es g1=id\_variable\_1:id\_valor\_1. Cuando no se especifica el id\_valor\_1 se devuelven todos los valores de id\_variable\_1 (g1=id\_variable\_1:). Para obtener las variables de una operación dada consultar [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC). Para obtener los valores de una variable específica de una operación data consultar [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/IPC](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/IPC).
        *   **g2**: segundo filtro de variables y valores. El formato es g2=id\_variable\_2:id\_valor\_2. Cuando no se especifica el id\_valor\_2 se devuelven todos los valores de id\_variable\_2 (g2=id\_variable\_2:). Seguiríamos con g3, g4,… según el número de filtros que se utilicen sobre variables.
    *   ### Salida
        
        Información de las series cuya definición de metadatos cumple los criterios establecidos: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad.
        
    *   ### Ejemplos
        
        *   Devuelve la definición de las series de la operación del IPC referentes a la provincia de Madrid (g1=115:29) para la variación mensual (g2=3:84) y todos los grupos ECOICOP (g3=762:)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1](https://servicios.ine.es/wstempus/js/ES/SERIE_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1)
            
        *   Consulta con nivel de detalle máximo
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&det=2](https://servicios.ine.es/wstempus/js/ES/SERIE_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&det=2)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/SERIE_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&det=2&tip=A)
            
        *   Consulta con metadatos y salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/SERIE\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&tip=AM](https://servicios.ine.es/wstempus/js/ES/SERIE_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&tip=AM)
            
*   PERIODICIDADES
    *   Obtener las periodicidades disponibles.
        
    *   ### Input
        
        Ninguno.
        
    *   ### Parámetros
        
        Ninguno.
        
    *   ### Salida
        
        Información de las periodicidades disponibles: identificador Tempus3 de la periodicidad, nombre y código.
        
    *   ### Ejemplos
        
        *   Devuelve todas las periodicidades
            
            [https://servicios.ine.es/wstempus/js/ES/PERIODICIDADES](https://servicios.ine.es/wstempus/js/ES/PERIODICIDADES)
            
*   PUBLICACIONES
    *   Obtener las publicaciones disponibles.
        
    *   ### Input
        
        Ninguno.
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’).
    *   ### Salida
        
        Información de todas las publicaciones: identificador Tempus3 de la publicación, nombre, identificador Tempus3 de la periodicidad e identificador Tempus3 de la publicación fecha.
        
    *   ### Ejemplos
        
        *   Devuelve todas las publicaciones
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES?det=2](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES?det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES?det=2&tip=A)
            
*   PUBLICACIONES\_OPERACION
    *   Obtener todas las publicaciones para una operación dada.
        
    *   ### Input
        
        Código identificativo de la operación. Para consultar las operaciones disponibles acceder a [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’).
    *   ### Salida
        
        Información de todas las publicaciones de una operación: identificador Tempus3 de la publicación, nombre, identificador Tempus3 de la periodicidad e identificador Tempus3 de la publicación fecha.
        
    *   ### Ejemplos
        
        *   Devuelve todas las publicaciones de la operación del IPC (IOE30138 / IPC / 25)
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/IPC)
            
        *   Consulta con nivel máximo de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES\_OPERACION/IPC?det=2](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/IPC?det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES\_OPERACION/IPC?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/IPC?det=2&tip=A)
            
*   PUBLICACIONFECHA\_PUBLICACION
    *   Obtener las fechas de publicación para una publicación dada.
        
    *   ### Input
        
        Código identificativo de la publicación. Para obtener una lista de las publicaciones acceder a [PUBLICACIONES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1159) o [PUBLICACIONES\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1160).
        
    *   ### Parámetros
        
        *   **det**: ofrece mayor nivel de detalle de la información mostrada. Valores válidos son 0, 1 y 2.
        *   **tip**: obtener la respuesta de las peticiones de modo más amigable (‘A’).
    *   ### Salida
        
        Información de todas las publicaciones de una operación: identificador Tempus3 de la publicación, nombre, identificador Tempus3 de la periodicidad e identificador Tempus3 de la publicación fecha.
        
    *   ### Ejemplos
        
        *   Obtener las fechas de la publicación "Índice de Precios de Consumo" (Id=8)
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA\_PUBLICACION/8](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA_PUBLICACION/8)
            
        *   Consulta con máximo nivel de detalle
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA\_PUBLICACION/8?det=2](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA_PUBLICACION/8?det=2)
            
        *   Consulta con salida amigable
            
            [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA\_PUBLICACION/8?tip=A](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA_PUBLICACION/8?tip=A)
            

*   [**Contacto**](https://www.ine.es/infoine/)
*   [Mapa web](https://www.ine.es/indiceweb.htm)
*   [Aviso legal](https://www.ine.es/dyngs/AYU/index.htm?cid=125)
*   [Accesibilidad](https://www.ine.es/dyngs/AYU/index.htm?cid=127)
*   [Prensa](https://www.ine.es/prensa/seccion_prensa.htm)
*   [Clasificaciones y estándares](https://www.ine.es/dyngs/MYP/es/index.htm?cid=1)
*   [Nuevos proyectos](https://www.ine.es/dyngs/MYP/es/index.htm?cid=10)
*   [Ver +](https://www.ine.es/dyngs/MYP/es/index.htm?cid=23 "Métodos y proyectos / Documentos de Trabajo")

*   [El INE](https://www.ine.es/dyngs/INE/es/index.htm?cid=498)
*   [Transparencia](https://www.ine.es/dyngs/INE/index.htm?cid=401)
*   [Organización Estadística en España](https://www.ine.es/dyngs/INE/es/index.htm?cid=581)
*   [Calidad y Código de buenas prácticas](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1259943453642&p=1259943453642&pagename=MetodologiaYEstandares%2FINELayout)
*   [Sistema Estadístico Europeo](https://www.ine.es/dyngs/INE/es/index.htm?cid=542)
*   [Ver +](https://www.ine.es/dyngs/INE/es/index.htm?cid=496 "El INE")

*   [Formación y empleo](https://www.ine.es/dyngs/FYE/index.htm?cid=132)
*   [Prácticas universitarias](https://www.ine.es/dyngs/FYE/index.htm?cid=133)
*   [Becas](https://www.ine.es/dyngs/FYE/index.htm?cid=134)
*   [Oposiciones](https://www.ine.es/dyngs/FYE/index.htm?cid=166)
*   [Explica](https://www.ine.es/explica/explica.htm)
*   [Ver +](https://www.ine.es/dyngs/FYE/index.htm?cid=132 "Formación y empleo")

*   [IPC en un clic](https://www.ine.es/ss/Satellite?L=0&c=Page&cid=1254735893337&p=1254735893337&pagename=ProductosYServicios%2FPYSLayout)
*   [Atención al público](https://www.ine.es/ss/Satellite?c=Page&cid=1254735550343&pagename=ProductosYServicios%2FPYSLayout&L=0)
*   [Publicaciones](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735110606&p=1254735110606&pagename=ProductosYServicios%2FPYSLayout)
*   [Datos abiertos](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1259942408928&p=1259942408928&pagename=ProductosYServicios%2FPYSLayout)
*   [Carta de servicios](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1259945091334&p=1259945091334&pagename=ProductosYServicios%2FPYSLayout)
*   [Ver +](https://www.ine.es/ss/Satellite?c=Page&cid=1254735550343&pagename=ProductosYServicios%2FPYSLayout&L=0 "Productos y Servicios")

*   Síguenos
*   [X](https://twitter.com/es_ine "Abre ventana nueva")
*   [Youtube](https://www.youtube.com/INEDifusion "Abre ventana nueva")
*   [Instagram](https://www.instagram.com/es_ine_/ "Abre ventana nueva")
*   [LinkedIn](https://es.linkedin.com/company/ine-es "Abre ventana nueva")
*   [Canal RSS](https://www.ine.es/dyngs/INE/es/index.htm?cid=1303 "Abre ventana nueva")

© 2025 [INE. Instituto Nacional de Estadística](https://www.ine.es/) [](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1 "Este sitio web y su contenido están bajo licencia CC BY-SA 4.0") Avda. Manoteras, 52 - 28050 - Madrid - España Tlf: (+34) 91 583 91 00
