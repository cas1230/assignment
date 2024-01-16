from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QApplication, QWidget
from LoginPage import LoginPage
from SignUpPage import SignUpPage
#from MainPage import MainPage
from PostResultPage import PostResultPage



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle('Main Window')
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

        self.post_result_page = PostResultPage()
        self.setCentralWidget(self.post_result_page)

    def show_login_page(self):
        login_page = LoginPage(self)
        self.setCentralWidget(login_page)
    def show_signup_page(self):
        signup_page = SignUpPage(self)
        self.setCentralWidget(signup_page)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
