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
        backward = QAction("<----",self)
        backward.triggered.connect(self.browser.reload)
        navbar.addAction(backward)
        forward = QAction("---->",self)
        forward.triggered.connect(self.browser.reload)
        navbar.addAction(forward )
        rel_btn = QAction("⟳",self)
        rel_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rel_btn)
        self.search = QLineEdit()
        self.search.returnPressed.connect(self.engine)
        navbar.addWidget(self.search)
        self.browser.urlChanged.connect(self.status)

    def engine(self):
        request = self.search.text()
        if request[0-5] != "https":
            print("Sorry duck duck go toolbar is still in the works")
        elif request[0-4] != "http":
            print("Sorry duck duck go toolbar is still in the works")
        self.browser.setUrl(QUrl(request))

    def status(self, where):
        self.search.setText(where.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Pybrowse")
window = Windows()
app.exec()
