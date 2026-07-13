from gui.view import Window 
import time
from PyQt5 import (QtCore,QtGui)
import glob
import contextlib

from PIL import Image


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

fp_in = ".png"
fp_out = "/path/to/image.gif"

# use exit stack to automatically close opened images
# with contextlib.ExitStack() as stack:

#     # lazily load images
#     imgs = (stack.enter_context(Image.open(f))
#             for f in sorted(glob.glob(fp_in)))

#     # extract  first image from iterator
#     img = next(imgs)

#     # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
#     img.save(fp=fp_out, format='GIF', append_images=imgs,
#              save_all=True, duration=200, loop=0)
       
    
        

        
    