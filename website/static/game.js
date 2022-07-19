$("button").click(function (e) { 
    e.preventDefault();
    
    x= $(this).text();

    $(this).addClass("disabled");
    $(this).addClass("btn-secondary");

    $.ajax({
        type: "POST",
        url: "",
        data: "hello",
        success: function (response) {
            console.log(data);
        }
    });
});

