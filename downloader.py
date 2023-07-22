import yt_dlp
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import Slot


class Downloader():
    def __init__(self, widget, display, error):
        self.widget = widget
        self.display = display
        self.error = error

    @Slot()
    def baixarMp4(self):
        linkYt = self.display.text()
        print(linkYt)
        pasta = QFileDialog.getExistingDirectory(None, 'Selecione uma pasta')

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/bestvideo[ext=mp4]/best',
            'outtmpl': f'{pasta}/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([linkYt])
                QMessageBox.information(
                    self.widget, 'Download concluído', 'Download concluído com sucesso!')
            except Exception as e:
                print(e)
                self.error()

    @Slot()
    def baixarMp3(self):
        linkYt = self.display.text()
        print(linkYt)
        pasta = QFileDialog.getExistingDirectory(None, 'Selecione uma pasta')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{pasta}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([linkYt])
                QMessageBox.information(
                    self.widget, 'Concluído', 'Download concluído com sucesso!')
            except Exception as e:
                print(e)
                self.error()
