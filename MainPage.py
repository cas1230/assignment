import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout, QScrollArea, QSizePolicy, QComboBox
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from PostResultPage import PostResultPage

class RiceImageWidget(QWidget):
    def __init__(self, image_path, result_text, parent=None):
        super(RiceImageWidget, self).__init__(parent)

        # QLabel to display the uploaded image
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(150, 100, aspectRatioMode=1)  # Maintain aspect ratio
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        # QLabel to display the result
        self.result_label = QLabel(result_text, self)

        # Create a QVBoxLayout for the custom widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.addWidget(self.result_label)

class MainPage(QWidget):
    def __init__(self):
        super(MainPage, self).__init__()

        # Load the pre-trained model from the .h5 file
        self.model = load_model('rice_image_classification.h5')

        # Variables to store processed images and results
        self.sample_images = []
        self.results = []

        # Create a QVBoxLayout for the main layout
        self.main_layout = QVBoxLayout()

        # Create a QScrollArea to enable scrolling if there are many images
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create a QWidget to serve as the content of the scroll area
        self.scroll_content = QWidget()
        self.scroll_area.setFixedHeight(200)
        self.scroll_area.setWidget(self.scroll_content)
        #self.scroll_content.setFixedHeight(200)

        # Create a QVBoxLayout for the content
        self.image_layout = QVBoxLayout(self.scroll_content)

        # Create a QComboBox for rice type selection
        self.rice_type_combobox = QComboBox(self)
        self.rice_type_combobox.addItems(["Arborio", "Basmati", "Ipsala", "Jasmine", "Karacadag"])

        # Create a QHBoxLayout for the button row
        button_layout = QHBoxLayout()

        # QPushButton to trigger image selection
        self.upload_button = QPushButton('Upload Images', self)
        self.upload_button.clicked.connect(self.upload_images)
        button_layout.addWidget(self.upload_button)

        # QPushButton to start processing and display results
        self.process_button = QPushButton('Process and Display Results', self)
        self.process_button.clicked.connect(self.process_and_display)
        button_layout.addWidget(self.process_button)

        # Create QLabel to display result
        self.result_label = QLabel(self)
        self.overall_result_label = QLabel(self)

        # Add the button layout to the main layout
        self.main_layout.addWidget(self.rice_type_combobox)
        self.main_layout.addLayout(button_layout)

        # Add the scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)

        # Add a stretchable space at the top to push everything else to the bottom
        self.main_layout.addStretch()

        # Add the QLabel for overall result at the bottom
        self.main_layout.addWidget(self.overall_result_label)

        self.done_button = QPushButton('Done', self)
        self.done_button.clicked.connect(self.switch_to_post_result)
        self.main_layout.addWidget(self.done_button)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)

    def upload_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Open Image Files", "",
                                                     "Images (*.png *.jpg *.jpeg *.bmp *.gif *.ico);;All Files (*)",
                                                     options=options)

        if 5 <= len(file_names) <= 10:
            # Clear previous data
            self.sample_images = []

            try:
                for i, file_name in enumerate(file_names[:10]):
                    # Load and preprocess each image
                    img = image.load_img(file_name, target_size=(224, 224))
                    img_array = image.img_to_array(img)
                    img_array = np.expand_dims(img_array, axis=0)
                    img_arr = preprocess_input(img_array)


                    # Display the uploaded image
                    pixmap = QPixmap(file_name)
                    pixmap = pixmap.scaled(150, 100, aspectRatioMode=1)  # Maintain aspect ratio

                    # QLabel to display the uploaded image
                    image_widget = RiceImageWidget(file_name, "", self)
                    image_widget.image_label.setPixmap(pixmap)

                    # Add the image_widget to the image_layout
                    self.image_layout.addWidget(image_widget)

                    # Store the processed image for later
                    self.sample_images.append((img_array, file_name))
                    # print(file_name)
                    # print(img_array)
            except Exception as e:
                print(f"1.Error creating user: {e}")

    def process_and_display(self):
        if not self.sample_images:
            return  # No images uploaded

        # Process each image and store the results
        try:
            input_data = [img[0] for img in self.sample_images]  # Extract only the numpy arrays

            # Convert the list of numpy arrays to a single numpy array
            input_data = np.concatenate(input_data, axis=0)

            # Use the model to predict
            self.results = self.model.predict(input_data)

            # Display the results in the console and update the result label
            overall_result = ""
            class_names = ["Arborio", "Basmati", "Ipsala", "Jasmine", "Karacadag"]

            selected_rice = self.rice_type_combobox.currentText()
            selected_rice_index = class_names.index(selected_rice)

            # Initialize counters for selected and other rice types
            selected_rice_count = 0
            other_rice_count = 0

            # Loop through each prediction
            for i, prediction in enumerate(self.results):
                # Get the index of the class with the highest probability
                predicted_class_index = np.argmax(prediction)

                # Get the corresponding class name
                predicted_class_name = class_names[predicted_class_index]

                # Display the result in the console
                print(f"Image {i + 1} - Predicted Rice Type: {predicted_class_name}")

                # Update the result_text
                result_text = f"Image {i + 1} - Predicted Rice Type: {predicted_class_name}"
                # Set the result_text in the corresponding image widget
                image_widget = self.image_layout.itemAt(i).widget()
                if image_widget:
                    image_widget.result_label.setText(result_text)

                if predicted_class_index == selected_rice_index:
                    selected_rice_count += 1
                else:
                    other_rice_count += 1
                overall_result += ""
            # Calculate percentages
            total_images = len(self.sample_images)
            percentage_selected_rice = (selected_rice_count / total_images) * 100
            percentage_other_rice = (other_rice_count / total_images) * 100

            # Display the result in the QLabel
            overall_result += f"\nOverall Percentage of {selected_rice}: {percentage_selected_rice:.2f}%\n" \
                           f"Overall Percentage of Other Rice Types: {percentage_other_rice:.2f}%"
            self.overall_result_label.setText(overall_result)

        except Exception as e:
            print(f"Error creating user: {e}")

        def switch_to_post_result(self):
            # Assuming 'self.parent()' is a QMainWindow or similar
            postresult_page = PostResultPage(self.parent())
            self.parent().setCentralWidget(postresult_page)

        def login(self):
            main_page = MainPage()
            self.parent().setCentralWidget(main_page)

