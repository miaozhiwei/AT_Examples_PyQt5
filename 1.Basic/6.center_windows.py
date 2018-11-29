import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(200, 100)
        # 调用居中方法：
        self.set_center()
        self.setWindowTitle('Center')
        self.show()

    def set_center(self):
        # 获取主窗口大小：qr = PyQt5.QtCore.QRect(0, 0, 199, 99)
        qr = self.frameGeometry()
        # QDesktopWidget提供了用户的桌面信息，包括屏幕的大小：cp = PyQt5.QtCore.QPoint(682, 363)
        cp = QDesktopWidget().availableGeometry().center()
        # 窗口移动
        qr.moveCenter(cp)
        # 把窗口的左上角的坐标设置为qr的矩形左上角的坐标
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
