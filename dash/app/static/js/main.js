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
