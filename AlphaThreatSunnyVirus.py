import os
import sys
import random
import ctypes
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# Obtenir le dossier contenant le script ou l'exécutable
base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

# Chemin du dossier contenant les images
image_folder = os.path.abspath(os.path.join(base_dir, "Sunny"))

# Vérification que le dossier existe
if not os.path.exists(image_folder):
    print(f"Erreur : le dossier {image_folder} n'existe pas.")
    sys.exit(1)

# Définir un identifiant unique pour l'application
myappid = 'SUNNY.M4G.V1'  
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class ImageViewer(QWidget):
    def __init__(self, image_folder):
        super().__init__()
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

        if not self.image_files:
            print("Aucun fichier image trouvé dans", image_folder)
            sys.exit(1)

        # Appliquer l'icône à la fenêtre principale
        icon_path = os.path.join(base_dir, "Sunny", "MesSentimentsPourSunny.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icône non trouvée à {icon_path}")

        # Label pour afficher le nom de l'image
        self.image_name_label = QLabel(self)
        self.image_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label pour afficher l'image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bouton pour afficher une image aléatoire
        self.random_button = QPushButton("Aléatoire")
        self.random_button.clicked.connect(self.show_random_image)

        # Layout pour organiser les éléments
        layout = QVBoxLayout()
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

            # Vérification
            if not os.path.exists(image_path):
                print(f"Erreur : Image introuvable {image_path}")
                return
        
            # Mise a jour
            self.image_name_label.setText(os.path.splitext(image_file)[0])
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_folder)
    viewer.show()
    sys.exit(app.exec())
