from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QLinearGradient, QColor, QBrush, QPainter
import spotlight_logic

def create_styled_button(text, textColor, color, click_action):
    button = QPushButton(text)
    button.setStyleSheet(f"""
        QPushButton {{ 
            text-align: center;
            line-height: 1.5;
            font-weight: 600;
            background-color: {color};
            border: 1px solid;
            border-color: {textColor};
            padding: 12px 40px;
            font-size: 16px;
            border-radius: 12px;
            color: {textColor};
            margin: 5px
        }}

        QPushButton:hover {{
            background-color: { textColor if not "#fff" == textColor else "#1a85ff" };
            border: 2px solid { textColor if not "#fff" == textColor else "#0d6efd" };
            color: white;
        }}
    """)
    button.clicked.connect(click_action)
    return button

class StyledTitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet(f"""
            font-size: 30px;
            font-weight: 300;
            color: {"#f0f0f0" if not spotlight_logic.detect_system_theme() else "#212121"};
            letter-spacing: 1px;
            text-transform: uppercase;
            text-align: center;
        """)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor( "#f0f0f0" if not spotlight_logic.detect_system_theme() else "#212121" ))
        gradient.setColorAt(0.33, QColor("#503090"))
        gradient.setColorAt(0.33, QColor("#553c9a"))
        gradient.setColorAt(0.66, QColor("#4834D4"))
        gradient.setColorAt(0.66, QColor("#4834D4"))
        gradient.setColorAt(0.99, QColor("#4834D4"))
        painter.fillRect(self.rect(), QBrush(gradient))
        super().paintEvent(event)
