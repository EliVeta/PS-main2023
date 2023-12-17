function ChangeForm() {
    $.ajax({
        url: '/appointment/appointment_info/',
        type: 'GET',
        data: $('#form').serialize()
    }).done(function (json) {
        if (json.result) {
            $("#form").html(json.forms);
        }
    })
}