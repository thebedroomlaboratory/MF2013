<?php
	include "mysql/class.MfSQL.php";

	$mfSql = new Mf_SQL();
	$mySql = $mfSql->getMySql();
	$temp = $mySql->Select('temp','','time DESC','10');
    echo json_encode(array_reverse($temp));
?>