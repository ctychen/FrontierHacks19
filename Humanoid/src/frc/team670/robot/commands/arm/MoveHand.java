package frc.team670.robot.commands.arm;

import edu.wpi.first.wpilibj.command.Command;
import frc.team670.robot.subsystems.arm.Hand;
import frc.team670.robot.utils.MathUtils;

public class MoveHand extends Command {

    private Hand Hand;
    private double target;
    private static final double DEGREE_TOLERANCE = 2;

    public MoveHand(Hand Hand, double targetDegrees) {
        this.Hand = Hand;
        this.target = targetDegrees;
        requires(hand);

        super.setInterruptible(true);
        setTimeout(2);
    }
    
    protected void initialize() {
    }

    protected void execute() {
        // turn the servo
    }
    
    protected boolean isFinished() {
        // angle that the Hand servo's at is close enough to the target
        return MathUtils.isWithinTolerance(hand.getAngleDegrees(), target, DEGREE_TOLERANCE);
    }

    protected void end() {
        
    }
    

}