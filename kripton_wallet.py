#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Криптокошелек KriptonWallet"""
import sys
import loginform_ui
import wallet_ui
import qdarkstyle
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class ErrorDialog(QDialog):
	def __init__(self, title='Ошибка', description='Ошибка'):
		super().__init__()

		self.setWindowTitle(title)

		self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6'))

		QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel(description)
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)


class WalletLogin(QDialog, loginform_ui.Ui_Dialog):
	def __init__(self):
		###### Инициализация и установка UI ######
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(500, 700)

		self.setWindowIcon(QtGui.QIcon('res/wallet_violet_icon.png'))

		self.pushButton.clicked.connect(self.is_good)

	def is_good(self):
		if self.login_line.text() == 'admin' and self.password_line.text() == 'admin':
			print('Logged as admin')
			self.accept()
		else:
			dlg = ErrorDialog('Ошибка', 'Неверный логин или пароль')
			dlg.exec()
			print('Not logged')


class KriptonWallet(QtWidgets.QMainWindow, wallet_ui.Ui_MainWindow):
	def __init__(self):
		###### Инициализация и установка UI ######
		super().__init__()
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('res/wallet_violet_icon.png'))


def main():
	app = QtWidgets.QApplication(sys.argv)
	login = WalletLogin()

	if login.exec() == login.accepted:
		window = KriptonWallet()
		window.show()
		sys.exit(app.exec())
	else:
		window = KriptonWallet()
		window.show()
		sys.exit(app.exec())


if __name__ == '__main__':
	main()
