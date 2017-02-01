var templateCache = {};

function setContent(link, id) {
    var cleanLink = window.location.href.split("/").pop();
    saveState(cleanLink);
    
    var pageData = templateCache[link];
    if(pageData == null) {
        $.get( "/" + link, 
            function( data ) {         
                $("#main_container").html( data );
                saveState(link.replace("Static/", "").replace("Static", ""));
                templateCache[link] = data;
            }
        ); 
    } else {
        $("#main_container").html( pageData );
        saveState(link.replace("Static/", "").replace("Static", ""));
    }
                
    $(".nav").find(".active").removeClass("active");
    $("#"+id).addClass("active");
}

function saveState(cleanLink) {
    if(window.history.state)
        if(window.history.state.state["url"] === cleanLink)
            return;
        
    var stateObj = {
         "html": document.getElementById("main_container").innerHTML,
         "url": cleanLink,
         "active":  $(".nav").find(".active").attr('id')
    };
    window.history.pushState({"state":stateObj},"", "/" + cleanLink);
}

window.onpopstate = function(e) {
    if(e.state){
        document.getElementById("main_container").innerHTML = e.state.state["html"];
        $(".nav").find(".active").removeClass("active");
        $("#" + e.state.state["active"]).addClass("active");
    }
};