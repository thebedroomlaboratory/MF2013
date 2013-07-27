function getLuxValue() {
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
            var lux = new Array();
            var json = data;
            var elm = json[0];
            x[0] = 0;
            lux[0] = parseInt(elm.lux);
            console.log("dateRange["+0+"] "+x[0]+" | "+lux[0]);
            result=lux[0];    
        }});     
	console.log("Test - "+result);
	return result;
} 

$(function () {
			
		    $('#light_container').highcharts({
			
			    chart: {
			        type: 'gauge',
			        plotBackgroundColor: null,
			        plotBackgroundImage: null,
			        plotBorderWidth: 0,
			        plotShadow: false
			    },
			    
			    title: {
			        text: 'Lux Meter'
			    },
			    
			    pane: {
			        startAngle: -150,
			        endAngle: 150,
			        background: [{
			            backgroundColor: {
			                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
			                stops: [
			                    [0, '#FFF'],
			                    [1, '#333']
			                ]
			            },
			            borderWidth: 0,
			            outerRadius: '109%'
			        }, {
			            backgroundColor: {
			                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
			                stops: [
			                    [0, '#333'],
			                    [1, '#FFF']
			                ]
			            },
			            borderWidth: 1,
			            outerRadius: '107%'
			        }, {
			            // default background
			        }, {
			            backgroundColor: '#DDD',
			            borderWidth: 0,
			            outerRadius: '105%',
			            innerRadius: '103%'
			        }]
			    },
			       
			    // the value axis
			    yAxis: {
			        min: 0,
			        max: 700,
			        
			        minorTickInterval: 'auto',
			        minorTickWidth: 1,
			        minorTickLength: 10,
			        minorTickPosition: 'inside',
			        minorTickColor: '#666',
			
			        tickPixelInterval: 30,
			        tickWidth: 2,
			        tickPosition: 'inside',
			        tickLength: 10,
			        tickColor: '#666',
			        labels: {
			            step: 2,
			            rotation: 'auto'
			        },
			        title: {
			            text: 'Lux'
			        },
			        plotBands: [{
			            from: 0,
			            to: 150,
			            color: '#55BF3B' // green
			        }, {
			            from: 150,
			            to: 350,
			            color: '#DDDF0D' // yellow
			        }, {
			            from: 350,
			            to: 700,
			            color: '#DF5353' // red
			        }]        
			    },
			
			    series: [{
			        name: 'Light Reading',
			        data: [80],
			        tooltip: {
			            valueSuffix: ' Lux'
			        }
			    }]
			
			}, 
			// Add some life
			function (chart) {
				if (!chart.renderer.forExport) {
				    setInterval(function () {
				        var point = chart.series[0].points[0],
				        	newVal;
				        
				        newVal = getLuxValue();
				        
				        point.update(newVal);
				        
				    }, 3000);
				}
			});
		});
