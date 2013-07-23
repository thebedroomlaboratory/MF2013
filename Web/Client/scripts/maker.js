/**
	This Script is a Prototype only. It is for proof of concept only and lacks proper design. Futher version expected to be implemented using Angularjs.

	functions in updateCCInfo() are currently hardcoded. as are the populateGraphs() and timer() fucnctions.
*/

$(function(ready){
    $('.socketSwitch').change(function() {
        sendCommands();
    });
    populateGraphs();
	    updateCCInfo();
setInterval( function(){updateCCInfo();}
	, 5000);
});
function updateCCInfo(){
	 getPeopleCounter();
	    setCurrentTemp();	    
	    setSomeoneHome();
	    setDayNight();
	    setBagelStatus();
}
function setCurrentTemp(){
	$('#currentTemp').html('16 degrees C');
}
function setSomeoneHome(){
	$('#someneHome_indicator').html('Someone is home');
	var heating_status = 'On';
	$('#heating_status_display').html(heating_status);
	var pplCount = 1;
	$('#people_count_indicator').html(pplCount);

}
var n=1;
function setBagelStatus(){
	$('#bagelStatus').html('queued');
	var currentCookTime = 'Cooking Time: '+n+' mins';
	$('#cookingTime_indicator').html(currentCookTime);
	n++;

}

function setDayNight(){
	$('#dayNight_indicator').html('Dark');
	var lights_indicator = "ON";
	$('#lights_indicator').html(lights_indicator);
}

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

function getPeopleCounter(){

	var peopleCounterGraph_ctx = $("#peopleCounter_Line_chart").get(0).getContext("2d");
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
	var pplChart = new Chart(peopleCounterGraph_ctx).Line(data);

}

function fitToContainer(canvas){
  canvas.style.width='100%';
  canvas.style.height='100%';
  canvas.width  = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
}
function timer(time){
	//Oven
	var colorTime = "blue";
	if(time<=20){
		colorTime = "orange"
	}
	if(time<=10){
		colorTime = "red"
	}

	if(time>0){
		var mydata = [
		{
			value: (100-time),
			color:"white"
		},
		{
			value : time,
			color : colorTime
		}
		];

		redrawDonut(mydata);
		time--;
		setTimeout(function(){
		timer(time);
			}, 1000);
	}
	else{
		if($('#oven_onoffswitch').is(':checked')){
          $('#oven_onoffswitch').prop('checked', false);;
     }else{
          $('#oven_onoffswitch').prop('checked', true);;
     }
			//$('.socketSwitch').change();
		
		return;
	}
}

function redrawDonut(data){

	//var canvas = $("#oven_temp_chart");
	var oven_ctx = $("#Oven_Line_chart").get(0).getContext("2d");
	options = {
		//Boolean - Whether we should animate the chart	
		animation : false
	}
	var ovenChart = new Chart(oven_ctx).Doughnut(data, options);
}
