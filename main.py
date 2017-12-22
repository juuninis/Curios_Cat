#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		main = QVBoxLayout()
		main.setContentsMargins(50, 50, 50, 50)

		import layout

		for i in range(0, 9):
			main.addWidget(layout.wrap[i])
		main.addWidget(layout.confirm_step1_wrap)
		main.addWidget(layout.confirm_step3_wrap)
		main.addWidget(layout.confirm_step4_wrap)
		main.addWidget(layout.confirm_step5_wrap)
		main.addWidget(layout.confirm_step6_wrap)
		main.addWidget(layout.confirm_step7_wrap)
		main.addWidget(layout.confirm_step8_wrap)

		window = QWidget()
		window.setStyleSheet("background: #000;")
		window.setLayout(main)
		self.setCentralWidget(window)

		#크기 설정
		self.setGeometry(300,100,800,0)
		self.setFixedSize(800, 0)
		#제목 설정
		self.setWindowTitle("SQLi-diot");
		self.show()

		#아이콘
		self.setWindowIcon(QIcon('icon.png'))

		#메뉴바
		menubar = self.menuBar()
		menubar.setStyleSheet("""
			QMenuBar{
				background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);
				font-family: Sansita, sans-serif;
				font-weight: light;
				font-size: 16px;
				color: #fff;
			}
			QMenuBar::item{
				font-family: Sansita, sans-serif;
			}
		""")
		menu = menubar.addMenu('Menu')

		save = menu.addAction("Save")
		exit = menu.addAction("Exit")

		save.setShortcut("Ctrl+S")
		save.setStatusTip("Save Process")
		save.triggered.connect(self.Save_File)
		import layout
		import active
		layout.confirm_step8_next.clicked.connect(active.Step8_Confirm_Save)
		layout.confirm_step8_next.clicked.connect(self.Save_File)

		exit.setShortcut("Ctrl+Q")
		exit.setStatusTip("Exit Application")
		exit.triggered.connect(quit)

		self.setMenuBar(menubar)

		#폰트
		QFontDatabase.addApplicationFont("Sansita-Regular.ttf")
		QFontDatabase.addApplicationFont("NanumGothic.ttf")

	def Save_File(self):
		fileName = QFileDialog.getSaveFileName(self, "Save File", "./", "Text files (*.txt)")
		fileName = str(fileName)[2 : str(fileName).find(",") -1] + ".txt"
		saveFile = open(fileName, 'w')
		import active
		saveFile.write(active.save)
		saveFile.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	do = Main()
	sys.exit(app.exec_())
