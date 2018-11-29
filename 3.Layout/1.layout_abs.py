import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 绝对定位
        lab1 = QLabel('Joseph', self)
        lab1.move(15, 10)

        lab2 = QLabel('Tony', self)
        lab2.move(35, 40)

        lab3 = QLabel('Luke', self)
        lab3.move(55, 70)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Demo')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
