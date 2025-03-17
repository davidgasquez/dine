API JSON / API JSON
===============               

[![Image 1: SIGLAS Instituto Nacional de Estadística](https://www.ine.es/menus/_b/img/LogoINE.svg)](https://www.ine.es/)

*   [English](https://www.ine.es/dyngs/DAB/en/index.htm?cid=1099 "English Page")

   

[](https://www.ine.es/indiceweb.htm "Menú de navegación") ![Image 2: Instituto Nacional de EstadÃ­stica](https://www.ine.es/menus/_b/img/LogoINESiglasMini.svg)

*   [Censo Electoral](https://www.ine.es/dyngs/CEL/index.htm?cid=41)
*   [Sede electrónica](https://sede.ine.gob.es/ss/Satellite?c=Page&cid=1254734719723&pagename=SedeElectronica%2FSELayout&lang=es_ES)
*   [Compartir](javascript:void(0))
    *   [X](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareTwitter "Abre ventana nueva X")
    *   [Facebook](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareFacebook "Abre ventana nueva Facebook")
    *   [Linkedin](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareLinkedin "Abre ventana nueva Linkedin")
    *   [WhatsApp](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareWhatsapp "Abre ventana nueva WhatsApp")
    *   [Correo Electrónico](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareMail "Abre ventana nueva")
    *   [Copiar al portapapeles](https://www.ine.es/dyngs/DAB/index.htm?cid=1099#shareClipboard "Abre ventana nueva")

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   API JSON
    ========
    

*   [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)
*   [Referencia de la API](https://www.ine.es/dyngs/DAB/index.htm?cid=1100)
*   [Lista de funciones](https://www.ine.es/dyngs/DAB/index.htm?cid=1100#is1128)
*   [Obtener datos de una tabla](https://www.ine.es/dyngs/DAB/index.htm?cid=1102)
*   [Otros casos de uso](https://www.ine.es/dyngs/DAB/index.htm?cid=1103)
*   [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104)
*   [Base de datos Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
*   [Generador de URLs](https://www.ine.es/dyngs/DAB/index.htm?cid=1347)
*   [Generador de gráficos](https://www.ine.es/dyngs/DAB/index.htm?cid=1348)

API JSON
--------

**Servicio web para la consulta de INEbase con salida en formato JSON**

El servicio API JSON INE (Java Script Object Notation) que se describe en esta sección permite acceder mediante peticiones URL a toda la información disponible en INEbase, sistema que utiliza el Instituto Nacional de Estadística (INE) para la publicación de la información estadística.

La estructura de las peticiones a través de URL y la simplicidad del formato JSON permiten la explotación automática de la información estadística.

INEbase es el sistema que utiliza el INE para la publicación de la información estadística. La información que será accesible a través del servicio API JSON del INE proviene de tres fuentes distintas:

*   Base de datos [Tempus3](https://www.ine.es/dyngs/INE/index.htm?cid=1105).
*   Repositorio de archivos [PC-Axis](https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735116596&p=1254735116596&pagename=ProductosYServicios%2FPYSLayout).
*   Repositorio de archivos tpx.

Para saber si una tabla estadística está almacenada en Tempus3, en el repositorio de archivos PC-Axis o en el repositorio de archivos tpx, consultar [Códigos identificadores de tablas y series](https://www.ine.es/dyngs/DAB/index.htm?cid=1104).

Toda la información publicada por el INE, independientemente de la fuente, va a poder ser consultada a través de la API JSON.

Paquete de R
------------

Se dispone del [paquete INEapir](https://github.com/es-ine/ineapir) para interactuar con la API JSON.

Para facilitar el acceso a la información que la API JSON proporciona se ha desarrollado un paquete de R que pone a disposición de los usuarios un conjunto de funciones para obtener datos y metadatos a través de llamadas a la propia API. El paquete INEapir incorpora todas las funcionalidades de ésta última y permite realizar las mismas consultas, desde las más generales a las más precisas, utilizando también los parámetros opcionales, pero con la ventaja de obtener la información directamente en los desarrollos realizados en R. Además, el paquete dispone de una página web con documentación y ejemplos de uso.

[![Image 3: INEapir](https://www.ine.es/GS_FILES/hex_logo_INEapir.png)](https://github.com/es-ine/ineapir)     [![Image 4: Cheatsheet](https://www.ine.es/GS_FILES/ineapir_thumbnail_p.png)](https://raw.githubusercontent.com/es-ine/ineapir/main/man/figures/ineapir.pdf)

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
