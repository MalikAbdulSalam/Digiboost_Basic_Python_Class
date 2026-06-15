import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal
import subprocess

# Import functions from the second file



class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Load UI
        try:
            uic.loadUi('drone.ui', self)
        except Exception as e:
            print(f"Error loading UI file: {e}")
            sys.exit(1)
       


        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Drone Control")
    sys.exit(app.exec_())

