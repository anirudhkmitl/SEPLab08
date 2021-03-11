import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()