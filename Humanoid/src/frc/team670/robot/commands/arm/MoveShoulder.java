package frc.team670.robot.commands.arm;

import edu.wpi.first.wpilibj.command.Command;
import frc.team670.robot.subsystems.arm.Shoulder;

public class MoveShoulder extends Command {

	private Shoulder shoulder;
	private double target;

	public MoveShoulder(Shoulder shoulder, double targetDegrees) {
		this.shoulder = shoulder;
		this.target = targetDegrees;
		requires(shoulder);

		super.setInterruptible(true);
		setTimeout(2);
	}

	protected void initialize() {

	}

	protected void execute() {

	}

	protected boolean isFinished() {
		return false;
	}

	protected void end() {

	}
}