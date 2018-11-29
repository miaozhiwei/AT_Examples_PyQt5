import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


# 通过画图方式将文字显示出来，含字体、颜色。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 定义文字，后面通过paintEvent方法绘制有颜色和字体的文字。
        self.text = 'Hello World'

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Draw Text')

    def paintEvent(self, event):

        painter = QPainter()

        painter.begin(self)
        self.draw_text(event, painter)
        painter.end()

    def draw_text(self, event, p):
        # 定义笔和字体
        p.setPen(QColor(100, 255, 100))
        p.setFont(QFont('Calibri', 18))
        # drawText()方法在窗口里绘制文本，rect()方法返回要更新的矩形区域。
        p.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
