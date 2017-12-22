#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *
import style
import active

wrap = []
layout = []
titleWrap = []
titleLayout = []
title = []
urlWrap = []
urlLayout = []
url = []
buttonWrap = []
buttonLayout = []
Prev = []
Next = []

def Wrap(i): #페이지
	wrap.append(QWidget())
	layout.append(QVBoxLayout())
	wrap[i].setLayout(layout[i])
	style.Wrap(wrap[i], layout[i]) #스타일 설정

def Title(titleName, submit, i): #페이지 제목
	titleWrap.append(QWidget())
	titleLayout.append(QHBoxLayout())
	titleWrap[i].setLayout(titleLayout[i])
	layout[i].addWidget(titleWrap[i]) #레이아웃에 추가

	title.append([])
	title[i].append(QLabel(titleName))
	title[i].append(QLabel(submit))

	titleLayout[i].addWidget(title[i][0])
	titleLayout[i].addWidget(title[i][1])
	titleLayout[i].addStretch(0) #이걸 추가해야 맨 앞으로 밀림.
	style.Title(titleWrap[i], titleLayout[i], title[i]) #스타일 설정

def Url(i): #페이지에 자동으로 입력되는 URL
	urlWrap.append(QWidget())
	urlLayout.append(QHBoxLayout())
	urlWrap[i].setLayout(urlLayout[i])
	layout[i].addWidget(urlWrap[i]) #레이아웃에 추가

	url.append(QLineEdit())
	urlLayout[i].addWidget(url[i])
	style.Url(urlLayout[i], url[i]) #스타일 설정

def Button(i): #이전, 다음 버튼
	buttonWrap.append(QWidget())
	buttonLayout.append(QHBoxLayout())
	buttonWrap[i].setLayout(buttonLayout[i])
	layout[i].addWidget(buttonWrap[i]) #레이아웃에 추가

	Prev.append(QPushButton("Prev"))
	Next.append(QPushButton("Next"))
	buttonLayout[i].addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	buttonLayout[i].addWidget(Prev[i])
	buttonLayout[i].addWidget(Next[i])
	buttonLayout[i].addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	style.Button(Prev[i], Next[i], buttonLayout[i]) #스타일 설정


selectZone = []
selectLayout = []
settingZone = []
settingLayout = []
settingZone.append([])
settingLayout.append([])
selectZone.append(QWidget())
selectLayout.append(QGridLayout())
setting = []
setting.append([])
slicedUrl = []
slicedUrl.append(QLabel())
setAscii = []
setAscii.append(QComboBox())


def SelectZone(i):
	selectZone.append(QWidget())
	selectLayout.append(QGridLayout())
	selectZone[i].setLayout(selectLayout[i])
	layout[i].addWidget(selectZone[i]) #레이아웃에 추가
	style.SelectZone(selectZone[i], selectLayout[i]) #스타일 설정

def SettingZone(i, j):
	settingZone.append([])
	settingLayout.append([])
	settingZone[i].append(QWidget())
	settingLayout[i].append(QVBoxLayout())
	settingZone[i][j].setLayout(settingLayout[i][j])
	selectLayout[i].addWidget(settingZone[i][j], 0, j)
	style.SettingZone(settingZone[i][j]) #레이아웃에 추가

def SetAscii(i):
	setAscii.append(QComboBox())
	setAscii[i].addItem("(옵션)Ascii None")
	setAscii[i].addItem("(옵션)Double Ascii")
	setAscii[i].addItem("(옵션)Triple Ascii")
	setAscii[i].addItem("(옵션)All Double Ascii")
	setAscii[i].addItem("(옵션)All Triple Ascii")
	style.Select(setAscii[i])

def SlicedUrl(i):
	slicedUrl.append(QLabel(""))
	style.Text(slicedUrl[i])

alphabetCase = []
alphabetCase.append([])
alphabetCase.append([])
whiteSpace = []
whiteSpace.append([])
whiteSpace.append([])
comment = []
comment.append([])
comment.append([])

