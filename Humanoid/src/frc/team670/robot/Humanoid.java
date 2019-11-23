/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package frc.team670.robot;

import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.command.Scheduler;
import frc.team670.robot.subsystems.Body;
import frc.team670.robot.utils.Logger;

import frc.team670.robot.subsystems.arm.*;
import frc.team670.robot.subsystems.leg.*;

/**
 * The VM is configured to automatically run this class, and to call the
 * functions corresponding to each mode, as described in the TimedRobot
 * documentation. If you change the name  of this class or the package after
 * creating this project, you must also update the build.gradle file in the
 * project.
 */
public class Humanoid extends TimedRobot {
  public static OI oi;

  public static Hand leftHand = new Hand();
  public static Hand rightHand = new Hand();
  public static Wrist leftWrist = new Wrist();
  public static Wrist rightWrist = new Wrist();
  public static Elbow leftElbow = new Elbow();
  public static Elbow rightElbow = new Elbow();
  public static Shoulder leftShoulder = new Shoulder(); 
  public static Shoulder rightShoulder = new Shoulder();
  public static Ankle leftAnkle = new Ankle();
  public static Ankle rightAnkle = new Ankle();
  public static Knee leftKnee = new Knee();
  public static Knee rightKnee = new Knee();
  public static Hip leftHip = new Hip();
  public static Hip rightHip = new Hip();
  
  public static Arm leftArm = new Arm(leftShoulder, leftElbow, leftWrist, leftHand);
  public static Arm rightArm = new Arm(rightShoulder, rightElbow, rightWrist, rightHand);
  public static Leg leftLeg = new Leg(leftHip, leftKnee, leftAnkle);
  public static Leg rightLeg = new Leg(rightHip, rightKnee, rightAnkle);
 

//  private Command autonomousCommand, operatorControl;
  
  public Humanoid() {

  }

  /**
   * This function is run when the robot is first started up and should be
   * used for any initialization code.
   */
  @Override
  public void robotInit() {
    // auton_chooser.addDefault("Default Auto", new TimeDrive());
    // chooser.addObject("My Auto", new MyAutoCommand());
    
    oi = new OI();

    try {
      Logger.CustomLogger.setup();
    } catch (Throwable e) {
      Logger.logException(e);
    }
    
    Logger.consoleLog();

    // The command we want to test goes here
   // Scheduler.getInstance().add(new DistanceDrive(10, 1.0));
  }

  /**
   * This function is called every robot packet, no matter the mode. Use
   * this for items like diagnostics that you want ran during disabled,
   * autonomous, teleoperated and test.
   *
   * <p>This runs after the mode specific periodic functions, but before
   * LiveWindow and SmartDashboard integrated updating.
   */  
 @Override
  public void robotPeriodic() {
    // SmartDashboard.putNumber("gyro", (int) sensors.getAngle() % 360);
    // SmartDashboard.putString("current-command", Scheduler.getInstance().getName());
   // driveBase.sendEncoderDataToDashboard();

  }
  /**
   * This function is called once each time the robot enters Disabled mode.
   * You can use it to reset any subsystem information you want to clear when
   * the robot is disabled.
   */
  @Override
  public void disabledInit() {
//    SmartDashboard.putString("robot-state", "disabledPeriodic()");
    Logger.consoleLog("Robot Disabled");
    // autonomousCommand = oi.getSelectedAutonCommand();
    //leds.setStillDrive(true);
    // driveBase.initCoastMode();
//    intake.stop();
//    elbow.stop();
//    extension.stop();
//    wrist.stop();
    //TODO Stop motors here
  }

  @Override
  public void disabledPeriodic() throws Exception {

    //sensors.sendUltrasonicDataToDashboard();
    //driveBase.sendEncoderDataToDashboard();

    Scheduler.getInstance().run();
  }

  

  @Override
  public void teleopInit() {
    //SmartDashboard.putString("robot-state", "teleopPeriodic()");
    //leds.setForwardData(true);
    //driveBase.initBrakeMode();

//    if(DriverStation.getInstance().getMatchTime() < 130) {
//      Scheduler.getInstance().add(new SafelyResetExtension());
//    }
	  
    Logger.consoleLog("Teleop Started");
    // This makes sure that the autonomous stops running when
    // teleop starts running. If you want the autonomous to
    // continue until interrupted by another command, remove
    // this line or comment it out.
//    if (autonomousCommand != null) {
//      autonomousCommand.cancel();
//    }
  }

  /**
   * This function is called periodically during operator control.
 * @throws Exception 
   */
  @Override
  public void teleopPeriodic() throws Exception {
    Scheduler.getInstance().run();
  }

  /**
   * This function is called periodically during test mode.
   */
  @Override
  public void testPeriodic() {

  }

}