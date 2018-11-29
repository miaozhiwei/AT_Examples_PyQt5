import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.btn = QPushButton('Click Me', self)
        self.btn.clicked.connect(self.show_dialog)

        self.line_edit = QLineEdit(self)

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        grid.addWidget(self.btn, 0, 0)
        grid.addWidget(self.line_edit, 0, 1)

        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Input Dialog')
        self.show()

    def show_dialog(self):
        # 第一个参数是输入框的标题，第二个参数是输入框的占位符。
        text, ok = QInputDialog.getText(self, 'Tips', 'Enter Something:')
        if ok:
            self.line_edit.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
