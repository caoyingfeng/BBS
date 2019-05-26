$(function () {
   $("#save-banner-btn").click(function (event) {
       event.preventDefault();
       var self = $(this);
       var dialog = $("#banner-dialog");
       var nameInput = $("input[name='name']");
       var imageInput = $("input[name='image_url']");
       var linkInput = $("input[name='link_url']");
       var priorityInput = $("input[name='priority']");

       var name = nameInput.val();
       var image_url = imageInput.val();
       var link_url = linkInput.val();
       var priority = priorityInput.val();

       var submitType = self.attr("data-type");
       var bannerId = self.attr("data-id");

       if (!name || !image_url || !link_url || !priority){
           myalert.alertInfoToast("请输入完整的轮播图数据");
           return;
       }

       var url= '';
       if(submitType=='update'){
           url="/cms/ubanner/";
       }else{
           url="/cms/abanner/";
       }


       myajax.post({
           "url":url,
           "data":{
             "name":name,
             "image_url":image_url,
             "link_url":link_url,
             "priority":priority,
             "banner_id":bannerId
           },
           "success":function (data) {
               dialog.modal("hide");//隐藏对话框
               if(data['code']==200){
                   // 重新加载这个页面
                   window.location.reload();
               }else{
                   myalert.alertInfo(data['message']);
               }

           },
           "fail":function () {
                myalert.alertNetworkError();
           }
       });
   })
});

$(function () {
   $(".edit-banner-btn") .click(function (event) {
       var self = $(this);
       var dialog = $("#banner-dialog");
       dialog.modal("show");

       var tr = self.parent().parent();
       var name = tr.attr("data-name");
       var image_url = tr.attr("data-image");
       var link_url = tr.attr("data-link");
       var priority = tr.attr("data-priority");

       var nameInput = dialog.find("input[name='name']");
       var imageInput = dialog.find("input[name='image_url']");
       var linkInput = dialog.find("input[name='link_url']");
       var priorityInput = dialog.find("input[name='priority']");
       var saveBtn = dialog.find("#save-banner-btn");

       nameInput.val(name);
       imageInput.val(image_url);
       linkInput.val(link_url);
       priorityInput.val(priority);
       saveBtn.attr("data-type","update"); // 绑定编辑类型，与添加区分
       saveBtn.attr("data-id",tr.attr("data-id"));
   });
});


$(function(){
    $(".delete-banner-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var banner_id = tr.attr("data-id");
        myajax.post({
            'url':"/cms/dbanner/",
            'data':{
                'banner-id':banner_id,
            },
            'success':function (data) {
                if(data['code']==200){
                    window.location.reload();
                }else{
                    myalert.alertInfo(data['message']);
                }
            }
        });
    });
});