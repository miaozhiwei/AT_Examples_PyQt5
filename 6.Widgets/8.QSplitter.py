import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        h_box = QHBoxLayout(self)
        self.setLayout(h_box)

        top_left = QFrame(self)
        # 使用子窗口模式，让显示更清晰。
        top_left.setFrameShape(QFrame.StyledPanel)

        top_right = QFrame(self)
        top_right.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 分割线 1，连接左右。
        splitter_1 = QSplitter(Qt.Horizontal)
        splitter_1.addWidget(top_left)
        splitter_1.addWidget(top_right)

        # 分割线 2，连接上下。
        splitter_2 = QSplitter(Qt.Vertical)
        splitter_2.addWidget(splitter_1)
        splitter_2.addWidget(bottom)
        h_box.addWidget(splitter_2)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
