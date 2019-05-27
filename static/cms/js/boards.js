$(function () {
   $("#add-board-btn").click(function (event) {
       event.preventDefault();
       myalert.alertOneInput({
           'text':"请输入板块名称",
           'placeholder':"板块名称",
           'confirmCallback':function (inputValue) {
               myajax.post({
                   'url':"/cms/aboard/",
                   'data':{
                       'name':inputValue
                   },
                   'success':function (data) {
                       if(data['code']==200){
                           window.location.reload();
                       }else{
                           myalert.alertInfo(data['message']);
                       }
                   }
               });
           }
       });
   });
});

$(function () {
   $(".edit-board-btn").click(function (event) {
       event.preventDefault();
       var self = $(this);
       var tr = self.parent().parent();
       var name = tr.attr('data-name');
       var board_id = tr.attr('data-id');

       myalert.alertOneInput({
           'text':"请输入新板块名称",
           'placeholder':name,
           'confirmCallback':function (inputValue){
               myajax.post({
                   'url':'/cms/uboard/',
                   'data':{
                        'board_id':board_id,
                       'name':inputValue
                   },
                   'success':function (data) {
                       if(data['code']==200){
                           window.location.reload();
                       }else{
                           myalert.alertInfo(data['message']);
                       }
                   }
               });
           }
       });
   });
});

$(function () {
   $(".delete-board-btn").click(function (event) {
       event.preventDefault();
       var self = $(this);
       var tr = self.parent().parent();
       var name = tr.attr('data-name');
       var board_id = tr.attr('data-id');

       myajax.post({
           'url':'/cms/dboard/',
           'data':{
                'board_id':board_id,
               'name':name
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