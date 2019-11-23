package frc.team670.robot.utils;

import frc.team670.robot.RobotConstants;

public class MathUtils {
	/**
	 * 
	 * @param ticks
	 * @return corresponding inch value for number of ticks
	 */
	public static double convertEncoderTicksToInches(int ticks) {
		return ticks*((Math.PI * RobotConstants.DRIVE_BASE_WHEEL_DIAMETER)/RobotConstants.ENCODER_TICKS_PER_ROTATION);
	}
	
	public static double convertInchesToEncoderTicks(double inches) {
		return inches
				* (RobotConstants.ENCODER_TICKS_PER_ROTATION / (Math.PI * RobotConstants.DRIVE_BASE_WHEEL_DIAMETER));
	}
	
    /**
     * Returns true if the value is within +/- tolerance of target
     * @param tolerance The tolerance (must be positive)
     */
    public static boolean isWithinTolerance(double value, double target, double tolerance) {
        return (value > target - tolerance && value < target + tolerance);
    }
}
