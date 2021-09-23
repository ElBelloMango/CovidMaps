<?php

require 'Medoo.php';  

use Medoo\Medoo;

$nombreDB = '../BD/CovidMaps.db'; // coloque aqui la dirección IP del servidor PostgreSQL


//$db_cxn = new PDO('pgsql:host='.$servidor.';port='.$puerto.';dbname='.$nombreDB.';user='.$usuario.';password='.$passwd);

$db_cxn = new Medoo([
	// required
	'database_type' => 'sqlite',
	'database' => $nombreDB
	]
);

?>





