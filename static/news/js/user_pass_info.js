function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {
    $(".pass_info").submit(function (e) {
        e.preventDefault();

        // TODO 修改密码

        // 取到两次密码进行判断
        var old_password = $("input[name='old_password']").val();
        var new_password = $("input[name='new_password']").val();
        var new_password2 = $("input[name='new_password2']").val();
        var csrf_token = $("input[name='csrf_token']").val();

        if (new_password != new_password2) {
            alert('两次密码输入不一致')
            return
        }

        params={'old_password':old_password,
        'new_password':new_password,
        'new_password2':new_password2,
        'csrf_token':csrf_token}

        $.ajax({
            url: "/user/pass_info",
            type: "post",
            dataType: "json",
            data: params,
            success: function (resp) {
                if (resp.errno == 200) {
                    // 修改成功
                    alert("修改成功")
                    window.location.reload()
                }else {
                    alert(resp.errmsg)
                }
            }
        })

    })
})