def AlphabetCase(i):
	alphabetCase.append(QComboBox())
	alphabetCase[i].addItem("(옵션)Lower Case")
	alphabetCase[i].addItem("(옵션)Upper Case")
	alphabetCase[i].addItem("(옵션)Random Case")
	alphabetCase[i].addItem("(옵션)Double Case")
	style.Select(alphabetCase[i]) #스타일 설정

def WhiteSpace(i):
	whiteSpace.append(QComboBox())
	whiteSpace[i].addItem("(옵션)Space = ' '")
	whiteSpace[i].addItem("(옵션)Space = Ascii")
	whiteSpace[i].addItem("(옵션)Space = Double Ascii")
	style.Select(whiteSpace[i]) #스타일 설정

def Comment(i):
	comment.append(QComboBox())
	comment[i].addItem("(옵션)주석 없음")
	comment[i].addItem("(옵션)주석 추가")
	style.Select(comment[i]) #스타일 설정

def Confirm(wrap, layout, titleWidget, titleLayout, title, titleText):
	wrap.setLayout(layout)
	style.Wrap(wrap, layout) #스타일 설정

	titleWidget.setLayout(titleLayout)
	layout.addWidget(titleWidget) #레이아웃에 추가

	title.setText(titleText)

	titleLayout.addWidget(title)
	titleLayout.addStretch(0) #이걸 추가해야 맨 앞으로 밀림.

	#타이틀 스타일 설정
	titleWidget.setStyleSheet("QWidget{padding: 0 30px; background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);}")
	titleWidget.setFixedHeight(90)
	titleLayout.setContentsMargins(0, 0, 0, 0)
	titleLayout.setSpacing(0)
	title.setStyleSheet("QLabel{margin-top: 14px; font-size: 16px; font-weight: 600; font-family: NanumGothic; color: #8492a1; background: none;}")

def Confirm_Button(layout, buttonWidget, buttonLayout, Prev, Next):
	buttonWidget.setLayout(buttonLayout)
	layout.addWidget(buttonWidget) #레이아웃에 추가

	buttonLayout.addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	buttonLayout.addWidget(Prev)
	buttonLayout.addWidget(Next)
	buttonLayout.addStretch(0) #버튼이 화면 끝까지 안커지고 일정 크기를 유지하도록 추가
	style.Button(Prev, Next, buttonLayout) #스타일 설정

def Confirm_Input(layout, inputWidget, inputLayout, _input, placeholder):
	inputWidget.setLayout(inputLayout)
	_input.setPlaceholderText(placeholder)
	style.Input(_input) #스타일 설정
	inputLayout.addWidget(_input)
	layout.addWidget(inputWidget) #레이아웃에 추가
	inputLayout.setContentsMargins(30, 30, 30, 30)

def Confirm_TextArea(layout, textareaWidget, textareaLayout, textarea, placeholder):
	textareaWidget.setLayout(textareaLayout)
	textarea.setStyleSheet("QTextEdit{color: #747a81;}")
	textarea.setPlaceholderText(placeholder)
	style.TextArea(textarea) #스타일 설정
	textareaLayout.addWidget(textarea)
	layout.addWidget(textareaWidget) #레이아웃에 추가
	textareaLayout.setContentsMargins(30, 30, 30, 0)


#------------------------------------------------------------------------

Wrap(0)
#wrap[0].hide()
Title("Step 0.", "취약한 페이지를 찾아 입력해주세요.", 0)
Url(0)
url[0].setPlaceholderText("취약한 페이지를 찾아 입력해주세요.")
Button(0)
Prev[0].hide()

Next[0].clicked.connect(active.Step0_Next) #다음으로 넘어가기

#-------------------------------------------------------------------

Wrap(1)
wrap[1].hide()
Title("Step 1.", "취약점 파악하기", 1)

SelectZone(1)
SettingZone(1, 0)
SettingZone(1, 1)

step1_number = QComboBox()
step1_number.addItem("")
step1_number.addItem("")
step1_number.addItem("")
style.Select(step1_number)

