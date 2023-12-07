
import time

import PySide6
from PySide6.QtWidgets import  QSplashScreen, QProgressBar, QApplication
from PySide6.QtGui import QMovie, QPixmap, QPainter
from PySide6.QtCore import QSize


class MovieSplashScreen(QSplashScreen):
    my_size = QSize(1280, 720)

    def __init__(self, path_to_gif: str):
        self.movie = QMovie(path_to_gif)
        self.movie.jumpToFrame(0)
        pixmap = QPixmap(self.my_size)
        QSplashScreen.__init__(self, pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        self.movie.start()

    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        self.movie.stop()

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        pixmap = pixmap.scaled(self.my_size)
        painter.drawPixmap(0, 0, pixmap)


def start_splash(app: QApplication, timer: int ):
    progressbar_value = timer
    path_to_gif = 'content/Alex 1280X720.gif'

    splash = MovieSplashScreen(path_to_gif)
    processbar = QProgressBar(splash)
    processbar.setMaximum(progressbar_value)
    processbar.setTextVisible(False)
    processbar.setGeometry(0, splash.my_size.height() - 50,
                           splash.my_size.width(), 20)

    splash.show()
    processbar.hide()
    for i in range(progressbar_value):
        processbar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()
