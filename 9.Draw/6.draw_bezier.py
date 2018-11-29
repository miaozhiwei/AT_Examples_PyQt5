import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt


# 贝赛尔曲线
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Draw Bezier')
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        self.draw_bezier(p)
        p.end()

    def draw_bezier(self, p):

        path = QPainterPath()
        path.moveTo(30, 30)
        # 起始点 控制点 终止点
        path.cubicTo(30, 30, 200, 350, 350, 30)

        p.drawPath(path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
