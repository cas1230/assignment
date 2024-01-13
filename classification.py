import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions

class RiceClassificationApp(QWidget):
    def __init__(self):
        super(RiceClassificationApp, self).__init__()

        # Load the pre-trained model from the .h5 file
        self.model = load_model('my_model.h5')

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Rice Classification App')

        # QLabel to display the uploaded image
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(300, 200)

        # QPushButton to trigger image selection
        self.upload_button = QPushButton('Upload Image', self)
        self.upload_button.clicked.connect(self.upload_image)

        # QLabel to display the classification result
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.result_label.setWordWrap(True)

        # QVBoxLayout to organize the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.ico);;All Files (*)", options=options)

        if file_name:
            # Load and preprocess the image
            print("1")
            img = image.load_img(file_name, target_size=(150, 150))
            print("2")
            img_array = image.img_to_array(img)
            print("3")
            img_array = np.expand_dims(img_array, axis=0)
            print("4")
            img_array = preprocess_input(img_array)

            # Display the uploaded image
            print("Display images")
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(300, 200, aspectRatioMode=1)  # Maintain aspect ratio
            self.image_label.setPixmap(pixmap)

            predictions = None
            decoded_predictions = None

            # Use the pre-trained model for prediction
            print("Use the pre-trained model for prediction")
            try:
                predictions = self.model.predict(img_array)
            except Exception as e:
                print(f"Error creating user: {e}")

            try:
                #if predictions.shape[1] == 1000:
                    #print("decoded")
                decoded_predictions = decode_predictions(predictions)[0]
                print("Done")
            except Exception as e:
                print(f"Error creating user: {e}")


            # Display the classification result
            result_text = "Classification Result:\n"
            for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
                result_text += f"{i + 1}. {label}: {score:.2f}\n"
            self.result_label.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RiceClassificationApp()
    window.show()
    sys.exit(app.exec_())
