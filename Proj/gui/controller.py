from gui.view import Window 
import time
from PyQt5 import (QtCore,QtGui)

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
       
        self.view.lbl_test.setText("STARTING...")
    def controller_reset(self):
        
        self.view.lbl_test.setText("Controller reset")
    def motor_position_traker(self):
        
        self.view.lbl_test.setText("Position_Traker reset")
    def motor_move(self):
        self.r = self.view.le_R.text
        self.speed = self.view.le_S.text
        self.view.lbl_test.setText("Motor is moving")
        return self.r, self.speed
       
    def motor_revolution(self):
        self.view.lbl_test.setText("Set revolutions")
        
    def motor_speed(self):
        self.view.lbl_test.setText("Set speed")
       
    
        

        
    