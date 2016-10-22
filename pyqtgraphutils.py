from PyQt4 import QtGui
from PyQt4 import QtCore
import pyqtgraph as pg


class LineSegmentItem(pg.GraphicsObject):
    def __init__(self, p1, p2):
        pg.GraphicsObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p.drawLine(QtCore.QPoint(self.p1[0], self.p1[1]), QtCore.QPoint(self.p2[0], self.p2[1]))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