settingLayout[1][0].addStretch(0)
settingLayout[1][0].addWidget(step1_number)

SetAscii(1)
setAscii[1].removeItem(len(setAscii[1]) - 2)
setAscii[1].removeItem(len(setAscii[1]) - 1)

setColon = QComboBox()
setColon.addItem("'")
setColon.addItem('"')
setColon.addItem(")")
style.Select(setColon)

settingLayout[1][1].addWidget(setAscii[1])
settingLayout[1][1].addWidget(setColon)

step1_number.currentIndexChanged.connect(active.Step1_SetNumber)
setColon.currentIndexChanged.connect(active.Step1_SetColon)
setAscii[1].currentIndexChanged.connect(active.Step1_SettingColon)

Url(1)
Button(1)

Prev[1].clicked.connect(active.Step1_Prev)
Next[1].clicked.connect(active.Step1_Next)

#-------------------------------------------------

confirm_step1_wrap = QWidget()
confirm_step1_layout = QVBoxLayout()
confirm_step1_titleWidget = QWidget()
confirm_step1_titleLayout = QHBoxLayout()
confirm_step1_title = QLabel("")
confirm_step1_buttonWidget = QWidget()
confirm_step1_buttonLayout = QHBoxLayout()
confirm_step1_prev = QPushButton("Prev")
confirm_step1_next = QPushButton("Next")

Confirm(confirm_step1_wrap, confirm_step1_layout, confirm_step1_titleWidget, confirm_step1_titleLayout, confirm_step1_title, "DB타입이 무엇입니까?")
confirm_step1_wrap.hide()

confirm_step1_radioButton = []
confirm_step1_radioButton.append(QRadioButton("MySQL"))
confirm_step1_radioButton.append(QRadioButton("ODBC"))
confirm_step1_radioButton.append(QRadioButton("Oracle"))
confirm_step1_radioButton.append(QRadioButton("postgreSQL"))
confirm_step1_radioButton.append(QRadioButton("MS-SQL ASPX"))
confirm_step1_radioButton.append(QRadioButton("MS-SQL Server"))
confirm_step1_radioButton.append(QRadioButton("MS-Access (Apache PHP)"))
confirm_step1_radioButton.append(QRadioButton("MS-Access (IIS ASP)"))
confirm_step1_radioButtonWidget = QGroupBox()
confirm_step1_radioButtonLayout = QVBoxLayout()
confirm_step1_radioButtonWidget.setLayout(confirm_step1_radioButtonLayout)
confirm_step1_prev = QPushButton("Prev")
confirm_step1_next = QPushButton("Next")

for i in range(0, 8):
	confirm_step1_radioButtonLayout.addWidget(confirm_step1_radioButton[i])

confirm_step1_layout.addWidget(confirm_step1_radioButtonWidget)
Confirm_Button(confirm_step1_layout, confirm_step1_buttonWidget, confirm_step1_buttonLayout, confirm_step1_prev, confirm_step1_next)

confirm_step1_prev.clicked.connect(active.Step1_Confirm_Prev)
confirm_step1_next.clicked.connect(active.Step1_Confirm_Next)

#-------------------------------------------------

Wrap(2)
wrap[2].hide()
Title("Step 2.", "컬럼 갯수 알아내기", 2)

SelectZone(2)
SettingZone(2, 0)
SettingZone(2, 1)
SettingZone(2, 2)

order_by = QComboBox()
order_by.addItem(" order by ")
order_by.addItem(" group by ")
style.Select(order_by)

AlphabetCase(2)
SetAscii(2)
WhiteSpace(2)
Comment(2)
settingLayout[2][0].addWidget(alphabetCase[2])
settingLayout[2][0].addWidget(setAscii[2])
settingLayout[2][0].addWidget(whiteSpace[2])
settingLayout[2][0].addWidget(comment[2])
settingLayout[2][0].addWidget(order_by)

