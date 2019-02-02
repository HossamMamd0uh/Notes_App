$(document).ready(function(){
  event.preventDefault()

  $("#add").click(function (e){
    event.preventDefault()
    $('#steps').append('<div> عنوان الخطوة: <br> <input type="text" name="step"> <br> الخطوة: <br> <input type="text" name="your"> <br> <button type="button" class="btn btn-primary" id="photo">add photo</button> <br> <button type="button" class="btn btn-primary" id="delete">delete</button> </div>');
    $('#steps').append('<form action="http://google.com"><button type="submit" class="btn btn-primary">Next section</button><button type="button" class="btn btn-primary" id="no">not yet?</button></form>');
  });

  $('body').on('click','#delete',function (e){
    $(this).parent('div').remove();
  });
  $('body').on('click','#no',function (e){
    $(this).parent('form').remove();
  });

  $('body').on('click','#photo',function(e){
    $('#steps').append('<span> <br> <input type="file" name="pic" accept="image"> <br> <button type="button" class="btn btn-primary" id="del">delete photo</button> </span>');
  });

  $('body').on('click','#del',function (e){
    $(this).parent('span').remove();
  });
});
