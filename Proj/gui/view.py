import sys
from PyQt5.QtWidgets import (QToolTip, QMainWindow,QWidget, QLabel, QPushButton,  QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import (QMovie)
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt




class Window(QMainWindow):

    
    def __init__(self):
        """
        Makes new page
        
        """

        super().__init__()
        self.setWindowTitle("Window for motor")
        self.setMinimumSize(900,650)
        

        # widget = Color(self,"green")
        # self.setCentralWidget(widget)

       
        self.page = self.create_page()
        self.setCentralWidget(self.page)
        self.page.setStyleSheet(""" 
            background-color: #6960EC;
                                
                                """)
    

        
    def create_page(self):
       
        page = QtWidgets.QWidget()
        page_layout = QtWidgets.QVBoxLayout(page)
        self.setGeometry(560, 100, 0, 0)

        #Buttons
        self.btn_start = QPushButton("POWER")
        self.btn_start.setToolTip("Giving power to the motor")
        self.btn_start.setFixedSize(210,50)
        self.btn_start.setStyleSheet(f""" 
            background-color: #FF0000;
            border-style: solid;
            border-width: 3px;
            font-weight: bold;
            
                                     """)
        self.btn_reset = QPushButton("RESET")
        self.btn_reset.setToolTip("Resets the controller")
        self.btn_reset.setFixedSize(210,50)
        self.btn_reset.setStyleSheet(f""" 
                                    background-color: #00FF00;
                                    font-weight: bold;
                                    border-style: solid;
                                    border-width: 3px;
                                    
                                    """)
        self.btn_move = QPushButton("MOVE MOTOR")
        self.btn_move.setToolTip("Move the motor")
        self.btn_move.setStyleSheet(f"""
                                    background-color: #FFFFFF;
                                    font-weight: bold;
                                    """)
        self.btn_position_traker = QPushButton("POSITION TRAKER")
        self.btn_position_traker.setStyleSheet(f"""
                                    background-color: #FFFFFF;
                                    font-weight: bold;
                                    """)

        #Gif Movie
        script_dir = r"C:\Appl\Proj\gui"
        root_gif1 = os.path.join(script_dir, "motor_spinning.gif")
        self.movieScr = QLabel()
        
        self.GIf_movie = QMovie(root_gif1)
        
        
        #LineEdit 1
        
        self.le_R = QLineEdit(self)
        self.le_R.setToolTip("Set the revolutions")
        self.le_R.setFixedSize(200,50)
        self.le_R.setText("0")
        self.le_R.setStyleSheet("""
            background-color: #FFFFFF;                   
                                """)

        self.le_S = QLineEdit(self)
        self.le_S.setToolTip("Set the speed")
        self.le_S.setFixedSize(200,50)
        self.le_S.setStyleSheet("""
            background-color: #FFFFFF;                   
                                """)
        self.le_S.setText("0")

        #QWidgets
        self.widget_image = QWidget()
        

        #Qlable
        self.lbl_RPM = QLabel("Degrees")
        self.lbl_RPM.setFixedSize(100,50)
        self.lbl_RPM.setStyleSheet("""
            background-color: #323432;
            color: #FFFFFF;
            font-family: Titilium;
            font-size: 16px;
            border-color: beige;
            padding: 6px;
            """)
        
        self.lbl_test = QLabel()
        self.lbl_test.setToolTip("Results")
        self.lbl_test.setAlignment(Qt.AlignCenter)
        self.lbl_test.setStyleSheet(f""" 
                                    background-color: #808080;
                                    font-weight: bold;
                                    border-style: solid;
                                    border-width: 3px;
                                    font-size: 32px;
                                    """)
        
        self.lbl_speed = QLabel("Speed")
        self.lbl_speed.setFixedSize(100,50)
        self.lbl_speed.setStyleSheet("""
            background-color: #323432;
            color: #FFFFFF;
            font-family: Titilium;
            font-size: 16px;
            border-color: beige;
            padding: 6px;
            """)
        

        #Hbox1
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.btn_start)
        hbox.addWidget(self.le_R)
        hbox.addWidget(self.lbl_RPM)
       
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.btn_move)
        hbox1.addWidget(self.btn_position_traker)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.btn_reset)
        hbox2.addWidget(self.le_S)
        hbox2.addWidget(self.lbl_speed)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.movieScr)
        #Vbox1
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_test)

        
        #Page_layout

        vbox.addStretch(1)
        
        page_layout.addLayout(hbox)
        page_layout.addLayout(hbox2)
        page_layout.addLayout(vbox)
        page_layout.addLayout(hbox3)
        page_layout.addLayout(hbox1)
        return page
       
        


