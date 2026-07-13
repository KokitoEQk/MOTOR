import sys
from PyQt5.QtWidgets import (QMainWindow ,QWidget, QToolTip, QLabel, QPushButton, QApplication, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import (QFont, QPalette, QColor,QPixmap, QIcon)

from PyQt5 import QtWidgets



class Window(QMainWindow):

    
    def __init__(self):
        """
        Makes new page
        
        """
        super().__init__()
        self.setWindowTitle("Window for motor")
        self.setMinimumSize(400,400)

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
        self.setGeometry(700, 200, 200, 200)
        #Button 1
        self.btn_start = QPushButton("START")
        self.btn_start.setStyleSheet(""" 
            border-color: rgb(0,30,100);
                                     """)
        self.btn_reset = QPushButton("RESET")
        self.btn_move = QPushButton("MOVE_MOTOR")
        self.btn_position_traker = QPushButton("POSITION TRAKER")
        #QPixmaps
        pixmap = QPixmap("motor_spinning.gif")
        self.pixmap = QLabel()
        self.pixmap.setPixmap(pixmap)
        
        #LineEdit 1
        self.le = QLineEdit(self)
        self.le.setStyleSheet("""
            border-color: beige;

                            
                                """)
        self.le_R = QLineEdit(self)
        self.le_S = QLineEdit(self)
        #QWidgets
        self.widget_image = QWidget()
        self.widget_image.setStyleSheet("""
            image: CAR.png;
                """)

        #Qlable
        self.lbl_RPM = QLabel("RPM")
        self.lbl_RPM.setStyleSheet("""
            background-color: #323432;
            color: #FFFFFF;
            font-family: Titilium;
            font-size: 16px;
            border-color: beige;
            padding: 6px;
            """)
        
        self.lbl_test = QLabel("Test")
        self.lbl_test.setStyleSheet("""
            background-color: #555555;
            color: #FFFFFF;
            font-family: Titilium;
            font-size: 16px;
            """)
        
        self.lbl_speed = QLabel("SPEED")
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
        hbox.addStretch()
        hbox.addWidget(self.btn_start)
        hbox.addWidget(self.le)
        hbox.addWidget(self.lbl_RPM)
       
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.btn_move)
        hbox1.addWidget(self.btn_position_traker)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.btn_reset)
        hbox2.addWidget(self.le_S)
        hbox2.addWidget(self.lbl_speed)
        #Vbox1
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_test)

        vbox.addWidget(self.pixmap)
        #Page_layout

        vbox.addStretch(2)
        page_layout.addLayout(hbox)
        page_layout.addLayout(hbox2)
        page_layout.addLayout(vbox)
        page_layout.addLayout(hbox1)
        return page
       
        


