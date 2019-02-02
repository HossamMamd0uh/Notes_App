$(document).ready(function(){
  event.preventDefault()

  $("#add").click(function (e){
    event.preventDefault()
    $('#steps').append('<form action="." method="post" enctype="multipart/form-data"><div class="form-group"><input type="text" class="form-control" name="step_title" id="inputUsernameEmail" placeholder="Email"></div></form>');
    $('#steps').append('<form id="next" action="http://google.com"><button type="submit" class="btn btn-primary">الخطوة القادمة</button> &nbsp <button type="button" class="btn btn-primary" id="no">الاستمرار</button></form>');
  });

  $('body').on('click','#delete',function (e){
    $(this).parent('form').remove();
  });
  $('body').on('click','#no',function (e){
    $(this).parent('form').remove();
  });

  $('body').on('click','#photo',function(e){
    $('#steps').append('<span> <form method="post" enctype="multipart/form-data"> <input type="file" name="pic" accept="image"> <br> <input type="file" name="pic" accept="image"> <br> <button type="button" class="btn btn-primary" id="del">حذف الصورة</button> </form> </span>');
  });

  $('body').on('click','#del',function (e){
    $(this).parent('form').remove();
  });
  var val = document.getElementById('inputUsernameEmail').value
});
