package frc.team670.robot.subsystems.leg;


public class Leg {
    
    Ankle ankle;
    Hip hip;
    Knee knee;

    public Leg(Hip hip, Knee knee, Ankle ankle) {
        this.hip = hip;
        this.knee = knee;
        this.ankle = ankle;
    }

}