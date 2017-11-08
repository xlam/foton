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
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        dock = QtGui.QDockWidget(self)
        dock.setWidget(self.imagesTable)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        hbox.addWidget(QtGui.QPushButton('Button 1'))
        hbox.addWidget(QtGui.QPushButton('Button 2'))
        vbox.addLayout(hbox)
        widget.setLayout(vbox)

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
            return QtGui.QColor(120, 0, 0)
        if img.status == image.STATUS_PARTIAL:
            return QtGui.QColor(120, 120, 0)
        if img.status == image.STATUS_FULL:
            return QtGui.QColor(0, 120, 0)
