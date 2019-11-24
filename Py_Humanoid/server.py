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
   # Pass the template data into the template main.html and #return it to the user
   return message
  
def walkForward():
   humanoid.stand()
   humanoid.walkForward()

def turnLeft():
   humanoid.turnLeft()

def turnRight():
   humanoid.turnRight()

def stand():
   humanoid.stand()

#arm motion

def openLeftClaw():
   humanoid.openLeftClaw()

def closeLeftClaw():
   humanoid.closeLeftClaw()

def turnLeftWristRight():
   humanoid.turnLeftWristRight()

def turnLeftWristLeft():
   humanoid.turnLeftWristLeft()

def openLeftElbow():
   humanoid.openLeftElbow()

def closeLeftElbow():
   humanoid.closeLeftElbow()

def raiseLeftShoulder():
   humanoid.raiseLeftShoulder()

def midRaiseLeftShoulder():
   humanoid.midRaiseLeftShoulder()

def lowerLeftShoulder():
   humanoid.lowerLeftShoulder()

#Right side
    
def openRightClaw():
   humanoid.openRightClaw()

def closeRightClaw():
   humanoid.closeRightClaw()

def turnRightWristRight():
   humanoid.turnRightWristRight()

def turnRightWristLeft():
   humanoid.turnRightWristLeft()

def openRightElbow():
   humanoid.openRightElbow()

def closeRightElbow():
   humanoid.closeRightElbow()

def raiseRightShoulder():
   humanoid.raiseRightShoulder()

def midRaiseRightShoulder():
   humanoid.midRaiseRightShoulder()

def lowerRightShoulder():
   humanoid.lowerRightShoulder()

def armHome():
   humanoid.armHome()

def TPose():
   humanoid.TPose()

def pushUp():
   humanoid.pushUp()



@app.route("/<action1>")
def action1(action1):
   # Convert the pin from the URL into an integer:
   global message
   if action1 == "walkForward":
      message = "walkForward"
      thread = threading.Thread(target=walkForward)
      thread.start()
      return render_template('main.html')  
   elif action1 == "turnLeft":
      message = "turnLeft"
      thread = threading.Thread(target=turnLeft)
      thread.start()
      return render_template('main.html')  
   elif action1 == "turnRight":
      message = "turnRight"
      thread = threading.Thread(target=turnRight)
      thread.start()
      return render_template('main.html')  
   elif action1 == "stand":
      message = "stand"
      thread = threading.Thread(target=stand)
      thread.start()
      return render_template('main.html')  
 
#  left claw
   elif action1 == "openLeftClaw":
      message = "openLeftClaw"
      thread = threading.Thread(target=openLeftClaw)
      thread.start()
      return render_template('main.html')  
   elif action1 == "closeLeftClaw":
      message = "closeLeftClaw"
      thread = threading.Thread(target=closeLeftClaw)
      thread.start()
      return render_template('main.html')  

   elif action1 == "turnLeftWristRight":
      message = "turnLeftWristRight"
      thread = threading.Thread(target=turnLeftWristRight)
      thread.start()
      return render_template('main.html')  
   elif action1 == "turnLeftWristLeft":
      message = "turnLeftWristLeft"
      thread = threading.Thread(target=turnLeftWristLeft)
      thread.start()
      return render_template('main.html')  

   elif action1 == "openLeftElbow":
      message = "openLeftElbow"
      thread = threading.Thread(target=openLeftElbow)
      thread.start()
      return render_template('main.html')  
   elif action1 == "closeLeftElbow":
      message = "closeLeftElbow"
      thread = threading.Thread(target=closeLeftElbow)
      thread.start()
      return render_template('main.html')  

   elif action1 == "raiseLeftShoulder":
      message = "raiseLeftShoulder"
      thread = threading.Thread(target=raiseLeftShoulder)
      thread.start()
      return render_template('main.html')  
   elif action1 == "midRaiseLeftShoulder":
      message = "midRaiseLeftShoulder"
      thread = threading.Thread(target=midRaiseLeftShoulder)
      thread.start()
      return render_template('main.html')  
   elif action1 == "lowerLeftShoulder":
      message = "lowerLeftShoulder"
      thread = threading.Thread(target=lowerLeftShoulder)
      thread.start()
      return render_template('main.html')  

# right claw
   elif action1 == "openRightClaw":
      message = "openRightClaw"
      thread = threading.Thread(target=openRightClaw)
      thread.start()
      return render_template('main.html')  
   elif action1 == "closeRightClaw":
      message = "closeRightClaw"
      thread = threading.Thread(target=closeRightClaw)
      thread.start()
      return render_template('main.html')  

   elif action1 == "turnRightWristRight":
      message = "turnRightWristRight"
      thread = threading.Thread(target=turnRightWristRight)
      thread.start()
      return render_template('main.html')  
   elif action1 == "turnRightWristLeft":
      message = "turnRightWristLeft"
      thread = threading.Thread(target=turnRightWristLeft)
      thread.start()
      return render_template('main.html')  

   elif action1 == "openRightElbow":
      message = "openRightElbow"
      thread = threading.Thread(target=openRightElbow)
      thread.start()
      return render_template('main.html')  
   elif action1 == "closeRightElbow":
      message = "closeRightElbow"
      thread = threading.Thread(target=closeRightElbow)
      thread.start()
      return render_template('main.html')  

   elif action1 == "raiseRightShoulder":
      message = "raiseRightShoulder"
      thread = threading.Thread(target=raiseRightShoulder)
      thread.start()
      return render_template('main.html')  
   elif action1 == "midRaiseRightShoulder":
      message = "midRaiseRightShoulder"
      thread = threading.Thread(target=midRaiseRightShoulder)
      thread.start()
      return render_template('main.html')  
   elif action1 == "lowerRightShoulder":
      message = "lowerRightShoulder"
      thread = threading.Thread(target=lowerRightShoulder)
      thread.start()
      return render_template('main.html')  

   elif action1 == "armHome":
      message = "armHome"
      thread = threading.Thread(target=armHome)
      thread.start()
      return render_template('main.html')  

   elif action1 == "TPose":
      message = "TPose"
      thread = threading.Thread(target=TPose)
      thread.start()
      return render_template('main.html') 

   elif action1 == "pushUp":
      message = "pushUp"
      thread = threading.Thread(target=pushUp)
      thread.start()
      return render_template('main.html') 

   else:
      message = ""

   templateData = {
      'message' : message,
   }

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