order_by.currentIndexChanged.connect(active.Step2_SetOrderBy)
alphabetCase[2].currentIndexChanged.connect(active.Step2_SettingOrderBy)
setAscii[2].currentIndexChanged.connect(active.Step2_SettingOrderBy)
whiteSpace[2].currentIndexChanged.connect(active.Step2_SettingOrderBy)
comment[2].currentIndexChanged.connect(active.Step2_SettingOrderBy)

column_amount = QLineEdit()
column_amount.setPlaceholderText("숫자를 입력해주세요.")
style.Input(column_amount)

lastComment = QComboBox()
lastComment.addItem("--")
lastComment.addItem("--+")
lastComment.addItem("--+-")
lastComment.addItem("-- -")
style.Select(lastComment)
settingLayout[2][1].addStretch(0)
settingLayout[2][1].addWidget(column_amount)

settingLayout[2][2].addStretch(0)
settingLayout[2][2].addWidget(lastComment)

keyPressed = pyqtSignal()
lastComment.currentIndexChanged.connect(active.Step2_SetOrderBy)
column_amount.textChanged.connect(active.Step2_SetOrderBy)

Url(2)
Button(2)

Prev[2].clicked.connect(active.Step2_Prev)
Next[2].clicked.connect(active.Step2_Next)

#----------------------------------------------------------

Wrap(3)
wrap[3].hide()
Title("Step 3.", "취약한 컬럼 파악하기", 3)

SelectZone(3)
SettingZone(3, 0)
SettingZone(3, 1)
SettingZone(3, 2)

error_factor = QComboBox()
error_factor.addItem("(옵션)에러유발인자 없음")
error_factor.addItem("(옵션)'-' 추가")
style.Select(error_factor)
settingLayout[3][0].addStretch(0)
settingLayout[3][0].addWidget(error_factor)

SetAscii(3)
AlphabetCase(3)
WhiteSpace(3)
Comment(3)

union_select = QComboBox()
union_select.addItem(" union select ")
union_select.addItem(" union all select ")
style.Select(union_select)

settingLayout[3][1].addWidget(alphabetCase[3])
settingLayout[3][1].addWidget(setAscii[3])
settingLayout[3][1].addWidget(whiteSpace[3])
settingLayout[3][1].addWidget(comment[3])
settingLayout[3][1].addWidget(union_select)

number = QComboBox()
number.addItem("")
number.addItem("")
number.addItem("")
style.Select(number)

settingLayout[3][2].addStretch(0)
settingLayout[3][2].addWidget(number)

error_factor.currentIndexChanged.connect(active.Step3_SetUrl)
union_select.currentIndexChanged.connect(active.Step3_SetUrl)
number.currentIndexChanged.connect(active.Step3_SetUrl)

alphabetCase[3].currentIndexChanged.connect(active.Step3_SetUnion)
setAscii[3].currentIndexChanged.connect(active.Step3_SetUnion)
whiteSpace[3].currentIndexChanged.connect(active.Step3_SetUnion)
comment[3].currentIndexChanged.connect(active.Step3_SetUnion)

Url(3)
Button(3)

Prev[3].clicked.connect(active.Step3_Prev)
Next[3].clicked.connect(active.Step3_Next)

#------------------------------------------------------

confirm_step3_wrap = QWidget()
confirm_step3_layout = QVBoxLayout()
confirm_step3_titleWidget = QWidget()
confirm_step3_titleLayout = QHBoxLayout()
confirm_step3_title = QLabel("")
confirm_step3_buttonWidget = QWidget()
confirm_step3_buttonLayout = QHBoxLayout()
confirm_step3_prev = QPushButton("Prev")
confirm_step3_next = QPushButton("Next")
confirm_step3_inputWidget = QWidget()
confirm_step3_inputLayout = QHBoxLayout()
confirm_step3_input = QLineEdit()

Confirm(confirm_step3_wrap, confirm_step3_layout, confirm_step3_titleWidget, confirm_step3_titleLayout, confirm_step3_title, "몇 번 컬럼이 취약합니까?")
confirm_step3_wrap.hide()

