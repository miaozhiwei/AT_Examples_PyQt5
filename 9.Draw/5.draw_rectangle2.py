import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


# 9个有渐变纹理的矩形
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Draw Rectangle2')
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_brush(p)
        p.end()

    def draw_brush(self, p):

        # 1
        brush = QBrush(Qt.SolidPattern)
        p.setBrush(brush)
        p.drawRect(10, 15, 90, 60)

        # 2
        brush.setStyle(Qt.Dense1Pattern)
        p.setBrush(brush)
        p.drawRect(130, 15, 90, 60)

        # 3
        brush.setStyle(Qt.Dense2Pattern)
        p.setBrush(brush)
        p.drawRect(250, 15, 90, 60)

        # 4
        brush.setStyle(Qt.DiagCrossPattern)
        p.setBrush(brush)
        p.drawRect(10, 105, 90, 60)

        # 5
        brush.setStyle(Qt.Dense5Pattern)
        p.setBrush(brush)
        p.drawRect(130, 105, 90, 60)

        # 6
        brush.setStyle(Qt.Dense6Pattern)
        p.setBrush(brush)
        p.drawRect(250, 105, 90, 60)

        # 7
        brush.setStyle(Qt.HorPattern)
        p.setBrush(brush)
        p.drawRect(10, 195, 90, 60)

        # 8
        brush.setStyle(Qt.VerPattern)
        p.setBrush(brush)
        p.drawRect(130, 195, 90, 60)

        # 9
        brush.setStyle(Qt.BDiagPattern)
        p.setBrush(brush)
        p.drawRect(250, 195, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
