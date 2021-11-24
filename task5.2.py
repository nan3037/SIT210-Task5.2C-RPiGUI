from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def _init_(self):
		super(MyWindow, self)._init_()
		self.initUI()
		
	def initUI(self):
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("Task 5.2C")
		self.heading1 = QtWidgets.QLabel(win)
		self.heading1.setText("Choose Color")
		self.heading1.move(50, 50)
		
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("clivk me")
		self.b1.clicked.connect(clicked)
		
	def clicked(self):
		self.label.setText("you pressed")
		
		
def clicked():
	print("clicked")
	
	
def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	
	
	heading = QtWidgets.QLabel(win)
	heading.setText("Choosen Color")
	heading.move(50, 50)
	
	win.show()
	sys.exit(app.exec_())
	
window()
