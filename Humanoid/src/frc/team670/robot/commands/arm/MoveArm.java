package frc.team670.robot.commands.arm;

import edu.wpi.first.wpilibj.command.CommandGroup;
import frc.team670.robot.subsystems.arm.*;

public class MoveArm extends CommandGroup{
    
    private Arm arm;
    private ArmState destination;
    
    public MoveArm(Arm arm, ArmState destination) {
        this.arm = arm;
        this.destination = destination;
        addSequential(new MoveShoulder(arm.getShoulder(), destination.getShoulderAngle()));
        addSequential(new MoveElbow(arm.getElbow(), destination.getElbowAngle()));
        addSequential(new MoveWrist(arm.getWrist(), destination.getWristAngle()));
        addSequential(new MoveHand(arm.getHand(), destination.getHandState()));
    }

}