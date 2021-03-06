import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5 import uic
from ui import Ui_Form

from random import randint


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
    
    def paint(self):
        self.do_paint = True
        self.repaint()
    
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_balls(qp)
            qp.end()

    def draw_balls(self, qp):
        for _ in range(randint(10, 50)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(randint(120, 200), randint(30, 200), randint(30, 100), randint(30, 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())