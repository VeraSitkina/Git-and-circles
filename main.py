# -*- coding: utf-8 -*-
import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtGui


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Круги')
        self.pushButton.clicked.connect(self.draw)
        
    def draw(self):
        self.flag = True
        self.update()
        
    def paint(self, event):
        if self.flag:
            p = QPainter(self)
            p.begin(self)
            self.drawFlag(p)
            p.end()
            
    def drawFlag(self, p):
        self.size = randint(10, 60)
        p.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        p.drawEllipse(randint(0, self.size), randint(0, (600 - self.size)),
                      self.size, self.size)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())