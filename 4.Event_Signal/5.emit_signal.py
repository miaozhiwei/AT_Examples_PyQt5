import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    # 创建信号，信号会在鼠标按下的时候触发
    close_app = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.c = Communicate()
        self.c.close_app.connect(self.close)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.close_app.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
