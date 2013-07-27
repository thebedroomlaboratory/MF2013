<html>
<head>
<title>Read DB!</title>
<script src="hc/js/jquery.min.js"></script>
<script src="hc/js/highcharts.js"></script>
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

$SQL_OVEN = "SELECT * FROM oven ORDER BY time DESC LIMIT 10";
$SQL_PPL = "SELECT * FROM people ORDER BY time DESC LIMIT 10";
$SQL_TEMP = "SELECT * FROM temp ORDER BY time DESC LIMIT 10";

$result_oven = mysql_query($SQL_OVEN);
$result_ppl = mysql_query($SQL_PPL);
$result_temp = mysql_query($SQL_TEMP);

?>

<h2>People</h2>
<?PHP
$y1 = array();
$y2 = array();
$i=0;
while ( $db_field_ppl = mysql_fetch_assoc($result_ppl) ) {
$y1[$i]=$db_field_ppl['counter'];
$y2[$i]=$db_field_ppl['switch'];
$i++;
}
array_reverse($y1);
array_reverse($y2);
?>

<script>
$(function () { 
    $('#people').highcharts({

        chart: { type : 'line',
                  animation: {
                     duration: 1500,
                     easing: 'easeOutBounce'
                  }
        },

        title: {
            text: 'People Counter'
        },
        xAxis: {
           text: 'Point'
        },
        yAxis: {
            title: {
                text: 'Value'
            }
        },
        series: [{
            name: 'Counter',
            data: [<?php print $y1[0]; ?>, <?php print $y1[1]; ?>, <?php print $y1[2]; ?>, <?php print $y1[3]; ?>, <?php print $y1[4]; ?>, <?php print $y1[5]; ?>, <?php print $y1[6]; ?>, <?php print $y1[7]; ?>, <?php print $y1[8]; ?>, <?php print $y1[9]; ?>]
        }, {
            name: 'Switch',
            data: [<?php print $y2[0]; ?>, <?php print $y2[1]; ?>, <?php print $y2[2]; ?>, <?php print $y2[3]; ?>, <?php print $y2[4]; ?>, <?php print $y2[5]; ?>, <?php print $y2[6]; ?>, <?php print $y2[7]; ?>, <?php print $y2[8]; ?>, <?php print $y2[9]; ?>]
        }]
    });
});
</script>
<div id="people" style="height: 200px; min-width: 500px"></div>
<h2>OVEN</h2>
<?PHP
$y1 = array();
$y2 = array();
$i=0;
while ( $db_field_oven = mysql_fetch_assoc($result_oven) ) {
$y1[$i]=$db_field_oven['temp'];
$y2[$i]=$db_field_oven['status'];
$i++;
}
array_reverse($y1);
array_reverse($y2);
?>

<script>
$(function () { 
    $('#oven').highcharts({

        chart: { type : 'line',
                  animation: {
                     duration: 1500,
                     easing: 'easeOutBounce'
                  }
        },

        title: {
            text: 'Bagel Oven'
        },
        xAxis: {
           text: 'Point'
        },
        yAxis: {
            title: {
                text: 'Value'
            }
        },
        series: [{
            name: 'Temp',
            data: [<?php print $y1[0]; ?>, <?php print $y1[1]; ?>, <?php print $y1[2]; ?>, <?php print $y1[2]; ?>, <?php print $y1[3]; ?>, <?php print $y1[4]; ?>, <?php print $y1[5]; ?>, <?php print $y1[6]; ?>, <?php print $y1[7]; ?>, <?php print $y1[8]; ?>, <?php print $y1[9]; ?>]
        }, {
            name: 'Status',
            data: [<?php print $y2[0]; ?>, <?php print $y2[1]; ?>, <?php print $y2[2]; ?>, <?php print $y2[2]; ?>, <?php print $y2[3]; ?>, <?php print $y2[4]; ?>, <?php print $y2[5]; ?>, <?php print $y2[6]; ?>, <?php print $y2[7]; ?>, <?php print $y2[8]; ?>, <?php print $y2[9]; ?>]
        }]
    });
});
</script>
<div id="oven" style="height: 200px; min-width: 500px"></div>
<h2>Thermostat</h2>
<?PHP
$y1 = array();
$y2 = array();
$y3 = array();
$y4 = array();
$i=0;
while ( $db_field_temp = mysql_fetch_assoc($result_temp) ) {
$y1[$i]=$db_field_temp['override'];
$y2[$i]=$db_field_temp['lux'];
$y3[$i]=$db_field_temp['temp'];
$y4[$i]=$db_field_temp['status'];
$i++;
}
array_reverse($y1);
array_reverse($y2);
array_reverse($y3);
array_reverse($y4);
?>

<script>
$(function () { 
    $('#temp').highcharts({

        chart: { type : 'line',
                  animation: {
                     duration: 1500,
                     easing: 'easeOutBounce'
                  }
        },

        title: {
            text: 'Thermostat'
        },
        xAxis: {
           text: 'Point'
        },
        yAxis: {
            title: {
                text: 'Value'
            }
        },
        series: [{
            name: 'Override',
            data: [<?php print $y1[0]; ?>, <?php print $y1[1]; ?>, <?php print $y1[2]; ?>, <?php print $y1[3]; ?>, <?php print $y1[4]; ?>, <?php print $y1[5]; ?>, <?php print $y1[6]; ?>, <?php print $y1[7]; ?>, <?php print $y1[8]; ?>, <?php print $y1[9]; ?>]
        }, {
            name: 'Light',
            data: [<?php print $y2[0]; ?>, <?php print $y2[1]; ?>, <?php print $y2[2]; ?>, <?php print $y2[3]; ?>, <?php print $y2[4]; ?>, <?php print $y2[5]; ?>, <?php print $y2[6]; ?>, <?php print $y2[7]; ?>, <?php print $y2[8]; ?>, <?php print $y2[9]; ?>]
        }, {
            name: 'Temparature',
            data: [<?php print $y3[0]; ?>, <?php print $y3[1]; ?>, <?php print $y3[2]; ?>, <?php print $y3[3]; ?>, <?php print $y3[4]; ?>, <?php print $y3[5]; ?>, <?php print $y3[6]; ?>, <?php print $y3[7]; ?>, <?php print $y3[8]; ?>, <?php print $y3[9]; ?>]
        }, {
            name: 'Status',
            data: [<?php print $y4[0]; ?>, <?php print $y4[1]; ?>, <?php print $y4[2]; ?>, <?php print $y4[3]; ?>, <?php print $y4[4]; ?>, <?php print $y4[5]; ?>, <?php print $y4[6]; ?>, <?php print $y4[7]; ?>, <?php print $y4[8]; ?>, <?php print $y4[9]; ?>]
        }]
    });
});
</script>
<div id="temp" style="height: 200px; min-width: 500px"></div>

<?PHP

mysql_close($db_handle);

}
else {

print "Database NOT Found ";
mysql_close($db_handle);

}

?>
</body>
</html>
