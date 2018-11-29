import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):
        # 提示窗口标题 + 提示内容 + 选项1 & 选项2 + 默认选项
        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
