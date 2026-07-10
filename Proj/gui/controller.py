from MOTOR.Proj.gui.view import Window 
import time
from PyQt5 import (QtCore,QtGui)
from src import controls

class controller:

    def __init__(self, view:Window):
        self.view = view
       
        self.r:float = 0.0
        self.speed:int = 0
        
        # Start Button
        self.view.btn_start.clicked.connect(self.motor_power)
        
        #Reset motor button 
        self.view.btn_reset.clicked.connect(self.controller_reset)
        
        #Motor_Move
        self.view.btn_move.clicked.connect(self.motor_move)
        #Position traker enable button
        self.view.btn_position_traker.clicked.connect(self.motor_position_traker)
        #Revolution set
        

    def motor_power(self):
        controls.motor_power("True")
        self.view.lbl_test.setText("STARTING...")
    def controller_reset(self):
        controls.controller_reset()
        self.view.lbl_test.setText("Controller reset")
    def motor_position_traker(self):
        controls.motor_position_tracker("True")
        self.view.lbl_test.setText("Position_Traker reset")
    def motor_move(self):
        self.r = self.view.le_R.text
        self.speed = self.view.le_S.text
        self.view.lbl_test.setText("Motor is moving")
        controls.motor_revolution((360/self.r))
        controls.motor_speed(int(self.speed))
        controls.motor_move()
        return self.r, self.speed
       
    def motor_revolution(self):
        controls.motor_revolution(self.r)
        self.view.lbl_test.setText("Set revolutions: {self.r}")
        
    def motor_speed(self):
        controls.motor_speed(self.speed)
        self.view.lbl_test.setText("Set speed")
       
    
        

        
    