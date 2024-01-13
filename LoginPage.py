from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from MainPage import MainPage
from database import Database


class LoginPage(QWidget):
    def __init__(self, parent):
        super(LoginPage, self).__init__(parent)

        self.worker_id_label = QLabel('Worker ID:')
        self.worker_id_input = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        self.error = QLabel("")
        self.error.raise_()


        layout = QVBoxLayout()
        layout.addWidget(self.worker_id_label)
        layout.addWidget(self.worker_id_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.error)

        self.setLayout(layout)

    def login(self):
        worker_id = self.worker_id_input.text()
        password = self.password_input.text()

        if len(worker_id)==0 or len (password_input) ==0:
            self.error.setText("Please input all fields.")

        else:

            if authenticate_user(worker_id, password):
                main_page = MainPage(self)
                self.parent().setCentralWidget(main_page)
            else:
                self.error.setText("Authentication failed")  # Replace with proper error handling
