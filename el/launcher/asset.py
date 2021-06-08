import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets

from utils.read_dump import read_json

class AssetLauncher(QtWidgets.QWidget):

    def __init__(self):
        super(AssetLauncher, self).__init__(parent=None)

        self.setWindowTitle('Elna Asset Launcher')
        self.setMinimumSize(600,200)


        self.create_widget()
        self.create_layout()
        self.create_connection()

    def create_widget(self):
        self.asset_type = QtWidgets.QComboBox()
        self.asset_type.addItems(['char', 'prop','envi','matte'])

        self.asset = QtWidgets.QComboBox()
        self.asset.addItems(['Mayday'])

        self.build_type = QtWidgets.QComboBox()
        self.build_type.addItems(['Model','zfile','Rig','Animation','Groom','LookDev','CFX','FX'])


        self.update_btn = QtWidgets.QPushButton('Update')


        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.headerItem().setText(0,'File name')

    def create_layout(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('Type', self.asset_type)
        form_layout.addRow('Asset', self.asset)
        form_layout.addRow('Build Type', self.build_type)



        # mainlayout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.update_btn)
        main_layout.addWidget(self.tree_widget)

    def create_connection(self):
        # get asset details
        self.asset_type.currentTextChanged.connect(self.asset_type_changed)
        self.asset.currentTextChanged.connect(self.detail_changed)
        self.build_type.currentTextChanged.connect(self.detail_changed)

        self.update_btn.clicked.connect(self.refresh_tree_widget)


    def refresh_tree_widget(self):

        # clear the iteam in tree widget
        self.tree_widget.clear()
        files = ['model_v001.mb', 'model_v002.mb', 'model_v003.mb']
        for name in files:
            item = self.create_item(name)
            self.tree_widget.addTopLevelItem(item)

    def add_children(self, item):
        pass


    def asset_type_changed(self):
        asset_type = self.asset_type.currentText()
        if asset_type == "prop":
            self.asset.clear()
            self.asset.addItems(['Prop asset'])

        elif asset_type == "char":
            self.asset.clear()
            self.asset.addItems(['char asset'])

        elif asset_type == "envi":
            self.asset.clear()
            self.asset.addItems(['Envi asset'])

        elif asset_type == "matte":
            self.asset.clear()
            self.asset.addItems(['Matte asset'])


    def detail_changed(self):

        pass 

    # create item on the tree widget
    def create_item(self, name):
        item  = QtWidgets.QTreeWidgetItem([name])

        return item



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = AssetLauncher()
    window.show()

    app.exec()