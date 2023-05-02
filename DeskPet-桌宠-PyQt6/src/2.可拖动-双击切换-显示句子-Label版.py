from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QSizePolicy
from PyQt6.QtGui import QPixmap,QImage,QMovie,QColor,QIcon
from PyQt6.QtCore import Qt,QTimer,QSize
import sys
import os
import random
current_path = os.path.abspath(os.path.dirname(__file__))
images_path=current_path+'/resources/gifs/'
# print(images_path)
class Window(QLabel):
    def __init__(self):
        super().__init__()
        self.dragging = False

        self.setWindowTitle("编程启航")
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint,True)

        # 调用 centre 方法将窗口居中显示
        self.setUI()
        self.addTimer()
    def addTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(2000)  # 设置为10秒钟
        self.timer.timeout.connect(self.show_phrase)
        self.timer.start()
        self.label=QLabel()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


    def show_phrase(self):
        # movie=QMovie(images_path+random.choice(['瞪眼睛.png','眨眼睛.png']))
        # custom_size = QSize(200, 200)
        # movie.setScaledSize(QSize(200,200))
        # movie=QMovie(images_path+'11.gif')
        # self.setMovie(movie)
        # movie.start()
        phrases = [
            "别玩了，赶紧工作吧",
            "喝口水休息一下吧",
            "又加班呀，辛苦了",
            "坚持一下，成功就在前方",
        ]

        # 随机选择一句话语
        phrase = random.choice(phrases)

        # 将话语显示在标签上
        self.label.setGeometry(self.pos().x()+2,self.pos().y()-15,0,0)
        self.label.setText(phrase)
        self.label.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint,True)

        # 显示标签
        self.label.adjustSize()
        self.label.show()
        # self.label.setText()
        # self.label.setGeometry(-20,-20,100,10)



    def setUI(self):
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        self.setStyleSheet("border-radius:5px;")
        movie=QMovie(images_path+'1.gif')
        # custom_size = QSize(200, 200)
        # movie.setScaledSize(QSize(200,200))
        # movie=QMovie(images_path+'11.gif')
        self.setMovie(movie)
        movie.start()
        self.adjustSize()
        self.center()

    # 居中显示
    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        print(self.geometry())
        print(event.pos())
        print(self.mapToGlobal(event.pos()))
        print(self.geometry().contains(event.pos()))
        if event.button() == Qt.MouseButton.LeftButton and self.geometry().contains(self.mapToGlobal(event.pos())):
            self.dis = self.mapToGlobal(event.pos()) - self.pos()
            self.dragging = True
            self.setCursor(Qt.CursorShape.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToGlobal(event.pos()) - self.dis)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.dragging:
            self.dragging = False
            self.setCursor(Qt.CursorShape.OpenHandCursor)

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            tmp=random.choice(os.listdir(images_path))
            movie = QMovie(images_path + tmp)
            self.setMovie(movie)
            movie.start()
            self.adjustSize()
            # self.center()

            # 处理双击事件...
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.close()
            self.close()
            # 处理双击事件...



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())