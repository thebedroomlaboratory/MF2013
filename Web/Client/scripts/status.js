$(function(ready){
    $('.socketSwitch').change(function() {
        //sendCommands();
    });
    //populateGraphs();
    //updateCCInfo();
	setInterval( function(){
		//updateCCInfo();
		updateStatus();
	}, 1000);
});

function updateStatus(){
	 $('#light_status').html(getLightStatus());
	 $('#heating_status').html(getHeatingStatus());	    
	 $('#oven_status').html(getOvenStatus());
}

function getLightStatus() {
	var result = null;
    $.ajax({
    	async: false,
    	url: "getPeopleData.php",
        data: "id=1",
        dataType: "json",
        success: function(data){
            console.log(data);
            // x axis data
            var x = new Array();
            // y axis data
            var status = new Array();
            var json = data;
            var elm = json[0];
            x[0] = 0;
            status[0] = parseInt(elm.switch);
            console.log("dateRange["+0+"] "+x[0]+" | "+status[0]);
            if(status[0]===1){
            	result="The lights are on!"
            }
            else {
            	result="The lights are off."
            }
        }});     
	console.log("Test - "+result);
	return result;
}

function getHeatingStatus() {
	var result = null;
    $.ajax({
    	async: false,
    	url: "getThermostatData.php",
        data: "id=1",
        dataType: "json",
        success: function(data){
            console.log(data);
            // x axis data
            var x = new Array();
            // y axis data
            var status = new Array();
            var json = data;
            var elm = json[0];
            x[0] = 0;
            status[0] = parseInt(elm.status);
            console.log("dateRange["+0+"] "+x[0]+" | "+status[0]);
            if(status[0]===1){
            	result="The heating is on!"
            }
            else {
            	result="The heating is off."
            }
        }});     
	console.log("Test - "+result);
	return result;
}


function getOvenStatus() {
	var result = null;
    $.ajax({
    	async: false,
    	url: "getOvenData.php",
        data: "id=1",
        dataType: "json",
        success: function(data){
            console.log(data);
            // x axis data
            var x = new Array();
            // y axis data
            var status = new Array();
            var json = data;
            var elm = json[0];
            x[0] = 0;
            status[0] = parseInt(elm.status);
            console.log("dateRange["+0+"] "+x[0]+" | "+status[0]);
            if(status[0]===1){
            	result="The oven is on!"
            }
            else {
            	result="The oven is off."
            }
        }});     
	console.log("Test - "+result);
	return result;
}
