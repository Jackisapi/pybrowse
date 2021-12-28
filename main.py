import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class Windows(QMainWindow):
   #Base browser
    def __init__(self):
        super(Windows, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
       #nav bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction("<--", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        fow_btn = QAction("-->",self)
        fow_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fow_btn)
        rel_btn = QAction("⟳",self)
        rel_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rel_btn)

app = QApplication(sys.argv)
QApplication.setApplicationName("Pybrowse")
window = Windows()
app.exec()