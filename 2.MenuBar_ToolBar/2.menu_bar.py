import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 创建菜单对象
        menu_bar = self.menuBar()

        # 创建主菜单（有下级菜单）：File
        file_menu = menu_bar.addMenu('File')

        # 创建一级菜单（无下级菜单）：Exit
        exit_act = QAction(QIcon('exit.png'), 'Exit', self)
        file_menu.addAction(exit_act)
        # 键盘快捷键
        exit_act.setShortcut('Ctrl+Q')
        # 状态栏显示
        exit_act.setStatusTip('Exit the App')
        # 触发退出方法
        exit_act.triggered.connect(qApp.quit)

        # 创建状态栏对象
        self.statusBar()

        # 主窗口属性
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu Bar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
