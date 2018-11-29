import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 创建菜单对象
        menu_bar = self.menuBar()

        # 创建主菜单（有下级菜单）：File
        file_menu = menu_bar.addMenu('File')

        # 创建一级菜单（无下级菜单）：New
        new_act = QAction('New', self)
        file_menu.addAction(new_act)

        # 创建一级菜单（有下级菜单）：Import
        # 加& 可以快捷访问到对应菜单
        imp_menu = QMenu('&Import', self)
        file_menu.addMenu(imp_menu)

        # 创建二级菜单（无下级菜单）：Import mail
        imp_act = QAction('Import mail', self)
        imp_menu.addAction(imp_act)

        # 主窗口属性
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Sub Menu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
