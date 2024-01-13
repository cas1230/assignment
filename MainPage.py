from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from datetime import datetime
from database import Database

class MainPage(QWidget):
    def __init__(self, parent):
        super(MainPage, self).__init__(parent)

        self.upload_button = QPushButton('Upload', self)
        self.process_button = QPushButton('Process', self)
        self.logout_button = QPushButton('Logout', self)

        self.upload_button.clicked.connect(self.upload)
        self.process_button.clicked.connect(self.process)
        self.logout_button.clicked.connect(self.logout)

        layout = QVBoxLayout()
        layout.addWidget(self.upload_button)
        layout.addWidget(self.process_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def upload(self):
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(None, 'Open Image File', '',
                                                   'Image Files (*.png *.jpg *.bmp);;All Files (*)')
        if file_name:
            # Display the uploaded image
            pixmap = QtGui.QPixmap(file_name)

            # Calculate the new size (e.g., 300x200)
            new_size = QtCore.QSize(100, 50)

            # Display the scaled image
            self.image_label.setPixmap(pixmap.scaled(new_size, QtCore.Qt.KeepAspectRatio))
            self.image_label.show()


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
