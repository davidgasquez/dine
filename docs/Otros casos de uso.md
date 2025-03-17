API JSON / Otros casos de uso
===============               

[![Image 1: SIGLAS Instituto Nacional de Estadística](https://www.ine.es/menus/_b/img/LogoINE.svg)](https://www.ine.es/)

*   [English](https://www.ine.es/dyngs/DAB/en/index.htm?cid=1103 "English Page")

   

[](https://www.ine.es/indiceweb.htm "Menú de navegación") ![Image 2: Instituto Nacional de EstadÃ­stica](https://www.ine.es/menus/_b/img/LogoINESiglasMini.svg)

*   [Censo Electoral](https://www.ine.es/dyngs/CEL/index.htm?cid=41)
*   [Sede electrónica](https://sede.ine.gob.es/ss/Satellite?c=Page&cid=1254734719723&pagename=SedeElectronica%2FSELayout&lang=es_ES)
*   [Compartir](javascript:void(0))
    *   [X](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareTwitter "Abre ventana nueva X")
    *   [Facebook](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareFacebook "Abre ventana nueva Facebook")
    *   [Linkedin](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareLinkedin "Abre ventana nueva Linkedin")
    *   [WhatsApp](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareWhatsapp "Abre ventana nueva WhatsApp")
    *   [Correo Electrónico](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareMail "Abre ventana nueva")
    *   [Copiar al portapapeles](https://www.ine.es/dyngs/DAB/index.htm?cid=1103#shareClipboard "Abre ventana nueva")

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   Otros casos de uso
    ==================
    

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   [Referencia de la API](https://www.ine.es/dyngs/DAB/index.htm?cid=1100)
*   [Lista de funciones](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128)
*   [Obtener datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102)
*   [Otros casos de uso](https://www.ine.es/dyngs/DAB/index.htm?cid=1103)
*   [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)
*   [Base de datos Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
*   [Generador de URLs](https://www.ine.es/dyngs/DAB/index.htm?cid=1347)
*   [Generador de gráficos](https://www.ine.es/dyngs/DAB/index.htm?cid=1348)

Otros casos de uso  
  
Obtener datos de una serie
--------------------------------------------------

Para obtener los datos de una única serie es necesario conocer su código identificativo (acceder a [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)).

Una vez se conoce el código de la serie de interés, se puede utilizar la función [DATOS\_SERIE](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1129) para obtener los datos de interés.

*   Obtener el último periodo de una serie
    *   Por ejemplo, para la serie con código [IPC251856](https://www.ine.es/consul/serie.do?s=IPC251856)
        
        [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=1](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=1)
        
*   Obtener los últimos 5 periodos de una serie
    *   Por ejemplo, para la serie con código [IPC251856](https://www.ine.es/consul/serie.do?s=IPC251856)
        
        [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?nult=5)
        
*   Obtener los datos entre dos fechas
    *   Por ejemplo, entre 01/01/2023 y 31/12/2023
        
        [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?date=20230101:20231231&tip=A](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?date=20230101:20231231&tip=A)
        
*   Obtener los datos a partir de una fecha
    *   Por ejemplo, a partir de 01/01/2024
        
        [https://servicios.ine.es/wstempus/js/ES/DATOS\_SERIE/IPC251856?date=20240101:&tip=A](https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC251856?date=20240101:&tip=A)
        

Consultar operaciones estadísticas
----------------------------------

La base de datos Tempus3 contiene la información de todas las operaciones estadísticas coyunturales del INE, aquellas cuya periodicidad de difusión de resultados es inferior al año, además de algunas operaciones estadísticas estructurales. La relación de operaciones en Tempus3 cambia a medida que se van integrando en la base de datos. Puede consultarse la lista de operaciones disponibles en cualquier momento con las funciones [OPERACIONES\_DISPONIBLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1143) y [OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1144).

*   Obtener las operaciones estadísticas disponibles del sistema
    *   [https://servicios.ine.es/wstempus/js/ES/OPERACIONES\_DISPONIBLES](https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES)
        
*   Obtener una operación estadística
    *   Por ejemplo, la operación IPC utilizando el código alfabético Tempus3 interno (IPC)
        
        [https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/OPERACION/IPC)
        

Consultar variables
-------------------

Se pueden obtener las variables del Sistema utilizando las funciones [VARIABLES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1145) y [VARIABLES\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1146).

*   Obtener todas las variables del sistema
    *   La respuesta está paginada (500 elementos por página)
        
        [https://servicios.ine.es/wstempus/js/ES/VARIABLES](https://servicios.ine.es/wstempus/js/ES/VARIABLES)
        
        [https://servicios.ine.es/wstempus/js/ES/VARIABLES?page=2](https://servicios.ine.es/wstempus/js/ES/VARIABLES?page=2)
        
*   Obtener variables para una operación
    *   Por ejemplo, las variables utilizadas en la operación IPC
        
        [https://servicios.ine.es/wstempus/js/ES/VARIABLES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/VARIABLES_OPERACION/IPC)
        

Consultar valores de variables
------------------------------

Se pueden obtener los valores de una variable utilizando las funciones [VALORES\_VARIABLE](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1147) y [VALORES\_VARIABLEOPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1148).

*   Obtener todos los valores de una variable
    *   Por ejemplo, de la variable Provincias (Id=115)
        
        [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLE/115](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/115)
        
*   Obtener todos los valores de una variable para una operación
    *   Por ejemplo, los valores de la variable "Grupos ECOICOP" (Id=762) para la operación IPC (IOE30138 / IPC / 25)
        
        [https://servicios.ine.es/wstempus/js/ES/VALORES\_VARIABLEOPERACION/762/25](https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLEOPERACION/762/25)
        

Obtener información de tablas
-----------------------------

En lo que se refiere a las tablas, se puede obtener un listado de las tablas de una operación con la función [TABLAS\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1149) y también las variables y valores que la definen con las funciones [GRUPOS\_TABLA](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1150) y [VALORES\_GRUPOSTABLA](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1151).

*   Obtener todas las tablas de una operación
    *   Por ejemplo, el listado de tablas de la operación estadística IPC (IOE30138 / IPC / 25)
        
        [https://servicios.ine.es/wstempus/js/ES/TABLAS\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/TABLAS_OPERACION/IPC)
        
*   Obtener la combinación de variables y valores que definen una tabla
    *   Una tabla está definida por diferentes grupos o combos de selección y cada uno de ellos por los valores que toman una o varias variables. La consulta de los valores y las variables que constituyen la tabla se debe realizar en dos partes:
        
        1.  Primera parte de la consulta: Grupos o combos de selección que definen a la tabla "[Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913)" (Id 50913)
            
            [https://servicios.ine.es/wstempus/js/ES/GRUPOS\_TABLA/50913](https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/50913)
            
        2.  Segunda parte de la consulta: Valores del grupo “Comunidades y Ciudades Autónomas” (Id=110924) perteneciente a la tabla "[Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913)" (Id=50913)
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110924?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110924?det=1)
            

Obtener información de series
-----------------------------

En lo que se refiere a las series, se puede obtener información de una serie con la función [SERIE](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1152), así como de las variables y valores que la definen con la función [VALORES\_SERIE](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1155). Además, también se puede obtener un listado de las series de una tabla con la función [SERIES\_TABLA](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1156) y un listado de las series de una operación [SERIES\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1154).

*   Obtener información de una serie
    *   Por ejemplo, de la serie que recoge los datos del índice general del IPC ([IPC251852](https://www.ine.es/consul/serie.do?s=IPC251852)) que recoge la variación mensual del Índice de precios de consumo
        
        [https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2&tip=A](https://servicios.ine.es/wstempus/js/ES/SERIE/IPC251852?det=2&tip=A)
        
*   Obtener las variables y valores que definen una serie
    *   Por ejemplo, de la serie que recoge los datos del índice general del IPC ([IPC251852](https://www.ine.es/consul/serie.do?s=IPC251852))
        
        [https://servicios.ine.es/wstempus/js/ES/VALORES\_SERIE/IPC251852?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_SERIE/IPC251852?det=1)
        
*   Obtener el listado de series de una tabla
    *   Por ejemplo, las series de la tabla [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Datos.htm?t=50913) de la operación IPC (Id 50913).
        
        [https://servicios.ine.es/wstempus/jsCache/ES/SERIES\_TABLA/50913](https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/50913)
        
        Se puede utilizar el parámetro tv para filtrar por variables y valores. Más información en [Como filtrar datos de una tabla](https://www.ine.es/dyngs/CEL/index.htm?cid=1102#is1110).
        
*   Obtener el listado de series de una operación
    *   Como el resultado está paginado, se debe utilizar el parámetro page. Consulta de las primeras 500 series pertenecientes a la operación IPC (IOE30138 / IPC / 25)
        
        [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=1](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=1)
        
        Consulta de las segundas 500 series pertenecientes a la operación IPC (IOE30138 / IPC / 25)
        
        [https://servicios.ine.es/wstempus/js/ES/SERIES\_OPERACION/IPC?page=2](https://servicios.ine.es/wstempus/js/ES/SERIES_OPERACION/IPC?page=2)
        

Consultar publicaciones
-----------------------

Se puede obtener un listado de las todas las publicaciones del sistema con la función [PUBLICACIONES](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1159), así como el listado de las publicaciones de una operación con la función [PUBLICACIONES\_OPERACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1160). Además, también se pueden consultar las fechas de publicación de una publicación en particular con la función [PUBLICACIONFECHA\_PUBLICACION](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1161).

*   Obtener el litado de todas las publicaciones
    *   [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES)
        
*   Obtener el listado de las publicaciones de una operación
    *   Por ejemplo, las publicaciones de la operación del IPC (IOE30138 / IPC / 25)
        
        [https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES\_OPERACION/IPC](https://servicios.ine.es/wstempus/js/ES/PUBLICACIONES_OPERACION/IPC)
        
*   Obtener las fechas de publicación de una publicación
    *   Por ejemplo, de la publicación "Índice de Precios de Consumo" (Id=8)
        
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
