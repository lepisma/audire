// Custom js stuff

$(document).ready(function(){
    // Init variables
    anomalyFlag = 1;
    speechFlag = 1;
    
    // Init charts
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    // Chart setup
    $("#level-graph").highcharts({
        chart: {
            type: "spline",
            animation: Highcharts.svg,
            marginRight: 5,
            events: {
                load: function(){
                    // set up the updating of the chart each 2 seconds
                    var series = this.series[0];
                    setInterval(function (){$.get("/level", function(data){
                        var x = (new Date()).getTime();
                        series.addPoint([x, parseInt(data)], true, true);
                    });}, 2000);
                }
            }
        },
        title: {
            text: ""
        },
        xAxis: {
            type: "datetime",
            tickPixelInterval: 150
        },
        yAxis: {
            title: {
                text: "Level"
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            enabled: false
            },
        exporting: {
            enabled: false
        },
        series: [{
            name: "Audio level",
            data: (function () {
                // generate an array of random data
                var data = [],
                    time = (new Date()).getTime(),
                    i;
                
                for (i = -19; i <= 0; i += 1) {
                    data.push({
                        x: time + i * 1000,
                        y: Math.random()
                    });
                }
                return data;
            }())
        }]
    });
    
    // Hide overlay
    $("#overlay").hide();

    // Modal popup
    $("#settings-btn").click(function(){
        $("#overlay").fadeIn();
    })

    // Modal fadeout
    $("#overlay-close-btn").click(function(){
        $("#overlay").fadeOut();
    });

    // Event check button
    $(".event-btn").click(function(){
        // Request event status
        var button = $(this);
        button.addClass("disabled");
        $("#event-loading").css("opacity", 1);
        
        $.get("/event", function(data){
            updateEvent(data);
            button.removeClass("disabled");
            $("#event-loading").css("opacity", 0);
        });
    });

    // Setting buttons
    $("#event-switch").change(function(){
        if($(this).is(":checked")){
            $(".event-btn").removeClass("disabled");
        }
        else{
            $(".event-btn").addClass("disabled");
        }
    });

    $("#anomaly-switch").change(function(){
        if($(this).is(":checked")){
            anomalyFlag = 1;
        }
        else{
            anomalyFlag = 0;
        }
    });

    $("#speech-switch").change(function(){
        if($(this).is(":checked")){
            speechFlag = 1;
        }
        else{
            speechFlag = 0;
        }
    });

    // WebSocket connection
    if("WebSocket" in window){
        var ws = new WebSocket("ws://localhost:5000/ws");

        ws.onopen = function(){
            console.log("connection established");
        };

        ws.onmessage = function(event){
            var message = event.data;
            message = message.split(":");
            var identifier = message[0].trim();
            var content = message[1].trim();

            // Anomaly detection
            if((identifier == "anomaly") & (content == "1")){
                if(anomalyFlag == 1){
                    $("#info-pane").addClass("anomaly");
                }
            }
            else if((identifier == "anomaly") & (content == "0")){
                setTimeout(function(){
                    $("#info-pane").removeClass("anomaly")
                }, 1000);
            }
            
            // Message
            if((identifier == "message") & (speechFlag == 1)){
                updateMsg(content);
            }
        };

        ws.onclose = function(){
            console.log("connection closed");
        };
    }
    else{
        console.log("WebSocket not supported in your browser");
    }
    
});

// --------------------
// UI Control functions

var flashBtn = function(direction){
    // Flash the direction button
    if(direction == "left"){
        var elem = $("#left-btn");
    }
    else if(direction == "right"){
        var elem = $("#right-btn");
    }

    var intervalId = setInterval(function(){
        elem.toggleClass("disabled");
    }, 400);

    setTimeout(function(){
        clearInterval(intervalId);
    }, 2000);
};

var updateMsg = function(message){
    // Update the message area
    var currentHolder = $("#messages h2");
    var previousHolders = $("#messages h3");

    addToHistory(message);
    
    var previousMsg = currentHolder.text();
    currentHolder.text(message);

    for(i = 2; i > 0; i--){
        var current = previousHolders.eq(i - 1).text();
        previousHolders.eq(i).text(current);
    }
    previousHolders.first().text(previousMsg);
}

var msgTime = function(){
    // Return current time formatted in HH:MM

    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();
    if(minutes < 10){
        minutes = "0" + minutes;
    }
    if(hours < 10){
        hours = "0" + hours;
    }
    return hours + ":" + minutes;
}

var addToHistory = function(message){
    // Add the message to history tab
    var currentMsgTime = msgTime();

    var parent = $("#history > div").first();
    var divToInsert = "<h4>" + message + "<span class='pull-right'>" + currentMsgTime + "</></h4>";
    parent.append(divToInsert);
}

var updateEvent = function(event){
    // Update the event text and image
    $("#events .carousel-desc > span").text(event);
    // var imgUrl = "/static/images/events/" + event + ".jpg";
    // $("#event-img").attr("src", imgUrl);
}