Confirm_Input(confirm_step3_layout, confirm_step3_inputWidget, confirm_step3_inputLayout, confirm_step3_input, "숫자를 입력해주세요.")
Confirm_Button(confirm_step3_layout, confirm_step3_buttonWidget, confirm_step3_buttonLayout, confirm_step3_prev, confirm_step3_next)

confirm_step3_prev.clicked.connect(active.Step3_Confirm_Prev)
confirm_step3_next.clicked.connect(active.Step3_Confirm_Next)
confirm_step3_input.textChanged.connect(active.Step3_Confirm_Input)

#------------------------------------------------------

Wrap(4)
wrap[4].hide()
Title("Step 4", "서버 운영체제 파악하기", 4)

SelectZone(4)
SettingZone(4, 0)

version = QComboBox()
version.addItem("version()")
version.addItem("@@version")
style.Select(version)

SetAscii(4)
AlphabetCase(4)
Comment(4)

alphabetCase[4].removeItem(3)

settingLayout[4][0].addWidget(alphabetCase[4])
settingLayout[4][0].addWidget(setAscii[4])
settingLayout[4][0].addWidget(comment[4])
settingLayout[4][0].addWidget(version)

alphabetCase[4].currentIndexChanged.connect(active.Step4_SetUrl)
setAscii[4].currentIndexChanged.connect(active.Step4_SetUrl)
comment[4].currentIndexChanged.connect(active.Step4_SetUrl)
version.currentIndexChanged.connect(active.Step4_SetUrl)

Url(4)
Button(4)

Prev[4].clicked.connect(active.Step4_Prev)
Next[4].clicked.connect(active.Step4_Next)

#----------------------------------------------------------

confirm_step4_wrap = QWidget()
confirm_step4_layout = QVBoxLayout()
confirm_step4_titleWidget = QWidget()
confirm_step4_titleLayout = QHBoxLayout()
confirm_step4_title = QLabel("")
confirm_step4_buttonWidget = QWidget()
confirm_step4_buttonLayout = QHBoxLayout()
confirm_step4_prev = QPushButton("Prev")
confirm_step4_next = QPushButton("Next")
confirm_step4_inputWidget = QWidget()
confirm_step4_inputLayout = QHBoxLayout()
confirm_step4_input = QLineEdit()

Confirm(confirm_step4_wrap, confirm_step4_layout, confirm_step4_titleWidget, confirm_step4_titleLayout, confirm_step4_title, "서버 운영체제가 무엇입니까?")
confirm_step4_wrap.hide()

Confirm_Input(confirm_step4_layout, confirm_step4_inputWidget, confirm_step4_inputLayout, confirm_step4_input, "서버 운영체제를 입력해주세요.")
Confirm_Button(confirm_step4_layout, confirm_step4_buttonWidget, confirm_step4_buttonLayout, confirm_step4_prev, confirm_step4_next)

confirm_step4_prev.clicked.connect(active.Step4_Confirm_Prev)
confirm_step4_next.clicked.connect(active.Step4_Confirm_Next)

#----------------------------------------------------------

Wrap(5)
wrap[5].hide()
Title("Step 5", "DB 이름 파악하기", 5)

SelectZone(5)
SetAscii(5)
AlphabetCase(5)
Comment(5)

Url(5)
Button(5)

Prev[5].clicked.connect(active.Step5_Prev)
Next[5].clicked.connect(active.Step5_Next)

#--------------------------------------------------------------

confirm_step5_wrap = QWidget()
confirm_step5_layout = QVBoxLayout()
confirm_step5_titleWidget = QWidget()
confirm_step5_titleLayout = QHBoxLayout()
confirm_step5_title = QLabel("")
confirm_step5_buttonWidget = QWidget()
confirm_step5_buttonLayout = QHBoxLayout()
confirm_step5_prev = QPushButton("Prev")
confirm_step5_next = QPushButton("Next")
confirm_step5_inputWidget = QWidget()
confirm_step5_inputLayout = QHBoxLayout()
confirm_step5_input = QLineEdit()

