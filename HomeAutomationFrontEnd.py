# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bens-Acer\Desktop\myui3.ui'
#
# Created: Thu Oct 25 13:53:48 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import random
import time
import sensors
class Ui_homeApp(object):
    def setupUi(self, homeApp):
        homeApp.setObjectName("homeApp")
        homeApp.resize(1117, 935)
        self.centralwidget = QtGui.QWidget(homeApp)
        self.centralwidget.setStyleSheet("background-color: rgb(35, 41, 44);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 51, 63);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.temp_sensor = QtGui.QLabel(self.centralwidget)
        self.temp_sensor.setGeometry(QtCore.QRect(-30, 170, 1151, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.temp_sensor.setFont(font)
        self.temp_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.temp_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_sensor.setObjectName("temp_sensor")
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(-10, 130, 1151, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label5 = QtGui.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(570, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label5.setFont(font)
        self.label5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(-20, 250, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.humidity = QtGui.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(-30, 320, 1151, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.humidity.setFont(font)
        self.humidity.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setObjectName("humidity")
        self.label7 = QtGui.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(580, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label7.setFont(font)
        self.label7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(-20, 380, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.light_sensor = QtGui.QLabel(self.centralwidget)
        self.light_sensor.setGeometry(QtCore.QRect(-20, 460, 1161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.light_sensor.setFont(font)
        self.light_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.light_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.light_sensor.setObjectName("light_sensor")
        self.label4 = QtGui.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(-20, 510, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.airQuality = QtGui.QLabel(self.centralwidget)
        self.airQuality.setGeometry(QtCore.QRect(-20, 580, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.airQuality.setFont(font)
        self.airQuality.setStyleSheet("color: rgb(255, 255, 255);")
        self.airQuality.setAlignment(QtCore.Qt.AlignCenter)
        self.airQuality.setObjectName("airQuality")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 650, 1151, 311))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.onLight = QtGui.QPushButton(self.centralwidget)
        self.onLight.setGeometry(QtCore.QRect(580, 710, 141, 71))
        self.onLight.clicked.connect(self.turnOnLight)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.onLight.setFont(font)
        self.onLight.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(40, 175, 65);")
        self.onLight.setObjectName("onLight")
        self.offLight = QtGui.QPushButton(self.centralwidget)
        self.offLight.setGeometry(QtCore.QRect(410, 710, 141, 71))
        self.offLight.clicked.connect(self.turnOffLight)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.offLight.setFont(font)
        self.offLight.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 80, 57);")
        self.offLight.setObjectName("offLight")
        homeApp.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(homeApp)
        self.statusbar.setObjectName("statusbar")
        homeApp.setStatusBar(self.statusbar)

        self.retranslateUi(homeApp)
        QtCore.QMetaObject.connectSlotsByName(homeApp)

    def retranslateUi(self, homeApp):
        homeApp.setWindowTitle(QtGui.QApplication.translate("homeApp", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("homeApp", "Welcome to the Home Automation Project", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_sensor.setText(QtGui.QApplication.translate("homeApp", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("homeApp", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("homeApp", "°F", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("homeApp", "Humidity", None, QtGui.QApplication.UnicodeUTF8))
        self.humidity.setText(QtGui.QApplication.translate("homeApp", "0.0%", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("homeApp", "RH", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("homeApp", "Lighting", None, QtGui.QApplication.UnicodeUTF8))
        self.light_sensor.setText(QtGui.QApplication.translate("homeApp", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("homeApp", "Air Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.airQuality.setText(QtGui.QApplication.translate("homeApp", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.onLight.setText(QtGui.QApplication.translate("homeApp", "Turn on light", None, QtGui.QApplication.UnicodeUTF8))
        self.offLight.setText(QtGui.QApplication.translate("homeApp", "Turn off light", None, QtGui.QApplication.UnicodeUTF8))
    def turnOnLight(self):
        self.light_sensor.setText("ON")
        sensors.RedLight(1)
        print("Turned on red light")
    def turnOffLight(self):
        self.light_sensor.setText("OFF")
        sensors.RedLight(0)
        print("Turned off red light")
    def refreshText(self):

        time = QtCore.QTime.currentTime().toString()
        print("Time: " + time)

        temp_sensor = "%.2f " % sensors.readTemperature()
        humidity_sensor = "%.2f " % sensors.readHumidity()

        self.temp_sensor.setText(str(temp_sensor))
        self.humidity.setText(str(humidity_sensor)+"%")


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_homeApp()
    ui.setupUi(MainWindow)
    MainWindow.show()

    RedLight(0)

    timer=QtCore.QTimer()
    timer.timeout.connect(ui.refreshText)
    timer.start(1000)

    sys.exit(app.exec_())

def generateRandowNumber():
    return random.randint(1,101)

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_homeApp()
    ui.setupUi(MainWindow)
    MainWindow.show()

    timer=QtCore.QTimer()
    timer.timeout.connect(ui.refreshText)
    timer.start(1000)

    sys.exit(app.exec_())

def generateRandowNumber():
    return random.randint(1,101)

if __name__ == '__main__':
    # App.main()
    main()
