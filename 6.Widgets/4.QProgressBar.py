import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # QProgressBar 默认值1 ~ 99
        self.p_bar = QProgressBar(self)
        self.p_bar.setGeometry(30, 40, 225, 25)

        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.do_action)
        self.btn.move(30, 80)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Progress Bar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Start')
            self.step = 0
            return
        self.step = self.step + 1
        self.p_bar.setValue(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
