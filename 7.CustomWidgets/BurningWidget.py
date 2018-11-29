from PyQt5.QtWidgets import QWidget, QSlider, QApplication, QLCDNumber, QGridLayout
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen
import sys


class Communicate(QObject):
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 自定义进度条的最小高度
        self.setMinimumSize(1, 100)
        # 默认值
        self.value = 0
        # 刻度
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def set_value(self, value):
        self.value = value

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.draw_widget(qp)
        qp.end()

    def draw_widget(self, qp):

        MAX_CAPACITY = 600
        OVER_CAPACITY = 750

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))

        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        lcd = QLCDNumber(self)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        # 范围
        sld.setRange(0, 750)
        # 默认值
        sld.setValue(0)
        sld.valueChanged.connect(lcd.display)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.set_value)
        sld.valueChanged[int].connect(self.change_value)

        grid = QGridLayout()
        grid.addWidget(lcd, 1, 0)
        grid.addWidget(sld, 2, 0)
        grid.addWidget(self.wid, 3, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 400, 220)
        self.setWindowTitle('Burning Widget')
        self.show()

    def change_value(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())