import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        cb = QCheckBox('Show Title', self)
        cb.move(50, 50)
        # 设置复选框默认选中状态
        cb.toggle()
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Check Box')
        self.show()

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('Check Box')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
