import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        line = QLineEdit(self)
        line.textChanged[str].connect(self.on_changed)
        line.move(60, 40)

        self.label = QLabel(self)
        self.label.move(60, 100)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QLineEdit')
        self.show()

    def on_changed(self, text):
        self.label.setText(text)
        # adjustSize()方法让标签自适应文本内容
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
