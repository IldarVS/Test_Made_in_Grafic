# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(500, 80, 351, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 491, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 20, 471, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonLoad.setObjectName("ButtonLoad")
        self.horizontalLayout.addWidget(self.ButtonLoad)
        self.ButtonUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonUpdate.setObjectName("ButtonUpdate")
        self.horizontalLayout.addWidget(self.ButtonUpdate)
        self.ButtonSave = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonSave.setObjectName("ButtonSave")
        self.horizontalLayout.addWidget(self.ButtonSave)
        self.ButtonGraph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonGraph.setObjectName("ButtonGraph")
        self.horizontalLayout.addWidget(self.ButtonGraph)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 65, 16))
        self.label.setObjectName("label")
        self.tableWidget.raise_()
        self.widget.raise_()
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.horizontalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Мой график"))
        self.ButtonLoad.setText(_translate("MainWindow", "Загрузить данные"))
        self.ButtonUpdate.setText(_translate("MainWindow", "Изменить данные"))
        self.ButtonSave.setText(_translate("MainWindow", "Сохранить данные в файл"))
        self.ButtonGraph.setText(_translate("MainWindow", "Нарисовать график"))
        self.label.setText(_translate("MainWindow", "Моя таблица"))

