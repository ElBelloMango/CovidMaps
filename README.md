# CovidMaps
Proyecto Final Telemática 2020
# Descripción
Es un servidor de página web basada en contenedores el cual ofrecerá información en tiempo real acerca de los casos locales de covid-19 (dependiendo de la ubicación del usuario en la localidad especificada) y mediante métodos estadísticos (grafos) le informará si es o no seguro salir. Los lenguajes que se usarán para la app web serán python, html y SQL (La interfaz gráfica sera una página web con html)
# ARQUITECTURA
   # Dockerfile
   Este archivo directamente relacionado con el contenedor se encargará de ejecutar las instrucciones necesarias al momento de montar el servidor. Levantara los servicios necesarios y ejecutará el .py por debajo de memoria
   # index.html
   Este archivo de hipertexto contendrá la interfaz de entrada que verá el usuario. Aca se obtendran los datos del usuario como el nombre y la edad, incluyendo su localización actual y si ha tenido covid-19; y se redireccionará al archivo proyect.py
   # proyect.py
   Aca se contendrá el cuerpo del proyecto (se utilizará la libreria flask de python). En este archivo se obtendrán los datos enviados por el index.html mediante el método POST y a partir de estos se buscará en la Base de datos la información de los casos de covid-19 de la localidad para realizar el gráfico y el analisis de Riesgo. Si según los datos ingresados el usuario tiene covid-19 o sospecha de ello entonces su información se añadiran con un poco menos de peso en la base de datos. (Recordar que la base de datos esta basado en grafos, por lo que cada usuario agregado se añadira como un nodo al grafo y se relacionará con el nodo de su localidad)
   # BaseDatos.db
   Esta base de datos tendrá la información de los casos confirmados de covid-19 en Medellín incluyendo los datos dados por los usuarios enfermos o con sospechas. Esta base de datos estará formada a partir del grafo construido
   # Contenedor en docker
   En el contenedor se almacenarán los archivos ya mencionados en el ubuntu que se usará para el servicio (se tendrá ya instalados el      flask, el pip y la versión de python que se necesitan para soportar el servicio además de la versión apache que se necesita). Así al    momento de levantar una imagen en memoría lo único que se hará es levantar el servicio 
   # Tipo de servidor y Firewall
   La página web funcionará en un servidor web http (Se usará la libreria flask de python para soportar la página). Se usuará el UFW como el firewall del sistema habilitando el puerto 80. Si el servicio se va montar en una red de servidores en la nube (como AWS) se activara el puerto 22 y se haran las configuraciones de los grupos de seguridad respectivos
   

