# Form implementation generated from reading ui file 'wallet_ui.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 127, 255), stop:1 rgba(85, 85, 255, 255));\n"
"border-radius: 15px\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(19, 20, 761, 561))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(17, 17, 17, 255), stop:1 rgba(31, 31, 31, 255));")
        self.widget.setObjectName("widget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 761, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(58, 166, 255);\n"
"background: rgba(11, 11, 11, .1);\n"
"padding: 10px;\n"
"border-radius: 0px;\n"
"font: 18pt \"Roboto\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("res/icon_big.png"))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setStyleSheet("color: rgb(58, 166, 255);\n"
"padding: 10px;\n"
"background: rgba(11, 11, 11, .1);\n"
"border-radius: 0px;\n"
"font: 24pt \"Roboto\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(300, 200, 200, 200))
        self.label_2.setStyleSheet("color: white;\n"
"border-radius: 100px;\n"
"font: 500 26pt \"Source Code Pro\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 127, 255), stop:1 rgba(85, 85, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kripton Wallet"))
        self.label_2.setText(_translate("MainWindow", "0.0\n"
"KRC"))
