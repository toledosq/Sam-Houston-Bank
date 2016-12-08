from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from transaction_view import Ui_Transactions
from new_user import Ui_NewUser

class Ui_Login(QtWidgets.QDialog):
    
    def showMessageBox(self, title, message):
        #Displays a message box when called
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showTransactionWindow(self):
        #Opens the transaction history window when called
        self.transactionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Transactions(self)
        self.ui.setupUi(self.transactionWindow, self.userID)
        self.transactionWindow.show()
        
    def showNewUserReg(self):
        #displays the new user registration window when called
        self.newUserWindow = QtWidgets.QDialog()
        self.ui = Ui_NewUser()
        self.ui.setupUi(self.newUserWindow)
        self.newUserWindow.show()
    
    def loginCheck(self):
        #obtain username and password from fields
        username = self.username_field.text()
        password = self.password_field.text()

        #connect to database
        connection = sqlite3.connect('bankDB.db')
        result = connection.execute('SELECT username, password FROM login WHERE username=? AND password=?', (username, password))

        #Define UI translator
        _translate = QtCore.QCoreApplication.translate
        
        if (len(result.fetchall()) > 0):
            #Check to see if the username/password combination exists in the database
            result = connection.execute('SELECT UID FROM login WHERE username=? AND password=?', (username, password))
            temp = result.fetchone()
            self.userID = temp[0]
            #If found, reset the username and password fields to empty
            self.username_field.setText(_translate("Dialog", ""))
            self.password_field.setText(_translate("Dialog", ""))
            #Display transaction window
            self.showTransactionWindow()
        else:
            #If username/password combo not found, show message box
            self.showMessageBox("Warning", "Invalid Username or Password!")
            self.password_field.setText(_translate("Dialog", ""))

        connection.close()

    def newUserCheck(self):
        self.showNewUserReg()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)

        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("shsuEdit1.jpg"))
        self.bg.setObjectName("bg")
        
        #New User Button
        self.new_user_button = QtWidgets.QPushButton(Dialog)
        self.new_user_button.setGeometry(QtCore.QRect(730, 360, 81, 23))
        self.new_user_button.setObjectName("new_user_button")
        ##### BUTTON EVENT #####
        self.new_user_button.clicked.connect(self.newUserCheck)
        ########################

        #LOG IN BUTTON
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(730, 330, 81, 23))
        self.login_button.setAutoFillBackground(False)
        self.login_button.setObjectName("login_button")
        ##### BUTTON EVENT #####
        self.login_button.clicked.connect(self.loginCheck)
        ########################
        
        self.username_field = QtWidgets.QLineEdit(Dialog)
        self.username_field.setGeometry(QtCore.QRect(480, 220, 331, 31))
        self.username_field.setAutoFillBackground(False)
        self.username_field.setObjectName("username_field")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(480, 310, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.password_field = QtWidgets.QLineEdit(Dialog)
        self.password_field.setGeometry(QtCore.QRect(480, 280, 331, 31))
        self.password_field.setObjectName("password_field")
        #HIDE PASSWORD - COMMENT FOLLOWING LINE TO DISPLAY PASSWORD
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.username_field, self.password_field)
        Dialog.setTabOrder(self.password_field, self.login_button)
        Dialog.setTabOrder(self.login_button, self.new_user_button)

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.new_user_button.setText(_translate("Dialog", "New User?"))
        self.login_button.setText(_translate("Dialog", "Log In"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

