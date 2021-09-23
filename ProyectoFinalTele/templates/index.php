<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, 
    initial-scale=1.0">
    <title>CovidMaps</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <link href="css/style.css" rel='stylesheet' type='text/css' />
</head>

<body>
    <div class=container>
        <h1>Bienvenido</h1>
        <form method="POST" action="/usuario">
            <legend>Datos personales</legend>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">Nombre: </span>
                <input name="nombre" class="form-control" type="text" />
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">Apellidos: </span>
                <input name="apellidos" class="form-control" type="text" />
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">*Sexo: </span>
                <select class=form-control name="sexo" required>
                    <option value="hombre">Hombre</option>
                    <option value="mujer">Mujer</option>
                </select>
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">*Edad: </span>
                <input class=form-control name="edad" type="text" required />
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">Email: </span>
                <input class=form-control name="email" type="email" />
            </div>

            <?php
                // Incluimos los datos de conexión
                require_once('datosConexion.php');
            ?>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon3">*Localidad: </span>

                <select name="localidad" class=form-control>
                            <?php
                                $localidades = $db_cxn->select(
                                    "localidades",
                                    [
                                        "id_localidad",
                                        "nombre_localidad"
                                    ],
                                    [
                                        "ORDER" => ["id_localidad"]
                                    ]
                                );

                                foreach($localidades as $localidad)
                                {                                    
                                    echo ('<option value="'. $localidad["id_localidad"] .'">'. $localidad["nombre_localidad"] . '</option>\n');
                                    echo ("\n");                                    
                                }    
                            ?>            
                </select>

                <!-- <select class=form-control name="localidad" required>
                    Opciones
                </select> -->

                <!--Sería buena idea tener una Tabla en la BD de localidad para ajustar esta parte como desplegable
                    y trabajar esto en un PHP-->
            </div>
            <div class=form-group>
                <legend>*¿Ha tenido Coronavirus?</legend>
                <div class="radio">
                    <label><input class="form-check-input" type="radio" name="corona" value=SI> Sí </label>
                </div>
                <div class="radio">
                    <label><input class="form-check-input" type="radio" name="corona" value="NO" checked> No </label>
                </div>
                <input type="submit" title="Enviar" required>
            </div>
    </div>
    </form>
    <!-- Script para mostrar las coordenadas-->

</body>

</html>