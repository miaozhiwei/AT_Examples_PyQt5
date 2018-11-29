import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        h_box = QHBoxLayout(self)
        self.setLayout(h_box)

        # 其他格式可能无法显示，尽量使用png格式。
        pix_map = QPixmap('QMC.png')

        label = QLabel(self)
        label.setPixmap(pix_map)
        h_box.addWidget(label)

        # 不设置尺寸，以图片实际尺寸为准显示。
        # self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QPixmap')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
