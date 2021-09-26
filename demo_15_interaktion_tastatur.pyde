txt = ""

def setup():
    size(600, 600)
    background(0, 0, 0)
    stroke(255, 255, 255)
    strokeWeight(8)
    textSize(36)
    textAlign(CENTER)
    
def draw():
    fill(0, 0, 0)
    rect(200, 200, 200, 200, 20)
    fill(255, 255, 255)
    text(txt, 300, 310)
    
def keyPressed():
    global txt
    if key == "a":
        txt = "AAA"
    if key == "b":
        txt = "BBB"
    if key == "c":
        txt = "CCC"
<<<<<<< HEAD
    if key == "d":
        txt = "DDD"
    if key == "e":
        txt = "EEE"
=======
>>>>>>> parent of 4a8cac2 (Update demo_15_interaktion_tastatur.pyde)

def keyReleased():
    global txt
    txt = ""
