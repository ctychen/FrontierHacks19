package frc.team670.robot.subsystems.arm;


public class Arm {

    Shoulder shoulder;
    Elbow elbow;
    Wrist wrist;
    Hand hand;

    public Arm(Shoulder shoulder, Elbow elbow, Wrist wrist, Hand hand) {
        this.shoulder = shoulder;
        this.elbow = elbow;
        this.wrist = wrist;
        this.hand = hand;
    }

    public Shoulder getShoulder() {
        return shoulder;
    }

    public Elbow getElbow() {
        return elbow;
    }
    
    public Wrist getWrist() {
        return wrist;
    }

    public Hand getHand(){
        return hand;
    }
}
