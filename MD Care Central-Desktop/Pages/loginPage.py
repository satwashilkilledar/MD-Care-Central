from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Pages.superadminHome import *
from Pages.doctorHome import *
from Pages.dispensaryHome import *
from Pages.bloodBankHome import *
from Pages.testCenterHome import *
from Pages.hospitalHome import *
from Pages.emergencyServiceHome import *
# import psycopg2 as pg2


class HoverButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)


class loginPage(object):
    def setup(self, loginPage):
        loginPage.setObjectName("loginPage")
        # loginPage.resize(1300,768)
        # loginPage.setStyleSheet("background: rgb(66, 140, 244);")
        self.centralwidget = QtWidgets.QWidget(loginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(560, 50, 621, 121))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.Logo.setFont(font)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(640, 480, 201, 31))
        self.loginButton.setStyleSheet("\n"
                                       "font: 50 12pt \"URW Bookman L\";")
        self.loginButton.setObjectName("loginButton")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(440, 370, 171, 31))
        self.usernameLabel.setStyleSheet("\n"
                                         "font: 50 13pt \"URW Bookman L\";")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setGeometry(QtCore.QRect(630, 370, 471, 31))
        self.userNameInput.setStyleSheet("border: 2px solid gray;\n"
                                         "    border-radius: 10px;\n"
                                         "    padding: 0 8px;\n"
                                         "    selection-background-color: darkgray;")
        self.userNameInput.setText("")
        self.userNameInput.setObjectName("userNameInput")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(440, 420, 171, 31))
        self.passwordLabel.setStyleSheet("\n"
                                         "font: 50 13pt \"URW Bookman L\";")
        self.passwordLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(630, 420, 471, 31))
        self.passwordInput.setStyleSheet("border: 2px solid gray;\n"
                                         "    border-radius: 10px;\n"
                                         "    padding: 0 8px;\n"
                                         "    selection-background-color: darkgray;\n"
                                         "lineedit-password-character: 9679;")
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.forgotPasswordLink = HoverButton(self.centralwidget)
        self.forgotPasswordLink.setGeometry(QtCore.QRect(440, 480, 171, 25))
        self.forgotPasswordLink.setStyleSheet("COLOR : RED;\n"
                                              "border-top: 3px transparent;\n"
                                              "border-bottom: 3px transparent;\n"
                                              "font: 30 oblique 8pt \"Tlwg Typo\";\n"
                                              "            border-right: 10px transparent;\n"
                                              "            border-left: 10px transparent;\n"
                                              "text-decoration : underline;")
        self.forgotPasswordLink.setObjectName("forgotPasswordLink")
        loginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "MainWindow"))
        self.Logo.setText(_translate("Ma   inLoginWindow", "MDTouch"))
        self.loginButton.setText(_translate("loginPage", "LOGIN"))
        self.usernameLabel.setText(_translate("loginPage", "USERNAME"))
        self.passwordLabel.setText(_translate("loginPage", "PASSWORD"))
        self.forgotPasswordLink.setText(_translate("loginPage", "FORGOT PASSWORD?"))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.eventsUi(loginPage)
        # self.loginEvent(loginPage)

    def eventsUi(self, loginPage):
        self.forgotPasswordLink.clicked.connect(lambda: self.forgotPasswordEvent(loginPage))
        self.passwordInput.returnPressed.connect(self.loginButton.click)
        self.loginButton.clicked.connect(lambda: self.loginEvent(loginPage))
        #self.loginButton.clicked.connect(lambda: self.justLogin(loginPage))

    def justLogin(self, loginPage):
        logintype = 'DS'
        if logintype == 'SA':
            self.superadminpage = superadminHome()
            self.superadminpage.setup(loginPage)
        elif logintype == 'D':
            self.doctorpage = doctorHome()
            self.doctorpage.setup(loginPage)
        elif logintype == 'DS':
            self.dispensarypage = dispensaryHome()
            self.dispensarypage.setup(loginPage)
        elif logintype == 'BB':
            self.bloodBankpage = bloodBankHome()
            self.bloodBankpage.setup(loginPage)
        elif logintype == 'T':
            self.testCenterpage = testCenterHome()
            self.testCenterpage.setup(loginPage)
        elif logintype == 'H':
            self.hospitalpage = hospitalHome()
            self.hospitalpage.setup(loginPage)
        elif logintype == 'ES':
            self.emergencyservicepage = emergencyServiceHome()
            self.emergencyservicepage.setup(loginPage)



    def forgotPasswordEvent(self, loginPage):

        # forgot Password Email Sent
        username = self.userNameInput.text()
        if username == "":
            self.dialog = messageBox()
            self.dialog.infoBox('Enter the username')
            return

        try:
            self.dialog = messageBox()
            self.dialog.infoBox('The link to reset your password has been sent to your email')
        except:
            self.dialog = messageBox()
            self.dialog.warningBox('Something happened with connection Try Again! Check Your Internet Connection')

    # Login Event

    def loginEvent(self, loginPage):
        # Checking id and password
        usernameInput = self.userNameInput.text()
        passwordInput = self.passwordInput.text()

        if usernameInput == "" or passwordInput == "":
            self.dialog = messageBox()
            self.dialog.infoBox('Invalid Credentials')
            return

        param = {
            "username" : usernameInput,
            "password" : passwordInput
        }
        URL = "http://127.0.0.1:8000/api/login/"
        import requests
        r = requests.get(url=URL,params=param)
        data = r.json()
        print(data)
        if len(data) == 0:
            self.dialog = messageBox()
            self.dialog.infoBox('Invalid Credentials')
            return
        if data[0]["dept"] == "SA":
            self.superadminpage = superadminHome()
            self.superadminpage.setup(loginPage,data[0])
            return
        if data[0]["dept"] == "D":
            self.doctorpage = doctorHome()
            self.doctorpage.setup(loginPage,data[0])
            return
        if data[0]["dept"] == "DS":
            self.dispensarypage = dispensaryHome()
            self.dispensarypage.setup(loginPage,data[0])
            return
        if data[0]["dept"] == "BB":
            self.bloodBankpage = bloodBankHome()
            self.bloodBankpage.setup(loginPage,data[0])
            return
        if data[0]["dept"] == "TC":
            self.testCenterpage = testCenterHome()
            self.testCenterpage.setup(loginPage,data[0])
            return
        if data[0]["dept"] == "H":
            self.hospitalpage = hospitalHome()
            self.hospitalpage.setup(loginPage,data[0])
        if data[0]["dept"] == "ES":
            self.espage = emergencyServiceHome()
            self.espage.setup(loginPage,data[0])










