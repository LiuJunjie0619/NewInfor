function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function () {

    $(".base_info").submit(function (e) {
        e.preventDefault()

        var signature = $("#signature").val()
        var nick_name = $("#nick_name").val()
        var gender = $(".base_info").find("input:radio:checked").val()
        var joy = $("input[name='joy']:checked")
        var joylist=[]
        $.each(joy,function(){
            joylist.push($(this).val())
        })
        var csrf_token = $("input[name='csrf_token']").val()

        var language = $(".language option:selected").val()


        if (!nick_name) {
            alert('请输入昵称')
            return
        }
        if (!gender) {
            alert('请选择性别')
        }

        //参数拼接
        var params = {
            "signature": signature,
            "nick_name": nick_name,
            "gender": gender,
            "csrf_token":csrf_token
        }
        console.log(params)

        // TODO 修改用户信息接口
        $.ajax({
            url:"/user/base_info",
            type:'POST',
            data:params,
            dataType:'json',
            success:function(resp){
                //判断是否注册成功
                if (resp.code == "200") {
                    // 更新父窗口内容
                    $('.user_center_name', parent.document).html(params['nick_name'])
                    $('#nick_name', parent.document).html(params['nick_name'])
                    $('.input_sub').blur()
                }else {
                    alert(resp.mes)
                }
            }
        })
    })
})