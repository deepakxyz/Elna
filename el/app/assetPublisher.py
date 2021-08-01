import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui




class AssetPublisher(QtWidgets.QWidget):

    def __init__(self):
        super(AssetPublisher, self).__init__(parent =None)

        self.setWindowTitle("Asset Publisher")

        self.setMinimumWidth(700)
        self.setMinimumHeight(450)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
        
    def create_widgets(self):
        self.current_asset_wgt = QtWidgets.QLabel()
        self.asset_type_wgt = QtWidgets.QLabel()
        self.publish_type_cat_wgt = QtWidgets.QComboBox()
        self.publish_sub_cat_wgt = QtWidgets.QComboBox()
        self.filepath_le = QtWidgets.QLineEdit()
        self.select_file_path_btn = QtWidgets.QPushButton()
        self.select_file_path_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        
        
        self.output_log_wget = QtWidgets.QTextBrowser()
        
        self.publish_btn_wgt = QtWidgets.QPushButton('Publish')
        self.cancle_btn_wgt = QtWidgets.QPushButton('Cancle')
        
        self.statusBar_wgt = QtWidgets.QStatusBar()
        
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        
        heading_layout = QtWidgets.QFormLayout()
        heading_layout.addRow('Asset Name',self.current_asset_wgt)
        heading_layout.addRow('Asset Type', self.asset_type_wgt)
        heading_layout.addRow('Publish Type',self.publish_type_cat_wgt)
        heading_layout.addRow('Publish Sub Cat', self.publish_sub_cat_wgt)
        
        file_load_layout = QtWidgets.QHBoxLayout()
        file_load_layout.addWidget(self.filepath_le)
        file_load_layout.addWidget(self.select_file_path_btn)

        output_layout = QtWidgets.QVBoxLayout()
        output_layout.addWidget(self.output_log_wget)
        
        publish_layout = QtWidgets.QHBoxLayout()
        publish_layout.addWidget(self.publish_btn_wgt)
        publish_layout.addWidget(self.cancle_btn_wgt)
        
        
        # add to the mainlayout
        main_layout.addLayout(heading_layout)
        main_layout.addLayout(file_load_layout)
        main_layout.addLayout(output_layout)
        main_layout.addLayout(publish_layout)
        main_layout.addWidget(self.statusBar_wgt)
        
    def create_connections(self):
        pass
    

if __name__ == "__main__":


	app = QtWidgets.QApplication(sys.argv)
	dialog = AssetPublisher()

	style_file = QtCore.QFile('Z:/Elna/el/app/resources/styles/usdviewstyle.qss')
	style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
	stream = QtCore.QTextStream(style_file)
	app.setStyleSheet(stream.readAll())

	# dialog.removeEventFilter(dialog.lineedit)
	dialog.show()
	app.exec()
