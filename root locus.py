#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np
import control

from PyQt4.QtGui import QMainWindow, QSizePolicy, \
        QPushButton, QApplication, QPainter, QFont, QWidget

from PyQt4.QtCore import SIGNAL, QSettings, QRect, QPoint, QVariant, QFileInfo, QTimer, pyqtSignal, QObject

class First(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QtGui.QPushButton("Root Locus")
        self.setCentralWidget(self.pushButton)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        self.pushButton.clicked.connect(self.plot)
        self.dialogs = list()

    def plot(self):
        G = control.TransferFunction((1, 1.5), (1, 11, 10, 0))
        kvect=np.linspace(100.0, -100.0, num=1000)
        rlist, klist = control.rlocus(G, kvect)
        plt.title('Root Locus')
        plt.grid()
        plt.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()