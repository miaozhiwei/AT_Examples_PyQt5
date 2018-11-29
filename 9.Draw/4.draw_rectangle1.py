import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


# 三个有颜色的矩形
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Draw Rectangle1')
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_rectangle(p)
        p.end()

    def draw_rectangle(self, p):

        # 设置画笔
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        p.setPen(col)

        # 画矩形
        p.setBrush(QColor(200, 0, 0))
        p.drawRect(10, 15, 90, 60)

        p.setBrush(QColor(255, 80, 0))
        p.drawRect(130, 15, 90, 60)

        p.setBrush(QColor(125, 0, 90))
        p.drawRect(250, 15, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
