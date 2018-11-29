import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


# 选中输入框文字，拖拽到按钮上，改变按钮文字。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        edit = QLineEdit('', self)
        # 输入框可拖拽
        edit.setDragEnabled(True)
        edit.move(30, 65)

        btn = Button('Button', self)
        btn.move(190, 65)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Drog and Drop')


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 激活按钮拖拽状态
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        # 设定接受拖拽的数据类型
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        # 更改按钮接受鼠标的释放事件的默认行为
        self.setText(e.mimeData().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
