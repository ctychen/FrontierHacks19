package frc.team670.robot.commands.arm;

import edu.wpi.first.wpilibj.command.Command;
import frc.team670.robot.subsystems.arm.Wrist;
import frc.team670.robot.utils.MathUtils;

public class MoveWrist extends Command {

    private Wrist wrist;
    private double target;
    private static final double DEGREE_TOLERANCE = 5;

    public MoveWrist(Wrist wrist, double targetDegrees) {
        this.wrist = wrist;
        this.target = targetDegrees;
        requires(wrist);

        super.setInterruptible(true);
        setTimeout(2);
    }
    
    protected void initialize() {
    }

    protected void execute() {
        // turn the servo
    }
    
    protected boolean isFinished() {
        // angle that the Wrist servo's at is close enough to the target
        return MathUtils.isWithinTolerance(wrist.getAngleDegrees(), target, DEGREE_TOLERANCE);
    }

    protected void end() {
        
    }
    

}