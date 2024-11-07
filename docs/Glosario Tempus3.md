# Glosario Tempus3

Fuente: https://www.ine.es/dyngs/DataLab/manual.html?cid=64

Para hacer un uso adecuado del servicio es necesario describir los siguientes conceptos, cuyos identificadores serán los **inputs** (valores de entrada) en la construcción de URLs.

La información en el Sistema se estructura en torno a la serie temporal, como elemento principal de Tempus3, y se organiza de la siguiente forma:

Variables

Una **variable** es una característica que puede fluctuar y cuya variación es susceptible de adoptar diferentes valores.

Las **variables o listas de valores** contenidas en Tempus3 y utilizadas en la difusión, son comunes a todas las operaciones estadísticas, es decir, no están duplicadas en el sistema, su identificador en Tempus3 **(Id)** y sus descriptores son únicos.

Un de estos descriptores es el campo **codigo** que contiene, en el caso de existir, el identificador estándar de la variable. Es conveniente que las definiciones y codificaciones de ciertas variables estadísticas sean siempre las mismas.  A día de hoy pocas de estas listas son un estándar aprobado por el INE pero estamos trabajando junto con la S.G de Metodología con el fin de conseguir su paulatina normalización.

Son ejemplos de variables las listas: _Grupos COICOP,  Sexo, CCAA,  Provincias_,...

![Image 1: variable](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/variable.jpg)

Valores

Los **valores** son los estados que puede presentar una variable determinada. Por ejemplo, la variable _Provincias_ contiene los valores: _Áraba/Álava_,  _Albacete,_ _Alicante/Alacant_,...etc.

Los **valores** contenidos en Tempus3 y utilizados en la difusión, son comunes a todas las operaciones estadísticas, es decir, no están duplicadas en el sistema, su identificador en Tempus3 **(Id)** y sus descriptores son únicos.

Un de estos descriptores es el campo **codigo** que contiene, en el caso de existir, el identificador estándar del valor. Es conveniente que las definiciones y codificaciones de ciertos valores estadísticos sean siempre las mismas.  A día de hoy pocas de estas listas son un estándar aprobado por el INE pero estamos trabajando junto con la S.G de Metodología con el fin de conseguir su paulatina normalización.

![Image 2: valores](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/valores.jpg)

Series

**¿Qué son las series temporales?**

Conjunto de observaciones medidas en determinados momentos del tiempo, ordenados cronológicamente y normalmente espaciados entre sí de manera uniforme.

Como entidad principal de la base de datos Tempus3, la serie tiene unas propiedades que la definen y que no cambian a lo largo del tiempo:

**Identificador único y características de la serie:** _id, nombre, periodicidad, escala, unidad, clasificación, decimales,.._

![Image 3: Identificador único y características de la serie](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/serie_prop.jpg)

Pero un literal o un id nos dice poco. Para dotar a la serie de significado, necesitamos definirla por una combinación de variables-valores, lo que llamaremos los _metadatos de la serie._

La serie _"Variación mensual del IPC en Andalucía"_ es el resultado del cruce de los valores Total _(de la variable Grupos COICOP)_, Andalucía _(de la variable CCAA)_, variación mensual _(de la variable Tipo de dato),.._

![Image 4: variables-valores](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/variables_valores.jpg)

![Image 5: variables-valores serie](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/meta_serie.jpg)

Tablas

Una de las ventajas de este Sistema es la facilidad que ofrece a la hora de gestionar las diferentes formas de presentación, que corresponden a las distintas formas en las que se pueden agrupar las series. Una de ellas es la agrupación en **tabla** (o cubo). Es la más utilizada por los usuarios, que acceden a las tablas estadísticas a través de INEbase.

Una tabla es el resultado del cruce de grupos de valores contenidos en una o varias variables, es decir, son una agrupación de series temporales definidas por estos grupos.

Por ejemplo, se navega por [INEbase](https://www.ine.es/inebmenu/indice.htm "Enlace a INEbase. Abre ventana nueva") para llegar a la tabla "Índices por comunidades autónomas de subgrupos" del Índice de Precios de Consumo, Base 2011.

[![Image 6: Tabla de INEbase](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/Tabla_seleccion_INEbase.jpg)](https://www.ine.es/dynt3/inebase/index.htm?padre=1935)

Una vez se ha accedido a la tabla, se observa que ésta contiene todas las series que resultan de la combinación de los grupos de valores contenidos en las siguientes variables:

**{Comunidades Autónomas} x {Subgrupos} x {Tipo de dato}**

Como entidad, la tabla tiene unas características propias como nombre, los periodos que comprende su un identificador que es único.

Fecha de publicación

Los datos en Tempus3 se publican a nivel de serie y están asociados a un instante de tiempo o **fecha de referenci**a **(periodo /año)**

![Image 7: Publicación](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/fecharef.jpg)

Pero..**¿cuándo se publican los datos? ¿cuándo se actualizan?**

Cada operación tiene asociada una o varias **publicaciones** según sus diferentes periodicidades, por ejemplo, hay dos publicaciones para el IPC, una con periodicidad mensual y otra anual. Y éstas siguen el calendario de publicaciones del INE.

De esta manera, una **publicación** contiene los momentos en los que se publican los datos de una operación estadística: **fechas de publicación**.

![Image 8: Fechas publicación](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/fechas_publi.jpg)

Con el identificador de la publicación se puede consultar la **fecha de publicación** de todas las operaciones estadísticas que se disponen en el calendario de publicaciones. Cada una de estas **fechas de publicación** tiene unas características:

![Image 9: Publicación](https://www.ine.es/menus/plantillas/webcontent/img/DataLab/publicacion.jpg)
