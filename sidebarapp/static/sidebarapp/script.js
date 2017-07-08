function formsubmit()
{
  $('#searchnav :input').not(':submit').clone().hide().appendTo('#formcomb');
  $('#formSidebar :input').not(':submit').clone().hide().appendTo('#formcomb');
    document.getElementById('formcomb').submit();
}
function submitRating(id,url,rating) {
  console.log("form submitted!")  // sanity check
  console.log(url,rating)  // sanity check
  create_post(id,url,rating);
}
function create_post(id,url,rating) {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : url, // the endpoint
        type : "POST", // http method
        data : { rating : rating ,movie_id : id}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function enterpress(event){
  console.log(event)
  if (event.keyCode == 13) {
    $('#searchnav :input').not(':submit').clone().hide().appendTo('#formcomb');
    $('#formSidebar :input').not(':submit').clone().hide().appendTo('#formcomb');
      document.getElementById('formcomb').submit();
   }
}
/*$('#1_stars').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
})*/
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
function show(){
  var left=document.getElementById("SideBar").style.left;
  document.getElementById("SideBar").style.left="0px";
}
