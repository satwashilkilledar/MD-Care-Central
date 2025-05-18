import math, sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *


class Overlay(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(16):
            if (self.counter / 2) % 16 == i:
                painter.setBrush(QBrush(QColor(0,0,0)))
            else:
                painter.setBrush(QBrush(QColor(127,127,127)))
            painter.drawEllipse(
                self.width() / 2 + 30 * math.cos(2 * math.pi * i / 16.0),
                self.height() / 2 + 30 * math.sin(2 * math.pi * i / 16.0),
                5, 5)

        painter.end()

    def showEvent(self, event):
        self.timer = self.startTimer(50)
        self.counter = 0
        self.show()

    def timerEvent(self, event):

        self.counter += 1
        self.update()
        if self.counter == 60:
            self.killTimer(self.timer)
            self.hide()


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setPlainText("  sample_text   filler_text  " * 100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        button = QPushButton("Wait")
        layout.addWidget(button, 1, 1, 1, 1)
        button2 = QPushButton("OK")
        layout.addWidget(button2, 1, 2, 1, 1)

        self.setCentralWidget(widget)
        self.overlay = Overlay(self.centralWidget())
        self.overlay.hide()
        button.clicked.connect(self.overlay.show)
        button2.clicked.connect(lambda : self.editor.setPlainText("  OK PRESSED  "))

    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())