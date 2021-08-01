
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance


import maya.OpenMayaUI as omui
import maya.OpenMaya as om

import maya.cmds as mc
import maya.mel as mm




def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    
    # OS
import os
import shutil
import time


# maya
import maya.cmds as mc
import maya.OpenMaya as om


class CurrentFileDetails():
    
    @staticmethod
    def current_file_details():
        # current file path
        filepath = mc.file(q=True,sn=True)
        
        # current file name
        filename = os.path.basename(filepath)
        
        raw,ext = os.path.splitext(filename)
        
        # directory name
        directory = filepath.replace(filename," ")
        dir = directory.split('/')
        del dir[-1:]
        current_directory = "\\".join(dir)


        output = {"filepath":filepath,"filename":filename,"raw":raw,"ext":ext,"current_directory":current_directory}
        return(output)


    @staticmethod
    def get_level_details(details):
        current_dir = details['current_directory']
        asset_types = ['char','env','prop','matte']
        current_dir = current_dir.replace('\\','/')
        BASE_DIR = "Y:/pipeline/Shows"

        if current_dir.startswith(BASE_DIR):

            current_dir = current_dir.split('/')
            asset_type_detail = current_dir[-3]
        else:
            current_dir = None
            
        if current_dir:
        
            for i, asset_type in enumerate(current_dir):
                if asset_type_detail == asset_type:
                    asset_type_out = asset_type
                    asset_name = current_dir[i + 1]
                
            # get show name
            for i, n in enumerate(current_dir):
                if n == "Shows":
                    show_name_index = i + 1
                    show_name = current_dir[show_name_index]
                    break


            level_detais = {"show_name":show_name,"asset_type":asset_type_out, "asset_name": asset_name}
            return level_detais
        
        else:
            return None
            
            

            
            
class AddnewEntity(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(AddnewEntity, self).__init__(parent)
        
        self.setWindowTitle('Add New Entity')
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumSize(400, 100)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
        
    def create_widgets(self):
        self.add_new_entity_le = QtWidgets.QLineEdit()
        self.add_new_entity_le.setStyleSheet("height:30px;")
        self.add_new_e_btn = QtWidgets.QPushButton('Add')
        
    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        
        le_layout = QtWidgets.QHBoxLayout()
        le_layout.addWidget(QtWidgets.QLabel("Name: "))
        le_layout.addWidget(self.add_new_entity_le)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.add_new_e_btn)
        
        
        
        # add to main layout
        main_layout.addLayout(le_layout)
        main_layout.addLayout(btn_layout)
        
        
    def create_connections(self):
        pass
        
            



