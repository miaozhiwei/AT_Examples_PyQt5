import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 创建两个按钮
        ok_btn = QPushButton('OK')
        cancel_btn = QPushButton('Cancel')

        # Horizontal - 水平
        hbox = QHBoxLayout()
        # stretch函数在两个按钮前面增加了一些弹性空间
        hbox.addStretch(1)
        hbox.addWidget(ok_btn)
        hbox.addWidget(cancel_btn)

        # Vertical - 垂直
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 盒布局生效
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Box Layout')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
