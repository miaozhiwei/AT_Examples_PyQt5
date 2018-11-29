import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        menu_bar = self.menuBar()

        # 菜单：View - 无self参数
        view_menu = menu_bar.addMenu('View')

        # 菜单：ViewStatusBar - 有self参数
        view_stat_act = QAction('ViewStatusBar', self)
        view_menu.addAction(view_stat_act)

        # 菜单属性
        view_stat_act.setStatusTip('View Status Bar')
        view_stat_act.setCheckable(True)
        view_stat_act.setChecked(True)
        view_stat_act.triggered.connect(self.toggle_menu)

        # 基本属性
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check Menu')
        self.show()

    def toggle_menu(self, state):
        status_bar = self.statusBar()
        if state:
            status_bar.hide()
        else:
            status_bar.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
