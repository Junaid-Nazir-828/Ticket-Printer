# Import necessary modules

from PyQt5.QtGui import QFont
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from css import style
from auth import user
from main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QCursor



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JD Tech')
        self.setObjectName("login window")
        self.setWindowIcon(QIcon("img/favicon.ico"))
        self.initializeUI()#1027, 748
        self.setFixedWidth(1027)
        self.setFixedHeight(748)            

    def openWindow2(self):        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)        
        self.hide()
        self.window.show()    

    def initializeUI(self):
        self.logo = QLabel(self)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("margin-top: 50;")


        self.user = QLabel(self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setStyleSheet(
            "margin-top: 50;"
            "color:#677788;"
            )
        # self.user.setText("Developer Contact: junaidnazir828@gmail.com\n")# Whatsapp : +92 348 5858573
      

        logo_image = QPixmap('/opt/lampp/htdocs/Front/img/logo-short.svg')
        # windowimage = QPixmap('/opt/lampp/htdocs/Front/undraw_Welcome_re_h3d9.png')
        self.logo.setPixmap(logo_image)
      


        self.singin_label = QLabel(self)
        self.singin_label.setText("Sign in")
        self.singin_label.setFont(QFont("Popins", 25))
        self.singin_label.setAlignment(Qt.AlignCenter)
        self.singin_label.setStyleSheet(
            "font-weight: bold;"
            "margin-top: 50;"
            "margin-bottom: 60;"
            "color:#377dff"
            )

        self.username_ql = QLineEdit(self)
        self.username_ql.setFixedWidth(400)
        self.username_ql.setTextMargins(20,0,0,0)
        self.username_ql.setPlaceholderText("Username")
        self.username_ql.setFont(QFont("Popins",12))
        self.username_ql.setStyleSheet(
            "margin-bottom: 50;"
            "border-radius: 25%;"
            "padding: 18px;"
            "background-color: #1e20229a;"
            "border: 1px solid #bdc5d1;"
            )

        self.password_ql = QLineEdit(self,)
        self.password_ql.setFixedWidth(400)
        self.password_ql.setTextMargins(20,0,0,0)
        self.password_ql.setEchoMode(QLineEdit.Password)
        self.password_ql.setPlaceholderText("Password")
        self.password_ql.setFont(QFont("Popins",12))
        self.password_ql.setStyleSheet(
            "margin-bottom: 15;"
            "border-radius: 25%;"
            "padding: 18px;"
            "background-color:#1e20229a;"
            "border: 1px solid #bdc5d1;"
            )


        self.show_password_cb = QCheckBox("Show Password", self)
        self.show_password_cb.setStyleSheet(
            "color:#677788;"
            "margin-left: 20px;")

        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        self.button = QPushButton(self)
        self.button.setFixedWidth(120)
        self.button.setMinimumHeight(45)
        self.button.setObjectName("Button")
        self.button.setText("Log in")
        self.button.setFont(QFont("Popins", 13))
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.clicked.connect(self.clickLoginButton)
        
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.logo,0,0)
        self.layout.addWidget(self.singin_label,1,0)
        self.layout.addWidget(self.username_ql,2,0)
        self.layout.addWidget(self.password_ql,3,0)
        self.layout.addWidget(self.show_password_cb ,4,0)
        self.layout.addWidget(self.button,5,0,Qt.AlignCenter)
        self.layout.addWidget(self.user,6,0)
        # self.layout.addWidget(self.window_image,7,0)


        self.layout .setRowStretch(7,1) 
        

    # Functions 
    def displayPasswordIfChecked(self,checked):
        if checked:
            self.password_ql.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_ql.setEchoMode(QLineEdit.EchoMode.Password)


    def clickLoginButton(self):
        #user_info = ['armando',1]
        username = self.username_ql.text().strip()
        password = self.password_ql.text().strip()
        QMessageBox()
        
        if user.authorize(username,password):
            self.openWindow2()            
        else:
            QMessageBox.warning(self, "Log in Error","Invalid username or password!",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setStyleSheet(style.style_sheet)
    window.show()
    sys.exit(app.exec_())
