# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from version import version
import image
import util
import scene


class FotonWindow(QtGui.QMainWindow):

    def __init__(self):
        super(FotonWindow, self).__init__(parent=None)
        self.setWindowTitle('Foton (v' + version() + ')')
        self.resize(800, 600)
        self.statusBar().showMessage('Готов')
        self.setupMenu()
        self.imagesTable = QtGui.QTableWidget()
        self.currentIdLabel = QtGui.QLabel()
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)

        dock = QtGui.QDockWidget(self)
        dock.setWidget(self.imagesTable)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

        self.scene = scene.Scene()
        self.scene.setSceneRect(QtCore.QRectF(0, 0, 800, 600))
        self.view = QtGui.QGraphicsView(self.scene)

        self.currentIdLabel.setText('Номер точки: <не выбрано>')

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.view)
        hbox.addStretch()
        vbox.addWidget(self.currentIdLabel)
        hboxIds = QtGui.QHBoxLayout()
        for i in range(6):
            b = QtGui.QPushButton(str(i + 1))
            b.clicked.connect(self.idButtonClick)
            hboxIds.addWidget(b)
        vbox.addLayout(hboxIds)
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()
        widget.setLayout(vbox)
        self.imagesTable.currentCellChanged.connect(self.imageChanged)
        self.workingDir = os.getcwd()
        self.currentImage = None
        self.qtImage = None
        self.images = None

    def idButtonClick(self):
        text = self.sender().text()
        self.currentIdLabel.setText('Номер точки: ' + text)

    def imageChanged(self, row, col, oldRow, oldCol):
        item = self.imagesTable.item(row, image.NAME)
        img = self.images.image(item.data(QtCore.Qt.UserRole))
        if img == self.currentImage:
            return
        path = self.workingDir + os.sep + img.name
        self.qtImage = QtGui.QImage(path)
        pixmap = QtGui.QPixmap.fromImage(self.qtImage)
        print('Loading image: {} ({}x{})'.format(
            path, str(pixmap.width()), str(pixmap.height())))
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        # self.scene.setSceneRect(p.boundingRect())
        for id, coords in img.annotations():
            self.drawPoint(int(coords[0]), int(coords[1]))
        self.currentImage = img

    def draw(self, event):
        print('image clicked at pos ({};{})'.format(event.pos().x(), event.pos().y()))
        self.drawPoint(event.pos().x(), event.pos().y())

    def drawPoint(self, x, y):
        e = self.scene.addEllipse(x, y, 10, 10)
        e.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        e.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

    def setupMenu(self):
        menu = QtGui.QMenu('Файл', self)
        self.menuBar().addMenu(menu)
        self.actionOpen = QtGui.QAction('Выбрать каталог', self)
        self.actionSave = QtGui.QAction('Сохранить', self)
        self.actionExport = QtGui.QAction('Экспорт в JSON', self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionExport.triggered.connect(self.fileExport)
        menu.addAction(self.actionOpen)
        menu.addAction(self.actionSave)
        menu.addAction(self.actionExport)

    def fileOpen(self):
        imagesDir = QtGui.QFileDialog.getExistingDirectory(
            None,
            'Выбор каталога с изображениями',
            '')
        self.workingDir = imagesDir
        self.images = util.scanDirForImages(imagesDir)
        self._populateImagesTable(self.images)

    def fileSave(self):
        filename = QtGui.QFileDialog.getSaveFileName(
            None,
            'Сохранить',
            os.getcwd())
        if(filename):
            self.images.saveToPickle(filename)

    def fileExport(self):
        pass

    def _populateImagesTable(self, images):
        self.imagesTable.clear()
        self.imagesTable.setSortingEnabled(False)
        self.imagesTable.setRowCount(len(images))
        headers = ['Статус', 'Имя']
        self.imagesTable.setColumnCount(len(headers))
        self.imagesTable.setHorizontalHeaderLabels(headers)
        for row, img in enumerate(images):
            color = self.itemColor(img)
            item = QtGui.QTableWidgetItem(image.STATUS_STR[str(img.status())])
            item.setTextColor(color)
            self.imagesTable.setItem(row, image.STATUS, item)
            item = QtGui.QTableWidgetItem(img.name)
            item.setData(QtCore.Qt.UserRole, int(id(img)))
            item.setTextColor(color)
            self.imagesTable.setItem(row, image.NAME, item)
        self.imagesTable.setSortingEnabled(True)
        # resize

    def itemColor(self, img):
        if img.status() == image.STATUS_EMPTY:
            return QtGui.QColor(200, 0, 0)
        if img.status() == image.STATUS_PARTIAL:
            return QtGui.QColor(0, 0, 200)
        if img.status() == image.STATUS_FULL:
            return QtGui.QColor(0, 200, 0)
