import sys
from theme import setupTheme
from display import Display
from variable import WINDOW_ICON_PATH
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from downloader import Downloader

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    widget = QWidget()

    app.setApplicationName('Media Downloader')
    icon = QIcon(str(WINDOW_ICON_PATH))
    widget.setWindowIcon(icon)

    widget.setFixedSize(570, 190)
    layout = QGridLayout(widget)
    layout.setVerticalSpacing(10)
    layout.setContentsMargins(10, 15, 10, 15)

    def error():
        QMessageBox.information(
            widget, 'ERROR', 'Error: Não foi possível baixar a mídia!')

    label = QLabel('Bem-vindo ao Media Downloader!')
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet('font-weight: bold; font-size: 15px')
    layout.addWidget(label, 0, 0, 1, 2)

    display = Display()
    layout.addWidget(display, 1, 0, 1, 2)

    # Pass the objects as arguments
    downloader = Downloader(widget, display, error)

    btnMp4 = QPushButton('MP4')
    btnMp4.setStyleSheet(
        'font-size: 17px; color: blue; height: 30px; width: 70px; font-weight: bold')
    btnMp4.clicked.connect(downloader.baixarMp4)
    layout.addWidget(btnMp4, 2, 1)

    btnMp3 = QPushButton('MP3')
    btnMp3.setStyleSheet(
        'font-size: 17px; color: blue; height: 30px; width: 70px; font-weight: bold')
    btnMp3.clicked.connect(downloader.baixarMp3)
    layout.addWidget(btnMp3, 2, 0)

    creditos = QLabel('Feito por Luiz Felipe Grifo')
    creditos.setAlignment(Qt.AlignmentFlag.AlignJustify)
    layout.addWidget(creditos, 3, 0)

    widget.show()
    sys.exit(app.exec())
