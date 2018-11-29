import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 创建工具栏对象
        toolbar = self.addToolBar('Exit')

        exit_act = QAction('Exit', self)
        toolbar.addAction(exit_act)

        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(qApp.quit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tool Bar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
