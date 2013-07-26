<html>
<head>
<title>Read DB!</title>
<script type="text/JavaScript">
function refresh(delay) {
	setTimeout("location.reload(true);",delay);
}
</script>
</head>
<body onload="refresh(1000);">
<?PHP

$user_name = "root";
$password = "password";
$database = "tbl_mf2013";
$server = "127.0.0.1";

$db_handle = mysql_connect($server, $user_name, $password);
$db_found = mysql_select_db($database, $db_handle);

if ($db_found) {

$SQL_OVEN = "SELECT * FROM oven ORDER BY time DESC LIMIT 2";
$SQL_PPL = "SELECT * FROM people ORDER BY time DESC LIMIT 2";
$SQL_TEMP = "SELECT * FROM temp ORDER BY time DESC LIMIT 2";

$result_oven = mysql_query($SQL_OVEN);
$result_ppl = mysql_query($SQL_PPL);
$result_temp = mysql_query($SQL_TEMP);

?>
<h2>People</h2>
<?PHP

while ( $db_field_ppl = mysql_fetch_assoc($result_ppl) ) {

print $db_field_ppl['time'] . "<BR>";
print $db_field_ppl['counter'] . "<BR>";
print $db_field_pp['switch'] . "<BR>";

}

?>
<h2>OVEN</h2>
<?PHP

while ( $db_field_oven = mysql_fetch_assoc($result_oven) ) {

print $db_field_oven['time'] . "<BR>";
print $db_field_oven['temp'] . "<BR>";
print $db_field_oven['status'] . "<BR>";

}
?>
<h2>TEMP</h2>
<?PHP
while ( $db_field_temp = mysql_fetch_assoc($result_temp) ) {

print $db_field_temp['time'] . "<BR>";
print $db_field_temp['override'] . "<BR>";
print $db_field_temp['lux'] . "<BR>";
print $db_field_temp['temp'] . "<BR>";
print $db_field_temp['status'] . "<BR>";

}

mysql_close($db_handle);

}
else {

print "Database NOT Found ";
mysql_close($db_handle);

}

?>
</body>
</html>
