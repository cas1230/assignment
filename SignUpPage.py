 #SignUpPage.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
#from database import Database
from LoginPage import LoginPage
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyAD2ci7C4qhkKHW8wZa6UYUAwU485Sed74",
  'authDomain': "rice1234334.firebaseapp.com",
  'databaseURL': "https://rice1234334-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "rice1234334",
  'storageBucket': "rice1234334.appspot.com",
  'messagingSenderId': "950315200025",
  'appId': "1:950315200025:web:14fae278a5712f9b178488",
  'measurementId': "G-XQDJP6N0HD"
};

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

class SignUpPage(QWidget):
    def __init__(self, parent):
        super(SignUpPage, self).__init__(parent)
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle('Sign Up Page')

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.password2_label = QLabel('Confirm Password:')
        self.password2_input = QLineEdit()
        self.password2_input.setEchoMode(QLineEdit.Password)

        self.signup_button = QPushButton('Sign Up', self)
        self.signup_button.clicked.connect(self.sign_up)

        self.error = QLabel("")
        self.error.raise_()


        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        #layout.addWidget(self.worker_id_label)
        #layout.addWidget(self.worker_id_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.password2_label)
        layout.addWidget(self.password2_input)
        layout.addWidget(self.error)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)
    def sign_up(self):
        email = self.email_input.text()
        password = self.password_input.text()
        password2 = self.password2_input.text()

        if len(email)==0 or len (password) ==0 or len (password2) ==0:
            self.error.setText("Please input all fields.")

        elif password == password2:
            try:
                auth.create_user_with_email_and_password(email, password)
                #print("Signed up sucessfully")
                login_page = LoginPage(self)
                self.parent().setCentralWidget(login_page)
            except:
                self.invalid.setVisible(True)

        else:
            print("Sign Up Button Clicked")
            #Database.add_user(worker_email, password)
            #login_page = LoginPage(self)
            #self.parent().setCentralWidget(login_page)
