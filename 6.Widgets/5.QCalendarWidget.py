import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        vbox = QVBoxLayout(self)
        self.setLayout(vbox)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.show_date)
        vbox.addWidget(cal)

        self.line = QLineEdit(self)
        date = cal.selectedDate()
        self.line.setText(date.toString(Qt.DefaultLocaleShortDate))
        vbox.addWidget(self.line)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Calender Widget')
        self.show()

    def show_date(self, date):
        # 显示选中的时间格式化
        self.line.setText(date.toString(Qt.DefaultLocaleShortDate))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
