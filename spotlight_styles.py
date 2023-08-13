from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame
from PyQt6.QtGui import QLinearGradient, QColor, QBrush, QPainter

def create_styled_button(text, color, hover_color, border_color, click_action):
    button = QPushButton(text)
    button.setStyleSheet(f"""
        QPushButton {{ 
            text-align: center;
            line-height: 1.5;
            font-weight: 600;
            background-color: {color};
            border: 1px solid;
            border-color: {border_color};
            padding: 12px 40px;
            font-size: 16px;
            border-radius: 12px;
            color: white;
            margin: 5px
        }}

        QPushButton:hover {{
            background-color: {hover_color};
            border: 2px solid {border_color};
        }}
    """)
    button.clicked.connect(click_action)
    return button

class StyledTitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            font-size: 30px;
            font-weight: 300;
            color: #222;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-align: center;
        """)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#0C0C0C"))
        gradient.setColorAt(0.33, QColor("#503090"))
        gradient.setColorAt(0.33, QColor("#553c9a"))
        gradient.setColorAt(0.66, QColor("#553c9a"))
        gradient.setColorAt(0.66, QColor("#4834D4"))
        gradient.setColorAt(0.99, QColor("#4834D4"))
        painter.fillRect(self.rect(), QBrush(gradient))
        super().paintEvent(event)
