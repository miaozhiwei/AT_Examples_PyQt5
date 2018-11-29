import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        # 定义栅格
        grid = QGridLayout()
        # 栅格元素间隔
        grid.setSpacing(10)

        # QGridLayout::addWidget ( QWidget * widget, int row, int column, Qt::Alignment alignment = 0 )
        # 行，列，占用行数，占用列数，对齐方式
        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 2, 1)

        self.setLayout(grid)

        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle('Layout Demo')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
