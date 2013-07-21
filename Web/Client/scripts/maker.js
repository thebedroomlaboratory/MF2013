/*
// This just displays the first parameter passed to it
// in an alert.
function show(json) {
	alert(json);
}

function run() {
	$.getJSON(
	"/maker/hello.php", // The server URL 
	{ id: 567 }, // Data you want to pass to the server.
	show // The function to call on completion.
	);
}
*/

$(function(ready){
    $('.socketSwitch').change(function() {
        sendCommands();
    });

    populateGraphs();

});


function populateGraphs(){

	//Thermostat
	//Get the context of the canvas element we want to select
	var thermostat_ctx = $("#thermostat_Line_chart").get(0).getContext("2d");
	//var myNewChart = new Chart(thermostat_ctx);
	var data = {
	labels : ["January","February","March","April","May","June","July"],
	datasets : [
					{
						fillColor : "rgba(151,187,205,0.5)",
						strokeColor : "rgba(151,187,205,1)",
						pointColor : "rgba(151,187,205,1)",
						pointStrokeColor : "#fff",
						data : [28,48,40,19,96,27,100]
					}
				]
			}
	var myNewChart = new Chart(thermostat_ctx).Line(data);
	//fitToContainer(document.querySelector('canvas'));


	//Oven
	var data2 = [
	{
		value: 30,
		color:"white"
	},
	{
		value : 120,
		color : "red"
	}

]
	//Thermostat
	//Get the context of the canvas element we want to select
	var oven_ctx = $("#Oven_Line_chart").get(0).getContext("2d");
	//var myNewChart = new Chart(thermostat_ctx);
	var ovenChart = new Chart(oven_ctx).Doughnut(data2);
	fitToContainer(document.querySelector('canvas'));

	var ovenTempChart_ctx = $("#oven_temp_chart").get(0).getContext("2d");
	var ovenTempChart = new Chart(ovenTempChart_ctx).Line(data);


}

function fitToContainer(canvas){
  canvas.style.width='100%';
  canvas.style.height='100%';
  canvas.width  = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
}
