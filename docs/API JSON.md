# API JSON del INE

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=45

El servicio API JSON INE _(Java Script Object Notation)_ que se describe en esta sección permite acceder mediante peticiones URL a toda la información disponible en [INEbase](https://www.ine.es/dyngs/INEbase/listaoperaciones.htm "Enlace a INEbase"), sistema que utiliza el Instituto Nacional de Estadística (INE) para la publicación de la información estadística.

La estructura de las peticiones a través de URL y la simplicidad del formato JSON, hacen que este tipo de aplicaciones sean ampliamente utilizadas para ofrecer datos y metadatos que permiten la explotación automática de la información estadística.

[INEbase](https://www.ine.es/dyngs/INEbase/listaoperaciones.htm "Enlace a INEbase") es el sistema que utiliza el INE para la publicación de la información estadística. La información que será accesible a través del servicio API JSON del INE que se describe en esta sección, proviene de dos fuentes distintas:

*   **Base de datos de difusión (Tempus3)**. ![Image 1: Elementos de TEMPUS3](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/TEMPUS3.jpg)

    *   Contiene la información de todas las operaciones estadísticas coyunturales del INE, aquellas cuya periodicidad de difusión de resultados es inferior al año, además de algunas operaciones estadísticas estructurales.
    *   La relación de operaciones en Tempus3 cambia a medida que éstas se van integrando en la base de datos.  Se pueden consultar las operaciones disponibles en el sistema Tempus3 a través de la siguiente URL: [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES "Enlace a OPERACIONES_DISPONIBLES . Abre ventana nueva")
    *   Tempus3 es una base de datos relacional que utiliza un conjunto de objetos organizados dentro de una jerarquía para almacenar y gestinar la información estadística. Su elemento principal  es la serie temporal, único objeto con datos asociados, en torno a él surgen el resto de elementos. Operaciones y tablas estadísticas serán objetos contenedores de series temporales. "[Glosario Tempus3](https://www.ine.es/dyngs/DataLab/manual.html?cid=64 "Enlace a Glosario TEMPUS3")"
*   **Repositorio de ficheros [PC-Axis](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735116596&p=1254735116596&pagename=ProductosYServicios%2FPYSLayout "Descarga del programa PC-Axis")**. El resto de operaciones no contenidas en Tempus3.

Toda la información publicada por el INE, independientemente de la fuente, va a poder ser consultada a través de la API JSON. La respuesta obtenida a través del servicio API JSON INE depedenderá de cuál sea su procedencia.

Para saber si una tabla estadística está almacenada en Tempus3 o en el repositorio de ficheros PC-Axis, consultar la sección [¿Cómo obtener identificadores de tablas utilizando INEbase?](https://www.ine.es/dyngs/DataLab/manual.html?cid=1259945948444).

En lo que sigue se describen las principales funciones de este servicio al tiempo que se ofrecen ejemplos que permiten su comprensión.
