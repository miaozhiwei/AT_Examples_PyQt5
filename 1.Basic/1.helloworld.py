import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':

    # 所有的PyQt5应用必须创建一个应用（Application）对象
    # sys.argv参数是一个来自命令行的参数列表
    app = QApplication(sys.argv)

    # Qwidget组件是PyQt5中所有用户界面类的基础类
    w = QWidget()

    # 调整了widget组件的大小
    w.resize(250, 250)

    # 移动widget组件到一个位置
    w.move(500,100)

    # 设置窗口标题
    w.setWindowTitle('HelloWorld')

    # 在屏幕上显示widget, 一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
    w.show()

    # 确保一个不留垃圾的退出
    sys.exit(app.exec_())
