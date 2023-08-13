import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt
import spotlight_logic
import spotlight_zipping_logic
import spotlight_styles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotlight Image Copy Tool")
        self.setGeometry(150, 70, 750, 570)
        self.setStyleSheet("background-color: #212121; color: #f0f0f0; border: 2px solid #212121;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title_label = spotlight_styles.StyledTitleLabel("Welcome to the Spotlight Image Copy Tool!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        description_label = QLabel(
            "<p style='font-size: 16px; text-align: center;'>Unlock the charm of your lock screen images on your desktop effortlessly.</p>"
            "<p style='font-size: 12px; text-align: center;'>🎨 Created by Sourav Sadhukhan 👨🏻‍💻🖥️</p>"
            "<hr />"
            "<p style='font-size: 14px; text-align: left;'>Ever admired those captivating images on your lock screen? Now, you can gather them all in a special folder named '<em>Spotlight Images</em>' right on your desktop.</p>"
            "<p style='font-size: 14px; text-align: left;'>No need to worry about image quality! This clever tool carefully selects images in landscape orientation, so they keep their original shape.</p>"
            "<p style='font-size: 14px; text-align: left;'>And the best part? It effortlessly converts these images into the versatile JPEG format, giving each image a sophisticated name like '<strong>Spotlight_Timestamp.jpg</strong>'.</p>"
            "<p style='font-size: 14px; text-align: left;'>With the Spotlight Image Copy Tool, you'll curate a delightful collection of images – perfectly organized and ready for your enjoyment. So, why wait? Just click the '<strong>Proceed</strong>' button below and let the enchantment begin!</p>",
            self)
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description_label)

        button_frame = QFrame()
        button_layout = QHBoxLayout(button_frame)
        button_frame.setStyleSheet("background-color: transparent;")

        btn_proceed = spotlight_styles.create_styled_button(
            "🚀 Proceed", "#0d6efd", "#0e5ede", "#0d6efd", spotlight_logic.copy_spotlight_images
        )
        button_layout.addWidget(btn_proceed)

        set_path_button = spotlight_styles.create_styled_button(
            "📁 Set location", "transparent", "#0d6efd", "#0d6efd", spotlight_logic.set_destination_folder
        )
        button_layout.addWidget(set_path_button)

        zip_folder_button = spotlight_styles.create_styled_button(
            "🗜️ Zip folder", "transparent", "#C07800", "#C07800", spotlight_zipping_logic.on_create_zip_clicked
        )
        button_layout.addWidget(zip_folder_button)

        layout.addWidget(button_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(button_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        version_label = QLabel("Version 2.0.0", self)
        version_label.setStyleSheet("font-size: 8px; color: #888;")
        version_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        version_label.setMaximumHeight(16)  # Set maximum height for version_label
        layout.addWidget(version_label, alignment=Qt.AlignmentFlag.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
