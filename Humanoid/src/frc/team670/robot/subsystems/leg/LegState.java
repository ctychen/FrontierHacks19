package frc.team670.robot.subsystems.leg;

public class LegState{

    private double hipAngle, kneeAngle, ankleAngle;

    /**
     * @param hipAngle   The absolute hip angle 
     * @param kneeAngle      The absolute knee angle 
     * @param ankleAngle      The absolute ankle angle 
     */
    public LegState(double hipAngle, double kneeAngle, double ankleAngle){
        this.hipAngle = hipAngle;
        this.kneeAngle = kneeAngle;
        this.ankleAngle = ankleAngle;
    }

    
    public double getHipAngle() {
        return hipAngle;
      }

    public double getKneeAngle() {
        return kneeAngle;
      }

    public double getAnkleAngle() {
        return ankleAngle;
      }



    
}