class AssetPublisher(QtWidgets.QDialog):
    
    FILE_FILTERS = "Alembic (*.abc);;obj (*.obj);;USD (*.usd *.usdc);;All Files (*.*)"

    selected_filter = "Alembic (*.abc)"
    
    BASE_DIR = "Y:/pipeline/Shows"

    def __init__(self, parent=maya_main_window()):
        super(AssetPublisher, self).__init__(parent)
        

        
        # current show detials
        path = CurrentFileDetails.current_file_details()
        level_details = CurrentFileDetails.get_level_details(path)
        print(level_details)
        self.current_show = (level_details['show_name'])
        self.asset_type = level_details['asset_type']
        self.asset_name = level_details['asset_name']

        self.setWindowTitle(f" Asset Publisher - {self.current_show}")

        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
        
        
        
        
        
    def create_widgets(self):
        self.current_asset_wgt = QtWidgets.QLabel(self.asset_name)
        self.current_asset_wgt.setStyleSheet("color:#C9B25B;"
                                            "font-size:18px;"
                                             "padding:3px;")
                                             
        self.asset_type_wgt = QtWidgets.QLabel(self.asset_type)
        self.asset_type_wgt.setStyleSheet("color:#C9B25B;"
                                            "font-size:18px;"
                                            "padding:3px;")
                                            
        self.publish_type_cat_wgt = QtWidgets.QComboBox()
        self.publish_type_cat_wgt.setStyleSheet("width:400px;"
                                                "height:30px")
        self.publish_type_cat_wgt.addItems(['model','zfile','rig','anim','groom','lookDev','cfx','fx'])
                                                
        # self.publish_sub_cat_wgt = QtWidgets.QComboBox()
        # self.publish_sub_cat_wgt.setStyleSheet("width:400px;"
                                                # "height:30px")
                                                
        self.filepath_le = QtWidgets.QLineEdit()
        self.filepath_le.setStyleSheet("width:400px;"
                                                "height:30px")
                                                
        self.select_file_path_btn = QtWidgets.QPushButton()
        self.select_file_path_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        
        self.clear_btn_wgt = QtWidgets.QPushButton('Clear')
        self.add_btn_wgt = QtWidgets.QPushButton('Add')
        
        self.output_log_wget = QtWidgets.QTreeWidget()
        self.output_log_wget.headerItem().setText(0,'File name')
        self.output_log_wget.headerItem().setText(1,'Type')
        self.output_log_wget.headerItem().setText(2,'Frame Range')
        self.output_log_wget.setColumnWidth(0, 400)
        
        self.entity_existing_wgt = QtWidgets.QComboBox()
        self.entity_existing_wgt.setStyleSheet("height:30px;"
                                                "width: 160px;")
        self.entity_new_wgt = QtWidgets.QPushButton('Add New Entity')

        
        self.publish_btn_wgt = QtWidgets.QPushButton('Publish')
        self.cancle_btn_wgt = QtWidgets.QPushButton('Cancle')
        
        self.statusBar_wgt = QtWidgets.QStatusBar()
        self.statusBar_wgt.setStyleSheet("color:#C9B25B;")
        
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        
        heading_layout = QtWidgets.QFormLayout()
        heading_layout.addRow('Asset Name',self.current_asset_wgt)
        heading_layout.addRow('Asset Type', self.asset_type_wgt)
        heading_layout.addRow('Publish Type',self.publish_type_cat_wgt)
        # heading_layout.addRow('Publish Sub Cat', self.publish_sub_cat_wgt)
        
        file_load_layout = QtWidgets.QHBoxLayout()
        file_load_layout.addWidget(self.filepath_le)
        file_load_layout.addWidget(self.select_file_path_btn)
        
        file_load_btn_layout = QtWidgets.QHBoxLayout()
        file_load_btn_layout.addWidget(self.clear_btn_wgt)
        file_load_btn_layout.addWidget(self.add_btn_wgt)

        output_layout = QtWidgets.QVBoxLayout()
        output_layout.addWidget(self.output_log_wget)
        
        publish_layout = QtWidgets.QHBoxLayout()
        publish_layout.addWidget(self.cancle_btn_wgt)
        publish_layout.addWidget(self.publish_btn_wgt)
        
        
        # entity layout
        entity_wgt = QtWidgets.QLabel('Entity:')
        entity_layout = QtWidgets.QHBoxLayout()
        entity_layout.addStretch()
        entity_layout.addWidget(entity_wgt)
        entity_layout.addWidget(self.entity_existing_wgt)
        entity_layout.addWidget(self.entity_new_wgt)
        
        
        # add to the mainlayout
        main_layout.addLayout(heading_layout)
        main_layout.addLayout(file_load_layout)
        main_layout.addLayout(file_load_btn_layout)
        main_layout.addLayout(output_layout)
        main_layout.addLayout(entity_layout)
        main_layout.addLayout(publish_layout)
        main_layout.addWidget(self.statusBar_wgt)
        
    def create_connections(self):
        self.select_file_path_btn.clicked.connect(self.show_file_select_dialog)
        
        # add selected file
        self.add_btn_wgt.clicked.connect(self.add_selected_file)
        # clear selected file
        self.clear_btn_wgt.clicked.connect(self.clear_output_log)
        
        # item clicked
        self.output_log_wget.itemClicked.connect(self.test)
        
        # add new entity
        self.entity_new_wgt.clicked.connect(self.create_new_entity)
        
        # publish clicked
        self.publish_btn_wgt.clicked.connect(self.publish)
        
        
        # cancle button
        self.cancle_btn_wgt.clicked.connect(self.close)
        
    def test(self,item):
        data = item.data(QtCore.Qt.UserRole,0)
        print(data)
        
    def show_file_select_dialog(self):
        self.file_path, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "", self.FILE_FILTERS, self.selected_filter)
        if self.file_path:
            self.filepath_le.setText(self.file_path)
            
    def add_selected_file(self):
        self.output_log_wget.clear()
        input_path = self.filepath_le.text()
        if input_path:
            path = input_path.split('/')
            raw, ext = os.path.splitext(path[-1])
            item = QtWidgets.QTreeWidgetItem([raw,ext])
            item.setData(QtCore.Qt.UserRole,0, input_path)
            self.output_log_wget.addTopLevelItem(item)
            
        # show message
        self.statusBar_wgt.showMessage(f'File added',4000)
            
    def clear_output_log(self):
        self.output_log_wget.clear()
        self.filepath_le.setText('')
        
    def create_new_entity(self):
        
        new_entity_diag = AddnewEntity()
        new_entity_diag.exec_()
        
    def publish(self):
        # selected_file = self.
        # get all element form the tree widget
        root = self.output_log_wget.invisibleRootItem()
        child_count = root.childCount()

        for i in range(child_count):
            item = root.child(i)
            input_path = item.data(QtCore.Qt.UserRole,0)
            input_path_split = input_path.split('/')
            raw, ext = os.path.splitext(input_path_split[-1])
        
            print(raw, ext)
            publish_type = self.publish_type_cat_wgt.currentText()
 
            output_path = os.path.join(AssetPublisher.BASE_DIR, self.current_show, 'assets', self.asset_type, self.asset_name, publish_type)

            
    

if __name__ == "__main__":

    try:
        dialog.close() # pylint: disable=E0601
        dialog.deleteLater()
    except:
        pass

    dialog = AssetPublisher()
    # dialog.removeEventFilter(dialog.lineedit)
    dialog.show()
