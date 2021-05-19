$(document).ready(function(){

        var WEBSOCKET_ROUTE = "/ws";

        if(window.location.protocol == "http:"){
            //localhost
            var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
        }
        else if(window.location.protocol == "https:"){
            //Dataplicity
            var ws = new WebSocket("wss://" + window.location.host + WEBSOCKET_ROUTE);
        }

        ws.onopen = function(evt) {
            // $("#ws-status").html("Connected");
            // $("#ws-status").css("background-color", "#afa");
            // $("#server_light").val("ON");
            $("#signal").html("READY");
            $("#ws-status").html("Connected");
            $("#ws-status").css("background-color", "#afa");
        };

        ws.onmessage = function(evt) {
            //console.log(evt);
            var sData = JSON.parse(evt.data);
            //console.log(sData);
            if (sData.info == 'temperature'){
                $("#tempinfo").html(sData.value);
              }

        };

        ws.onclose = function(evt) {
            $("#ws-status").html("Disconnected");
            $("#ws-status").css("background-color", "#faa");
            $("#server_light").val("OFF");
        };

        //MESSAGES TO SEND TO THE SERVER


        $("#temp").click(function(){
            var msg = '{"what": "Temperature"}';
            ws.send(msg);
        });

        $("#pumpon").click(function(){
            var msg = '{"what": "turnon"}';
            ws.send(msg);
        });

        $("#pumpoff").click(function(){
            var msg = '{"what": "turnoff"}';
            ws.send(msg);
        });

        $("#pumptime").change(function(){
          console.log("set pump time");
            var pt = $("#pumptime").val();
            console.log(pt);
            var msg = {"what": "pumptime", "time": pt};
            console.log(msg)

            ws.send(JSON.stringify(msg));
        });


        $("#restart").click(function(){
          let check = confirm("Restart Server?");
          if (check){
            var msg = '{"what": "restart"}';
            ws.send(msg);
          }
        });
        $("#reboot").click(function(){
            let check = confirm("Reboot Pi?");
            if (check){
              var msg = '{"what": "reboot"}';
              ws.send(msg);
            }
        });



      });