Confirm(confirm_step5_wrap, confirm_step5_layout, confirm_step5_titleWidget, confirm_step5_titleLayout, confirm_step5_title, "DB의 이름이 무엇입니까?")
confirm_step5_wrap.hide()

Confirm_Input(confirm_step5_layout, confirm_step5_inputWidget, confirm_step5_inputLayout, confirm_step5_input, "DB이름을 입력해주세요.")
Confirm_Button(confirm_step5_layout, confirm_step5_buttonWidget, confirm_step5_buttonLayout, confirm_step5_prev, confirm_step5_next)

confirm_step5_prev.clicked.connect(active.Step5_Confirm_Prev)
confirm_step5_next.clicked.connect(active.Step5_Confirm_Next)

#---------------------------------------------------------------

Wrap(6)
wrap[6].hide()
Title("Step 6", "Table 이름 알아내기", 6)

SelectZone(6)
SettingZone(6, 0)
SettingZone(6, 1)

WhiteSpace(4)
WhiteSpace(5)
WhiteSpace(6)

SetAscii(6)
AlphabetCase(6)
Comment(6)
alphabetCase[6].removeItem(3)

SetAscii(7)
AlphabetCase(7)
Comment(7)
WhiteSpace(7)
settingLayout[6][0].addWidget(alphabetCase[6])
settingLayout[6][0].addWidget(setAscii[6])
settingLayout[6][0].addWidget(comment[6])

settingLayout[6][1].addWidget(alphabetCase[7])
settingLayout[6][1].addWidget(setAscii[7])
settingLayout[6][1].addWidget(comment[7])
settingLayout[6][1].addWidget(whiteSpace[7])


alphabetCase[6].currentIndexChanged.connect(active.Step6_SetUrl)
setAscii[6].currentIndexChanged.connect(active.Step6_SetUrl)
comment[6].currentIndexChanged.connect(active.Step6_SetUrl)
alphabetCase[7].currentIndexChanged.connect(active.Step6_SetUrl)
setAscii[7].currentIndexChanged.connect(active.Step6_SetUrl)
comment[7].currentIndexChanged.connect(active.Step6_SetUrl)
whiteSpace[7].currentIndexChanged.connect(active.Step6_SetUrl)


Url(6)
Button(6)

Prev[6].clicked.connect(active.Step6_Prev)
Next[6].clicked.connect(active.Step6_Next)

#--------------------------------------------------------------------

confirm_step6_wrap = QWidget()
confirm_step6_layout = QVBoxLayout()
confirm_step6_titleWidget = QWidget()
confirm_step6_titleLayout = QHBoxLayout()
confirm_step6_title = QLabel("")
confirm_step6_buttonWidget = QWidget()
confirm_step6_buttonLayout = QHBoxLayout()
confirm_step6_prev = QPushButton("Prev")
confirm_step6_next = QPushButton("Next")
confirm_step6_inputWidget = QWidget()
confirm_step6_inputLayout = QHBoxLayout()
confirm_step6_input = QLineEdit()
confirm_step6_textareaWidget = QWidget()
confirm_step6_textareaLayout = QHBoxLayout()
confirm_step6_textarea = QTextEdit()

Confirm(confirm_step6_wrap, confirm_step6_layout, confirm_step6_titleWidget, confirm_step6_titleLayout, confirm_step6_title, "알아낸 Table들을 입력해주세요.")
confirm_step6_wrap.hide()

Confirm_TextArea(confirm_step6_layout, confirm_step6_textareaWidget, confirm_step6_textareaLayout, confirm_step6_textarea, "출력된 Table이름 전체를 붙여넣기 해주세요.")
Confirm_Input(confirm_step6_layout, confirm_step6_inputWidget, confirm_step6_inputLayout, confirm_step6_input, "정보를 추출해낼 Table의 이름을 하나만 입력해주세요.")
Confirm_Button(confirm_step6_layout, confirm_step6_buttonWidget, confirm_step6_buttonLayout, confirm_step6_prev, confirm_step6_next)


confirm_step6_prev.clicked.connect(active.Step6_Confirm_Prev)
confirm_step6_next.clicked.connect(active.Step6_Confirm_Next)

