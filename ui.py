import os
import sys
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cv2
import numpy as np
import pandas as pd
import copy
form_class = uic.loadUiType('UI.ui')[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.buttonFileOpen.clicked.connect(self.loadDataset)
        self.buttonRefresh.clicked.connect(self.refreshTable)
        self.buttonDrop.clicked.connect(self.dropColumn)
        self.buttonSetLabel.clicked.connect(self.setLabel)
        self.df_origin = None

    def loadDataset(self):
        print("1")
        f = QFileDialog.getOpenFileName(self)
        self.df = pd.read_csv(f[0])
        self.df_origin = copy.deepcopy(self.df)
        self.loadDatasetTable(self.df)

    def loadDatasetTable(self, df):
        self.tableDataset.setColumnCount(len(df.columns))
        self.tableDataset.setRowCount(len(df.index))
        self.tableDataset.setHorizontalHeaderLabels(df.keys())
        for i in range(0, len(df.index)):
            for j in range(0, len(df.columns)):
                self.tableDataset.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def dropColumn(self):
        dropColumnName = str(self.tableDataset.horizontalHeaderItem(self.tableDataset.currentColumn()).text())
        self.df = self.df.drop([dropColumnName], axis=1)
        self.loadDatasetTable(self.df)

    def refreshTable(self):
        self.df = self.df_origin
        self.loadDatasetTable(self.df)

    def setLabel(self):
        labelColumnName = str(self.tableDataset.horizontalHeaderItem(self.tableDataset.currentColumn()).text())
        print("label : {}".format(labelColumnName))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('ML')
    window.show()
    sys.exit(app.exec_())