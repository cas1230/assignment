from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from MainPage import MainPage
import pyrebase
#from database import Database

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


class LoginPage(QWidget):
    def __init__(self, parent):
        super(LoginPage, self).__init__(parent)
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle('Login Page')

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        self.error = QLabel("")
        self.error.raise_()


        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.error)

        self.setLayout(layout)

    def login(self):
        #print("Login")
        email = self.email_input.text()
        password = self.password_input.text()

        if len(email)==0 or len (password) ==0:
            self.error.setText("Please input all fields.")

        else:
            try:
                #print("Opening Firebase")
                auth.sign_in_with_email_and_password(email, password)
                print("Logged in successfully")
                main_page = MainPage()
                self.parent().setCentralWidget(main_page)
            except Exception as e:
                print(f"Error creating user: {e}")
                self.invalid.setVisible(True)
                #self.error.setText("Authentication failed")  # Replace with proper error handling

            # if authenticate_user(worker_id, password):
            #     main_page = MainPage(self)
            #     self.parent().setCentralWidget(main_page)
            # else:
            #     self.error.setText("Authentication failed")  # Replace with proper error handling
