$(".topic-item").click(function (e) { 
    e.preventDefault();
    let title = $(this).children().eq(0);

    topic = $(title).text();

    $.ajax({
        type: "POST",
        url: "/game",
        data: "data",
        success: function (data) {
            if(data.finished) {
                location.reload();
            } else {
                alert(data);
            }
        }
    });


    // $.post("/game", 
    //         {data: topic },
    //     function (data, textStatus, jqXHR) {
    //         console.log('status: ' + textStatus, + ", data: " + data.responseData);
    //         alert(data + " " + textStatus)
    //     },
    //     "json"
    // );

    
});