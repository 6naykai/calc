# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myCalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 519)
        MainWindow.setStyleSheet("background: white;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 381, 71))
        self.lineEdit.setStyleSheet("font-size:56px;\n"
"font-weight:bold;\n"
"color:rgb(255, 255, 255);\n"
"letter-spacing:10px;\n"
"outline-color:rgb(255, 255, 255);\n"
"border-radius:23px;\n"
"font: 20pt \"微软雅黑\";\n"
"background-color:rgba(0, 170, 127, 100)\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 381, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_0.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 9, 0, 1, 1)
        self.pushButton_power = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_power.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_power.setObjectName("pushButton_power")
        self.gridLayout.addWidget(self.pushButton_power, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 6, 0, 1, 1)
        self.pushButton_right = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_right.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayout.addWidget(self.pushButton_right, 0, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 7, 0, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_plus.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sqrt.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_equal.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 9, 2, 1, 1)
        self.pushButton_left = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_left.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayout.addWidget(self.pushButton_left, 0, 0, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sub.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 6, 3, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_div.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 9, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 1)
        self.pushButton_point = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_point.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 9, 1, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_mul.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 7, 3, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 90, 381, 61))
        self.layoutWidget1.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_DEL = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_DEL.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.horizontalLayout.addWidget(self.pushButton_DEL)
        self.pushButton_AC = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_AC.setStyleSheet("background-color:rgb(0, 170, 127);\n"
"font-size:46px;\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"border-radius: 20px;\n"
"font: 23pt \"微软雅黑\";")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.horizontalLayout.addWidget(self.pushButton_AC)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的计算器"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_power.setText(_translate("MainWindow", "^"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_right.setText(_translate("MainWindow", ")"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_sqrt.setText(_translate("MainWindow", "sqrt"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_left.setText(_translate("MainWindow", "("))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_mul.setText(_translate("MainWindow", "×"))
        self.pushButton_DEL.setText(_translate("MainWindow", "DEL"))
        self.pushButton_AC.setText(_translate("MainWindow", "AC"))
