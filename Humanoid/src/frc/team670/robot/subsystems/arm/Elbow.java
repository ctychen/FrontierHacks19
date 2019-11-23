package frc.team670.robot.subsystems.arm;

import edu.wpi.first.wpilibj.command.Subsystem;

public class Elbow extends Subsystem {
	
	private double angle;
	


	public Elbow() {

	}
	
	public void initDefaultCommand() {

	}
	
	public double getAngleDegrees() {
		return this.angle;
	}
	
	
//	public double getForwardSoftLimitAngle(){
//
//	}
//
//	public double getReverseSoftLimitAngle()
//	{
//		
//	}
}