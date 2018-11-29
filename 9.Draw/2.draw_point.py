import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


# 窗口内随机画 10000 个红点。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Draw Dot')
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_point(p)
        p.end()

    def draw_point(self, point):
        point.setPen(Qt.red)
        # 获取窗口的大小，每次改变大小，会均匀随机画点。
        size = self.size()

        for i in range(10000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            point.drawPoint(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
