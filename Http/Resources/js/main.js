$(window).load(
    function() {        
        $("#main").mCustomScrollbar({
                theme:"minimal",
                scrollInertia: 400
            }
        );
        
        $.get( "/Updates", 
            function( data ) {         
                $("#updatesSection").html( data );
            }
        ); 
    }
);
 
$(document).on('click','.navbar-collapse.in', 
    function(e) {
        if( $(e.target).is('a') && $(e.target).attr('class') !== 'dropdown-toggle' ) {
            $(this).collapse('hide');
        }
    }
);


