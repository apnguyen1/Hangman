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

$(".keyboard-button").click(function (e) { 
    e.preventDefault();
    let btn = this;
    $.ajax({
        type: "POST",
        url: "",
        data: {letter: $(this).text()},
        dataType: "json",
        success: function (response) {
            $(btn).addClass("jump disabled");

            if(response["won"] || response["lost"]) {
                window.location.reload();
            }


            if(response['contains']) {
                $(btn).addClass("btn-success");
                $(".secret-word").each(function (index, element) {
                    if(response.current[index] == $(btn).text()) {
                        $(element).addClass("flip")
                        $(element).text(response.current[index]);
                    }
                });
            } else {
                $(btn).addClass("btn-secondary");
                $(".drawing-body").children().slice(0, response["errors"]).show();
                
            }
        },
        error: function(xhr, status, error) {
            alert("Server is down!");
        }
    });
});

function updateDrawing() {

}
