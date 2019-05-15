
$(function () {
    $("#submit").click(function (event) {
        // 阻止按钮默认的提交表单事件
        event.preventDefault();

        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        // 1.要在模板的meta标签中渲染一个csrf-token
        // 2.在ajax请求的头部中设置X-CSRFtoken
        myajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success':function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error)
            }
        });

    });
});