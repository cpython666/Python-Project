from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QMovie, QPixmap
app = QApplication([])
window = QWidget()
# 加载 GIF 图像
movie = QMovie("1.gif")
# 创建 QLabel 组件并将其设置为动画
label = QLabel(window)
label.setMovie(movie)
# 开始播放动画
movie.start()


window.show()
app.exec()