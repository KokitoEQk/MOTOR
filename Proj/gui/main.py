import sys
from PyQt5 import QtWidgets

from gui.view import Window
from gui.controller import controller



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    cntr = controller(window)
    
    window.show()

    sys.exit(app.exec_())