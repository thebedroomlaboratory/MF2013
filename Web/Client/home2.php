<?php
  include "mysql/class.MfSQL.php";
?>
<html>
   <head>
      <script type="text/javascript" src="scripts/jquery-2.0.3.js"></script>
      <script type="text/javascript" src="scripts/controlCenter.js" ></script>
      <script type="text/javascript" src="scripts/Chart.js"></script>
      <script type="text/javascript">
        /**
         * Prevents jQuery code from running before the document is finished loading
         */
        $(function(){
        // check the sliders
          updateSliders();
          // plot the graphs
          plotThermostatGraph();
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
        function plotThermostatGraph(){
          var json = getLast10DescendingOvenValues();
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
          var ctx = getContextOfCanvasElement('thermostat_chart');
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
      <!-- End of CSS -->
   </head>
   <body>
      <div id="house_div">
          <!-- Thermostat -->
         <div class="house_room" id="roomLightTemp">
           <div class="graph_container">
              <div id="thermostat_Canvas_container" style="float:left;width: 250px; height: 150px;">             
                 <canvas id="thermostat_chart"></canvas>
               </div>

               <div id="light_indicator_container" style="width: 250px; height: 150px; float:left;">
               
                  <div id="light_indicator" style="width:100%;   height:60%;">
                    <div id="light" class="level-100">
                    </div>
                  </div>

               </div>   
            </div>
              <br/>
              <div id="heating_Controls" class="control">
               <div class="controlLabel"> 
                  <label style="display:inline" style="position:relative;top:-10px"> Heating:</label>
               </div>
               <div class="sliderWrapper">
                  <div class="onoffswitch">
                     <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox socketSwitch" id="heat_onoffswitch" checked>
                     <label class="onoffswitch-label" for="heat_onoffswitch">
                        <div class="onoffswitch-inner">
                           <div class="onoffswitch-active">
                              <div class="onoffswitch-switch">ON</div>
                           </div>
                           <div class="onoffswitch-inactive">
                              <div class="onoffswitch-switch">OFF</div>
                           </div>
                        </div>
                     </label>
                  </div>
               </div>
            </div>    

           
         </div>
          <!-- End of Thermostat -->


         <div class="house_room" id="counterDisplay">

           <div class="graph_container">
              <div id="peopleCounter_Canvas_container" style="float:left;width: 250px; height: 150px;">
                 <canvas id="people_chart"></canvas>
               </div>
            </div>
            <!-- light_Controls -->
            <div id="light_Controls" class="control">
               <div class="controlLabel"> 
                  <label style="display:inline" style="position:relative;top:-10px" > Lights:</label>
               </div>
               <div class="sliderWrapper">
                  <div class="onoffswitch">
                     <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox socketSwitch" id="light_onoffswitch" checked>
                     <label class="onoffswitch-label" for="light_onoffswitch">
                        <div class="onoffswitch-inner">
                           <div class="onoffswitch-active">
                              <div class="onoffswitch-switch">ON</div>
                           </div>
                           <div class="onoffswitch-inactive">
                              <div class="onoffswitch-switch">OFF</div>
                           </div>
                        </div>
                     </label>
                  </div>
               </div>
            </div>
            <!-- End of light_Controls -->
         </div>
        


         <div class="house_room" id="ovenDisplay">
           
           <div class="graph_container">
              <div id="Oven_Canvas_container" style="float:left;width: 250px; height: 150px;">
                  
                 <canvas id="oven_timer_chart"></canvas>
                 <div>
                    <label>Time:</label><input id="timerInput" type="number" /><button onclick="timer($('#timerInput').val())"> Go!</button>
                 </div>
                  <div id="oven_Controls" class="control">
                    <div class="controlLabel"> 
                      <label style="display:inline" style="position:relative;top:-10px"> Oven:</label>
                    </div>
                     <div class="sliderWrapper">
                        <div class="onoffswitch">
                           <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox socketSwitch" id="oven_onoffswitch" checked>
                           <label class="onoffswitch-label" for="oven_onoffswitch">
                              <div class="onoffswitch-inner">
                                 <div class="onoffswitch-active">
                                    <div class="onoffswitch-switch">ON</div>
                                 </div>
                                 <div class="onoffswitch-inactive">
                                    <div class="onoffswitch-switch">OFF</div>
                                 </div>
                              </div>
                           </label>
                        </div>
                     </div>
            </div>
            <!-- End of hlight_Controls -->
               </div>

               <div id="oven_temp_container" style="float:left;width: 250px; height: 150px;">
                    <canvas id="oven_temp_chart"></canvas>
               </div>   
            </div>
         </div>
        

         <!-- Control Center: contains the 3 toggles for Heat, Light, Oven control -->
         <div class="house_room" id="controlCenter">
            
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
         <!--End of controlCenter -->
      </div>
   </body>
</html>
