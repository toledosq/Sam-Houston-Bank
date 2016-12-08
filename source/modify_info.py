from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_ModifyInfo():

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def saveInfo(self):
        newFName = self.new_first_name.text()
        newLName = self.new_last_name.text()

        #Obtain phone and SSN
        try:
            newPhone = int(self.new_phone.text())
        except:
            self.showMessageBox("Warning", "Invalid Phone Number. Please do not include any punctuation.")
            return
        newAddr = self.new_addr.text()
        try:
            newSSN = int(self.new_SSN.text())
        except:
            self.showMessageBox("Warning", "Invalid Social Security Number. Please do not include any punctuation.")
            return

        #Check them for validity
        if len(str(newPhone)) != 10:
            self.showMessageBox("Warning", "Invalid Phone Number. Make sure you include all 10 digits.")
            return
        if len(str(newSSN)) != 9:
            self.showMessageBox("Warning", "Invalid Social Security Number. Make sure you include all 9 digits.")
            return

        connection = sqlite3.connect('bankDB.db')
        connection.execute('UPDATE userInfo SET firstName=?, lastName=?, phone=?, addr=?, ssn=? WHERE UID=?', (newFName, newLName, newPhone, newAddr, newSSN, self.uid))

        connection.commit()
        connection.close()

        self.showMessageBox("Success!", "Your personal information has been updated.")
    
    def setupUi(self, Dialog, userID = 1):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 350)

        self.uid = userID
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 210, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.new_last_name = QtWidgets.QLineEdit(Dialog)
        self.new_last_name.setGeometry(QtCore.QRect(170, 130, 191, 31))
        self.new_last_name.setObjectName("new_last_name")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(140, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.Save_button = QtWidgets.QPushButton(Dialog)
        self.Save_button.setGeometry(QtCore.QRect(230, 300, 75, 23))
        self.Save_button.setObjectName("Save_button")
        ##### BUTTON EVENT #####
        self.Save_button.clicked.connect(self.saveInfo)
        ########################
        
        self.new_phone = QtWidgets.QLineEdit(Dialog)
        self.new_phone.setGeometry(QtCore.QRect(170, 170, 191, 31))
        self.new_phone.setObjectName("new_phone")
        
        self.new_first_name = QtWidgets.QLineEdit(Dialog)
        self.new_first_name.setGeometry(QtCore.QRect(170, 90, 191, 31))
        self.new_first_name.setObjectName("new_first_name")
        
        self.new_addr = QtWidgets.QLineEdit(Dialog)
        self.new_addr.setGeometry(QtCore.QRect(170, 210, 191, 31))
        self.new_addr.setObjectName("new_addr")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.new_SSN = QtWidgets.QLineEdit(Dialog)
        self.new_SSN.setGeometry(QtCore.QRect(170, 250, 191, 31))
        self.new_SSN.setObjectName("new_SSN")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        Dialog.setTabOrder(self.new_first_name, self.new_last_name)
        Dialog.setTabOrder(self.new_last_name, self.new_phone)
        Dialog.setTabOrder(self.new_phone, self.new_addr)
        Dialog.setTabOrder(self.new_addr, self.new_SSN)
        Dialog.setTabOrder(self.new_SSN, self.Save_button)

    def retranslateUi(self, Dialog):
        connection = sqlite3.connect('bankDB.db')
        temp = connection.execute('SELECT firstName, lastName, phone, addr, SSN FROM userInfo WHERE UID=?', (self.uid,))
        uInfo = temp.fetchone()
        connection.close()
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Modify Personal Information"))
        self.label_6.setText(_translate("Dialog", "Phone Number"))
        self.label_7.setText(_translate("Dialog", "Address"))
        self.new_last_name.setText(_translate("Dialog", uInfo[1]))
        self.label_4.setText(_translate("Dialog", "First Name"))
        self.label_8.setText(_translate("Dialog", "SSN"))
        self.Save_button.setText(_translate("Dialog", "Save"))
        self.new_phone.setText(_translate("Dialog", str(uInfo[2])))
        self.new_first_name.setText(_translate("Dialog", uInfo[0]))
        self.new_addr.setText(_translate("Dialog", uInfo[3]))
        self.label_5.setText(_translate("Dialog", "Last Name"))
        self.new_SSN.setText(_translate("Dialog", str(uInfo[4])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ModifyInfo()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

