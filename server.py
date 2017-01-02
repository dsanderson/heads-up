from flask import Flask
from flask import jsonify
import glob
import codecs
import random

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
        //console.log(times[mode]);
        //console.log(start);
        var now = new Date();
        secs_remaining = times[mode]-(now.getTime()-start.getTime())/1000;
        //console.log(secs_remaining);
        if (secs_remaining<=0) {
            start = now;
            mode = (mode == "work" ? "rest" : "work");
            secs_remaining = times[mode]-(now.getTime()-start.getTime())/1000;
        };
        var mins = Math.floor(secs_remaining/60);
        //console.log(mins)
        var secs = Math.floor(secs_remaining-mins*60);
        var line = document.getElementById("mode");
        var minutes = document.getElementById("minutes");
        var seconds = document.getElementById("seconds");
        line.innerHTML = mode;
        minutes.innerHTML = (mins < 10 ? '0' : '') + mins;
        seconds.innerHTML = (secs < 10 ? '0' : '') + secs;
    };
    var pomoTimer = window.setInterval(run, 100);
</script>
"""
    return data

@app.route("/flash")
def flash():
    """returns a javascript/html stub that will fetch & run flashcards from the server"""
    cards = get_cards()
    data = """
<div id="flashcard">
    <p id="flashcard-text"></p>
</div>
<script type="text/javascript">
    var cards = """
    data = data + [['a','b']]#"{}".format(cards)
    data = data + """;
    function shuffle(a) {
        var j, x, i;
        for (i = a.length; i; i--) {
            j = Math.floor(Math.random() * i);
            x = a[i - 1];
            a[i - 1] = a[j];
            a[j] = x;
        }
    }
    shuffle(cards);
    var i=0;
    var flash_state=0;
    function update() {
     if (flash_state == 0) {
        flash_state = 1;
        elem = getElementById("flashcard-text");
        elem.innerHTML = cards[i][0]
     }
     else {
        flash_state = 0;
        i=(i+1)%%cards.length;
        elem = getElementById("flashcard-text");
        elem.innerHTML = cards[i][1]
     }
    }
    var flashTimer = window.setInterval(update, 1500);
</script>"""
    return data

def get_cards(project_names=None):
    projects = glob.glob("flashcards/*.csv")
    lines = []
    for p in projects:
        f = codecs.open(p, "r", "utf-8")
        for l in f.readlines():
            if (l.strip()[0] != '#') and (l.strip() != ''):
                lines.append(l)
        f.close()
    #pick a line at random
    data = [l.strip().split('|') for l in lines]
    #process the line
    return data
