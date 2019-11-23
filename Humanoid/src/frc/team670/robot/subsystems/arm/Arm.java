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
    

}
