<?php
	include "mysql/class.MfSQL.php";

	$mfSql = new Mf_SQL();
	$mySql = $mfSql->getMySql();
	$people = $mySql->Select('people','','time DESC','2');
    echo json_encode(array_reverse($people));
?>
