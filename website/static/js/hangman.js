$(".topic-item").click(function (e) {
    e.preventDefault();

    let ele = $(this).children().eq(0);
    $.ajax({
        type: "POST",
        url: "/game",
        data: {topic: $(ele).text()},
        dataType: "json",
        success: function (response) {
            let id = response["gameid"]
            let origin = window.location.href;

            window.location.href = origin + "/" + id;
        },
    });
});

$("button").click(function (e) { 
    e.preventDefault();

    $.ajax({
        type: "POST",
        url: "",
        data: {letter: $(this).text()},
        // dataType: "text",
        success: function (response) {
            console.log(response["contains"])

            $(".secret-word").text(response["current"])
            
        }
    })
    // .done(function(data) {
    //     window.location.reload();
    // });
    
    x= $(this).text();

    $(this).addClass("disabled");
    $(this).addClass("btn-secondary");
});

