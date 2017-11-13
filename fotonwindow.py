# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from version import version
import image
import util


class FotonWindow(QtGui.QMainWindow):

    def __init__(self):
        super(FotonWindow, self).__init__(parent=None)
        self.setWindowTitle('Foton (v' + version() + ')')
        self.resize(600, 300)
        self.statusBar().showMessage('Готов')
        self.setupMenu()
        self.imagesTable = QtGui.QTableWidget()
        self.imageLabel = QtGui.QLabel()
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        dock = QtGui.QDockWidget(self)
        dock.setWidget(self.imagesTable)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        hbox.addWidget(self.imageLabel)
        vbox.addLayout(hbox)
        widget.setLayout(vbox)
        self.imagesTable.currentCellChanged.connect(self.showImage)
        self.workingDir = os.getcwd()
        self.currentImageName = ''

    def showImage(self, row, col, oldRow, oldCol):
        nameItem = self.imagesTable.item(row, image.NAME)
        name = nameItem.text()
        if self.currentImageName != name:
            path = self.workingDir + os.sep + name
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(path))
            print('Loading image: {} ({}x{})'.format(path, str(pixmap.width()), str(pixmap.height())))
            self.imageLabel.setPixmap(pixmap)
            self.currentImageName = name
    
    def setupMenu(self):
        menu = QtGui.QMenu('Файл', self)
        self.menuBar().addMenu(menu)
        self.actionOpen = QtGui.QAction('Выбрать каталог', self)
        self.actionOpen.triggered.connect(self.fileOpen)
        menu.addAction(self.actionOpen)

    def fileOpen(self):
        imagesDir = QtGui.QFileDialog.getExistingDirectory(
            self,
            'Выбор каталога с изображениями',
            '')
        self.workingDir = imagesDir
        self._populateImagesTable(util.scanDirForImages(imagesDir))

    def _populateImagesTable(self, images):
        self.imagesTable.clear()
        self.imagesTable.setSortingEnabled(False)
        self.imagesTable.setRowCount(len(images))
        headers = ['Статус', 'Имя']
        self.imagesTable.setColumnCount(len(headers))
        self.imagesTable.setHorizontalHeaderLabels(headers)
        for row, img in enumerate(images):
            color = self.itemColor(img)
            #print('{}\t{} ({} points)'.format(row, img.name, len(img.annotations)))
            item = QtGui.QTableWidgetItem(image.STATUS_STR[str(img.status)])
            item.setTextColor(color)
            self.imagesTable.setItem(row, image.STATUS, item)
            item = QtGui.QTableWidgetItem(img.name)
            item.setTextColor(color)
            self.imagesTable.setItem(row, image.NAME, item)
        self.imagesTable.setSortingEnabled(True)
        # resize

    def itemColor(self, img):
        if img.status == image.STATUS_EMPTY:
            return QtGui.QColor(200, 0, 0)
        if img.status == image.STATUS_PARTIAL:
            return QtGui.QColor(0, 0, 200)
        if img.status == image.STATUS_FULL:
            return QtGui.QColor(0, 200, 0)
