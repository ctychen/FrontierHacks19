package frc.team670.robot.subsystems.arm;

import edu.wpi.first.wpilibj.command.Subsystem;

public class Wrist extends Subsystem {
	
	private double angle;
	
	public Wrist() {

	}
	
	public void initDefaultCommand() {

	}
	
	public double getAngleDegrees(){
		return this.angle;
	}
}