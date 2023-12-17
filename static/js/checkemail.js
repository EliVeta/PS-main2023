$("#email").change(function () {
     let url = "reg";
     let email = $(this).val();
     $.ajax({
         url: url,
         data: {
             csrfmiddlewaretoken: getCookie(),
             email: email
             },
         type: 'POST',
         dataType: 'json',
         success: function (data) {
             console.log(data);
             $("span.ajax-response").html(data.message);
         },
         error: function (e) {
             console.log(e);
         },
     });
 });