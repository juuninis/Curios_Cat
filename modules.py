#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
import style

def RandomNumber():
	return random.randint(1000, 9999)

def DoubleAscii(word):
	result = ""
	for i in range(0, len(word)):
		result += hex(ord(word[i])).replace("0x", "%25").upper()

	return result

def TripleAscii(word):
	result = ""
	for i in range(0, len(word)):
		result += hex(ord(word[i])).replace("0x", "%2525").upper()

	return result

def RandomCase(word):
	result = ""
	for i in range(0, len(word)):
		if random.randint(0, 1) == 1:
			result += word[i].upper()
		else:
			result += word[i]

	return result

def Comment(word):
	word = "/*!" + word + "*/"
	return word

def WhiteSpace():
	result = ""
	if random.randint(0, 4) == 0:
		result += "%0A"
	elif random.randint(0, 4) == 1:
		result += "%0B"
	elif random.randint(0, 4) == 2:
		result += "%0C"
	elif random.randint(0, 4) == 3:
		result += "%0D"
	elif random.randint(0, 4) == 4:
		result += "%09"

	return result

def WhiteSpaceDouble():
	result = ""

	if random.randint(0, 4) == 0:
		result += "%0A"
	elif random.randint(0, 4) == 1:
		result += "%0B"
	elif random.randint(0, 4) == 2:
		result += "%0C"
	elif random.randint(0, 4) == 3:
		result += "%0D"
	elif random.randint(0, 4) == 4:
		result += "%09"

	if random.randint(0, 4) == 0:
		result += "%0A"
	elif random.randint(0, 4) == 1:
		result += "%0B"
	elif random.randint(0, 4) == 2:
		result += "%0C"
	elif random.randint(0, 4) == 3:
		result += "%0D"
	elif random.randint(0, 4) == 4:
		result += "%09"

	return result

def ScrathHTML(number):
	result = ""
	for i in range(0, number):
		result += str(i) + str(i) + str(i) + str(i)
		if i != number - 1:
			result += ","

	return result

def Null(number):
	result = ""
	for i in range(0, number):
		result += "null"
		if i != number - 1:
			result += ","

def CommaComment(word):
	word = word.replace(",", "/*!,*/")
	return word

def Error(title, text):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText(text)
	msg.setWindowTitle(title)

	msg.setStandardButtons(QMessageBox.Ok)

	msg.setStyleSheet("""
		QMessageBox{
			background: #22282e;
		}
		QLabel{
			margin-top: 10px;
			margin-bottom: 10px;
			font-size: 16px;
			font-family: NanumGothic;
			color: #747a81;
		}
		QPushButton{
			min-width: 90px;
			min-height: 35px;
			color: #fff;
			font-size: 18px;
			font-weight: bold;
			font-family: Sansita;
			background: #ce70ff;
		}
	""")

	msg.show()
	msg.exec_()
