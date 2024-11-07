# Petición de datos

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=1259945947373

El campo **valor** derivado de las siguientes consultas es el único que contiene datos. El resto de los campos que acompañan al dato son necesarios para que esté bien definido, siendo los más relevantes:

**Sistema Tempus3:**

*   **Tipo de dato**: puede ser: definitivo (1), provisional (2), avance (3), primera estimación (4), estimado (5).
*   **Fecha**: fecha, en milisegundos, a la que hace referencia el dato. Por defecto, es la fecha correspondiente al día 1 del mes que indica el periodo más el año, pero puede ocurrir que los datos estén referidos a una fecha concreta.
*   **Secreto**: _true_ cuando el campo valor se oculta por secreto estadístico, _false_ en caso contrario.

**Repositorio de ficheros PC-Axis:**

*   **NombrePeriodo**: fecha a la que hace referencia el dato (sólo para PC-Axis con datos de diferentes periodos) .

Se pueden obtener **datos** utilizando las siguientes funciones:

*   _**DATOS\_SERIE**_  (Sólo disponible para Tempus3)
*   _**DATOS\_TABLA**_
*   **_DATOS\_METADATAOPERACION_** (Sólo disponible para Tempus3)

Obtención de datos Sistema Tempus3

**Obtener el último dato de una serie**

*   **Consulta:** Último dato publicado para la serie que recoge la variación mensual del Índice de precios de consumo. Base 2016.
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=1 "Enlace a DATOS_SERIE. Abre ventana nueva")
*   **{función}** \= DATOS\_SERIE
*   **{input} =** código identificativo de la serie (COD=IPC206449).
*   **{?parámetro obligatorio} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, un solo dato, por tanto el parámetro _nult_ tomará el valor 1.
*   **{output} =** Información de la serie y último dato publicado: Nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato).
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

**Obtener los n últimos datos de una serie**

*   **Consulta:** Últimos cinco datos publicados para la serie que recoge la variación mensual del Índice de precios de consumo. Base 2016.
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=5 "Enlace a DATOS_SERIE. Abre ventana nueva")
*   **{función}** \= DATOS\_SERIE
*   **{input} =** código identificativo de la serie (COD=IPC206449).
*   **{?parámetro obligatorio} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, los 5 últimos datos, por tanto el parámetro _nult_ tomará el valor 5.
*   **{output} =**Información de la serie y los 5 últimos datos publicados: Nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato).
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

**Obtener datos de una serie entre dos fechas**

*   **Consulta:** Datos publicados entre 01/01/2013 y 01/01/2016 para la serie que recoge la variación mensual del Índice de precios de consumo. Base 2016.
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?date=20130101:20160101](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?date=20130101:20160101 "Enlace a DATOS_SERIE. Abre ventana nueva")
*   **{función}** \= DATOS\_SERIE
*   **{input} =** código identificativo de la serie (COD=IPC206449).
*   **{?parámetro obligatorio} =** Rango de fechas entre las cuales se quiere obtener datos y se especifican en el parámetro _date_ (date=20130101:20160101).
*   **{output} =** Información de la serie y los datos publicados entre dos fechas: Nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato) .
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

**Obtener datos de una serie a partir de una fecha**

*   **Consulta:** Datos publicados desde 01/01/2010 para la serie que recoge la variación mensual del Índice de precios de consumo. Base 2016.
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC206449?date=20100101:](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?date=20100101: "Enlace a DATOS_SERIE. Abre ventana nueva")
*   **{función}** \= DATOS\_SERIE
*   **{input} =** código identificativo de la serie (COD=IPC206449).
*   **{?parámetro obligatorio} =** Fecha a partir de la cual se quiere obtener datos y se especifica en el parámetro _date_ (date=20100101:).
*   **{output} =** Información de la serie y los datos publicados a partir de una fecha: Nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato) _(ver detalle de los objetos Tempus3 usando el parámetro det)_.
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

**Obtener los n últimos datos de una tabla**

*   **Consulta:** Obtener los 4 últimos datos de las series contenidas en la tabla [¿ Índices por comunidades autónomas: general y de grupos ECOICOP"](https://www.ine.es/jaxiT3/Tabla.htm?t=22350)
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/22350?nult=4](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/22350?nult=4 "Enlace a DATOS_TABLA. Abre ventana nueva")
*   **{función}** \= DATOS\_TABLA
*   **{inputs} =** código identificativo de la tabla (Id=22350).
*   **{?parámetro obligatorio} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, los 4 últimos datos, por tanto el parámetro _nult_ tomará el valor 4.
*   **{output} =** Información y datos de las series contenidas en la tabla: Nombre de la serie, identificador Tempu3 de la unidad, identificador Tempus3 de la escala, fecha, identificador Tempus3 del tipo de dato, identificador Tempus3 del periodo, año y valor (dato).
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

**Obtener n los últimos datos de series mediante el cruce de metadatos**

Para saber cómo están definidas las series dentro de una operación, por ejemplo del IPC, es necesario realizar la siguiente petición:

VARIABLES\_OPERACION \=  [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC "Enlace a SERIES_TABLA. Abre ventana nueva")

Y para cada una de estas variables, por ejemplo para la variable provincias (id=115), la siguiente consulta:

VALORES\_VARIABLEOERACION =  [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/115/IPC](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/115/IPC "Enlace a SERIES_TABLA. Abre ventana nueva")

