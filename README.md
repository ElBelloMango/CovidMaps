# CovidMaps
Proyecto Sistemas Empresariales 2021 (Producto Mínimo Viable)
# Descripción
Es un servidor de página web  el cual ofrecerá información en tiempo real acerca de los casos locales de covid-19 (dependiendo de la ubicación del usuario en la localidad especificada) y mediante métodos algorítmicos le informará el número de casos que hay en una zona de Medellín. Los lenguajes que se usarán para la app web serán python, html y SQL (La interfaz gráfica sera una página web con html)
# Resumen
CovidMaps busca colocar en un mapa digital puntos con una ubicación aproximada de los contagiados a nivel local. La ubicación dada no será exactamente el lugar donde el contagiado está hospedado, pues hay que proteger la identidad de los usuarios de la aplicación por diversas razones como evitar marginaciones, proteger su identidad privada, etc.
# Idea de Negocio
Se tendrán dos versiones del modelo, una estándar con publicidad abierta para todo el público y otra como versión paga sin publicidad y con funciones exclusivas para empresas.

En la versión estándar generaremos ganancias por medio del hosting de anuncios.
# ARQUITECTURA
  
   # index.html
   Este archivo de hipertexto contendrá la interfaz de entrada que verá el usuario. Aca se obtendran los datos del usuario como el nombre y la edad, incluyendo su localización actual y si ha tenido covid-19; y se redireccionará al archivo proyect.py. (Este archivo estará en un directorio llamada templates)
   # covidmaps.py
   Aca se contendrá el cuerpo del proyecto (se utilizará la libreria flask de python). En este archivo se obtendrán los datos enviados por el index.html mediante el método POST y a partir de estos se buscará en las Bases de datos la información de los casos de covid-19 de la localidad para realizar el gráfico y el analisis por zonas. Si según los datos ingresados el usuario tiene covid-19 o sospecha de ello entonces su información se añadira a la base de datos. (Se implementaron dos bases de datos: La primera es una base de datos basada en una hoja de cálculo dada por el municipio y la otra es una base de datos en sqlite3 que almacena las localizaciones de las personas con covid-19 que ingresan a la página)


   # Tipo de servidor y Firewall
   La página web funcionará en un servidor web http (Se usará la libreria flask de python para soportar la página). Se usuará el UFW como el firewall del sistema habilitando el puerto 80. Si el servicio se va montar en una red de servidores en la nube (como AWS) se activara el puerto 22 y se haran las configuraciones de los grupos de seguridad respectivos. El SO que se usara será un Ubuntu Server 18.04