# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coffe/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.mol_zern = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mol_zern.setFont(font)
        self.mol_zern.setObjectName("mol_zern")
        self.gridLayout.addWidget(self.mol_zern, 3, 1, 1, 1)
        self.step = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.step.setFont(font)
        self.step.setObjectName("step")
        self.gridLayout.addWidget(self.step, 2, 1, 1, 1)
        self.val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.val.setFont(font)
        self.val.setObjectName("val")
        self.gridLayout.addWidget(self.val, 5, 1, 1, 1)
        self.descr = QtWidgets.QTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descr.setFont(font)
        self.descr.setObjectName("descr")
        self.gridLayout.addWidget(self.descr, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.cost = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cost.setFont(font)
        self.cost.setObjectName("cost")
        self.gridLayout.addWidget(self.cost, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.id_l = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.id_l.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_l.setFont(font)
        self.id_l.setObjectName("id_l")
        self.gridLayout.addWidget(self.id_l, 0, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 10, 251, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.update_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.update_.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.update_.setFont(font)
        self.update_.setObjectName("update_")
        self.verticalLayout.addWidget(self.update_)
        self.errors = QtWidgets.QTextEdit(self.centralwidget)
        self.errors.setEnabled(False)
        self.errors.setGeometry(QtCore.QRect(530, 360, 251, 191))
        self.errors.setObjectName("errors")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 319, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add/Edit CoffeeDB"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.label_5.setText(_translate("MainWindow", "Объём:"))
        self.label_3.setText(_translate("MainWindow", "Молотый/Зерновой:"))
        self.label_6.setText(_translate("MainWindow", "Описание:"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_4.setText(_translate("MainWindow", "Цена:"))
        self.label_7.setText(_translate("MainWindow", "id:"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.update_.setText(_translate("MainWindow", "Обновить"))
        self.label_8.setText(_translate("MainWindow", "Сообщения об ошибках:"))
