from adafruit_servokit import ServoKit 
from Subsystem import Subsystem
import time

kit = ServoKit(channels=16)

leftAnkle = Subsystem(4)
rightAnkle = Subsystem(8)

leftKnee = Subsystem(5)
rightKnee  = Subsystem(9)

leftThigh = Subsystem(6)
rightThigh = Subsystem(10)

leftShoulder = Subsystem(13)
rightShoulder = Subsystem(15)

leftElbow = Subsystem(12)
rightElbow = Subsystem(14)

leftWrist = Subsystem(0)
rightWrist = Subsystem(2)

leftHand = Subsystem(3)
rightHand = Subsystem(1)

delay = 1

class Humanoid():


    def stand(self):
        leftAnkle.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(120)   #L KNEE
        leftThigh.rotateTo(125)   #L HIP

        rightAnkle.rotateTo(100)  #R ANKLE
        rightKnee.rotateTo(100)   #R KNEE
        rightThigh.rotateTo(95) #R HIP

        print('standing')

    def walkForward(self):
        rightAnkle.rotateTo(90)   #L ANKLE
        leftAnkle.rotateTo(80)   #L ANKLE

        time.sleep(delay)

        rightThigh.rotateTo(120)   #L ANKLE
        rightKnee.rotateTo(120)   #L ANKLE
        leftThigh.rotateTo(140)   #L ANKLE
     
        leftKnee.rotateTo(140)   #L ANKLE

        time.sleep(delay)

        rightAnkle.rotateTo(100)   #L ANKLE
        leftAnkle.rotateTo(100)   #L ANKLE

        time.sleep(delay)

        leftAnkle.rotateTo(130)   #L ANKLE
        rightAnkle.rotateTo(130)   #L ANKLE

        time.sleep(delay)

        leftThigh.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(100)  #L ANKLE
        rightThigh.rotateTo(90)   #L ANKLE
        rightKnee.rotateTo(90)   #L ANKLE

        time.sleep(delay)

        leftAnkle.rotateTo(100)   #L ANKLE
        rightAnkle.rotateTo(100)   #L ANKLE

        print('Walking Forward')

    def turnLeft(self):
        rightAnkle.rotateTo(80)   #L ANKLE
        leftAnkle.rotateTo(70)   #L ANKLE

        time.sleep(0.25)

        rightThigh.rotateTo(120)   #L ANKLE
        rightKnee.rotateTo(120)   #L ANKLE
        leftThigh.rotateTo(120)   #L ANKLE
        leftKnee.rotateTo(120)   #L ANKLE

        time.sleep(0.25)

        rightAnkle.rotateTo(100)   #L ANKLE
        leftAnkle.rotateTo(100)   #L ANKLE

        leftAnkle.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(120)   #L KNEE
        leftThigh.rotateTo(120)   #L HIP
        rightAnkle.rotateTo(100)  #R ANKLE
        rightKnee.rotateTo(100)   #R KNEE
        rightThigh.rotateTo(100) #R HIP

        print('Turning Left')

    def bend(self):
        leftThigh.rotateTo(85)
        leftKnee.rotateTo(85)
        rightThigh.rotateTo(145)
        rightKnee.rotateTo(145)

    def turnRight(self):
        leftAnkle.rotateTo(130)   #L ANKLE
        rightAnkle.rotateTo(130)   #L ANKLE

        time.sleep(0.25)

        leftThigh.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(100)  #L ANKLE
        rightThigh.rotateTo(90)   #L ANKLE
        rightKnee.rotateTo(90)   #L ANKLE

        time.sleep(0.25)

        leftAnkle.rotateTo(100)   #L ANKLE
        rightAnkle.rotateTo(100)   #L ANKLE

        leftAnkle.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(120)   #L KNEE
        leftThigh.rotateTo(120)   #L HIP
        rightAnkle.rotateTo(100)  #R ANKLE
        rightKnee.rotateTo(100)   #R KNEE
        rightThigh.rotateTo(100) #R HIP

    def waveLeft(self):
        leftShoulder.rotateTo(150)
        leftElbow.rotateTo(150)
        leftWrist.rotateTo(100)
        leftHand.rotateTo(150)

    def openLeftClaw(self):
        leftHand.rotateTo(150)

    def closeLeftClaw(self):
        leftHand.rotateTo(0)

    def turnLeftWristRight(self):
        leftWrist.rotateTo(50)

    def turnLeftWristLeft(self):
        leftWrist.rotateTo(100)

    def openLeftElbow(self):
        leftElbow.rotateTo(160)

    def closeLeftElbow(self):
        leftElbow.rotateTo(50)

    def raiseLeftShoulder(self):
        leftShoulder.rotateTo(180)

    def midRaiseLeftShoulder(self):
        leftShoulder.rotateTo(60)

    def lowerLeftShoulder(self):
        leftShoulder.rotateTo(0)

# Right side
    
    def openRightClaw(self):
        rightHand.rotateTo(150)

    def closeRightClawLeft(self):
        rightHand.rotateTo(0)

    def turnRightWristRight(self):
        rightWrist.rotateTo(50)

    def turnRightWristLeft(self):
        rightWrist.rotateTo(100)

    def openRightElbow(self):
        rightElbow.rotateTo(160)

    def closeRightElbow(self):
        rightElbow.rotateTo(50)

    def raiseRightShoulder(self):
        rightShoulder.rotateTo(180)

    def midRaiseRightShoulder(self):
        rightShoulder.rotateTo(60)

    def lowerRightShoulder(self):
        rightShoulder.rotateTo(0)

    

    

    




       
        
        

