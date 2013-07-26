<?php
  include "mysql/class.MfSQL.php";
?>
<html>
    <head>
        <script type="text/javascript" src="scripts/jquery-2.0.3.js"></script>
        <script type="text/javascript" src="scripts/controlCenter.js" ></script>
        <script type="text/javascript" src="scripts/maker2.js" ></script>
        <script type="text/javascript" src="scripts/Chart.js"></script>
        <script type="text/javascript">
        $(function(){
          // check the sliders
          updateSliders();
          // plot the graphs
          plotOvenTempGraph();
          // TODO: plotPeopleCounterGraph()
          // TODO: plotOvenGraph()
        });
        

        /**
         * If the sliders have changed, make web socket call
         */
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
         * Get the x axis and y axis data for the oven 
         */
        function plotOvenTempGraph(){
          var json = getLast10DescendingOvenValues();
          // x axis data
          var index = new Array();
          // y axis data
          var tempRange = new Array();
          // loop over the data
          for(var i=0; i<json.length; i++){
            var elm = json[i];
            index[i] = i;
            tempRange[i] = parseInt(elm.temp);
          }
          var data = createGraphData(index, tempRange);
          // get canvas context
          var ctx = getContextOfCanvasElement('oven_temp_chart');
          new Chart(ctx).Line(data);
        }


        /**
         * Create graph data
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

        /**
         ***********************
         ***** MySQL Calls *****
         *************************/

        /**
         * Get last 10 Desending values from the oven table
         */
        function getLast10DescendingOvenValues(){
          var json = <?php      
            $mfSql = new Mf_SQL();

            $mySql = $mfSql->getMySql();
            $oven = $mySql->Select('oven','','time DESC','10');
        
            echo json_encode(array_reverse($oven));


          ?>;
          return json;
        }
        </script>
        <!-- CSS -->
        <!-- toggle Button CSS styles the Toggle switches for control Center -->
        <link rel="stylesheet" type="text/css" href="style/toggleButton.css"/>
        <link rel="stylesheet" type="text/css" href="style/main.css"/>
        <link rel="stylesheet" type="text/css" href="style/light.css"/>

        <link href='http://fonts.googleapis.com/css?family=Finger+Paint' rel='stylesheet' type='text/css'>
        <!-- End of CSS -->
    </head>
      <body>

      <div id="house_div">

      <!--      TOP LEFT -->
          <div class="house_room" id="roomLightTemp">
            <h2>Thermostat</h2>

            <div class="graph_container">
              <div id="thermostat_Canvas_container" style="float:left;width: 50%; height: 75%;">
                <canvas id="thermostat_Line_chart" width="300" height="225"></canvas>
              </div>
                <div id="light_indicator_container" >
                    <div id="sun" style="">
                        <div id="innerSun" class="Lux-100">
                        </div>
                    </div>
                </div>
              </div>

            <div id="heating_Controls" class="control">
              <label style="display:inline" class="toggleLabel"> Heating:</label>
              <div class='togglebox'>
                  <input type='checkbox' id="heat_onoffswitch" class="socketSwitch">
                  <label for='heat_onoffswitch'><b></b></label>
              </div>
            </div>
          </div>

        <!-- TOP RIGHT -->
        <div class="house_room" id="counterDisplay">
          
          <h2>People counter</h2>
            <div class="graph_container">
                <div id="peopleCounter_Canvas_container" style="float:left;width: 250px; height: 150px;">
                    <canvas id="peopleCounter_Line_chart" width="600" height="225">
                    </canvas>
                </div>
            </div>
                    

          <div id="light_Controls" class="control">
            <label style="display:inline" class="toggleLabel"> Lights:</label>
            <div class='togglebox'>
                <input type='checkbox' id="light_onoffswitch" class="socketSwitch">
                <label for='light_onoffswitch'><b></b></label>
            </div>
          </div>
        </div>

        <!-- BOTTOM LEFT -->
          <div class="house_room" id="ovenDisplay">
          <h2>Oven</h2>

            <div id="Oven_Canvas_container" style="float:left;width: 250px; height: 150px;">
                  <div>
                    <label>Time:</label><input id="timerInput" type="number" /><button onclick="timer($('#timerInput').val())"> Go!</button>
                 </div>
                 <canvas id="Oven_Line_chart" width="226" height="200">
                    
                 </canvas>
                 

            <div id="oven_Controls" class="control">
              <label style="display:inline" class="toggleLabel"> Oven:</label>
              <!--Oven -->
              <div class='togglebox'>
                <input type='checkbox' id="oven_onoffswitch" class="socketSwitch">
                <label for='oven_onoffswitch'><b></b></label>
              </div>
            </div>
          </div>

          <div id="oven_temp_container" style="float:left;width: 250px; height: 150px;">

                    <canvas id="oven_temp_chart" width="300" height="225">
                    
                    </canvas>

               </div>  
          </div>


          <div class="house_room" id="controlCenter">
            <h2>Info</h2>
            <div class="ccInfo">
                <p>Temp: <span id="currentTemp"></span></p>
                <p><span id="someneHome_indicator"></span>  -&gt; heating: <span id="heating_status_display">heating_status</span> </p>
            </div>
            <div class="ccInfo night">
                <p>Its <span id="dayNight_indicator"></span> Outside &amp; there is <span id="people_count_indicator"></span> people home</p>
                <p>Lights are: <span id="lights_indicator"></span></p>
            </div>
            <div class="ccInfo">
                <p>Bagle status: <span id="bagelStatus"></span> </p>
                <p id="cookingTime_indicator"></p>
            </div>

          </div>
        
        </div>

      </body>
</html>
