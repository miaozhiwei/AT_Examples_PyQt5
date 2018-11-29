import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        btn1 = QPushButton('Button 1', self)
        btn2 = QPushButton('Button 2', self)
        btn1.clicked.connect(self.btn_clicked)
        btn2.clicked.connect(self.btn_clicked)

        btn1.move(50, 50)
        btn2.move(150, 50)

        self.statusBar()

        self.setWindowTitle('Event Sender')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def btn_clicked(self):
        # 调用sender()方法的方式决定了事件源
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
