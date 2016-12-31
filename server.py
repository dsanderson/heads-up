from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """return the skeleton that loads other modules into flexboxes, as well as a default window"""
    data = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>headsup</title>
    <link rel="stylesheet" href="css/index.css">
    <script src="script.js"></script>
  </head>
  <body>
    <div class='box 1-1' id="pomodoro-box">
    </div>
  </body>
  <body>
    <div class='box 2-1' id="flash-box">
    </div>
  </body>
  <script type="text/javascript">
    function fetch_pomodoro(text) {
        // document.getElementById("pomodoro-box").innerHTML = text;
        insertHtml("pomodoro-box",text);
    }

    function fetch_flash(text) {
        // document.getElementById("flash-box").innerHTML = text;
        insertHtml("flash-box",text);
    }

    function insertHtml(id, html)
    {
       var ele = document.getElementById(id);
       ele.innerHTML = html;
       var codes = ele.getElementsByTagName("script");
       for(var i=0;i<codes.length;i++)
       {
           eval(codes[i].text);
       }
    }

    var pomodoroXmlHttp = new XMLHttpRequest();
    pomodoroXmlHttp.onreadystatechange = function() {
            if (pomodoroXmlHttp.readyState == 4 && pomodoroXmlHttp.status == 200)
                fetch_pomodoro(pomodoroXmlHttp.responseText);
    }
    pomodoroXmlHttp.open("GET", "./pomodoro", true);
    pomodoroXmlHttp.send(null);

    var flashXmlHttp = new XMLHttpRequest();
    flashXmlHttp.onreadystatechange = function() {
            if (flashXmlHttp.readyState == 4 && flashXmlHttp.status == 200)
                fetch_flash(flashXmlHttp.responseText);
    }
    flashXmlHttp.open("GET", "./flash", true);
    flashXmlHttp.send(null);
  </script>
</html>
"""
    return data

@app.route("/pomodoro")
def pomodoro():
    """returns a javascript/html stub that will run as a 20/5 pomodoro timer"""
    data = """
<div id="clock">
    <span id="mode"></span></br>
    <span id="minutes"></span>:<span id="seconds"></span>
</div>
<script type="text/javascript">
    var mode = "work";
    var times = {"work":1500,"rest":300};
    var start = new Date();
    function run() {
        console.log(times[mode]);
        console.log(start);
        var now = new Date();
        secs_remaining = times[mode]-(now.getTime()-start.getTime())/1000;
        console.log(secs_remaining);
        if (secs_remaining<=0) {
            start = now;
            mode = (mode == "work" ? "rest" : "work");
            secs_remaining = times[mode]-(now.getTime()-start.getTime())/1000;
        };
        var mins = Math.floor(secs_remaining/60);
        console.log(mins)
        var secs = secs_remaining-mins*60;
        var line = document.getElementById("mode");
        var minutes = document.getElementById("minutes");
        var seconds = document.getElementById("seconds");
        line.innerHTML = mode;
        minutes.innerHTML = (mins < 10 ? '0' : '') + mins;
        seconds.innerHTML = (secs < 10 ? '0' : '') + secs;
    };
    var pomoTimer = window.setInterval(run, 500);
</script>
"""
    return data

@app.route("/flash")
def flash():
    """returns a javascript/html stub that will fetch & run flashcards from the server"""
    return ""

@app.route("/get_flash")
def get_flash():
    """returns, in json format, the content of a flash card, including the timing"""
    return ""
