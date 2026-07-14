from gui.view import Window 
from PyQt5.QtWidgets import QPushButton
import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from PyQt5.QtCore import Qt


class controller:

    def __init__(self, view:Window):
        self.view = view
       
        self.rev = 0
        self.degree = 0
        self.speed = 0
        
        # Start Button
        self.view.btn_start.setCheckable(True)
        
        self.view.btn_start.clicked.connect(lambda:self.motor_power(self.view.btn_start.isChecked()))
       
        
        self.view.btn_start.clicked.connect(lambda:self.change_color_btn(button=self.view.btn_start, color="#00FF00"))
        #Reset motor button 
        self.view.btn_reset.clicked.connect(self.controller_reset)
        
        #Motor_Move
        self.motor_speed()
        if(int(self.speed) < 30):

            self.view.btn_move.clicked.connect(self.motor_move)
            
        else:
            self.view.lbl_test.setText("Set speed under 30")
        
        #Position traker enable button
        self.view.btn_position_traker.clicked.connect(self.motor_position_traker)
        #Revolution set
        
        

        
        self.view.movieScr.setMovie(self.view.GIf_movie)
        self.view.movieScr.setScaledContents(True)
        self.view.movieScr.setFixedSize(800,400)
        self.view.movieScr.setAlignment(Qt.AlignCenter)
        self.view.GIf_movie.start()
        self.view.GIf_movie.stop()
        
    def controller_reset(self):
        self.view.GIf_movie.stop()
        self.view.lbl_test.setText("Controller reset")
    def motor_position_traker(self):
        
        self.view.lbl_test.setText("Position_Traker reset")
    
    def motor_speed(self):
        return self.speed
    def motor_move(self):
        self.view.GIf_movie.start()
        self.degree = self.view.le_R.text() 
        self.rev = int(self.degree)/360
        self.view.lbl_test.setText(f"DEGREES:{self.rev}")
        
        
        
        if(int(self.speed) < 30):

            self.view.lbl_test.setText("Motor is moving")
        else:
            self.view.lbl_test.setText("Set speed under 30")
            
        return self.rev, self.speed
       
    def motor_revolution(self):
        self.view.lbl_test.setText("Set revolutions")
        
    def motor_speed(self):
        self.view.lbl_test.setText("Set speed")

    def change_color_btn(self, button:QPushButton,color):
        button.setStyleSheet(f"""
            background-color: {color};
            font-weight: bold;
            border-color: rgb(0,30,100);
                             """)        
    
    def motor_power(self, is_checked):
        if(is_checked):
            self.view.btn_start.setText("MOTOR: ON")
            self.view.btn_start.setStyleSheet(f"""
            background-color: #00FF00;
            font-weight: bold;
            border-style: solid;
            border-width: 3px;
            outline: none;
            
                             """)       
        else:
            self.view.btn_start.setText("MOTOR: OFF")
            self.view.btn_start.setStyleSheet(f"""
            background-color: #FF0000;
            font-weight: bold;
            border-style: solid;
            border-width: 3px;
            outline: none;
                             """)       
    





       



        

        
    