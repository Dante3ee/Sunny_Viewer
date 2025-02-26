import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtCore import Qt
import ctypes

class ImageViewer(QWidget):
    def __init__(self, image_folder):
        super().__init__()
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

        # Appliquer l'icône à la fenêtre principale                                                            #Cette partie marche pas
        self.setWindowIcon(QIcon("Cadeau\Sunny\icon.ico"))                                                     #
        myappid = 'SUNNY.M4G.V1'                                                                               #                           
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)                                 #

        #afficher le nom de l'image
        self.image_name_label = QLabel(self)
        self.image_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # afficher l'image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.random_button = QPushButton("Aléatoire")            # Bouton aléatoire
        self.random_button.clicked.connect(self.show_random_image)

        layout = QVBoxLayout()                         #Layout
        layout.addWidget(self.image_name_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.random_button)
        self.setLayout(layout)
        self.setWindowTitle("SUNNY")
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
    folder_path = "Cadeau\Sunny"  # En theorie je peux retirer ça
    viewer = ImageViewer(folder_path)
    viewer.show()
    sys.exit(app.exec())
