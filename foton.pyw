# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from os import path
from fotonwindow import FotonWindow

def main():
    QtCore.QCoreApplication.addLibraryPath(path.join(path.dirname(QtCore.__file__), "plugins"))
    app = QtGui.QApplication(sys.argv)
    foton = FotonWindow()
    foton.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
