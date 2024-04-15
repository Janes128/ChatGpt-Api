import sys, os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

from star_sign_helper import StarSignHelper
from ui_star_sign import Ui_MainWindow

class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.htmlview = QWebEngineView()

        # Link widget connections
        self.ui.pushButton.clicked.connect(self.btn_test)

        # Init the StarSignHelper
        self.helper = StarSignHelper()
        
    def viewhtml(self, html):
        self.htmlview.setHtml(html)
        self.ui.vbox.addWidget(self.htmlview)
        self.ui.groupBox_Output.setLayout(self.ui.vbox)
        self.ui.groupBox_Output.show()

    def btn_test(self):
        print("user information:")
        name = self.ui.lineEdit_NickName.text()
        date = self.ui.lineEdit_BirthDay.text()

        print(name, " | " , date)
        self.helper.generate_output()
        self.viewhtml('''<b>WebView Public Gist</b>''')

if __name__ == '__main__':
    app = QApplication([])
    hb_window = UiMainWindow()
    hb_window.show()
    app.exec()

''' # For star-sign.ui method
if __name__ == '__main__':
    app = QApplication([])

    loader = QUiLoader()
    hb_window = loader.load("star-sign.ui")
    hb_window.show()

    app.exec()
'''
