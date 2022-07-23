$(".topic-item").click(function (e) {
    // $(".topic-form").submit();

    $.post("/play",
        function (data, textStatus, jqXHR) {
          console.log("SUCCESS")  
        },
    );
});