import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        exit_act = QAction(QIcon('exit.png'), '&Exit', self)
        file_menu.addAction(exit_act)

        # 添加属性
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit the App')
        # 三种关闭方式均支持
        # exit_act.triggered.connect(qApp.quit)
        # exit_act.triggered.connect(qApp.exit)
        exit_act.triggered.connect(self.close)

        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main Window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
