API JSON / Base de datos Tempus3
===============
                                             

[![Image 1: SIGLAS Instituto Nacional de Estadística](https://www.ine.es/menus/_b/img/LogoINE.svg)](https://www.ine.es/)

*   [English](https://www.ine.es/dyngs/DAB/en/index.htm?cid=1105 "English Page")

   

[Menú de navegación](https://www.ine.es/indiceweb.htm "Menú de navegación") ![Image 2: Instituto Nacional de EstadÃ­stica](https://www.ine.es/menus/_b/img/LogoINESiglasMini.svg)

*   [Censo Electoral](https://www.ine.es/dyngs/CEL/index.htm?cid=41)
*   [Sede electrónica](https://sede.ine.gob.es/ss/Satellite?c=Page&cid=1254734719723&pagename=SedeElectronica%2FSELayout&lang=es_ES)
*   [Compartir](javascript:void(0))
    *   [X](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareTwitter "Abre ventana nueva X")
    *   [Facebook](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareFacebook "Abre ventana nueva Facebook")
    *   [Linkedin](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareLinkedin "Abre ventana nueva Linkedin")
    *   [WhatsApp](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareWhatsapp "Abre ventana nueva WhatsApp")
    *   [Correo Electrónico](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareMail "Abre ventana nueva")
    *   [Copiar al portapapeles](https://www.ine.es/dyngs/DAB/index.htm?cid=1105#shareClipboard "Abre ventana nueva")

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   Base de datos Tempus3
    =====================
    

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   [Referencia de la API](https://www.ine.es/dyngs/DAB/index.htm?cid=1100)
*   [Lista de funciones](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128)
*   [Obtener datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102)
*   [Otros casos de uso](https://www.ine.es/dyngs/DAB/index.htm?cid=1103)
*   [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)
*   [Base de datos Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
*   [Generador de URLs](https://www.ine.es/dyngs/DAB/index.htm?cid=1347)
*   [Generador de gráficos](https://www.ine.es/dyngs/DAB/index.htm?cid=1348)

Base de datos Tempus3
---------------------

Tempus3 contiene la información de todas las operaciones estadísticas coyunturales del INE, aquellas cuya periodicidad de difusión de resultados es inferior al año, además de algunas operaciones estadísticas estructurales.

La relación de operaciones en Tempus3 cambia a medida que éstas se van integrando en la base de datos.  Se pueden consultar las operaciones disponibles en el sistema Tempus3 a través de la siguiente URL: [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES).

Tempus3 es una base de datos relacional que utiliza un conjunto de objetos organizados dentro de una jerarquía para almacenar y gestionar la información estadística. Su elemento principal es la serie temporal, único objeto con datos asociados, en torno a él surgen el resto de los elementos. Operaciones y tablas estadísticas serán objetos contenedores de series temporales.

Conceptos fundamentales
-----------------------

Para hacer un uso adecuado del servicio es necesario describir los siguientes conceptos, cuyos identificadores serán los inputs (valores de entrada) en la construcción de URLs.

Variables
---------

Una variable es una característica que puede fluctuar y cuya variación es susceptible de adoptar diferentes valores.

Las variables o listas de valores contenidas en Tempus3 y utilizadas en la difusión, son comunes a todas las operaciones estadísticas, es decir, no están duplicadas en el sistema, su identificador en Tempus3 (Id) y sus descriptores son únicos. Se pueden consultar las variables con la función [VARIABLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1145).

Son ejemplos de variables las listas: Grupos COICOP, Sexo, CCAA, Provincias,...

Valores
-------

Los valores son los estados que puede presentar una variable determinada. Por ejemplo, la variable Provincias contiene los valores: Áraba/Álava, Albacete, Alicante/Alacant,...

Los valores contenidos en Tempus3 y utilizados en la difusión, son comunes a todas las operaciones estadísticas, es decir, no están duplicadas en el sistema, su identificador en Tempus3 (Id) y sus descriptores son únicos. Se pueden consultar los valores con la función [VALORES\_VARIABLE](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1147).

Series
------

**¿Qué son las series temporales?**

Conjunto de observaciones medidas en determinados momentos del tiempo, ordenados cronológica y normalmente espaciados entre sí de manera uniforme.

Como entidad principal de la base de datos Tempus3, la serie tiene unas propiedades que la definen y que no cambian a lo largo del tiempo:

**Identificador único y características de la serie:** _id, nombre, periodicidad, escala, unidad, clasificación, decimales,..._

Tablas
------

Una de las ventajas de este Sistema es la facilidad que ofrece a la hora de gestionar las diferentes formas de presentación, que corresponden a las distintas formas en las que se pueden agrupar las series. Una de ellas es la agrupación en **tabla** (o cubo). Es la más utilizada por los usuarios, que acceden a las tablas estadísticas a través de INEbase.

Una tabla es el resultado del cruce de grupos de valores contenidos en una o varias variables, es decir, son una agrupación de series temporales definidas por estos grupos.

Por ejemplo, se navega por [INEbase](https://www.ine.es/inebmenu/indice.htm) para llegar a la tabla [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913) del Índice de Precios de Consumo, Base 2021. Una vez se ha accedido a la tabla, se observa que ésta contiene todas las series que resultan de la combinación de los grupos de valores contenidos en las siguientes variables:

**{Comunidades y Ciudades Autónomas} x {Grupos ECOICOP} x {Tipo de dato}**

Como entidad, la tabla tiene unas características propias como nombre, los periodos que comprende y su un identificador, que es único. Puede obtener un listado de todas las tablas de una operación con la función [TABLAS\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1149).

Fecha de publicación
--------------------

Los datos en Tempus3 se publican a nivel de serie y están asociados a un instante de tiempo o **fecha de referenci**a **(periodo /año)**.

Pero **¿cuándo se publican los datos? ¿cuándo se actualizan?**

Cada operación tiene asociada una o varias **publicaciones** según sus diferentes periodicidades, por ejemplo, hay dos publicaciones para el IPC, una con periodicidad mensual y otra anual. Y éstas siguen el calendario de publicaciones del INE.

De esta manera, una **publicación** contiene los momentos en los que se publican los datos de una operación estadística: **fechas de publicación**.

Con el identificador de la publicación se puede consultar la **fecha de publicación** de todas las operaciones estadísticas que se disponen en el calendario de publicaciones con la función [PUBLICACIONFECHA\_PUBLICACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1161). Cada una de estas **fechas de publicación** tiene unas características:

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

© 2025 [INE. Instituto Nacional de Estadística](https://www.ine.es/) [Este sitio web y su contenido están bajo licencia CC BY-SA 4.0](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1 "Este sitio web y su contenido están bajo licencia CC BY-SA 4.0") Avda. Manoteras, 52 - 28050 - Madrid - España Tlf: (+34) 91 583 91 00

Volver arriba

Este sitio utiliza cookies para ofrecerle una mejor experiencia de navegación. Obtenga más información sobre [cómo utilizamos las cookies.](https://www.ine.es/dyngs/AYU/index.htm?cid=302)Aceptar
