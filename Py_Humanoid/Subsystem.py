from adafruit_servokit import ServoKit 
import time

kit = ServoKit(channels=16)

class Subsystem:

    port = 0
    
    def __init__(self, port):
        self.port = port

    def rotateTo(self, angle):
        kit.servo[self.port].angle = angle   #L ANKLE
        print('subsystem rotated to', angle)

    