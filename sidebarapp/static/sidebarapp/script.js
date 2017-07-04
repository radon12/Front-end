function formsubmit()
{
  $('#searchnav :input').not(':submit').clone().hide().appendTo('#formcomb');
  $('#formSidebar :input').not(':submit').clone().hide().appendTo('#formcomb');
    document.getElementById('formcomb').submit();
}
function submitRating(id) {
  document.getElementById(id).submit();
}
function enterpress(event){
  console.log(event)
  if (event.keyCode == 13) {
    $('#searchnav :input').not(':submit').clone().hide().appendTo('#formcomb');
    $('#formSidebar :input').not(':submit').clone().hide().appendTo('#formcomb');
      document.getElementById('formcomb').submit();
   }
}
