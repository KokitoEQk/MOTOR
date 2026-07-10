from gui.view import Window 
import time
class controller:

    def __init__(self, view:Window):
        self.view = view
        self.motor_power:bool = False
        self.cr:bool = False
        self.mpt:bool = False
        self.motor_move:bool = False
        self.motor_revolution:float = 0.0
        self.motor_speed:int = 0
        self.motor_set_homing:bool = False
        self.motor_homing_offset:float = 0
        r:float
        speed:int

        # Start Button
        self.view.btn_start.clicked.connect(self.motor_power(True))
        #Reset motor button 
        self.view.btn_reset.clicked.connect(self.controller_reset)
        #Motor_Move
        self.view.btn_move.clicked.connect(self.motor_move)
        #Position traker enable button
        self.view.btn_position_traker.clicked.connect(self.motor_position_traker(True))
        #Revolution set
        self.motor_revolution(r)
        #Speed set
        self.motor_speed(speed)

    def motor_power(self):
       
        self.view.lbl_test.setText("STARTING...")
    def controller_reset(self):
        
        self.view.lbl_test.setText("Controller reset")
    def motor_position_traker(self):
        
        self.view.lbl_test.setText("Position_Traker reset")
    def motor_move(self):
        r = self.view.le.text
        speed = self.view.le1.text
        self.view.lbl_test.setText("Motor is moving")
        return r, speed
       
    def motor_revolution(self):
        self.view.lbl_test.setText("Set revolutions")
        
    def motor_speed(self):
        self.view.lbl_test.setText("Set speed")
       
        
        

        
    