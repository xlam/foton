# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class Scene(QtGui.QGraphicsScene):

    def __init__(self, parent=None):
        super(Scene, self).__init__(parent)

        self.setSceneRect(QtCore.QRectF(0, 0, 800, 600))

    def dragLeaveEvent(self, event):
        print('Scene.dragLeaveEvent: {}'.format(event))

    def dropEvent(self, event):
        print('Scene.dropEvent: {}'.format(event))

    def dragMoveEvent(self, event):
        print('Scene.dragMoveEvent: {}'.format(event))


class View(QtGui.QGraphicsView):

    def __init__(self, scene):
        super(View, self).__init__(scene)

        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setRenderHint(QtGui.QPainter.Antialiasing)

    def wheelEvent(self, event):
        factor = 1.4 ** (-event.delta() / 240.0)
        self.scale(factor, factor)
        print('View.wheelEvent: {}'.format(event))
