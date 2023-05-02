from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QSizePolicy
from PyQt6.QtGui import QPixmap,QImage,QMovie,QColor,QIcon
from PyQt6.QtCore import Qt,QTimer,QSize
import sys
import os
import random
current_path = os.path.abspath(os.path.dirname(__file__))
images_path=current_path+'/resources/images/'

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 是否在拖拽属性
        self.dragging = False
        # 设置标题与logo
        self.setWindowTitle("编程启航")
        self.setWindowIcon(QIcon('logo.png'))
        # 窗口置顶与窗口无边框
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint,True)
        # 设置窗口大小且透明
        self.setGeometry(0,0,200,200)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # 内容设置
        self.setUI()

    def setUI(self):
        # 给label设置图片
        self.label=QLabel(self)
        img=QPixmap(images_path+'1.png')
        img=img.scaled(QSize(100,100))
        self.label.setPixmap(img)
        self.label.adjustSize()
        self.centra()
        self.addBlinkTimer()
    def restoreImg(self):
        img = QPixmap(images_path + '1.png')
        img = img.scaled(QSize(100, 100))
        self.label.setPixmap(img)
        self.label.adjustSize()
    def blink(self):
        img=QPixmap(images_path+'2.png')
        img=img.scaled(QSize(100,100))
        self.label.setPixmap(img)
        self.label.adjustSize()
        QTimer.singleShot(500,  self.restoreImg)


        # img=QPixmap(images_path+'1.png')
        # img=img.scaled(QSize(100,100))
        # self.label.setPixmap(img)
        # self.label.adjustSize()


    def addBlinkTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.blink)
        self.timer.start()
        # self.label=QLabel()
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


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

    # 居中显示
    def centra(self):
        # 窗口居中
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # 标签居中
        dis=(self.size() - self.label.size())/2
        self.label.move(dis.width(),dis.height())


    def mousePressEvent(self, event):
        # 鼠标按压
        if event.button() == Qt.MouseButton.LeftButton and self.geometry().contains(self.mapToGlobal(event.pos())):
            self.dis = self.mapToGlobal(event.pos()) - self.pos()
            self.dragging = True
            self.setCursor(Qt.CursorShape.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        # 鼠标移动
        if self.dragging:
            self.move(self.mapToGlobal(event.pos()) - self.dis)
    def enterEvent(self, e) -> None:
        self.timer.stop()
        img=QPixmap(images_path+'3.png')
        img=img.scaled(QSize(100,100))
        self.label.setPixmap(img)
        self.label.adjustSize()

    def leaveEvent(self, e) -> None:
        self.timer.start()
        img=QPixmap(images_path+'1.png')
        img=img.scaled(QSize(100,100))
        self.label.setPixmap(img)
        self.label.adjustSize()

    def mouseReleaseEvent(self, event):
        # 鼠标释放
        if event.button() == Qt.MouseButton.LeftButton and self.dragging:
            self.dragging = False
            self.setCursor(Qt.CursorShape.OpenHandCursor)

    def mouseDoubleClickEvent(self, e):
        # 处理双击事件...
        if e.button() == Qt.MouseButton.LeftButton:

            pass

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.close()
            self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())