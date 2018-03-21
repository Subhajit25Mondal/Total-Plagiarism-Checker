$(document).ready(function()
{
       console.log("strt");
        $("span#close_res").click(function(){
                   console.log("works");
                   $(this).parent().css("display","none");
        });

});