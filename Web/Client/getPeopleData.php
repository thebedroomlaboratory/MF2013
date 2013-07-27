<?php
	include "mysql/class.MfSQL.php";
	include "debug/ChromePhp.php";

	$mfSql = new Mf_SQL();
	$mySql = $mfSql->getMySql();
	$people = $mySql->Select('people','','time DESC','10');
    echo json_encode(array_reverse($people));
?>