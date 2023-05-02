from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QMovie

app = QApplication([])
window = QWidget()

# 加载 GIF 图像
movie = QMovie("1.gif")

# 创建 QLabel 组件并将其设置为动画
label = QLabel(window)
label.setMovie(movie)

# 设置动画循环次数为 3，然后开始播放动画
movie.start()
loop_count = 0

def on_frame_changed(frame):
    global loop_count

    print(frame)
    # 检查当前帧是否为最后一帧
    if frame == movie.frameCount() - 1:
        loop_count += 1

        # 检查循环次数是否达到预设次数，如果达到则停止动画
        if loop_count >= 3:
            movie.setPaused(True)


# 连接 QMovie 的帧变化信号
movie.frameChanged.connect(on_frame_changed)

window.show()
app.exec()