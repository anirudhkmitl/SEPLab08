import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100),QPoint(100,150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon(
            [QPoint(50,200),QPoint(150,200),QPoint(100,400),]
            )
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        super().__init__()
        

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,22),QPoint(100,110),
            QPoint(25,100),QPoint(100,150),
            ])

        p.setPen(QColor(255,121,0))
        p.setBrush(QColor(124,127,0))
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()


class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.sun = QPixmap("sun.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100),QPoint(100,150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon(
            [QPoint(50,200),QPoint(150,200),QPoint(100,400),]
            )
        p.drawPixmap(QRect(200,100,320,320),self.sun)
        p.end()
        
class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        #QWidget.__init__(self, None)
        super().__init__()

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(215,85,85))
        p.setBrush(QColor(0,127,255))
        p.drawPolygon([
            QPoint(150,100),QPoint(120,110),
            QPoint(130,170),QPoint(60,150),
            ])
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()

    #w = Simple_drawing_window()
    w3 = Simple_drawing_window3()
    
    #w.show()
    w3.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

