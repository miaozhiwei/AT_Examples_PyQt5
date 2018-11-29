import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        # 在一个组件里显示鼠标的X和Y坐标
        self.text = 'x:{0}, y:{0}'.format(x, y)
        # QLabel提供一个文本或图像的显示，没有提供用户交互功能。
        self.lable = QLabel(self.text, self)
        grid.addWidget(self.lable, 0, 0, Qt.AlignTop)

        # 鼠标追踪默认没有开启，当有鼠标点击事件发生后才会开启。
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Event Object')
        self.show()

    def mouseMoveEvent(self, e):
        # e代表事件对象，此处获取xy坐标
        x = e.x()
        y = e.y()
        text = 'x:{0}, y:{0}'.format(x, y)
        self.lable.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
