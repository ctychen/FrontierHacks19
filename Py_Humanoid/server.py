from flask import Flask, render_template, request, redirect, url_for
import Humanoid
import threading

app = Flask(__name__)

humanoid = Humanoid.Humanoid()

@app.route('/')
def index():
    return render_template('main.html')
   
@app.route("/")
def main():
   templateData = {
      'message': ""
      }
   # Pass the template data into the template main.html and return it to the user
   return message
  
def walkForward():
   humanoid.walkForward()

def turnLeft():
   humanoid.turnLeft()

def turnRight():
   humanoid.turnRight()

def stand():
   humanoid.stand()

#arm motion

def openLeftClaw():
   humanoid.openLeftClaw(150)

def closeLeftClawLeft():
   humanoid.closeLeftClaw(0)

def turnLeftWristRight():
   humanoid.turnLeftWristRight(50)

def turnLeftWristLeft():
   humanoid.turnLeftWristLeft(100)

def openLeftElbow():
   humanoid.openLeftElbow(160)

def closeLeftElbow():
   humanoid.closeLeftElbow(50)

def raiseLeftShoulder():
   humanoid.raiseLeftShoulder(180)

def midRaiseLeftShoulder():
   humanoid.midRaiseLeftShoulder(60)

def lowerLeftShoulder():
   humanoid.lowerLeftShoulder(0)

#Right side
    
def openRightClaw():
   humanoid.openRightClaw(150)

def closeRightClawLeft():
   humanoid.closeRightClawLeft(0)

def turnRightWristRight():
   humanoid.turnRightWristRight(50)

def turnRightWristLeft():
   humanoid.turnRightWristLeft(100)

def openRightElbow():
   humanoid.openRightElbow(160)

def closeRightElbow():
   humanoid.closeRightElbow(50)

def raiseRightShoulder():
   humanoid.raiseRightShoulder(180)

def midRaiseRightShoulder():
   humanoid.midRaiseRightShoulder(60)

def lowerRightShoulder():
   humanoid.lowerRightShoulder(0)



@app.route("/<action1>")
def action1(action1):
   # Convert the pin from the URL into an integer:
   global message
   if action1 == "walkForward":
      message = "walkForward"
      thread = threading.Thread(target=walkForward)
      thread.start()
      return message + ' started'  
   elif action1 == "turnLeft":
      message = "turnLeft"
      thread = threading.Thread(target=turnLeft)
      thread.start()
      return message + ' started' 
   elif action1 == "turnRight":
      message = "turnRight"
      thread = threading.Thread(target=turnRight)
      thread.start()
      return message + ' started' 
   elif action1 == "stand":
      message = "stand"
      thread = threading.Thread(target=stand)
      thread.start()
      return message + ' started' 
   elif action1 == "waveLeft":
      message = "waveLeft"
      thread = threading.Thread(target=waveLeft)
      thread.start()
      return message + ' started' 
   else:
      message = ""

   templateData = {
      'message' : message,
   }

  

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)