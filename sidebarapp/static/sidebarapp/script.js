function formsubmit()
{
  $('#searchnav :input').not(':submit').clone().hide().appendTo('#formcomb');
  $('#formSidebar :input').not(':submit').clone().hide().appendTo('#formcomb');
    document.getElementById('formcomb').submit();
}
