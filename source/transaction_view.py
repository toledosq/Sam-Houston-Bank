from PyQt5 import QtCore, QtGui, QtWidgets
from deposit_window import Ui_Deposit
from withdraw_window import Ui_Withdraw
from modify_info import Ui_ModifyInfo
import sqlite3


class Ui_Transactions(QtWidgets.QMainWindow):

    def showMessageBox(self, title, message):
        #Displays a customizable message box
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def modifyInfo(self):
        #launches the modify user info window
        self.modifyWindow = QtWidgets.QDialog()
        self.ui = Ui_ModifyInfo()
        self.ui.setupUi(self.modifyWindow, self.uid)
        self.modifyWindow.show()

    def refreshTable(self):
        #Refreshes transactions table and total balance at bottom of window
        connection = sqlite3.connect('bankDB.db')
        c = connection.cursor()

        #Count the # of transactions currently stored to obtain # of rows to display in table
        row = c.execute('SELECT count(*) FROM transactions WHERE UID=?', (self.uid,))
        rowcount = row.fetchone()
        #pass the number of rows obtained into the table. Column will always be 4
        self.transactionTable.setRowCount(rowcount[0])
        self.transactionTable.setColumnCount(5)

        #obtained transaction type, amount, current balance, and date from transaction table
        result = c.execute('SELECT type, amount, curB, date, description FROM transactions WHERE UID=?', (self.uid,))
        #Display rows in table
        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.transactionTable.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

        #Fetch total balance from account
        temp = c.execute('SELECT totalBalance FROM accountList WHERE UID=?', (self.uid,))
        balance = temp.fetchone()[0]
        #Place into string that will appear at bottom of window
        balance = str("Your current balance is: $" + format(balance, '.2f'))
        #Pass string to label at bottom of window
        _translate = QtCore.QCoreApplication.translate
        self.balanceLabel.setText(_translate("Dialog", balance))

        c.close()
        connection.close()
        
    def deposit(self):
        #Call deposit window
        self.depositWindow = QtWidgets.QDialog()
        self.ui = Ui_Deposit()
        self.ui.setupUi(self.depositWindow, self.uid)
        self.depositWindow.show()
        print(self.uid)
                
    def withdraw(self):
        #Call withdraw window
        self.withdrawWindow = QtWidgets.QDialog()
        self.ui = Ui_Withdraw()
        self.ui.setupUi(self.withdrawWindow, self.uid)
        self.withdrawWindow.show()
        print(self.uid)
        
    def closeAndReturn(self):
        import sys
        sys.exit(app.exec_())
    
    def setupUi(self, Dialog, userID = 1):
        #AUTO GENERATED CODE (except button events)
        #The following code creates the GUI
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)

        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("shsuEdit2.jpg"))
        self.bg.setObjectName("bg")

        self.uid = userID
        
        self.logOutButton = QtWidgets.QPushButton(Dialog)
        self.logOutButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.logOutButton.setObjectName("logOutButton")
        ##### BUTTON EVENT #####
        self.logOutButton.clicked.connect(self.closeAndReturn)
        ########################
        
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 40, 801, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")        
        self.verticalLayout.addWidget(self.label)
        
        self.transactionTable = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transactionTable.sizePolicy().hasHeightForWidth())
        self.transactionTable.setSizePolicy(sizePolicy)
        self.transactionTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transactionTable.setAutoFillBackground(False)
        self.transactionTable.setAlternatingRowColors(True)
        self.transactionTable.setObjectName("transactionTable")
        self.transactionTable.setColumnCount(5)
        self.transactionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.transactionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionTable.setHorizontalHeaderItem(4, item)
        self.transactionTable.horizontalHeader().setDefaultSectionSize(156)
        self.verticalLayout.addWidget(self.transactionTable)
        
        
        self.depositButton = QtWidgets.QPushButton(self.layoutWidget)
        self.depositButton.setObjectName("depositButton")
        self.verticalLayout.addWidget(self.depositButton)
        ##### BUTTON EVENT #####
        self.depositButton.clicked.connect(self.deposit)
        ########################

        self.withdrawButton = QtWidgets.QPushButton(self.layoutWidget)
        self.withdrawButton.setObjectName("withdrawButton")
        self.verticalLayout.addWidget(self.withdrawButton)
        ##### BUTTON EVENT #####
        self.withdrawButton.clicked.connect(self.withdraw)
        ########################
        
        self.balanceLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceLabel.setObjectName("balanceLabel")
        
        self.verticalLayout.addWidget(self.balanceLabel)
        self.userLabel = QtWidgets.QLabel(Dialog)
        self.userLabel.setGeometry(QtCore.QRect(20, 20, 201, 31))
        self.userLabel.setObjectName("userLabel")
        
        self.refreshButton = QtWidgets.QPushButton(Dialog)
        self.refreshButton.setGeometry(QtCore.QRect(1050, 90, 75, 23))
        self.refreshButton.setObjectName("refreshButton")
        ##### BUTTON EVENT #####
        self.refreshButton.clicked.connect(self.refreshTable)
        ########################
        
        self.editInfo = QtWidgets.QPushButton(Dialog)
        self.editInfo.setGeometry(QtCore.QRect(20, 80, 131, 23))
        self.editInfo.setObjectName("editInfo")
        ##### BUTTON EVENT #####
        self.editInfo.clicked.connect(self.modifyInfo)
        ########################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        connection = sqlite3.connect('bankDB.db')

        #Fetch name from userInfo
        temp = connection.execute('SELECT firstName, lastName FROM userInfo WHERE UID=?', (self.uid,))
        userNames = temp.fetchone()
        #Place names into strings
        firstName = userNames[0]
        lastName = userNames[1]

        #Create string that displays current user logged in. Passed into label below.
        fullName = ("Currently logged in as " + firstName + " " + lastName)
        
        #Fetch total balance from accountList. Passed into label below.
        temp = connection.execute('SELECT totalBalance FROM accountList WHERE UID=?', (self.uid,))
        balance = temp.fetchone()[0]
        balance = str("Your current balance is: $" + format(balance, '.2f'))
        
        connection.close()
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logOutButton.setText(_translate("Dialog", "Log Out"))
        self.label.setText(_translate("Dialog", ""))
        item = self.transactionTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Transaction Type"))
        item = self.transactionTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Amount"))
        item = self.transactionTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Total Balance Remaining"))
        item = self.transactionTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        item = self.transactionTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Description"))
        self.depositButton.setText(_translate("Dialog", "Make a deposit"))
        self.withdrawButton.setText(_translate("Dialog", "Make a Withdrawal"))
        self.balanceLabel.setText(_translate("Dialog", balance))
        self.userLabel.setText(_translate("Dialog", fullName))
        self.refreshButton.setText(_translate("Dialog", "Refresh"))
        self.editInfo.setText(_translate("Dialog", "Edit Personal Information"))
        self.refreshTable()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Transactions()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