Así nos puede interesar acceder al último dato de todas las series correspondientes a la variación mensual del IPC en Madrid según los diferentes grupos ECOICOP.

*   **Consulta:** Series mensuales de la operación IPC cuya definición en términos de metadatos (variables y valores)  cumple lo siguiente:
    *   ¿Provincias¿ \=  "Madrid"
    *   ¿Tipo de dato¿  \= ¿Variación mensual¿
    *   ¿Grupos ECOICOP¿ \= Todos los grupos
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1&nult=1 "Enlace a SERIE_METADATAOPERACION. Abre ventana nueva")
*   **{función} \=** DATOS\_METADATAOPERACION
*   **{input}** \= Código identificativo de la operación (IOE30138 /IPC/ 25) y códigos identificativos de las variables y valores:
    *   ¿Provincias¿ _(FK\_VARIABLE=115)_ \= "Madrid" _(FK\_VALOR=29)  ¿  g1=115:29_
    *   ¿Tipo de dato¿ _(FK\_VARIABLE=3)_ \= ¿Variación mensual¿   _(FK\_VALOR=84) ¿ g2=3:84_
    *   ¿Grupos ECOICOP¿ _(FK\_VARIABLE=762)_ \= "Todos los grupos ECOICOP¿ _(FK\_VALOR=null) ¿  g3=762:_
    *   "Serie mensual" _(FK\_PERIODICIDAD=1) ¿  p=1  (Ver [PUBLICACIONES\_OPERACION](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/25))_
*   **{?parámetro obligatorio} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, el último dato, por tanto el parámetro _nult_ tomará el valor 1.
*   **{output}** \= Información de las series cuya deficición de metadatos cumple los criterios establecidos: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad..
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder a los atributos del objeto dato, y _tip=AM para obtener los metadatos (cruce variables-valores) de la serie y una salida de tipo amigable._

Obtención de datos PcAxis

**Obtener los n últimos datos de una tabla**

*   **Consulta:** Obtener los 4 últimos datos de las series contenidas en la tabla ["Población (españoles/extranjeros) por edad (3 grupos de edad), sexo y año"](http://xn--poblacin%20(espaoles-j7b8a/extranjeros)%20por%20edad%20(3%20grupos%20de%20edad),%20sexo%20y%20a%C3%B1o)
*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?nult=4](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?nult=4)
*   **{función}** = DATOS\_TABLA
*   **{inputs} =** código identificativo de la tabla _**(t20/e245/p08/l0/01001.px)**._
*   **{?parámetro} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, los 4 últimos datos, por tanto el parámetro _nult_ tomará el valor 4. _Posibilidad de usar _tip=M para obtener el campo metadata con los códigos de selección.__
*   **{output} =** descripción y 4 últimos datos de las series contenidas en la tabla: Nombre de la serie y Data (NombrePeriodo, valor y secreto).

**Obtener los n últimos datos de una tabla filtrando por metadata**

*   **Consulta:** Obtener los 2 últimos datos de las series contenidas en la tabla ["Población (españoles/extranjeros) por edad (3 grupos de edad), sexo y año"](http://xn--poblacin%20(espaoles-j7b8a/extranjeros)%20por%20edad%20(3%20grupos%20de%20edad),%20sexo%20y%20a%C3%B1o)  filtrando por:
    *   Edad (3 grupos de edad) =  "0-15 años"
    *   Españoles/Extranjeros  = "Extranjeros"
    *   Sexo \= "Hombres"  y "Mujeres"

Para obtener el campo metadata con los códigos de selección en una tabla será necesario realizar la siguiente consulta:

[https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?nult=2&tip=M](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?nult=2&tip=M)

*   [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?tv=edad3gruposdeedad:015anos&tv=espanolesextranjeros:extranjeros&tv=sexo:mujeres&tv=sexo:hombres&nult=2](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?tv=edad3gruposdeedad:015anos&tv=espanolesextranjeros:extranjeros&tv=sexo:mujeres&tv=sexo:hombres&nult=2)
*   **{función} \=** DATOS\_TABLA
*   **{input}** \= Código identificativo de la tabla **_(t20/e245/p08/l0/01001.px)_** y códigos de selección:
    *   Edad (3 grupos de edad) **_(codigo=edad3gruposdeedad)_** \= "0-15 años" _**(**_**_codigo=_**_**015anos)** --  **tv=**_**edad3gruposdeedad:015anos**
    *   Españoles/Extranjeros **_(codigo=_espanolesextranjeros_)_** \= "Extranjeros" **_(codigo=_extranjeros**_**)**  \--  **tv=**_**espanolesextranjeros:extranjeros**
    *   Sexo  **_(codigo=sexo)_** \= "Hombre" _**(**_**_codigo=_**_**hombres)**  \-- **tv=sexo:hombres**_
    *   Sexo  **_(codigo=sexo)_** \= "Mujeres" _**(**_**_codigo=_**_**mujeres)**  \-- **tv=sexo:mujeres**_
*   **{?parámetro} =** Número de datos, o de periodos, que se quieren visualizar. En este caso, los 2 últimos datos, por tanto el parámetro _nult_ tomará el valor 2. _Posibilidad de usar _tip=M para obtener el campo metadata con los códigos de selección.__
*   **{output} =** descripción y 2 últimos datos de las series contenidas en la tabla: Nombre de la serie y Data (NombrePeriodo, valor y secreto).
