import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 设置提示框字体，覆盖默认字体
        QToolTip.setFont(QFont('SansSerif', 15))
        # 鼠标停留窗口，查看提示效果。
        self.setToolTip('This is a <b>QWidget</b> Widget')

        btn = QPushButton('Button', self)
        # 鼠标停留按钮上，查看提示效果。
        btn.setToolTip('This is a <b>QPushButton</b> Widget')
        # sizeHint()方法提供了一个默认的按钮大小
        btn.resize(btn.sizeHint())
        btn.move(100,200)

        self.setGeometry(300, 100, 800, 400)
        self.setWindowTitle('ToolTips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
