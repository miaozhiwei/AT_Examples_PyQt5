import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QLCDNumber, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        lcd = QLCDNumber(self)
        grid.addWidget(lcd, 0, 0)

        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setRange(0, 100)
        slider.valueChanged.connect(lcd.display)
        slider.valueChanged[int].connect(self.change_value)
        grid.addWidget(slider, 1, 0)

        self.label = QLabel(self)
        # QPixmap是处理图片的组件
        self.label.setPixmap(QPixmap('voice_mute.png'))
        grid.addWidget(self.label, 1, 1)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QSlider')
        self.show()

    def change_value(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('voice_mute.png'))
        else:
            self.label.setPixmap(QPixmap('voice_max.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
