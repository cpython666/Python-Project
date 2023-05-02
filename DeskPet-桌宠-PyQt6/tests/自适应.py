from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.movie = QMovie('1.gif')
        self.movie.setCacheMode(QMovie.CacheMode.CacheAll)

        # 获取 GIF 图像的大小
        self.gif_size = self.movie.frameRect().size()

        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.label.setMovie(self.movie)

        # 创建垂直布局
        self.vlayout = QVBoxLayout()
        # 添加标签到布局中
        self.vlayout.addWidget(self.label)
        # 设置垂直布局为主窗口布局
        self.setCentralWidget(QLabel())
        self.centralWidget().setLayout(self.vlayout)

        # 开始播放 GIF 图像
        self.movie.start()

        # 连接信号resized
        self.movie.resized.connect(self.on_movie_resized)

        # 设置主窗口大小
        # self.setMinimumSize(self.gif_size.width(), self.gif_size.height())
        # self.setMaximumSize(self.gif_size.width(), self.gif_size.height())
        # self.resize(self.gif_size)

        # 设置主窗口标题
        self.setWindowTitle("GIF 图像大小变化监测示例")

    def on_movie_resized(self):
        self.gif_size = self.movie.frameRect().size()
        self.setMinimumSize(self.gif_size.width(), self.gif_size.height())
        self.setMaximumSize(self.gif_size.width(), self.gif_size.height())
        self.resize(self.gif_size)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()