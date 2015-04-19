$(document).ready(function(){ 
  if ("WebSocket" in window) {
    var ws = new WebSocket("ws://localhost:8888/datasync/");
    
    ws.onopen = function() {
      console.log('Seadog DataSync online');
    };
    
    ws.onmessage = function (evt) {
      
      // WebSocket DataSync to UI
      var json = evt.data;
      msg = JSON.parse(json);
      

      if (msg['funds'] != null) {
        $('#funds').html(msg['funds']);
      }



    };
    
    ws.onclose = function() {
      console.log('Seadog DataSync offline');
    };
  } else {
    alert("WebSocket not supported");
  }
});