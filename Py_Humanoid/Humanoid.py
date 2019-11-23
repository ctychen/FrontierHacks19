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

class Humanoid():

    def stand(self):
        leftAnkle.rotateTo(100)   #L ANKLE
        leftKnee.rotateTo(120)   #L KNEE
        leftThigh.rotateTo(120)   #L HIP
        rightAnkle.rotateTo(100)  #R ANKLE
        rightKnee.rotateTo(100)   #R KNEE
        rightThigh.rotateTo(100) #R HIP
        print('standing')

    def walkForward(self):
        rightAnkle.rotateTo(80)   #L ANKLE
        leftAnkle.rotateTo(70)   #L ANKLE

        time.sleep(0.25)

        rightThigh.rotateTo(120)   #L ANKLE
        rightKnee.rotateTo(120)   #L ANKLE
        leftThigh.rotateTo(140)   #L ANKLE
        leftKnee.rotateTo(140)   #L ANKLE

        time.sleep(0.25)

        rightAnkle.rotateTo(100)   #L ANKLE
        leftAnkle.rotateTo(100)   #L ANKLE

        time.sleep(0.25)

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
        rightKnee.rotate(145)

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

    




       
        
        

