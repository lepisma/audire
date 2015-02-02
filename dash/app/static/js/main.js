// Custom js stuff

$(document).ready(function(){
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
});

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
