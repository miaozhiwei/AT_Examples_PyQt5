import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QPen')
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_line(p)
        p.end()

    def draw_line(self, p):

        # 预定义样式1
        pen = QPen(Qt.black, 5, Qt.SolidLine)
        p.setPen(pen)
        # 起止点（start end）
        p.drawLine(20, 40, 250, 40)

        # 预定义样式2
        pen.setStyle(Qt.DashLine)
        p.setPen(pen)
        p.drawLine(20, 80, 250, 80)

        # 预定义样式3
        pen.setStyle(Qt.DashDotLine)
        p.setPen(pen)
        p.drawLine(20, 120, 250, 120)

        # 预定义样式4
        pen.setStyle(Qt.DotLine)
        p.setPen(pen)
        p.drawLine(20, 160, 250, 160)

        # 预定义样式5
        pen.setStyle(Qt.DashDotDotLine)
        p.setPen(pen)
        p.drawLine(20, 200, 250, 200)

        # 自定义样式
        pen.setStyle(Qt.CustomDashLine)
        # 1像素线，4像素空格，5像素线，4像素空格
        pen.setDashPattern([1, 4, 5, 4])
        p.setPen(pen)
        p.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
