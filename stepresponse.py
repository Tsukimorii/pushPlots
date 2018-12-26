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
import scipy
from scipy import signal
import control

from PyQt4.QtGui import QMainWindow, QSizePolicy, \
        QPushButton, QApplication, QPainter, QFont, QWidget

from PyQt4.QtCore import SIGNAL, QSettings, QRect, QPoint, QVariant, QFileInfo, QTimer, pyqtSignal, QObject

class First(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QtGui.QPushButton("Step Response")
        self.setCentralWidget(self.pushButton)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        self.pushButton.clicked.connect(self.plot)
        self.dialogs = list()

    def plot(self):
        G = signal.TransferFunction(3, (2,1))
        T, yout = signal.step(G)
        plt.figure(1)
        plt.plot(T,yout)
        plt.title('Step Response')
        plt.grid()
        plt.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()