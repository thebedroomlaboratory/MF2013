  function updateSliders(){
    $('.socketSwitch').change(function() {
      sendCommands();
    });
  }

  /**
   * Gets all the canvas elements
   */
  function getCanvasElements(){
    return $("canvas");
  }

  /**
   * Get all ids from canvas elements
   */
  function getIdsFromCanvasElements(){
    var canvasElements = getCanvasElements();
    var ids = new Array();
      for(var i=0; i<canvasElements.length; i++){
        ids[i] = sliderInputs[i].id;
      }
    return ids;
  }

  /**
   * Get the context of the chart by id
   */
  function getContextOfCanvasElement(id){
    return document.getElementById(id).getContext("2d");
  }

  /**
   * Get the thermostat data
   */
  function getThermostatData(){
    var json = $.getJSON('getThermostatData.php?id=1', function(data) {
      console.log(data);
      json = data;
    });
    console.log(json);
    return json;    
  }

  /**
   * Get the oven temp data
   */
  function getOvenData(){
    var json =  $.getJSON('getOvenData.php?id=1', function(data) {
      console.log(data);
      return data;
    });
    console.log(json);
    return json;
  }


  /**
   * Get the x axis and y axis data for the oven 
   */
  function plotThermostatGraph(){
    var json = getThermostatData();
    // x axis data
    var dateRange = new Array();
    // y axis data
    var tempRange = new Array();
    // loop over the data
    for(var i=0; i<json.length; i++){
      var elm = json[i];
      dateRange[i] = new Date(elm.time).getHours();
      tempRange[i] = parseInt(elm.temp);
    }
    var data = createGraphData(dateRange, tempRange);
    // get canvas context
    var ctx = getContextOfCanvasElement('thermostat_Line_chart');
    new Chart(ctx).Line(data);
  }

  /**
   * Set up a data object to be used by the graph
   */
  function createGraphData(x,y){
    var data = {
      labels : x,
      datasets : [{
        fillColor : "rgba(151,187,205,0.5)",              
        strokeColor : "rgba(151,187,205,1)",
        pointColor : "rgba(151,187,205,1)",
        pointStrokeColor : "#fff",
        data : y
      }]
    }
    return data;  
  }
