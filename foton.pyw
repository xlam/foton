# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from fotonwindow import FotonWindow

def main():
	app = QtGui.QApplication(sys.argv)
	foton = FotonWindow()
	foton.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
