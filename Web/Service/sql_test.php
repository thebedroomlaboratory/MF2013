<?php
include "mysql/class.MfSQL.php";
?>
<!DOCTYPE html>
<html>
	<head>
    <script type="text/javascript">
    function getOvenJson() {
 		var json = <?php			
 			$mfSql = new Mf_SQL();
 			$mySql = $mfSql->getMySql();
 			$oven = $mySql->Select('oven');
 			echo json_encode($oven);
 		?>;
 		var jsonString = JSON.stringify(json);
		alert(jsonString);      
    }

    function getPeopleJson(){
  		var json = <?php			
 			$mfSql = new Mf_SQL();
 			$mySql = $mfSql->getMySql();
 			$people = $mySql->Select('people');
 			echo json_encode($people);
 		?>;
 		var jsonString = JSON.stringify(json);
		alert(jsonString);    	
    }

     function getTempJson(){
  		var json = <?php 			
 			$mfSql = new Mf_SQL();
 			$mySql = $mfSql->getMySql();
 			$temp = $mySql->Select('temp');
 			echo json_encode($temp);
 		?>;
 		var jsonString = JSON.stringify(json);
		alert(jsonString);    	
    }
    </script>
	</head>
<body>
<title>SQL Test</title>
<h1>SQL Databases</h1>
<button onclick="getOvenJson();">Oven</button>
<button onclick="getPeopleJson();">People</button>
<button onclick="getTempJson();">Temperature</button>
</p>
</body>
</html>