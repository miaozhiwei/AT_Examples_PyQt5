import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 设置默认颜色：黑色
        self.color = QColor(0, 0, 0)

        btn_red = QPushButton('Red', self)
        # 按钮可切换状态
        btn_red.setCheckable(True)
        btn_red.move(10, 20)
        # 把点击事件转换成布尔值
        btn_red.clicked[bool].connect(self.set_color)

        btn_green = QPushButton('Green', self)
        btn_green.setCheckable(True)
        btn_green.move(10, 70)
        btn_green.clicked[bool].connect(self.set_color)

        btn_blue = QPushButton('Blue', self)
        btn_blue.setCheckable(True)
        btn_blue.move(10, 120)
        btn_blue.clicked[bool].connect(self.set_color)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 120, 120)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.color.name())

        self.setGeometry(300, 300, 300, 180)
        self.setWindowTitle('Togle Button')
        self.show()

    def set_color(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.color.setRed(val)
        elif source.text() == 'Green':
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
