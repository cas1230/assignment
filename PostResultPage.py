from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QApplication
from MainWindow import MainWindow
from MainPage import MainPage
from LoginPage import LoginPage

class PostResultPage(QWidget):
    def __init__(self, parent):
        super(PostResultPage, self).__init__(parent)
        layout = QVBoxLayout()

        upload_again_button = QPushButton('Upload Images Again', self)
        upload_again_button.clicked.connect(self.switch_to_main)
        layout.addWidget(upload_again_button)

        logout_button = QPushButton('Logout', self)
        logout_button.clicked.connect(self.switch_to_login)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def switch_to_main(self):
        self.switch_to_page(MainPage)

    def switch_to_login(self):
        self.switch_to_page(LoginPage)

    def switch_to_page(self, page_class):
        new_page = page_class(self.parent())
        self.parent().setCentralWidget(new_page)