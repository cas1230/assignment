from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QApplication, QWidget
from LoginPage import LoginPage
from LoginPage2 import LoginPage2
from SignUpPage import SignUpPage
from MainPage import MainPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.login_button = QPushButton('Login', self)
        self.signup_button = QPushButton('Sign Up', self)

        layout = QVBoxLayout()
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.login_button.clicked.connect(self.show_login_page)

        self.signup_button.clicked.connect(self.show_signup_page)

    def show_login_page(self):
        login_page = LoginPage(self)
        #self.login_page.show()
        #self.hide()
        self.setCentralWidget(login_page)
    def show_signup_page(self):
        signup_page = SignUpPage(self)
        #self.login_page.hide()
        #self.hide()
        self.setCentralWidget(signup_page)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
