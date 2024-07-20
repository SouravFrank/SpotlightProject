import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
import spotlight_logic
import spotlight_zipping_logic
import spotlight_styles

class AeroFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 10px;
        """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotlight Image Copy Tool")
        self.setGeometry(150, 70, 850, 650)
        
        # Get the system palette
        palette = QApplication.palette()
        is_dark_mode = palette.color(QPalette.ColorRole.Window).value() < 128

        if is_dark_mode:
            self.setStyleSheet("""
                background: linear-gradient(135deg, #282c34, #1e1e1e);
                color: #f5f5f5;
                font-family: 'Segoe UI', sans-serif;
            """)
            desc_background = "rgba(40, 40, 40, 0.9)"
            button_text_color = "#fff"
        else:
            self.setStyleSheet("""
                background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
                color: #333;
                font-family: 'Segoe UI', sans-serif;
            """)
            desc_background = "rgba(255, 255, 255, 0.9)"
            button_text_color = "#000"

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title_label = QLabel("Welcome to the Spotlight Image Copy Tool!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(f"""
            font-size: 32px;
            font-weight: 700;
            color: {palette.color(QPalette.ColorRole.Highlight).name()};
            margin-bottom: 20px;
            padding: 10px;
        """)
        layout.addWidget(title_label)

        description_label = QLabel(
        "<p style='font-size: 18px; text-align: center;'>Discover and curate your favorite Spotlight images effortlessly with this powerful tool.</p>"
        "<p style='font-size: 14px; text-align: center;'>🎨 Crafted by Sourav Sadhukhan 👨🏻‍💻🖥️</p>"
        "<hr style='border: 1px solid #444;' />"
        "<p style='font-size: 16px; text-align: left;'>Ever wondered how to gather those stunning images from your lock screen? Now, you can effortlessly collect them in a folder named '<em>Spotlight Images</em>' exactly where you want.</p>"
        "<p style='font-size: 16px; text-align: left;'>No more hassle of repeatedly specifying the folder location – this tool remembers it for you. Need to change it? Just click the <strong>Set location</strong> button below.</p>"
        "<p style='font-size: 16px; text-align: left;'>Concerned about image quality? Don’t be! The tool smartly picks only landscape-oriented images, keeping their original quality intact, and ensures no duplicates.</p>"
        "<p style='font-size: 16px; text-align: left;'>And the best part? Create a zip archive of your entire Spotlight collection with a single click on the <strong>Zip folder</strong> button.</p>"
        "<p style='font-size: 16px; text-align: left;'>Start curating your amazing image collection today! Hit the <strong>Proceed</strong> button and let the magic unfold!</p>",
        self)
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setStyleSheet(f"""
            padding: 20px;
            border-radius: 15px;
            background: {desc_background};
            margin-bottom: 30px;
        """)
        layout.addWidget(description_label)

        button_frame = AeroFrame()
        button_layout = QHBoxLayout(button_frame)
        button_frame.setStyleSheet("background-color: transparent;")

        def create_button(text, callback):
            button = QPushButton(text)
            button.setStyleSheet(f"""
                background-color: {palette.color(QPalette.ColorRole.Highlight).name()};
                color: {button_text_color};
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: 600;
                border-radius: 12px;
                background: rgba(255, 255, 255, 0.1);
                border: 2px solid {palette.color(QPalette.ColorRole.Highlight).name()};
            """)
            button.clicked.connect(callback)
            button.setFixedSize(220, 60)  # Wider button size
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            # Add hover effect using a different method
            def on_enter(event):
                button.setStyleSheet(f"""
                    background-color: {palette.color(QPalette.ColorRole.Highlight).darker(120).name()};
                    color: {button_text_color};
                    border: none;
                    padding: 15px 30px;
                    font-size: 18px;
                    font-weight: 600;
                    border-radius: 12px;
                    background: rgba(255, 255, 255, 0.1);
                    border: 2px solid {palette.color(QPalette.ColorRole.Highlight).darker(120).name()};
                """)

            def on_leave(event):
                button.setStyleSheet(f"""
                    background-color: {palette.color(QPalette.ColorRole.Highlight).name()};
                    color: {button_text_color};
                    border: none;
                    padding: 15px 30px;
                    font-size: 18px;
                    font-weight: 600;
                    border-radius: 12px;
                    background: rgba(255, 255, 255, 0.1);
                    border: 2px solid {palette.color(QPalette.ColorRole.Highlight).name()};
                """)

            button.installEventFilter(self)
            button.eventFilter = lambda obj, event: on_enter(event) if event.type() == event.Type.Enter else on_leave(event)

            return button

        proceed_button = create_button("🚀 Let's Get Started!", spotlight_logic.copy_spotlight_images)
        set_path_button = create_button("📁 Choose Location", spotlight_logic.set_destination_folder)
        zip_folder_button = create_button("🗜️ Compress Folder", spotlight_zipping_logic.on_create_zip_clicked)

        button_layout.addWidget(proceed_button)
        button_layout.addWidget(set_path_button)
        button_layout.addWidget(zip_folder_button)

        layout.addWidget(button_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        version_label = QLabel("Version 2.1.0", self)
        version_label.setStyleSheet("font-size: 10px; color: #888;")
        version_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        version_label.setMaximumHeight(20)
        layout.addWidget(version_label, alignment=Qt.AlignmentFlag.AlignRight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
