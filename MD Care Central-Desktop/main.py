import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.superadminHome import *
from Pages.superadmin.Doctor import *
from Pages.superadmin.Hospital import *
from Pages.superadmin.BloodBank import *
from  Pages.superadmin.Events import *
import sys
from Pages.loginPage import *
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MDTouch")
        self.loginpage = loginPage()
        self.superadmin_home = superadminHome()
        self.doctor_home = Doctor()
        self.hospital_home = Hospital()
        self.event_home = Events()
        self.blood_home = BloodBank()
        self.loginpage.setup(self)
        # self.bloodbank = Ui_MainWindow()
        # self.bloodbank.setupUi(self)
        #self.showFullScreen()
        self.shortcutQuit = QShortcut(QKeySequence(self.tr("Alt+C")), self)
        self.shortcutQuit.activated.connect(self.close)
        self.shortcutQuit.setEnabled(True)
        self.showFullScreen()
        # self.setFixedSize(1540,915)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_pix = QPixmap('Images/splash_screen.jpg')
    splash_pix = splash_pix.scaled(800,600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(100)
    progressBar.setTextVisible(True)
    progressBar.setAlignment(Qt.AlignCenter)
    progressBar.setGeometry(20, splash_pix.height() - 50, splash_pix.width() - 40, 20)
    css = """
QProgressBar{
    border: 2px solid grey;
    color:black;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: green;
    width: 10px;
}
"""
    progressBar.setStyleSheet(css)
    splash.show()

    for i in range(1, 101):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.0001:
            app.processEvents()
    time.sleep(1)
    window = MainWindow()
    splash.finish(window)
    sys.exit(app.exec())
