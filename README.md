# CovidMaps
Proyecto Final Telemática 2020
# Descripción
Es un servidor de página web basada en contenedores el cual ofrecerá información en tiempo real acerca de los casos locales de covid-19 (dependiendo de la ubicación del usuario en la localidad especificada) y mediante métodos algorítmicos le informará el número de casos que hay en una zona de Medellín. Los lenguajes que se usarán para la app web serán python, html y SQL (La interfaz gráfica sera una página web con html)
# ARQUITECTURA
   # Dockerfile
   Este archivo directamente relacionado con el contenedor se encargará de ejecutar las instrucciones necesarias al momento de montar el servidor. Levantara los servicios necesarios y ejecutará el .py por debajo de memoria (Este archivo no se implemento en la entrega final)
   # index.html
   Este archivo de hipertexto contendrá la interfaz de entrada que verá el usuario. Aca se obtendran los datos del usuario como el nombre y la edad, incluyendo su localización actual y si ha tenido covid-19; y se redireccionará al archivo proyect.py. (Este archivo estará en un directorio llamada templates)
   # bdtesting.py
   Aca se contendrá el cuerpo del proyecto (se utilizará la libreria flask de python). En este archivo se obtendrán los datos enviados por el index.html mediante el método POST y a partir de estos se buscará en las Bases de datos la información de los casos de covid-19 de la localidad para realizar el gráfico y el analisis por zonas. Si según los datos ingresados el usuario tiene covid-19 o sospecha de ello entonces su información se añadira a la base de datos. (Se implementaron dos bases de datos: La primera es una base de datos basada en una hoja de cálculo dada por el municipio y la otra es una base de datos en sqlite3 que almacena las localizaciones de las personas con covid-19 que ingresan a la página)
   # BaseDatos2.db
   Esta base de datos tendrá la información de los casos confirmados de covid-19 dadas por los usuarios que ingresen a la página
   # BaseDeDatosValleDeAburra100%realNoFake.xls
   Esta hoja de cálculo contiene las ubicaciones de los casos confirmados de covid-19 dados por el municipio (Un dummy data)
   # Contenedor en docker
   En el contenedor se almacenarán los archivos ya mencionados en el ubuntu que se usará para el servicio (se tendrá ya instalados el      flask, el pip y la versión de python que se necesitan para soportar el servicio además de la versión apache que se necesita). Así al    momento de levantar una imagen en memoría lo único que se hará es levantar el servicio (No implementado en el proyecto final)
   # Tipo de servidor y Firewall
   La página web funcionará en un servidor web http (Se usará la libreria flask de python para soportar la página). Se usuará el UFW como el firewall del sistema habilitando el puerto 80. Si el servicio se va montar en una red de servidores en la nube (como AWS) se activara el puerto 22 y se haran las configuraciones de los grupos de seguridad respectivos. El SO que se usara será un Ubuntu Server 18.04
