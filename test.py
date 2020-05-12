'''
* Python serial example;
 - reading system clock and CPU temperature.
 - send the values to serial buffer.
'''

import sys
import serial
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, QPushButton, QLineEdit, QTextEdit, QLabel, QDialog)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QTimer, QTime
import wmi
import pythoncom

class SerialUI(QMainWindow):

    global ser
    ser = serial.Serial()
    global flag
    flag = True

    def __init__(self):
        super(SerialUI,self).__init__()
        self.InitUI()

    def InitUI(self):
        # QMainWindow settings
        self.setWindowTitle('pySerial')
        self.setGeometry(10, 10, 1000, 750)
        self.move(500, 300)

        # Create push button
        self.b1 = QPushButton('Start', self)
        self.b1.move(380, 650)
        self.b1.clicked.connect(self.start_call)


        self.b2 = QPushButton('Stop', self)
        self.b2.move(550, 650)
        self.b2.clicked.connect(self.stop_call)

        # Create textbox
        self.tb1 = QLineEdit(self)  # COMPORT
        self.tb1.resize(200,70)
        self.tb1.move(280,80)

        self.tb2 = QLineEdit(self)  # BAUDRATE
        self.tb2.resize(200, 70)
        self.tb2.move(550, 80)

        # Create label
        self.lb1 = QLabel(self)
        self.lb1.setFont(QFont('SansSerif', 15))
        self.lb1.setStyleSheet("color: black")
        self.lb1.resize(250,50)
        self.lb1.move(400,160)
        self.lb1.setText("ECG Signal:")

        self.tb3 = QTextEdit(self)  # Time
        self.tb3.setFont(QFont('SansSerif', 15))
        self.tb3.setStyleSheet("color: black")
        self.tb3.resize(500, 400)
        self.tb3.move(250, 230)
        #self.lb3.setText("0")

        self.lb5 = QLabel(self)
        self.lb5.resize(200, 30)
        self.lb5.move(335, 50)
        self.lb5.setText("COMPORT:")

        self.lb6 = QLabel(self)
        self.lb6.resize(200, 30)
        self.lb6.move(605, 50)
        self.lb6.setText("BAUDRATE:")

        # Create timer
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.timer_slot)
        #
        # # Create time
        # self.time = QTime()
        self.show()

    # @pyqtSlot()
    # def b1_slot(self):
    #     self.timer.start(1000)
    #

    @pyqtSlot()
    def start_call(self):
        # Serial settings
        ser.port = self.tb1.text()
        ser.baudrate = self.tb2.text()
        if ser.is_open is not True:  # Open serial port
            ser.open()
        flag = True
        # # Read ECG signal
        while(flag==True):
            QApplication.processEvents()
            signal = ser.readline().decode('ascii')
            self.tb3.append(signal)
        # show time label


        if ser.is_open is not True:  # Check the serial port again whether it is open or not.
            ser.open()
        # else:
        #     # ser.write(b'ch_value') <-- without .encode()
        #     # Data format: (time#temperature) --> (8 characters; 00:00:00 + # + 5 characters; 00.00)
        #     ser.write((signal).encode())

    @pyqtSlot()
    def stop_call(self):
        flag = False
        ser.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SerialUI()
    sys.exit(app.exec_())