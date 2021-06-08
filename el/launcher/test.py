import sys
import os
from PySide6 import QtWidgets



class TestWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.create_widget()
        self.create_layout()
        self.create_connection()

    def create_widget(self):
        self.btn = QtWidgets.QPushButton('Click me')


    def create_layout(self):
        main_layout =  QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.btn)

    def create_connection(self):
        self.btn.clicked.connect(self.hello)

    def hello(self):
        h = os.getcwd()
        print(h)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = TestWindow()
    win.show()

    sys.exit(app.exec())