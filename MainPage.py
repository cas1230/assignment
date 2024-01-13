from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from datetime import datetime
from database import Database

class MainPage(QWidget):
    def __init__(self, parent):
        super(MainPage, self).__init__(parent)
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle('Main Page')
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(300, 200)

        self.upload_button = QPushButton('Upload', self)
        self.process_button = QPushButton('Process', self)
        self.logout_button = QPushButton('Logout', self)

        self.upload_button.clicked.connect(self.upload)
        self.process_button.clicked.connect(self.process)
        self.logout_button.clicked.connect(self.logout)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.process_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def upload(self):
        try:
            file_dialog = QFileDialog()
            file_name, _ = file_dialog.getOpenFileName(self, 'Open Image File', '',
                                                   'Image Files (*.png *.jpg *.bmp);;All Files (*)')
            print("Displaying image")

            if file_name:
                # Display the uploaded image
                pixmap = QPixmap(file_name)
                pixmap = pixmap.scaled(300, 200, aspectRatioMode=1)  # Maintain aspect ratio
                self.image_label.setPixmap(pixmap)
                print("Images should be displayed")


        except Exception as e:
            print(f"Error creating user: {e}")

            # Display the scaled image
            #self.image_label.setPixmap(pixmap.scaled(new_size, QtCore.Qt.KeepAspectRatio))
           # self.image_label.show()


    def process(self):
        # Implement the logic for processing images here
        db = Database()
        db.save_log(
            worker_name='John Doe',
            worker_id='123',
            images=['image1.jpg', 'image2.jpg'],
            num_rice_packages=1,
            percentages={
                'arborio': 10,
                'basmati': 20,
                'ipsala': 30,
                'jasmine': 25,
                'karacadag': 15
            },
            final_rice_type='Long Grain'
        )

    def logout(self):
        # Implement the logic for logging out here
        login_page = LoginPage(self)
        self.parent().setCentralWidget(login_page)
