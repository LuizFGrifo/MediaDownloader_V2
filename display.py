from PySide6.QtWidgets import QLineEdit
from variable import SMALL_FONT_SIZE, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margin = [TEXT_MARGIN for _ in range(4)]
        self.setPlaceholderText('Digite o link do video:')
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setTextMargins(*margin)
