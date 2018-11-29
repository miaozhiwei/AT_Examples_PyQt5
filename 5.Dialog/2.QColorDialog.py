import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog, QGridLayout
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        # 设置默认颜色
        init_color = QColor(0, 0, 0)

        self.btn = QPushButton('Click Me to Change Color', self)
        self.btn.clicked.connect(self.show_dialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget { background-color: %s }" % init_color.name())

        grid.addWidget(self.btn, 0, 0)
        grid.addWidget(self.frame, 1, 0)
        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Color Dialog')
        self.show()

    def show_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
