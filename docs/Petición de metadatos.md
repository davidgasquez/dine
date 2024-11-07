# Petición de metadatos

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=48

El Sistema Tempus3 tiene una arquitectura relacional compleja para almacenar datos y metadatos. Los datos únicamente están asociados al objeto [serie](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Glosario Tempus3") y éstas pueden agruparse en diferentes elementos, siendo el más utilizado la tabla estadística. Por tanto, la [tabla estadística](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Glosario Tempus3") en Tempus3 es una agrupación de series temporales.

Por otro lado, los metadatos estructurales ([variables y valores](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Glosario Tempus3")) son objetos de Tempus3 que describen tanto a las series temporales como a las tablas estadísticas y permiten su definición.

Todos estos objetos de la base de datos tienen un identificador asociado que resulta imprescindible para el correcto uso del servicio, correspondiendo a la parte {inputs} de las peticiones URL. ([Ver Glosario Tempus3](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Glosario Tempus3"))

A continuación se detallan las formas de obtención de metadatos.

Obtención de operaciones estadísticas

La base de datos Tempus3 contiene la información de todas las operaciones estadísticas coyunturales del INE, aquellas cuya periodicidad de difusión de resultados es inferior al año, además de algunas operaciones estadísticas estructurales. La relación de operaciones en Tempus3 cambia a medida que se van integrando en la base de datos .

Puede consultarse la lista de operaciones disponibles en cualquier momento a través de las siguientes funciones:

*   **_OPERACIONES\_DISPONIBLES_**
*   _**OPERACION**_

Construcción de las URLs:

**Obtener las operaciones estadísticas disponibles del sistema**

*   **Consulta**: Todas las operaciones estadísticas disponibles.
*   [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES "Enlace a OPERACIONES_DISPONIBLES . Abre ventana nueva")
*   **{función}** \= OPERACIONES\_DISPONIBLES
*   **{input}** = ninguno
*   **{output}** = Se obtienen los identificadores del elemento operación estadística. Existen tres códigos para la identificación de  la operación estadística "Índice de Precios de Consumo (IPC)":
    *   código numérico Tempus3 interno **_(Id=25)_**
    *   código de la operación estadística en el Inventario de Operaciones Estadísticas **(_IOE30138_)**
    *   código alfabético Tempus3 interno **(_IPC_)**

**Obtener una operación estadística**

*   **Consulta**: Operación Índice de Precios de Consumo (IPC), IPC.
*   [https://servicios.ine.es/wstempus/js/ES/OPERACION/IOE30138](https://servicios.ine.es/wstempus/js/ES/OPERACION/IOE30138 "Enlace a OPERACIONES. Abre ventana nueva")
*   [https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC "Enlace a OPERACION. Abre ventana nueva")
*   [https://servicios.ine.es/wstempus/js/ES/OPERACION/25](https://servicios.ine.es/wstempus/js/ES/OPERACION/25 "Enlace a OPERACION. Abre ventana nueva")
*   **{función}** \= OPERACION
*   **{input} =** Códigos para identificar la operación IPC: IOE30138 / IPC / 25
*   **{output} =** Información de la operación estadística IPC: identificador Tempus3, código del IOE y nombre de la operación.

Obtención de variables

Acceso a las [**variables**](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Enlace a Glosario TEMPUS3") del Sistema utilizando las siguientes funciones:

*   **_VARIABLES_**
*   **_VARIABLES\_OPERACION_**

Construcción de las URLs:

**Obtener todas las variables del sistema**

*   **Consulta:** Todas las variables.
*   [https://servicios.ine.es/wstempus/js/ES/VARIABLES](https://servicios.ine.es/wstempus/js/ES/VARIABLES "Enlace a VARIABLES. Abre ventana nueva")
*   **{función} \=** VARIABLES
*   **{input}** \= ninguno
*   **{output}** = Información de todas las variables del Sistema: identificador Tempus3, nombre de la variable y código oficial.

**Obtener variables para una operación**

*   **Consulta:** Variables operación IPC.
*   [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/25](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/25 "Enlace a VARIABLES_OPERACION. Abre ventana nueva")
*   **{función} \=** VARIABLES\_OPERACION
*   **{input}** \= Códigos identificadores de la operación EOTR: IOE30138 / IPC/ 25
*   **{output}** = Información de las variables que describen la operación: identificador Tempus3, nombre de la variable y código oficial.

Obtención de valores

Acceso a los [**valores**](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Enlace a Glosario Tempus3") de una variable utilizando las siguientes funciones :

*   **_VALORES\_VARIABLE_**
*   **_VALORES\_VARIABLEOPERACION_**

Construcción de las URLs:

**Obtener todos los valores de una variable**

*   **Consulta:** Valores de la variable “Provincias”.
*   [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLE/115](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/115 "Enlace a VALORES_VARIABLE. Abre ventana nueva")
*   **{función} \=** VALORES\_VARIABLE
*   **{input}** \= código identificador de la variable (Id=115).
*   **{output}** = Información de los valores que puede tomar la variable: identificador Tempus3 del valor, identificador Tempus 3 de la variable a la que pertenece, nombre del valor y código oficial.
*   **\[?parámetros\] =** posibilidad de usar det=1 para ver el detalle de la variable a la que pertenece.

**Obtener todos los valores de una variable para una operación**

*   **Consulta:** Valores de la variable “Grupos ECOICOP" para la operación IPC.
*   [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/25](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/25 "Enlace a VALORES_VARIABLEOPERACION. Abre ventana nueva")
*   **{función} \=** VALORES\_VARIABLEOPERACION
*   **{inputs}** \= códigos identificadores de la variable (Id=762) y de la operación (IOE30138 / IPC / 25).
*   **{output}** = Información de los valores que puede tomar la variable para describir la operación: identificador Tempus3 del valor, objeto variable Tempus3 a la que pertenece, nombre del valor y código oficial.
*   **\[?parámetros\] \=** posibilidad de usar det=1 para ver el detalle de la variable a la que pertenece.

Obtención de tablas

Acceso a las [**tablas**](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Enlace a Glosario Tempus3") del Sistema utilizando las siguientes funciones :

*   **_TABLAS\_OPERACION_**
*   **_GRUPOS\_TABLA_**
*   **_VALORES\_GRUPOSTABLA_**

Construcción de las URLs:

**Obtener todas las tablas de una operación**

*   **Consulta:** Tablas estadísticas asociadas a la operación estadística IPC.
*   [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IOE30138](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IOE30138 "Enlace a TABLAS_OPERACION. Abre ventana nueva")
*   **{función} \=** TABLAS\_OPERACION
*   **{input}** \= código identificativo de la operación (IOE30138 / IPC / 25).
*   **{output}** = Información de las tablas asociadas a la operación: identificador Tempus3 de la tabla, nombre de la tabla, código con información del nivel geográfico y clasificación, objeto Tempus3  periodicidad, objeto Tempus3  publicación, _PubFechaAct_ \* dentro de la publicación,  objeto Tempus3  periodo inicio, año inicio, _FechaRef\_fin_\* y última modificación.
*   **\[?parámetros\] =**  posibilidad de usar det=2 para ver dos niveles de profuncidad, en concreto hasta acceder al objeto PubFechaAct , geo=1 para acceder sólo a tablas con contenido geográfico y tip=A para que la respuesta sea de tipo amigable, en concreto el campo ultima\_modificacion.
*   **Observaciónes:**
    *   _\*FechaRef\_fin_: nulo cuando el último periodo publicado coincide con el de la publicación fecha, en otro caso, cuando la tabla está cortada en un periodo anterior al de la publicación fecha, es sustituido por Fk\_perido\_fin/ Anyo\_perido\_fin (fecha del último dato publicado). Ver: [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/33](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/33 "Enlace a TABLAS_OPERACION. Abre ventana nueva")
    *   \* _PubFechaAct =_ contiene la última fecha de actualización de la tabla y el último periodo-año publicado.

**Obtener la combinación de variables y valores que definen una tabla**

*   **Consulta:** Una tabla está definida por diferentes grupos o combos de selección y cada uno de ellos por los valores que toman una o varias variables. Para consultar los valores y las variables que constituyen la tabla, se utilizarán las dos funciones siguientes:
    *   **\- Primera parte de la consulta**: Grupos o combos de selección que definen a la tabla  ["Índices por comunidades autónomas: general y de grupos ECOICOP"](https://www.ine.es/jaxiT3/Tabla.htm?t=22350), la primera de las tablas obtenidas en la consulta anterior.
        *   [https://servicios.ine.es/wstempus/js/ES/GRUPOS\_TABLA/22350](https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/22350 "Enlace a GRUPOS_TABLA. Abre ventana nueva")
        *   **{función} \=** GRUPOS\_TABLA
        *   **{input}** \= código identificativo de la tabla (Id=22350).
        *   **{output}** = Grupos de valores que definen la tabla: identificador Tempus3 del grupo y nombre del grupo.
    *   **\- Segunda parte de la consulta**: Sobre el primer grupo de valores, consultar los valores que éste toma y la variable a la que pertenecen.
        *   [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/22350/81497](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/22350/81497 "Enlace a VALORES_DIMENSIONTABLA. Abre ventana nueva")
        *   **{función} =** VALORES\_GRUPOSTABLA
        *   **{input}** \= códigos identificativos de la tabla (Id=22350) y del grupo "Comunidades y Ciudades Autónomas"  (Id=81497).
        *   **{output}** = Información de los valores pertenecientes al grupo:  identificador Tempus3 del valor, identificador Tempus 3 de la variable a la que pertenece, nombre del valor y código oficial.
        *   **\[?parámetros\] \=** posibilidad de usar det=1 para ver el detalle de la variable a la que pertenece.

Obtención de series

Acceso a las [**series**](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Enlace a Glosario TEMPUS3"), utilizando las siguientes funciones:

*   **_SERIE_**
*   **_SERIES\_OPERACION_**
*   **_VALORES\_SERIE_**
*   **_SERIES\_TABLA_**
*   **_SERIE\_METADATAOPERACION_**

Consultar ["¿Cómo obtener identificadores de objetos utilizando INEbase?"](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945947403).

Construcción de las URLs:

**Obtener serie**

*   **Consulta:** [Serie IPC206449](https://www.ine.es/consul/serie.do?s=IPC206449 "Enlace a la serie "), recoge la variación mensual del Índice de precios de consumo. Base 2016.
*   [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC206449](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC206449 "Enlace a SERIE. Abre ventana nueva")
*   **{función} \=**  SERIE
*   **{input}** \= código identificativo de la serie (COD=IPC206449). Consultar  ["¿Cómo obtener identificadores de objetos utilizando INEbase?"](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945947403).
*   **{output}** = Información de la serie: identificadores Tempus3 de la serie, objetoTempus3 operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, objeto Tempus3  periodicidad, objeto Tempus3 publicación, _PubFechaAct_ \* dentro de la publicación_,_ objeto Tempsu3 _clasificación_ \*, objeto Tempus3  escala y objeto Tempus3 unidad.
*   **\[?parámetros\]=** posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder al objeto _PubFechaAct_ y _tip=M para obtener los metadatos (cruce variables-valores) de la serie._
*   **Observaciónes:**
    *   \* _PubFechaAct =_ contiene la última fecha de actualización de la serie y el último periodo-año publicado.
    *   \* _clasificación =  nos da información de la versión temporal de la serie, por ejempo, la [clasificación nacional](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735839296&p=1254735839296&pagename=MetodologiaYEstandares%2FINELayout) que en algunos casos sigue, marco poblacional, base utilizada en el cálculo de los índices,..._

**Obtener todas las series de una operación**

*   **Consulta:** Series pertenecientes a la operación IPC.
*   [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1 "Enlace a SERIES_OPERACION. Abre ventana nueva")
*   **{función}**  \= SERIES\_OPERACION
*   **{input}** \= código identificativo de la operación (IOE30138 / IPC / 25)
*   **{output}** = Información de las series: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad.
*   **\[?parámetros\]=** posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder al objeto _PubFechaAct_ y _tip=M_ para obtener los metadatos (cruce variables-valores) de la serie.

**Obtener los metadatos que definen una serie**

*   **Consulta:** Definición en términos de metadatos (variables y valores) de la serie que recoge los datos de la variación mensual del IPC, [IPC206449.](https://www.ine.es/consul/serie.do?s=IPC206449 "Ver serie")
*   [https://servicios.ine.es/wstempus/js/ES/VALORES\_SERIE/IPC206449](https://servicios.ine.es/wstempus/js/ES/VALORES_SERIE/IPC206449 "Enlace a VALORES_SERIE. Abre ventana nueva")
*   **{función} \=** VALORES\_SERIE
*   **{input}** \= Código identificativo de la serie (IPC206449)
*   **{output}** \= Información de los metadatos que definen a la serie: identificador Tempus3 del valor, identificador Tempus3 de la variable a la que pertenece, nombre del valor y código oficial del valor.
*   **\[?parámetros\] =** posibilidad de usar det=1 para acceder al objeto variable.

**Obtener las series de una tabla**

*   **Consulta:** Series que aparecen en la tabla ["Índices por comunidades autónomas: general y de grupos ECOICOP"](https://www.ine.es/jaxiT3/Tabla.htm?t=22350) de la operación IPC.
*   [https://servicios.ine.es/wstempus/js/ES/SERIES\_TABLA/22350](https://servicios.ine.es/wstempus/js/ES/SERIES_TABLA/22350 "Enlace a SERIES_TABLA. Abre ventana nueva")
*   **{función} \=** SERIES\_TABLA
*   **{input}** \= código identificativo de la tabla (Id=22350)
*   **{output}** \= Información de las series resultado de la tabla: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad.
*   **\[?parámetros\]** \=  posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder al objeto _PubFechaAct_ y _tip=M_ para obtener los metadatos (cruce variables-valores) de la serie.

**Obtener las series de una tabla filtrando por variables-valores**

*   **Consulta:** Obtener las series contenidas en la tabla "[Índices por comunidades autónomas: general y de grupos ECOICOP"](https://www.ine.es/jaxiT3/Tabla.htm?t=22350) filtrando por:
    *   Comunidades y Ciudades Autónomas =  "Madrid, Comunidad de" y "Comunitat Valenciana"
    *   Tipo de dato  = "Variación mensual"
    *   _Grupos ECOICOP \= "Índice general"_

Para conocer las variables y los valores de las series contenidas en una tabla será necesario realizar la siguiente consulta:

GRUPOS\_TABLA \=  [https://servicios.ine.es/wstempus/js/ES/GRUPOS\_TABLA/22350](https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/22350 "Enlace a SERIES_TABLA. Abre ventana nueva")

Y para cada uno de los grupos, por ejemplo para el grupo "Comunidades y Ciudades Autónomas"  (id=81497), la siguiente consulta:

VALORES\_GRUPOSTABLA =  [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/22350/81497?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/22350/81497?det=2&tip=A "Enlace a SERIES_TABLA. Abre ventana nueva")

*   [https://servicios.ine.es/wstempus/js/ES/SERIES\_TABLA/22350?tv=70:9009&tv=70:9006&tv=762:304092&tv=3:84](https://servicios.ine.es/wstempus/js/ES/SERIES_TABLA/22350?tv=70:9009&tv=70:9006&tv=762:304092&tv=3:84)
*   **{función} \=** SERIES\_TABLA
*   **{input}** \= Código identificativo de la tabla (Id=22350) y códigos identificativos de las variables y valores:
    *   Comunidades y Ciudades Autónomas _(FK\_VARIABLE=70)_ \= "Madrid, Comunidad de" _(FK\_VALOR=9009)  --  tv=70:9009_
    *   Comunidades y Ciudades Autónomas _(FK\_VARIABLE=70)_ \= "Comunitat Valenciana" _(FK\_VALOR=9006)  --  tv=70:9006_
    *   Grupos ECOICOP _(FK\_VARIABLE=762)_ \= "Índice general" _(FK\_VALOR=304092) --  tv=762:304092_
    *   Tipo de dato _(FK\_VARIABLE=3)_ \= "Variación mensual"   _(FK\_VALOR=84) \--  tv=3:84_
*   **{output}** \= Información de las series contenidas en la tabla cuya definición de metadatos cumple los criterios establecidos: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad..
*   **{?parámetros}=** posibilidad de usar det=2 para ver dos niveles de detalle, en concreto para poder acceder al objeto _PubFechaAct_ y _tip=M_ para obtener los metadatos (cruce variables-valores) de la serie.

**Obtener series mediante cruce de metadatos**

Para saber cómo están definidas las series dentro de una operación, por ejemplo del IPC, es necesario realizar la siguiente petición:

VARIABLES\_OPERACION \=  [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC "Enlace a SERIES_TABLA. Abre ventana nueva")

Y para cada una de estas variables, por ejemplo para la variable provincias (id=115), la siguiente consulta:

VALORES\_VARIABLEOERACION =  [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/115/IPC](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/115/IPC "Enlace a SERIES_TABLA. Abre ventana nueva")

Así nos puede interesar acceder a todas las series correspondientes a la variación mensual del IPC en Madrid según los diferentes grupos ECOICOP.

*   **Consulta:** Series mensuales de la operación IPC cuya definición en términos de metadatos (variables y valores)  cumple lo siguiente:
    *   Provincias =  "Madrid"
    *   Tipo de dato  = "Variación mensual"
    *   Grupos ECOICOP \= "Todos los grupos"
*   [https://servicios.ine.es/wstempus/js/ES/SERIE\_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1](https://servicios.ine.es/wstempus/js/ES/SERIE_METADATAOPERACION/IPC?g1=115:29&g2=3:84&g3=762:&p=1 "Enlace a SERIE_METADATAOPERACION. Abre ventana nueva")
*   **{función} \=** SERIE\_METADATAOPERACION
*   **{input}** \= Código identificativo de la operación (IOE30138 /IPC/ 25) y códigos identificativos de las variables y valores:
    *   Provincias _(FK\_VARIABLE=115)_ \= "Madrid" _(FK\_VALOR=29)  \-- g1=115:29_
    *   Tipo de dato _(FK\_VARIABLE=3)_ \= "Variación mensual"   _(FK\_VALOR=84) \-- g2=3:84_
    *   Grupos ECOICOP _(FK\_VARIABLE=762)_ \= "Todos los grupos ECOICOP" _(FK\_VALOR=null) --  g3=762:_
    *   Serie mensual _(FK\_PERIODICIDAD=1) \--  p=1  (Ver [PUBLICACIONES\_OPERACION](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/25))_
*   **{output}** \= Información de las series cuya deficición de metadatos cumple los criterios establecidos: identificadores Tempus3 de la serie, identificador Tempus3 de la operación, nombre de la serie, número de decimales que se van a visualizar para los datos de esa serie, identificador Tempus3 de la periodicidad, identificador Tempus3 de la publicación, identificador Tempsu3 de la clasificación, identificador Tempus3 de la escala e identificador Tempus3 de la unidad..
*   **\[?parámetros\]** \=  posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder al objeto _PubFechaAct_ y _tip=M_ para obtener los metadatos (cruce variables-valores) de la serie.

Obtención de publicaciones

Acceso a las [**publicaciones**](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=64 "Enlace a Glosario Tempus3: conceptos fundamentales") utilizando las siguientes funciones:

*   **_PUBLICACIONES_**
*   **_PUBLICACIONES\_OPERACION_**
*   **_PUBLICACIONFECHA\_PUBLICACION_**

Construcción de las URLs:

**Obtener todas las publicaciones**

*   **Consulta:** Todas las publicaciones del sistema.
*   [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES "Enlace a PUBLICACIONES. Abre ventana nueva")
*   **{función} \=** PUBLICACIONES
*   **{input}** \= ninguno
*   **{output}** = Información de todas las publicaciones: identificador Tempus3 de la publicación, nombre, identificador Tempus3 de la periodicidad e identificador Tempus3 de la publicación fecha.
*   **\[?parámetros\]=** posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder a los atributos del objeto _PubFechaAct_ .

**Obtener las publicaciones de una operación**

*   **Consulta:** Publicaciones asociadas a la operación IPC.
*   [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES\_OPERACION/IOE30138](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/IOE30138 "Enlace a PUBLICACIONES_OPERACION. Abre ventana nueva")
*   **{función} \=** PUBLICACIONES\_OPERACION
*   **{input}** \= Código identificativo de la operación (IOE30138 / IPC / 25).
*   **{output}** = Información de todas las publicaciones de una operación: identificador Tempus3 de la publicación, nombre, identificador Tempus3 de la periodicidad e identificador Tempus3 de la publicación fecha.
*   **\[?parámetros\]=** posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder a los atributos del objeto _PubFechaAct_ .

**Obtener las fechas de publicación de una publicación**

*   **Consulta:** Fechas de publicación asociadas a la publicación “Índice de Precios de Consumo”, la primera de las publicaciones obtenidas en la consulta anterior.
*   [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA\_PUBLICACION/8](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONFECHA_PUBLICACION/8 "Enlace a PUBLICACIONFECHA_PUBLICACION. Abre ventana nueva")
*   **{función} \=** PUBLICACIONFECHA\_PUBLICACION
*   **{input}** \=  Código identificativo de la publicación (Id=8).
*   **{output}** = Fechas en las que se producen nuevas incorporaciones de datos: identificador Tempus3 de la publicación fecha, identificador Tempus3 de la publicación a la que pertenece, fecha en que se produce la publicación y periodo al que se refieren los datos publicados.
*   **\[?parámetros\]=** posibilidad de usar _det=2_ para ver dos niveles de detalle, en contreto para poder acceder a los atributos del objeto _PubFechaAct_ .
