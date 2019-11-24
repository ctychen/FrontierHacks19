import WatchKit
import Foundation
import CoreMotion

class InterfaceController: WKInterfaceController {


    @IBOutlet weak var labelX: WKInterfaceLabel!
    @IBOutlet weak var labelY: WKInterfaceLabel!
    @IBOutlet weak var labelZ: WKInterfaceLabel!
    let motionManager = CMMotionManager()


    func awakeWithContext(context: AnyObject?) {
        super.awake(withContext: context)

        motionManager.accelerometerUpdateInterval = 0.1
    }

    override func willActivate() {
        super.willActivate()

        if (motionManager.isAccelerometerAvailable) {
            let handler:CMAccelerometerHandler = {(data: CMAccelerometerData?, error: NSError?) -> Void in
                self.labelX.setText(String(format: "%.2f", data!.acceleration.x))
                self.labelY.setText(String(format: "%.2f", data!.acceleration.y))
                self.labelZ.setText(String(format: "%.2f", data!.acceleration.z))
                } as! CMAccelerometerHandler
            motionManager.startAccelerometerUpdates(to: OperationQueue.current!, withHandler: handler)
        }
        else {
            self.labelX.setText("not available")
            self.labelY.setText("not available")
            self.labelZ.setText("not available")
        }
    }

    override func didDeactivate() {
        super.didDeactivate()

        motionManager.stopAccelerometerUpdates()
    }
}
