import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):

        # super()构造器方法返回父级的对象
        # __init__()方法是构造器的一个方法
        super().__init__()
        # 使用init_ui()方法创建一个GUI。
        self.init_ui()

    def init_ui(self):

        # 屏幕坐标的x、y和窗口大小的宽高
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('QMC.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
