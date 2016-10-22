from PyQt4 import QtGui
import pyqtgraph as pg
import sys
import pyqtgraphutils as pgutils


class TestApp(QtGui.QWidget):
    def initUI(self):
        self.mainLayout = QtGui.QHBoxLayout()
        self.plotui = pg.PlotWidget()

        item = pgutils.LineSegmentItem([10,20], [40,40])
        self.plotui.addItem(item)

        item1 = pgutils.CircleItem([10, 20], 50)
        self.plotui.addItem(item1)

        self.mainLayout.addWidget(self.plotui)
        self.setLayout(self.mainLayout)

    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.initUI()


def main():
    app = QtGui.QApplication(sys.argv)
    w = TestApp()
    w.resize(600, 600)
    w.move(300, 300)
    w.setWindowTitle('Test pyqtgraph')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
