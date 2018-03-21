$(document).ready(function()
{
        $.ajaxSetup({
            "beforeSend" : function (xhr)
                           {
                                xhr.overrideMimeType('application/json');
                           }
       });

       $("button#getres").click(function(){

                console.log("In")
                console.log(document.getElementById("symps").value);

                if ($("input#is_logged_in").val() === '0')
                {
                      alert("Please Login First To Use Our Web App!! If you dont't have an account yet, then register today!!");
                }
                else
                {
                   $.get("/predictor/predict/",
                        {
                           "symps": document.getElementById("symps").value
                        },
                        function(data,status,xhr)
                        {
                           console.log(JSON.stringify(data))
                           $("span#predres").text('Your probable disease is : '+data.PredDis+' and Severity is : '+data.Sev);
                        },"json");
                }

       });
});

