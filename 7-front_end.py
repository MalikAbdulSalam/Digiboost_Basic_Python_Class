import sys
from PyQt5 import QtGui, uic ,QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class MyWindow(QtWidgets.QDialog):
    def __init__(self): # init function
        super(MyWindow, self).__init__()
        uic.loadUi('7-front_end.ui', self)
        self.show()




    # def ftn1(self):
    #     print("First Button Pressed")
if __name__ == '__main__': # code starts from here
    app = QtWidgets.QApplication(sys.argv) # application run
    window = MyWindow() # run myWindow class
    sys.exit(app.exec_()) # Close application
