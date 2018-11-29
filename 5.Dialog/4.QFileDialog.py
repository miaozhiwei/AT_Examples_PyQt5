import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTextEdit, QAction, QFileDialog


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.text_edit = QTextEdit()
        # setCentralWidget statusBar 只有在QMainWindow 才可以设置，QWidget下是不可以的。
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction('Open', self)
        open_file.setStatusTip('open new file')
        open_file.triggered.connect(self.show_dialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def show_dialog(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open File', filter='*.txt')
        if f_name[0]:
            f = open(f_name[0], 'r')

            with f:
                data = f.read()
                self.text_edit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
