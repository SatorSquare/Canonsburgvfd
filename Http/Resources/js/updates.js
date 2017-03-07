function saveUpdate() {
    $.ajax({
      type: "POST",
      url: "/Updates",
      data: {
                id: $("#update_key").val(),
                title: $("#update_title").val(),
                text: $("#update_text").val()              
            },
      success: function() {
                $.get( "/Updates", 
                    function( data ) {         
                        $("#updatesSection").html( data );
                    }
                ); 
            },
      dataType: "json"
    });
    
    $("#update_key").val("");
    $("#update_title").val("");
    $("#update_text").val("");
}

function configureEditModal(id, title, text) {
    $("#update_key").val(id);
    $("#update_title").val(title);
    $("#update_text").val(text);
    $("#UpdatesModal").modal();
}

function deleteUpdate(id) {
    $.ajax({
      type: "POST",
      url: "/DeleteUpdates",
      data: {
                id: id          
            },
      success: function() {
                $.get( "/Updates", 
                    function( data ) {         
                        $("#updatesSection").html( data );
                    }
                ); 
            },
      dataType: "json"
    });
}