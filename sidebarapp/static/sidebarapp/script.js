function colortoggle(id)
{
    var background;
    background=document.getElementById(id).style.background;
    if(background!="blue")
      document.getElementById(id).style.background="blue";
    else
      document.getElementById(id).style.background="";
    
    console.log(background);
    console.log(id);
}
