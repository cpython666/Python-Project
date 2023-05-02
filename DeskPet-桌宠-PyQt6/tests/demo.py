from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("鼠标悬停显示提示框")
        self.message_box = QLabel(self)


    def mouseMoveEvent(self, event):
        self.message_box.setText("鼠标悬停在窗口中！")
        # self.message_box.show()
        # message_box.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()