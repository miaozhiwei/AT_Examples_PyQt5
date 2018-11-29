import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 创建状态栏对象
        status_bar = self.statusBar()
        # 显示出来
        status_bar.showMessage('Status: Ready')

        # 主窗口属性
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Status Bar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