#-----------------------------------------------------------------------

Wrap(7)
wrap[7].hide()
Title("Step 7", "Column 이름 알아내기", 7)

Url(7)
Button(7)

Prev[7].clicked.connect(active.Step7_Prev)
Next[7].clicked.connect(active.Step7_Next)

#--------------------------------------------------------------------

confirm_step7_wrap = QWidget()
confirm_step7_layout = QVBoxLayout()
confirm_step7_titleWidget = QWidget()
confirm_step7_titleLayout = QHBoxLayout()
confirm_step7_title = QLabel("")
confirm_step7_buttonWidget = QWidget()
confirm_step7_buttonLayout = QHBoxLayout()
confirm_step7_prev = QPushButton("Prev")
confirm_step7_next = QPushButton("Next")
confirm_step7_inputWidget = QWidget()
confirm_step7_inputLayout = QHBoxLayout()
confirm_step7_input = QLineEdit()
confirm_step7_textareaWidget = QWidget()
confirm_step7_textareaLayout = QHBoxLayout()
confirm_step7_textarea = QTextEdit()

Confirm(confirm_step7_wrap, confirm_step7_layout, confirm_step7_titleWidget, confirm_step7_titleLayout, confirm_step7_title, "알아낸 Column들을 입력해주세요.")
confirm_step7_wrap.hide()

Confirm_TextArea(confirm_step7_layout, confirm_step7_textareaWidget, confirm_step7_textareaLayout, confirm_step7_textarea, "출력된 Column이름 전체를 붙여넣기 해주세요.")
Confirm_Input(confirm_step7_layout, confirm_step7_inputWidget, confirm_step7_inputLayout, confirm_step7_input, "정보를 추출해낼 Column의 이름을 입력해주세요.(다수 가능. 콤마로 구분해주세요.)")
Confirm_Button(confirm_step7_layout, confirm_step7_buttonWidget, confirm_step7_buttonLayout, confirm_step7_prev, confirm_step7_next)

confirm_step7_prev.clicked.connect(active.Step7_Confirm_Prev)
confirm_step7_next.clicked.connect(active.Step7_Confirm_Next)

#------------------------------------------------------------------------

Wrap(8)
wrap[8].hide()
Title("Step 8", "Column에서 데이터 추출하기", 8)

Url(8)
Button(8)

Prev[8].clicked.connect(active.Step8_Prev)
Next[8].clicked.connect(active.Step8_Next)

#--------------------------------------------------------------------------

confirm_step8_wrap = QWidget()
confirm_step8_layout = QVBoxLayout()
confirm_step8_titleWidget = QWidget()
confirm_step8_titleLayout = QHBoxLayout()
confirm_step8_title = QLabel("")
confirm_step8_buttonWidget = QWidget()
confirm_step8_buttonLayout = QHBoxLayout()
confirm_step8_prev = QPushButton("Prev")
confirm_step8_next = QPushButton("Save")
confirm_step8_textareaWidget = QWidget()
confirm_step8_textareaLayout = QHBoxLayout()
confirm_step8_textarea = QTextEdit()

Confirm(confirm_step8_wrap, confirm_step8_layout, confirm_step8_titleWidget, confirm_step8_titleLayout, confirm_step8_title, "알아낸 Data들을 입력해주세요.")
confirm_step8_wrap.hide()

Confirm_TextArea(confirm_step8_layout, confirm_step8_textareaWidget, confirm_step8_textareaLayout, confirm_step8_textarea, "출력된 Data 전체를 붙여넣기 해주세요.")
Confirm_Button(confirm_step8_layout, confirm_step8_buttonWidget, confirm_step8_buttonLayout, confirm_step8_prev, confirm_step8_next)
confirm_step8_textareaLayout.setContentsMargins(30, 30, 30, 30)


confirm_step8_prev.clicked.connect(active.Step8_Confirm_Prev)
#confirm_step8_next.clicked.connect(active.Step8_Confirm_Save)
