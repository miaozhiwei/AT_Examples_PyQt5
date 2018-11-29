import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        lcd = QLCDNumber(self)
        # 默认：0 ~ 99
        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(1, 100)

        v_box = QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(sld)

        self.setLayout(v_box)

        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('LCD Number')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
