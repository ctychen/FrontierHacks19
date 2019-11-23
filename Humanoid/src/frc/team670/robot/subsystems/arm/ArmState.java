package frc.team670.robot.subsystems.arm;

public class ArmState{

    private double shoulderAngle, elbowAngle, wristAngle;
    private boolean handOpened;

    /**
     * @param shoulderAngle   The absolute Shoulder angle 
     * @param elbowAngle      The absolute Elbow angle 
     * @param wristAngle      The absolute Wrist angle 
     * @param handOpened      Whether the Hand should be open or closed
     */
    public ArmState(double shoulderAngle, double elbowAngle, double wristAngle, boolean handOpened){
        this.shoulderAngle = shoulderAngle;
        this.elbowAngle = elbowAngle;
        this.wristAngle = wristAngle;
        this.handOpened = handOpened;
    }

    
    public double getShoulderAngle() {
        return shoulderAngle;
      }

    public double getElbowAngle() {
        return elbowAngle;
      }

    public double getWristAngle() {
        return wristAngle;
      }

    public boolean getHandState(){
        return handOpened;
    }

    
}