/*  	Control Center related functions	*/
function getCommands(){
	var isHeatOn = $('#heat_onoffswitch').is(':checked')  === true?2:0;
	var isLightOn = $('#light_onoffswitch').is(':checked') === true?1:0;
	var isOvenOn = $('#oven_onoffswitch').is(':checked') === true?1:0;
	return String(isHeatOn)+String(isLightOn)+String(isOvenOn);		
}//End of getCommands()

function sendCommands()
{
  	commands = getCommands();	
    var connection=new WebSocket("ws://localhost:9090/ws");
    connection.onopen = function () {
      connection.send(commands); //send a message to server once connection is opened.
    };
    connection.onerror = function (error) {
      console.log('Error Logged: ' + error); //log errors
    };
    connection.onmessage = function (e) {
      console.log('Received From Server: ' + e.data); //log the received message
    };
    connection.onclose = function(){
    	console.log('connection closed');
    };
}//End of sendCommands()

/*		End of Control Center related functions		*/
