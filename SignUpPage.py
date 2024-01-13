 #SignUpPage.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from database import Database
from LoginPage import LoginPage
import pyrebase

firebaseConfig={
    'apiKey': "AIzaSyBUTX8Rim1OMPAKOMFjRzsf4CHmPW_6gMY",
    'authDomain': "authdemo-79174.firebaseapp.com",
    'databaseURL':"https://authdemo-79174.firebaseio.com",
    'projectId': "authdemo-79174",
    'storageBucket': "authdemo-79174.appspot.com",
    'messagingSenderId': "498091607020",
    'appId': "1:498091607020:web:0142211b6f901ad33cf6c9",
    'measurementId': "G-R733GSGM2L"}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()



class SignUpPage(QWidget):
    def __init__(self, parent):
        super(SignUpPage, self).__init__(parent)

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
                print(password)
                print(password2)
                auth.create_user_with_email_and_password(email, password)
                login = Login()
                login_page = LoginPage(self)
                self.parent().setCentralWidget(login_page)
            except:
                self.invalid.setVisible(True)

        else:
            print("Sign Up Button Clicked")
            #Database.add_user(worker_email, password)
            #login_page = LoginPage(self)
            #self.parent().setCentralWidget(login_page)
