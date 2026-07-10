from gui.view import Window 
import time
class controller:

    def __init__(self, view:Window):
        self.view = view
        self.motor_power:bool = False
        self.controller_reset:bool = False
        self.motor_position_traker:bool = False
        self.motor_move:bool = False
        self.motor_revolution:float = 0.0
        self.motor_speed:int = 0
        self.motor_set_homing:bool = False
        self.motor_homing_offset:float = 0


        # Start Button
        self.view.btn_start.clicked.connect(self.starting)
        #Reset motor button 
        self.view.btn_reset.clicked.connect(self.reset_contr)
        #Motor_Move
        self.view.btn_move.clicked.connect(self.motor_start_move)
        #Position traker enable button
        self.view.btn_position_traker.clicked.connect(self.motor_start_position_traker)
        


        


    
        
    def starting(self):
        self.motor_power = True
        self.view.lbl_test.setText("STARTING...")
       
        self.controller_reset = True
        time.sleep(2)
        self.controller_reset = False
    def reset_contr(self):
        self.controller_reset = True
        self.view.lbl_test.setText("Controller reset")
    def motor_start_position_traker(self):
        self.motor_position_traker = True
        self.view.lbl_test.setText("Position_Traker reset")
    def motor_start_move(self):
        self.view.lbl_test.setText("Motor is moving")
        self.motor_move = True
    def motor_rev_set(self, n):
        self.view.lbl_test.setText("Set revolutions")
        self.motor_revolution = n
    def motor_speed(self, n):
        self.view.lbl_test.setText("Set speed")
        self.motor_speed = n
        
        

        
    