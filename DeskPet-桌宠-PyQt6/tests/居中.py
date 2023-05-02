from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QLabel
from PyQt6.QtGui import QPixmap,QImage,QMovie,QColor
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyWindow")
        self.setGeometry(0, 0, 400, 400)

        # 调用 centre 方法将窗口居中显示
        self.centre()
        self.setUI()

    def setUI(self):
        self.l=QLabel(self)
        self.l.setFixedSize(100,100)
        self.l.setStyleSheet("background-color:blue;")
        movie=QMovie('1.gif')
        self.l.setMovie(movie)
        print(movie.frameCount())
        print(movie.loopCount())
        print(movie.backgroundColor())
        movie.start()
        movie.setSpeed(1000)
        # movie.setP
        # movie.setBackgroundColor()

    def centre(self):
        # 获取窗口大小
        qr = self.frameGeometry()
        # 获取屏幕大小
        cp = QApplication.primaryScreen().geometry().center()
        # 移动窗口并居中显示
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())