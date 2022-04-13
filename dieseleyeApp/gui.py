# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from serial import serialutil
import TOFcalculater


class Ui_MainWindow(object):
    startcheck = False
    valcheck = False
    setupcheck = False
    tof = TOFcalculater.TOFSerial()
    _port = ''
    _baudrate = 9600
    _buff = 50

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TOF-counter")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Startbtn.setGeometry(QtCore.QRect(20, 160, 95, 36))
        self.Startbtn.setObjectName("Start(A)")
        self.Startbtn.setStyleSheet("background:light green")
        self.Startbtn.clicked.connect(self.startevent)
        self.Startbtn.setText("start(A)")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 70, 480, 61))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(15)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 171, 31))
        self.label.setObjectName("label")
        self.label.setText("TOF Measurements are in micro seconds")

        self.stopbtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopbtn.setGeometry(QtCore.QRect(360, 160, 95, 36))
        self.stopbtn.setObjectName("stopbtn")
        self.stopbtn.setStyleSheet("background:red")
        self.stopbtn.clicked.connect(self.stopevent)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 270, 113, 36))
        self.lineEdit.setText("com")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 270, 113, 36))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('9600')

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 270, 113, 36))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('70')

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 340, 113, 36))
        self.lineEdit_4.setObjectName("lineEdit_3")
        self.lineEdit_4.setText('2')

        self.savebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savebtn.setGeometry(QtCore.QRect(30, 340, 95, 36))
        self.savebtn.setObjectName("savebtn")
        self.savebtn.clicked.connect(self.saveParams)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 250, 60, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 250, 81, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 250, 60, 17))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 320, 60, 17))
        self.label_5.setObjectName("label_4")
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(30, 390, 91, 41))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")     
        self.qtimer = QTimer()
        self.qtimer.setInterval(500)
        self.qtimer.timeout.connect(self.updateData)
        self.qtimer.start()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TOF-calculater"))
        self.Startbtn.setText(_translate("MainWindow", "start"))
        self.label.setText(_translate("MainWindow", "TOF in micro seconds"))
        self.stopbtn.setText(_translate("MainWindow", "stop"))
        self.savebtn.setText(_translate("MainWindow", "save"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.label_3.setText(_translate("MainWindow", "Baudrate"))
        self.label_4.setText(_translate("MainWindow", "Buffer"))
        self.label_5.setText(_translate("MainWindow", "Meas mode"))

    def saveParams(self):
        self._port = self.lineEdit.text()
        self._baudrate = int(self.lineEdit_2.text())
        self._buff = int(self.lineEdit_3.text())

        try:
            self.tof.setupSerial(self._port, self._baudrate)
        except serialutil.SerialException:
            self.label.setText("cant open the com port :" + self._port)

    def startevent(self):
        print('starting')
        self.valcheck = True
        self.startcheck = True

    def stopevent(self):
        self.startcheck = False
        self.valcheck = False
        self.tof.stopSerial()
        print('stopped')

    def updateData(self):  # updater
        self.Startbtn.setText("start(A)")
        if self.startcheck == True:
            try:
                data = self.tof.startSerial(self._buff)
                self.lcdNumber.display(data)
                self.label.setText("TOF in micro seconds")
            except AttributeError:
                self.label.setText("choose correct settings and save first")
            except ZeroDivisionError:
                self.label.setText("check if sensor is connected")
        elif self.startcheck == False:
            self.lcdNumber.display("press A")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # type: ignore
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#TOF1 =(TIME1)(normLSB)+(CLOCK _ COUNT1)(CLOCKperiod) -(TIME2)(normLSB)