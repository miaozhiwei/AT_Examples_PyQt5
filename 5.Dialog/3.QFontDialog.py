import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        btn = QPushButton('Click Me to Change Font', self)
        # 适配按钮上的文字
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(self.show_dialog)
        grid.addWidget(btn, 0, 0)

        self.label = QLabel('Hello World', self)
        grid.addWidget(self.label, 1, 0)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Font Dialog')
        self.show()

    def show_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
