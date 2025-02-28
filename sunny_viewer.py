import os
import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

#Step 1: Find the script directory
base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))                   

#Step 2: find the pictures file (here Sunny cuz he's really a foodie)
image_folder = os.path.abspath(os.path.join(base_dir, "Sunny"))                                  

#Step 3: Create the visual interface (Kinda usefull to see pictures)
class ImageViewer(QWidget):                                                                    
    def __init__(self, image_folder):                                                           
        super().__init__()
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

        # Step 3.1: put your icon HERE (replace default_sunny_icon.ico)
        icon_path = os.path.join(base_dir,"default_sunny_icon.ico")       
        if os.path.exists(icon_path):                                                   
            self.setWindowIcon(QIcon(icon_path))

        self.image_name_label = QLabel(self)
        self.image_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Step 3.2: you could change the name of the button
        self.random_button = QPushButton("RANDOM PIC")                    
        self.random_button.clicked.connect(self.show_random_image)

        layout = QVBoxLayout()                                      
        layout.addWidget(self.image_name_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.random_button)
        self.setLayout(layout)
        #Step 3.3: you could change the name of the window (but dont do it pls)
        self.setWindowTitle("SUNNY VIEWER")                               
        self.show_random_image()

    def show_random_image(self):
        if self.image_files:
            image_file = random.choice(self.image_files)
            image_path = os.path.join(self.image_folder, image_file)

            self.image_name_label.setText(os.path.splitext(image_file)[0])
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_folder)
    viewer.show()
    sys.exit(app.exec())          

#Step 4: enjoy like Sunny does
#           __..--''``---....___   _..._    __
# /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
#///_.-' _..--.'_    \                    `( ) ) // //
#/ (_..-' // (< _     ;_..__               ; `' / ///
# / // // //  `-._,_)' // / ``--...____..-' /// / //  Made By Dante3ee