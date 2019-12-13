# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.showAll_b = QtWidgets.QPushButton(self.centralwidget)
        self.showAll_b.setGeometry(QtCore.QRect(380, 230, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showAll_b.setFont(font)
        self.showAll_b.setObjectName("showAll_b")
        self.add_b = QtWidgets.QPushButton(self.centralwidget)
        self.add_b.setGeometry(QtCore.QRect(379, 10, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_b.setFont(font)
        self.add_b.setObjectName("add_b")
        self.edit_b = QtWidgets.QPushButton(self.centralwidget)
        self.edit_b.setGeometry(QtCore.QRect(380, 80, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.edit_b.setFont(font)
        self.edit_b.setObjectName("edit_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Players Stat"))
        self.showAll_b.setText(_translate("MainWindow", "Показать все виды"))
        self.add_b.setText(_translate("MainWindow", "Добавить вид кофе"))
        self.edit_b.setText(_translate("MainWindow", "Выбрать для редактирования"))
