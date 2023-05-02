from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QSizePolicy
from PyQt6.QtGui import QPixmap,QImage,QMovie,QColor,QIcon
from PyQt6.QtCore import Qt
import sys
import os
import random

current_path = os.path.abspath(os.path.dirname(__file__))
images_path=current_path+'/resources/images/'
print(images_path)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("编程启航")
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint,True)

        # 调用 centre 方法将窗口居中显示
        self.center()
        self.setUI()

    def setUI(self):

        # 添加存放图片的标签
        self.l=QLabel(self)
        self.l.setCursor(Qt.CursorShape.PointingHandCursor)
        # self.l.setFixedSize(100,100)
        # self.l.setStyleSheet("background-color:blue;")

        movie=QMovie(images_path+'1.gif')
        self.l.setMovie(movie)

        movie.start()
        print(self.l.size())
        self.l.adjustSize()
        print(self.l.size())
        self.setFixedSize(self.l.size())

    def center(self):
        # 获取窗口大小
        qr = self.frameGeometry()
        # 获取屏幕大小
        cp = QApplication.primaryScreen().geometry().center()
        # 移动窗口并居中显示
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            pass
            # 处理双击事件...
        elif e.button() == Qt.MouseButton.RightButton:
            self.close()
            # 处理双击事件...

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())