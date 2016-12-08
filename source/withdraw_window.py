from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import time

class Ui_Withdraw():

    def setUserID(self, userID):
        self.uid = userID

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


    def withdraw(self):

        connection = sqlite3.connect('bankDB.db')
        cur = connection.cursor()
        withdrawAmount = self.withdraw_line.text()
        desc = self.desc_line.text()

        if desc == "Description (optional)":
            desc = ""
        elif len(desc) > 30:
            self.showWarningBox("Error", "Description must be 30 characters or less")
            return
        
        #New transaction ID is +1 from last
        temp1 = cur.execute('SELECT count(*) FROM transactions')
        temp2 = temp1.fetchone()
        new_transaction_ID = temp2[0] + 1

        #attempt to typecast depositAmount to int for storage
        try:
            withdrawAmount = float(withdrawAmount)
        except:
            try:
                withdrawAmount = withdrawAmount.translate({ord(c): None for c in '$,'})
                withdrawAmount = float(withdrawAmount)
            except:
                self.showWarningBox("Error", "Invalid amount")
                return
        if withdrawAmount < 0.0:
            self.showWarningBox("Error", "Invalid amount")
            return
        elif withdrawAmount > 10000:
            self.showWarningBox("Error", "Cannot withdraw more than $10,000")
            return
        
        #update current balance
        result = cur.execute('SELECT totalBalance FROM accountList WHERE UID=?', (self.uid,))
        almostThere = result.fetchone()
        temp = almostThere[0]
        newBalance = temp - withdrawAmount
   
        #get current date stamp
        date = time.strftime("%m/%d/%Y")
        daSTR = ("$"+str(format(withdrawAmount, '.2f')))
        nbSTR = ("$"+str(format(newBalance, '.2f')))
        #insert deposit
        cur.execute('INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)', (new_transaction_ID, self.uid, "Withdrawal", daSTR, date, nbSTR, desc))
        cur.execute('UPDATE accountList SET totalBalance=? WHERE UID=?', (newBalance, self.uid))

        connection.commit()
        connection.close()

        #Show message box to confirm successful deposit
        insertMsg = ("Withdrew " + daSTR +"\nYour remaining balance is " + nbSTR)
        self.showMessageBox("Success!", insertMsg)

        _translate = QtCore.QCoreApplication.translate
        self.withdraw_line.setText(_translate("Dialog", ""))
        self.desc_line.setText(_translate("Dialog", "Description (optional)"))
        
    def setupUi(self, Dialog, userID = 1):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 160)

        self.uid = userID
        
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 20, 301, 111))
        self.widget.setObjectName("widget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        self.withdraw_line = QtWidgets.QLineEdit(self.widget)
        self.withdraw_line.setObjectName("withdraw_line")
        self.verticalLayout.addWidget(self.withdraw_line)

        self.desc_line = QtWidgets.QLineEdit(self.widget)
        self.desc_line.setObjectName("Desc_line")
        self.verticalLayout.addWidget(self.desc_line)
        
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.verticalLayout.addWidget(self.okButton)
        ##### BUTTON EVENT #####
        self.okButton.clicked.connect(self.withdraw)
        ########################
        
        self.label.raise_()
        self.withdraw_line.raise_()
        self.okButton.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Amount to Withdraw"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.desc_line.setText(_translate("Dialog", "Description (optional)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Withdraw()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    

