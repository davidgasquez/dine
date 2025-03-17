API JSON / Obtener datos de una tabla
===============               

[![Image 1: SIGLAS Instituto Nacional de Estadística](https://www.ine.es/menus/_b/img/LogoINE.svg)](https://www.ine.es/)

*   [English](https://www.ine.es/dyngs/DAB/en/index.htm?cid=1102 "English Page")

   

[](https://www.ine.es/indiceweb.htm "Menú de navegación") ![Image 2: Instituto Nacional de EstadÃ­stica](https://www.ine.es/menus/_b/img/LogoINESiglasMini.svg)

*   [Censo Electoral](https://www.ine.es/dyngs/CEL/index.htm?cid=41)
*   [Sede electrónica](https://sede.ine.gob.es/ss/Satellite?c=Page&cid=1254734719723&pagename=SedeElectronica%2FSELayout&lang=es_ES)
*   [Compartir](javascript:void(0))
    *   [X](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareTwitter "Abre ventana nueva X")
    *   [Facebook](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareFacebook "Abre ventana nueva Facebook")
    *   [Linkedin](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareLinkedin "Abre ventana nueva Linkedin")
    *   [WhatsApp](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareWhatsapp "Abre ventana nueva WhatsApp")
    *   [Correo Electrónico](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareMail "Abre ventana nueva")
    *   [Copiar al portapapeles](https://www.ine.es/dyngs/DAB/index.htm?cid=1102#shareClipboard "Abre ventana nueva")

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   Obtener datos de una tabla
    ==========================
    

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   [Referencia de la API](https://www.ine.es/dyngs/DAB/index.htm?cid=1100)
*   [Lista de funciones](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128)
*   [Obtener datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102)
*   [Otros casos de uso](https://www.ine.es/dyngs/DAB/index.htm?cid=1103)
*   [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)
*   [Base de datos Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
*   [Generador de URLs](https://www.ine.es/dyngs/DAB/index.htm?cid=1347)
*   [Generador de gráficos](https://www.ine.es/dyngs/DAB/index.htm?cid=1348)

Obtener datos de una tabla
--------------------------

Para obtener los datos de una tabla es necesario conocer su código identificativo (acceder a [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)).

Una vez se conoce el código de la tabla de interés, se puede utilizar la función [DATOS\_TABLA](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128) para obtener los datos asociados.

**Obtener todos los datos de la tabla**

Por ejemplo, para la tabla [Índices nacionales: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50902) (Id 50902):

[https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902)

**Obtener los n últimos datos**

Utilizamos el parámetro nult. Por ejemplo nult=5 para obtener los últimos 5 datos:

[https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50902?nult=5](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50902?nult=5)

Como filtrar datos de una tabla
-------------------------------

Cuando realizamos una petición de datos de una tabla existe la posibilidad de filtrar por variables y valores de interés utilizando el parámetro tv. Para ello vamos a distinguir los tres tipos posibles de fuentes de las tablas (tablas Tempus 3, tablas pc-axis y tablas tpx).

*   Tablas Tempus 3
    *   Para poder filtrar es necesario conocer los códigos identificadores numéricos (Id) de las variables y los valores por los que queremos filtrar. Por lo tanto, debemos hacer lo siguiente:
        
        1.  Conocer los grupos de la tabla de interés [Índices por comunidades autónomas: general y de grupos ECOICOP](https://www.ine.es/jaxiT3/Tabla.htm?t=50913) (Id = 50913):
            
            [https://servicios.ine.es/wstempus/js/ES/GRUPOS\_TABLA/50913](https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/50913)
            
        2.  Conocer los valores de los grupos:
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110924?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110924?det=1)
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110925?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110925?det=1)
            
            [https://servicios.ine.es/wstempus/js/ES/VALORES\_GRUPOSTABLA/50913/110926?det=1](https://servicios.ine.es/wstempus/js/ES/VALORES_GRUPOSTABLA/50913/110926?det=1)
            
        3.  Filtrar por la variables y valores que nos interesan:
            
            Por ejemplo, variación anual (id\_variable = 3, id\_valor = 74 y tv=3:74) del índice general (id\_variable = 762, id\_valor = 304092 y tv=762:304092) de Castilla y León (id\_variable = 70, id\_valor = 9003 y tv=70:9003)
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:9003](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:9003)
            
            Si no se especifica ningún valor, se obtienen todos los valores de la variable. Por ejemplo, con tv=70: se obtiene todas las Comunidades Autónomas
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:)
            
            Si queremos filtrar por varios valores de una misma variable, tenemos que incluir tantos parámetros tv como valores. Por ejemplo, para obtener datos tanto de Castilla y León como del Principado de Asturias (id\_variable = 70, id\_valor = 9003 y tv=70:8999)
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:9003&tv=70:8999](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50913?nult=2&tip=A&tv=3:74&tv=762:304092&tv=70:9003&tv=70:8999)
            
*   Tablas tpx
    *   Para poder filtrar es necesario conocer los códigos identificadores alfanuméricos de las variables y los valores por los que queremos filtrar. Por lo tanto, debemos hacer lo siguiente:
        
        1.  Pedir los metadatos de las series que conforman la tabla de interés [Extracción nacional por tipo de material y años](https://www.ine.es/jaxi/Tabla.htm?tpx=33387&L=0)  (Id = 33387)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_TABLA/33387?tip=M](https://servicios.ine.es/wstempus/js/ES/SERIES_TABLA/33387?tip=M)
            
        2.  Filtrar por la variables y valores que nos interesan:
            
            Por ejemplo, para biomasa (id\_variable = tipodematerial, id\_valor = tipodematerial, tv= tipodematerial: tipodematerial
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/33387?nult=2&tv=tipodematerial:1biomasa](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/33387?nult=2&tv=tipodematerial:1biomasa)
            
            Si no se especifica ningún valor, se obtienen todos los valores de la variable. Por ejemplo, con tv=sexo: se obtiene la población de hombres, mujeres y ambos sexos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/33387?nult=2&tv=tipodematerial:](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/33387?nult=2&tv=tipodematerial:)
            
            Si queremos filtrar por varios valores de una misma variable, tenemos que incluir tantos parámetros tv como valores. Por ejemplo, para obtener biomasa y minerales metálicos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/33387?nult=2&tv=tipodematerial:1biomasa&tv=tipodematerial:2mineralesmetalicosmineralenbruto](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/33387?nult=2&tv=tipodematerial:1biomasa&tv=tipodematerial:2mineralesmetalicosmineralenbruto)
            
    *   ### Tablas tpx con códigos identificadores de Tempus 3
        
        Existen tablas tpx que contienen códigos identificadores de Tempus 3 ([Censo agrario 2020](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176851&menu=resultados&idp=1254735727106)). En este caso además de filtrar usando los códigos alfanuméricos, como para una tabla tpx normal, también se puede filtrar utilizando los códigos numéricos Tempus 3 de las variables y los valores. Para ello, debemos hacer lo siguiente:
        
        1.  Pedir lo metadatos de las series que conforman la tabla de interés [Mano de obra en la explotación, familiar y contratada de manera regular, por relación con el titular, porcentaje de unidad de trabajo-año total (UTAT) y sexo](https://www.ine.es/jaxi/Tabla.htm?tpx=52056&L=0) (Id=52056). A la función [SERIES\_TABLA](https://www.ine.es/dyngs/CEL/index.htm?cid=1100#is1156) también le podemos pasar un filtro (útil para tablas con un gran número de series debido a una gran segmentación territorial), por ejemplo total nacional (tv=NAC:00):
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_TABLA/52056?tip=M&tv=NAC:00](https://servicios.ine.es/wstempus/js/ES/SERIES_TABLA/52056?tip=M&tv=NAC:00)
            
        2.  Para utilizar los identificadores numéricos añadimos el alias ~id al final (tv=id\_varaible~id:id\_valor~id). Por ejemplo  para el Total Nacional (tv=349~id:16473~id),  Total tramos UTAT (tv=916~id:391871~id), Nº explotaciones (tv=942~id:274282~id), Total mano de obra (tv=999~id:391770~id) y Valor absoluto (tv=3~id:11406~id) tendríamos:
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/52056?tv=349~id:16473~id&tv=916~id:391871~id&tv=942~id:274282~id&tv=999~id:391770~id&tv=3~id:11406~id](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/52056?tv=349~id:16473~id&tv=916~id:391871~id&tv=942~id:274282~id&tv=999~id:391770~id&tv=3~id:11406~id)
            
*   Tablas pc-axis
    *   Para poder filtrar es necesario conocer los códigos identificadores alfanuméricos (Código) de las variables y los valores por los que queremos filtrar. Por lo tanto, debemos hacer lo siguiente:
        
        1.  Pedir los metadatos de las series que conforman la tabla de interés [Población por edad (3 grupos de edad), Españoles/Extranjeros, Sexo y Año](https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01001.px) (Id = t20/e245/p08/l0/01001.px)
            
            [https://servicios.ine.es/wstempus/js/ES/SERIES\_TABLA/t20/e245/p08/l0/01001.px?tip=M](https://servicios.ine.es/wstempus/js/ES/SERIES_TABLA/t20/e245/p08/l0/01001.px?tip=M)
            
        2.  Filtrar por la variables y valores que nos interesan:
            
            Por ejemplo, para la población de mujeres (id\_variable = sexo, id\_valor = mujeres, tv=sexo:mujeres) españolas (id\_variable = espanolesextranjeros, id\_valor = españoles, tv= espanolesextranjeros:españoles) de todas las edades (id\_variable = edad3gruposdeedad, id\_valor = totaledades, tv=edad3gruposdeedad:totaledades)
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:mujeres&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:mujeres&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades)
            
            Si no se especifica ningún valor, se obtienen todos los valores de la variable. Por ejemplo, con tv=sexo: se obtiene la población de hombres, mujeres y ambos sexos
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades)
            
            Si queremos filtrar por varios valores de una misma variable, tenemos que incluir tantos parámetros tv como valores. Por ejemplo, para obtener la población de hombres y mujeres
            
            [https://servicios.ine.es/wstempus/js/ES/DATOS\_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:mujeres&tv=sexo:hombres&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t20/e245/p08/l0/01001.px?nult=2&tv=sexo:mujeres&tv=sexo:hombres&tv=espanolesextranjeros:espanoles&tv=edad3gruposdeedad:totaledades)
            

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
