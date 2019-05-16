$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();

        myajax.get({
            'url':'/cms/email_captcha/',
            'data':{
                'email':email
            },
            'success':function (data) {
                if(data['code']==200){
                    myalert.alertSuccessToast('邮件发送成功！');
                }
                else{
                    myalert.alertInfo(data['message']);
                }
            },
            'fail':function (data) {
                myalert.alertNetworkError();
            }
        });
    });
});

$(function () {
   $("#submit").click(function (event) {
       event.preventDefault();
       var emailE = $("input[name=email]")
       var captchaE = $("input[name=captcha]");

       var email = emailE.val();
       var captcha = captchaE.val();

       myajax.post({
           "url":"/cms/resetemail/",
           "data":{
               "email":email,
               "captcha":captcha
           },
           "success":function (data) {
               if(data["code"]==200){
                   myalert.alertSuccessToast("恭喜！邮箱修改成功");
               }
               else{
                   myalert.alertInfo(data['message']);
               }
           },
           "fail":function (data) {
                myalert.alertError();
       }
       });
   });
});