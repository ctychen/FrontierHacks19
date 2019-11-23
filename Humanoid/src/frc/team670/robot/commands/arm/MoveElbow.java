package frc.team670.robot.commands.arm;

import edu.wpi.first.wpilibj.command.Command;
import frc.team670.robot.subsystems.arm.Elbow;
import frc.team670.robot.utils.MathUtils;

public class MoveElbow extends Command {

    private Elbow elbow;
    private double target;
    private static final double DEGREE_TOLERANCE = 5;

    public MoveElbow(Elbow elbow, double targetDegrees) {
        this.elbow = elbow;
        this.target = targetDegrees;
        requires(elbow);

        super.setInterruptible(true);
        setTimeout(2);
    }
    
    protected void initialize() {
    }

    protected void execute() {
        // turn the servo
    }
    
    protected boolean isFinished() {
        // angle that the elbow servo's at is close enough to the target
        return MathUtils.isWithinTolerance(elbow.getAngleDegrees(), target, DEGREE_TOLERANCE);
    }

    protected void end() {
        
    }
    

}