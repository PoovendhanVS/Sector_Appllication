$(document).ready(function() {
   
    $(".nav-item").click(function(e) {
        e.preventDefault();

        var url = $(this).data("url");

    
        $.ajax({
            url: url,
            type: "GET",
            success: function(data) {
                $("#content").html(data);
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log("Error:", errorThrown);
            }
        });
    });
});
