package frc.team670.robot.commands.arm;


import edu.wpi.first.wpilibj.command.Command;
import frc.team670.robot.subsystems.arm.Elbow;


public class MoveShoulder extends Command {

private Shoulder shoulder;
private double target; 
private longExecute; 

public MoveShoulder(Shoulder shoulder, double targetDegrees) {
this.shoulder = shoulder;
this. target = targetDegrees;
requires(shoulder);

super.setInterruptible(true);
setTimout(2);
}

protected void initialize () {

}

protected void execute(){

}

protected void isFinished(){

}

protected void end(){
    
}
}