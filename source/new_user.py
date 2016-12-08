from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random

class Ui_NewUser(object):
    
    def showWarningBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
    def insertData(self):
        newUser = self.new_username.text()
        newPass = self.new_password.text()
        newFName = self.new_first_name.text()
        newLName = self.new_last_name.text()
        newUID = random.randint(10000, 99999)

        #Obtain Phone and SSN
        try:
            newPhone = int(self.new_phone.text())
        except:
            self.showWarningBox("Warning", "Invalid Phone Number. Please do not include any punctuation.")
            return
        newAddr = self.new_addr.text()
        try:
            newSSN = int(self.new_SSN.text())
        except:
            self.showWarningBox("Warning", "Invalid Social Security Number. Please do not include any punctuation.")
            return

        #Check them for validity
        if len(str(newPhone)) != 10:
            self.showWarningBox("Warning", "Invalid Phone Number. Make sure you include all 10 digits.")
            return
        if len(str(newSSN)) != 9:
            self.showWarningBox("Warning", "Invalid Social Security Number. Make sure you include all 9 digits.")
            return

        
        input_values = (newUID, newFName, newLName, newPhone, newAddr, newSSN)
        
        connection = sqlite3.connect("bankDB.db")
        
        cmp = connection.execute("SELECT username FROM login WHERE username=?", [newUser])
        
        if (len(cmp.fetchall()) > 0):
            self.showWarningBox("Warning", "This username is already taken!")
        else:
            connection.execute('INSERT INTO login VALUES(?, ?, ?)', (newUID, newUser, newPass))
            connection.execute('INSERT INTO userInfo VALUES(?, ?, ?, ?, ?, ?)', input_values)
            connection.execute('INSERT INTO accountList VALUES (?, ?, ?, ?)', (newUID, "Checking", 1, 0.00))
            self.showMessageBox("Success", "Welcome to Sam Houston Bank!")
            
        connection.commit()
        connection.close()
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.new_username = QtWidgets.QLineEdit(Dialog)
        self.new_username.setGeometry(QtCore.QRect(160, 100, 191, 31))
        self.new_username.setObjectName("new_username")
        
        self.new_password = QtWidgets.QLineEdit(Dialog)
        self.new_password.setGeometry(QtCore.QRect(160, 140, 191, 31))
        self.new_password.setObjectName("new_password")
        
        self.new_first_name = QtWidgets.QLineEdit(Dialog)
        self.new_first_name.setGeometry(QtCore.QRect(160, 220, 191, 31))
        self.new_first_name.setObjectName("new_first_name")
        
        self.new_last_name = QtWidgets.QLineEdit(Dialog)
        self.new_last_name.setGeometry(QtCore.QRect(160, 260, 191, 31))
        self.new_last_name.setObjectName("new_last_name")
        
        self.new_phone = QtWidgets.QLineEdit(Dialog)
        self.new_phone.setGeometry(QtCore.QRect(160, 300, 191, 31))
        self.new_phone.setObjectName("new_phone")
        
        self.new_addr = QtWidgets.QLineEdit(Dialog)
        self.new_addr.setGeometry(QtCore.QRect(160, 340, 191, 31))
        self.new_addr.setObjectName("new_addr")
        
        self.new_SSN = QtWidgets.QLineEdit(Dialog)
        self.new_SSN.setGeometry(QtCore.QRect(160, 380, 191, 31))
        self.new_SSN.setObjectName("new_SSN")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(70, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 380, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(220, 430, 75, 23))
        self.signup_button.setObjectName("signup_button")
        ##### BUTTON EVENT #####
        self.signup_button.clicked.connect(self.insertData)
        ########################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "New User Registration"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "First Name"))
        self.label_5.setText(_translate("Dialog", "Last Name"))
        self.label_6.setText(_translate("Dialog", "Phone Number"))
        self.label_7.setText(_translate("Dialog", "Address"))
        self.label_8.setText(_translate("Dialog", "SSN"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NewUser()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

