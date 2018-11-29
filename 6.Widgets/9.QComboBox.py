import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout(self)
        self.setLayout(grid)

        self.label = QLabel('Joseph', self)
        grid.addWidget(self.label, 0, 0)

        combo = QComboBox(self)
        combo.addItem('Joseph')
        combo.addItem('Tony')
        combo.addItem('Mark')
        grid.addWidget(combo, 0, 1)
        combo.activated[str].connect(self.on_activated)

        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('QComboBox')
        self.show()

    def on_activated(self, str):
        self.label.setText(str)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
