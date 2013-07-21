function getSliderValue(id){
  return $('#'+id).is(':checked') === true;
}

function getInputDomObjects(){
  return $("input:checkbox");
}

function getIdsFromSocketInputs(){
  var sliderInputs = getInputDomObjects();
  var ids = new Array();
  for(var i=0; i<sliderInputs.length; i++){
    // input has socketSwitch class
    if($(sliderInputs[i]).hasClass('socketSwitch')){
      ids[i] = sliderInputs[i].id;
    }
  }
  return ids;
}

function populateJsonMessage(){
  var jsonObj = {};
  var ids = getIdsFromSocketInputs();
  for(var i=0; i<ids.length; i++){
    jsonObj[ids[i]] = getSliderValue(ids[i]) ;
  }
  return JSON.stringify(jsonObj);
}

function sendCommands()
{
  var jsonMessage = populateJsonMessage();
  console.log(jsonMessage);
  var connection=new WebSocket("ws://localhost:9090/ws");
  connection.onopen = function () {
    connection.send(jsonMessage); //send a message to server once connection is opened.
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
