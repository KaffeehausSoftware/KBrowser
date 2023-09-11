import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from darktheme.widget_template import DarkApplication, DarkPalette

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowIcon(QIcon('/home/kappa/KaffeehausSoftware/KaffeehausWebBrowser/icon.png'))

		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()

		# menubar
		menubar = QToolBar()
		self.addToolBar(Qt.LeftToolBarArea, menubar)

		homeBtn = QAction("Home", self)
		homeBtn.triggered.connect(self.navigate_home)
		menubar.addAction(homeBtn)

		backBtn = QAction("Back", self)
		backBtn.triggered.connect(self.browser.back)
		menubar.addAction(backBtn)

		forwardBtn = QAction("Forward", self)
		forwardBtn.triggered.connect(self.browser.forward)
		menubar.addAction(forwardBtn)

		reloadBtn = QAction("Reload", self)
		reloadBtn.triggered.connect(self.browser.reload)
		menubar.addAction(reloadBtn)

		makersBtn = QAction("Makers", self)
		makersBtn.triggered.connect(self.makers)
		menubar.addAction(makersBtn)

		# navbar

		navbar = QToolBar()
		self.addToolBar(Qt.BottomToolBarArea, navbar)

		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate)
		navbar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url)

	def navigate_home(self):
		self.browser.setUrl(QUrl('http://google.com'))

	def navigate(self):
		URL = self.url_bar.text()
		self.browser.setUrl(QUrl(URL))

	def update_url(self, URL):
		self.url_bar.setText(URL.toString())

	def makers(self):
		self.browser.setUrl(QUrl('https://kaffeehaussoftware.github.io'))

app = QApplication(sys.argv)
app.setPalette(DarkPalette())

QApplication.setApplicationName('Kaffeehaus Browser')
window = MainWindow()

app.exec_()