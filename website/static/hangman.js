$(".topic-item").click(function(e) {
    e.preventDefault();

    console.log(this);

    let ele = $(this).children().eq(0);

    $.ajax({
        type: "GET",
        url: "/game/createid",
        success: function (response) {
            let topic = $(ele).text().toLowerCase();
            window.location.href = "/game/" + topic + "/" + response;
        }
    });
})