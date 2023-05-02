from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QMovie, QPixmap, QColor, QImage, QPainter
from PyQt6.QtCore import Qt,QSize

app = QApplication([])
window = QWidget()

# 加载 GIF 图像
movie = QMovie("1.gif")

# 创建 QLabel 组件并将其设置为动画
label = QLabel(window)
label.setMovie(movie)
label.setFixedSize(100, 100)
label.setStyleSheet("background-color:blue;")
# 开始播放动画
movie.start()

# 定义需要抠出的颜色
color_to_replace = QColor(255, 255, 255)   # 将所有白色像素替换为透明色
def compare_colors(color1, color2):
    delta_red = abs(color1.red() - color2.red())
    delta_green = abs(color1.green() - color2.green())
    delta_blue = abs(color1.blue() - color2.blue())
    return delta_red < 20 and delta_green < 20 and delta_blue < 20
# 循环遍历 GIF 中的每帧，并进行像素操作
for i in range(movie.frameCount()):
    # 获取当前帧的像素数据并转换成 QImage 对象
    movie.jumpToFrame(i)
    pixmap = movie.currentPixmap()
    image = pixmap.toImage()

    # 创建和当前帧一样大小的新 QImage 对象，并将所有像素设置为透明色
    transparent = QImage(image)
    transparent.fill(QColor(255,255,255,0))

    # 创建 QPainter 对象并使用它绘制新 QImage 对象
    painter = QPainter()
    painter.begin(transparent)

    # 将需要抠出的颜色替换为透明色
    for y in range(image.height()):
        for x in range(image.width()):
            pixel_color = QColor(image.pixel(x, y))

            if compare_colors(pixel_color,color_to_replace):
            # if pixel_color == color_to_replace:
                painter.setPen(QColor(255,255,255,0))
                painter.drawPoint(x, y)
            else:
                painter.setPen(pixel_color)
                painter.drawPoint(x, y)

    painter.end()

    # 将修改后的 QImage 对象转换成 QPixmap 并显示
    pixmap = QPixmap.fromImage(transparent)
    label.setPixmap(pixmap)

    label.repaint()

window.show()
app.exec()