<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <title>
            Test simple server
        </title>
    </head>
    <body>
        <button onclick="readServer()">go</button>
        <div id="output"></div>
    </body>
    <script>
        function readServer(){
            $.ajax({
                "url": "http://127.0.0.1:5000/",
                "method":"GET",
                "data":"",
                "dataType": "HTML",
                "success":function(result){
                    console.log(result);
                    document.getElementById("output").innerHTML = result;
                },
                "error":function(xhr,status,error){
                    console.log("error: "+status+" msg:"+error);
                }
            });

        }
    </script>
</html>