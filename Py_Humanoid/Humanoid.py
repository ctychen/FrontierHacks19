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

delay = 0.4

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

        rightThigh.rotateTo(125)   #L ANKLE
        rightKnee.rotateTo(115)   #L ANKLE
        leftThigh.rotateTo(135)   #L ANKLE
        leftKnee.rotateTo(135)   #L ANKLE

        time.sleep(delay)

        rightAnkle.rotateTo(100)   #L ANKLE
        leftAnkle.rotateTo(100)   #L ANKLE

        time.sleep(delay)

        leftAnkle.rotateTo(125)   #L ANKLE
        rightAnkle.rotateTo(125)   #L ANKLE

        time.sleep(delay)

        leftThigh.rotateTo(120)   #L ANKLE
        leftKnee.rotateTo(120)  #L ANKLE
        rightThigh.rotateTo(105)   #L ANKLE
        rightKnee.rotateTo(105)   #L ANKLE

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
        leftAnkle.rotateTo(120)   #L ANKLE
        rightAnkle.rotateTo(120)   #L ANKLE

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
        leftHand.rotateTo(100)

    def closeLeftClaw(self):
        leftHand.rotateTo(20)

    def turnLeftWristRight(self):
        leftWrist.rotateTo(100)

    def turnLeftWristLeft(self):
        leftWrist.rotateTo(50)

    def openLeftElbow(self):
        leftElbow.rotateTo(50)

    def closeLeftElbow(self):
        leftElbow.rotateTo(160)

    def raiseLeftShoulder(self):
        leftShoulder.rotateTo(0)

    def midRaiseLeftShoulder(self):
        leftShoulder.rotateTo(60)

    def lowerLeftShoulder(self):
        leftShoulder.rotateTo(180)

# Right side
    
    def openRightClaw(self):
        rightHand.rotateTo(100)

    def closeRightClaw(self):
        rightHand.rotateTo(0)

    def turnRightWristRight(self):
        rightWrist.rotateTo(50)

    def turnRightWristLeft(self):
        rightWrist.rotateTo(100)

    def openRightElbow(self):
        rightElbow.rotateTo(50)

    def closeRightElbow(self):
        rightElbow.rotateTo(160)

    def raiseRightShoulder(self):
        rightShoulder.rotateTo(180)

    def midRaiseRightShoulder(self):
        rightShoulder.rotateTo(70)

    def lowerRightShoulder(self):
        rightShoulder.rotateTo(0)

# arms home

    def armHome(self):
        rightWrist.rotateTo(100)
        leftWrist.rotateTo(100)
        rightElbow.rotateTo(160)
        leftElbow.rotateTo(180)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(180)

    def TPose(self):
        rightShoulder.rotateTo(180)
        leftShoulder.rotateTo(0)
        rightElbow.rotateTo(55)
        leftElbow.rotateTo(55)
        rightWrist.rotateTo(100)
        leftWrist.rotateTo(50)

    def pushUp(self):
        # for x in range (5):      
        rightElbow.rotateTo(50)
        leftElbow.rotateTo(50)
        time.sleep(1)
        rightElbow.rotateTo(160)
        leftElbow.rotateTo(160)

    def dab(self):
        rightShoulder.rotateTo(70)
        rightWrist.rotateTo(50)
        leftShoulder.rotateTo(0)
        leftElbow.rotateTo(55)
        leftWrist.rotateTo(50)

        time.sleep(1)

        rightWrist.rotateTo(100)
        leftWrist.rotateTo(100)
        rightElbow.rotateTo(160)
        leftElbow.rotateTo(180)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(180)

   # def rickRoll(self):

    def dance(self):
     #8times hands up and same hand out
     #16 times one hand out and other hand going out and in

        leftShoulder.rotateTo(0)
        time.sleep(0.55)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.55)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

        rightElbow.rotateTo(160)
        leftShoulder.rotateTo(0)
        time.sleep(0.5)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.55)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

        rightElbow.rotateTo(160)
        leftShoulder.rotateTo(0)
        time.sleep(0.5)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.5)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

        rightElbow.rotateTo(160)
        leftShoulder.rotateTo(0)
        time.sleep(0.55)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.55)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

    # 2nd step

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        leftElbow.rotateTo(50)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        time.sleep(0.275)

        # shuffling

        rightElbow.rotateTo(160)
        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(60)
        time.sleep(0.275)

        rightElbow.rotateTo(50)
        rightShoulder.rotateTo(70)
        time.sleep(0.1)
        rightElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.1)
        rightShoulder.rotateTo(0)
        time.sleep(0.1)
        leftShoulder.rotateTo(0)
        rightShoulder.rotateTo(0)
        time.sleep(0.5)

        leftElbow.rotateTo(50)
        leftShoulder.rotateTo(70)
        time.sleep(0.275)
        leftElbow.rotateTo(160)
        leftShoulder.rotateTo(180)
        time.sleep(0.275)

        leftShoulder.rotateTo(0)
        time.sleep(0.55)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.55)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

        rightElbow.rotateTo(160)
        leftShoulder.rotateTo(0)
        time.sleep(0.5)
        leftShoulder.rotateTo(60)
        leftElbow.rotateTo(50)

        time.sleep(0.55)

        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        time.sleep(0.55)
        rightShoulder.rotateTo(70)
        rightElbow.rotateTo(50)

        time.sleep(0.55)

        rightElbow.rotateTo(160)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(180)
        time.sleep(0.2)

        rightElbow.rotateTo(50)
        leftElbow.rotateTo(50)
        rightShoulder.rotateTo(70)
        leftShoulder.rotateTo(70)

        time.sleep(0.275)

        rightElbow.rotateTo(160)
        leftElbow.rotateTo(160)
        rightShoulder.rotateTo(180)
        leftShoulder.rotateTo(0)

        time.sleep(0.275)

        rightShoulder.rotateTo(180)
        leftShoulder.rotateTo(0)
        rightElbow.rotateTo(55)
        leftElbow.rotateTo(55)
        rightWrist.rotateTo(100)
        leftWrist.rotateTo(50)

        time.sleep(0.5)

        rightWrist.rotateTo(100)
        leftWrist.rotateTo(100)
        rightElbow.rotateTo(160)
        leftElbow.rotateTo(180)
        rightShoulder.rotateTo(0)
        leftShoulder.rotateTo(180)

        time.sleep(0.5)




        


    

    

    




       
        
        
