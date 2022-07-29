$(document).ready(function() {
    if(sessionStorage.getItem("reloadAfterPageLoad") == "true") {
        $(".secret-word").each(function(index) {
            $(this).addClass("bounce");
        
            $(this).css({
                '--transition-delay' : .1*(index) + 's'
            })
        });

        setTimeout(function() {
            $("#mymodel").modal('show');
        }, 2000)
        sessionStorage.setItem("reloadAfterPageLoad", "false");
    }
});


$(".topic-item").click(function (e) {
    e.preventDefault();

    let ele = $(this).children().eq(0);
    var top = $(ele).text().toLowerCase();
    $.ajax({
        type: "POST",
        url: "/",
        data: {topic: top},
        dataType: "json",
        success: function (response) {
            let id = response["gameid"]

            window.location.replace(top + "/" + id);
        },
    });
});

$(".play-again").click(function (e) {
    e.preventDefault();

    var top = $(this).val();

    $.ajax({
        type: "POST",
        url: "/",
        data: {topic: top},
        dataType: "json",
        success: function (response) {
            let id = response["gameid"]

            window.location.replace(id);
        }
    });
});

$(".keyboard-button").click(function (e) { 
    e.preventDefault();
    let btn = this;
    $.ajax({
        type: "post",
        url: "",
        data: {letter: $(this).text()},
        dataType: "json",
        success: function (response) {
            res = response;
            $(btn).addClass("jump disabled");

            if(response["won"] || response["lost"]) {
                sessionStorage.setItem("reloadAfterPageLoad", "true")
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
                $(".drawing-body").children().slice(0, response["errors"]).addClass("fade-in");
                $("#life-left").text(8 - response["errors"]);
            }
            
        },
        error: function(xhr, status, error) {
            alert("Server is down!");
        }
    });
});



