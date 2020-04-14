# CovidMaps
Proyecto de telematica con la idea de mostrar en tiempo real las estadisticas acerca del Covid19 en la localidad en la que se conecte el usuario que entre a la pagina, mostrando estadisticas tales como el riesgo de contagio, cantidad de contagiados en una zona, etc.
# Contenedor Y DockerFile
El contenedor subido con el DockerFile contiene el archivo HTML de la pagina web, que recibe la localizacion aproximada del usuario (por el dispositivo o por la IP, aun está por definirse) y muestra la informacion correspondiente.
# HTML
Los archivos HTML basados en HTTP implementando Python se encargara de la pagina web para mostrar la informacion correspondiente, luego de tomar la ubicacion del cliente, hablo de varios HTML en caso de que haga falta varios archivos para mostrar cada informacion o hacer acciones correspondientes.
