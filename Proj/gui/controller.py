from gui.view import Window 

import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class controller:

    def __init__(self, view:Window):
        self.view = view
       
        self.rev = 0
        self.degree = 0
        self.speed = 0
        
        # Start Button
        self.view.btn_start.clicked.connect(self.motor_power)
        
        #Reset motor button 
        self.view.btn_reset.clicked.connect(self.controller_reset)
        
        #Motor_Move
        self.view.btn_move.clicked.connect(self.motor_move)
        #Position traker enable button
        self.view.btn_position_traker.clicked.connect(self.motor_position_traker)
        #Revolution set


        
        self.view.movieScr.setMovie(self.view.GIf_movie)
        self.view.GIf_movie.start()
        self.view.GIf_movie.stop()

    def motor_power(self):
       
        self.view.lbl_test.setText("STARTING...")
        self.view.GIf_movie.start()
    def controller_reset(self):
        self.view.GIf_movie.stop()
        self.view.lbl_test.setText("Controller reset")
    def motor_position_traker(self):
        
        self.view.lbl_test.setText("Position_Traker reset")
    def motor_move(self):
        self.view.GIf_movie.start()
        self.degree = self.view.le_R.text() 
        self.rev = int(self.degree)/360
        self.view.lbl_test.setText(f"DEGREES:{self.rev}")
        self.speed = self.view.le_S.text()
        self.view.lbl_test.setText("Motor is moving")
        return self.rev, self.speed
       
    def motor_revolution(self):
        self.view.lbl_test.setText("Set revolutions")
        
    def motor_speed(self):
        self.view.lbl_test.setText("Set speed")

       



        

        
    