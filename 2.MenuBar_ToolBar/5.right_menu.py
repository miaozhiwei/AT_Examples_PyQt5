import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Right Menu')
        self.show()

    # contextMenuEvent定义右键菜单，修改方法名会导致右键菜单不可用。
    def contextMenuEvent(self, event):
        q_menu = QMenu(self)
        about_act = q_menu.addAction('About')
        quit_act = q_menu.addAction('Quit')
        # exec_()方法显示菜单
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口的绝对坐标
        action = q_menu.exec_(self.mapToGlobal(event.pos()))

        if action == about_act:
            qApp.aboutQt()

        if action == quit_act:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
