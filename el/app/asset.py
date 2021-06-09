import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet

from utils.read_dump import read_json


class Files():


    @classmethod
    def get_files(cls,path, build_type):
        files=[]
        type_path = os.path.join(path, build_type)
        all_files = os.listdir(type_path)
        for file in all_files:
            file_path = os.path.join(type_path, file)
            if os.path.isfile(file_path):
                files.append(file)
        return(files)

    @classmethod
    def create_file_list(cls,files):
        files_list = []
        for file in files:
            name , ext = os.path.splitext(file)
            if "_" in name:
                name = name.split('_')
                del name[-1]
                name = "_".join(name)
            
            else:
                name = name

            if name not in files_list:
                files_list.append(name)

        return files_list


    @classmethod
    def get_children(cls,parent, files):
        children = []
        for file in files:
            if file.startswith(parent):

                children.append(file)

        return children

    @classmethod
    def get_only_version(cls, list):
        version_list = []
        full_list = list 
        for i in list:
            split_text = i.split("_")
            version_list.append(split_text[-1])

        return [version_list, full_list]


    @classmethod
    def find_type(cls, filename):
        if filename.endswith('.mb'):
            return 'Maya'

        elif filename.endswith('.hip'):
            return 'Houdini'

        else:
            return "Unsupported format"

    @classmethod
    def find_master_file_type(cls,master_file, all_files):
        for file in all_files:
            if file.startswith(master_file):
                raw, ext = os.path.splitext(file)
                if ext == ".mb" or ext == ".ma":
                    file_type = "Maya"
                    return file_type
                elif ext == ".hip":
                    file_type = "Houdini"
                    return file_type
                else:
                    return "Unsupported format"





class AssetLauncher(QtWidgets.QWidget):


    def __init__(self):
        super(AssetLauncher, self).__init__(parent=None)

        self.setWindowTitle('El Asset Launcher')
        self.setMinimumSize(1000,300)


        self.BASE_PATH = os.path.join(os.getcwd(), 'asset_build')
        self.launch_file_path = None

        self.create_widget()
        self.create_layout()
        self.create_connection()

        self.clipboard_data = QtGui.QGuiApplication.clipboard()

    def create_widget(self):
        self.asset_type = QtWidgets.QComboBox()
        self.asset_type.addItems(['char', 'prop','env','matte'])

        self.asset = QtWidgets.QComboBox()

        # read the char asset at the first
        path = os.path.join(self.BASE_PATH, 'char')
        assets = os.listdir(path)
        self.asset.addItems(assets)


        self.build_type = QtWidgets.QComboBox()
        self.build_type.addItems(['model','zfile','rig','anim','groom','lookDev','cfx','fx'])


        self.update_btn = QtWidgets.QPushButton('Update')


        self.tree_widget = QtWidgets.QTreeWidget()
        # self.tree_widget.setColumnCount(2)
        self.tree_widget.headerItem().setText(0,'File name')
        self.tree_widget.headerItem().setText(1,'Type')
        self.tree_widget.setColumnWidth(0, 400)

        # buttom buttom
        self.launch_blank = QtWidgets.QPushButton('Launch Blank')
        self.launch_selected = QtWidgets.QPushButton('Launch Selected')

        # blank file launch type
        self.maya_blk_file = QtWidgets.QRadioButton('Maya')
        self.maya_blk_file.setChecked(True)
        self.hou_blk_file = QtWidgets.QRadioButton('Houdini')
        self.nuk_blk_file = QtWidgets.QRadioButton('Nuke')


        # status bar 
        self.statusBar_wgt = QtWidgets.QStatusBar()
        self.statusBar_wgt.showMessage('Hello',1000)

        # output log
        self.output_log_wget = QtWidgets.QTextBrowser()
        self.output_log_wget.setMaximumWidth(360)
        html = '''
        <p>Output :</p>
        '''
        self.output_log_wget.insertHtml(html)
        self.output_log_wget.append('')



    def create_layout(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('Type', self.asset_type)
        form_layout.addRow('Asset', self.asset)
        form_layout.addRow('Build Type', self.build_type)

        # launch btn layout
        launch_btn_layout = QtWidgets.QHBoxLayout()
        launch_btn_layout.addWidget(self.launch_blank)
        launch_btn_layout.addWidget(self.launch_selected)

        # blank types
        launch_blank_type_layout = QtWidgets.QHBoxLayout()
        launch_blank_type_layout.addStretch(True)
        launch_blank_type_layout.addWidget(self.maya_blk_file)
        launch_blank_type_layout.addWidget(self.hou_blk_file)
        launch_blank_type_layout.addWidget(self.nuk_blk_file)




        # mainlayout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.update_btn)
        main_layout.addWidget(self.tree_widget)
        main_layout.addLayout(launch_btn_layout)
        main_layout.addLayout(launch_blank_type_layout)
        main_layout.addWidget(self.statusBar_wgt)

        # ouput layout
        output_layout = QtWidgets.QVBoxLayout()
        output_layout.addWidget(self.output_log_wget)

        # toplayout
        top_layout = QtWidgets.QHBoxLayout(self)
        top_layout.addLayout(main_layout)
        top_layout.addLayout(output_layout)

    def create_connection(self):
        # get asset details
        self.asset_type.currentTextChanged.connect(self.asset_type_changed)
        # self.asset.currentTextChanged.connect(self.detail_changed)
        # self.build_type.currentTextChanged.connect(self.detail_changed)

        self.tree_widget.itemClicked.connect(self.set_launch_data)
        self.tree_widget.itemDoubleClicked.connect(self.update_output)


        self.update_btn.clicked.connect(self.refresh_tree_widget)

        self.launch_blank.clicked.connect(self.launch_blank_command)
        self.launch_selected.clicked.connect(self.launch_selected_file)


        self.output_log_wget.anchorClicked.connect(self.url_clicked)


    def url_clicked(self,url):
        data = QtCore.QUrl.toString(url)
        os.system(f'start {data}')

    def update_output(self,item):
        double_clicked_item_data = item.data(QtCore.Qt.UserRole,0)
        if double_clicked_item_data:
            html = f'''
            <p><pre>{double_clicked_item_data} to clipboard.</pre></p>
            '''
            self.output_log_wget.insertHtml(html)
            self.output_log_wget.append('')
            self.output_log_wget.moveCursor(QtGui.QTextCursor.End)

            # clipboard
            self.clipboard_data.setText(self.launch_file_path)

    def set_launch_data(self, item):
        self.item_data = item.data(QtCore.Qt.UserRole,0)
        if self.item_data:
            self.launch_file_path = os.path.join(self.path, self.build_type_data, self.item_data)
            # status bar
            self.statusBar_wgt.showMessage(f'Launch file: {self.item_data}')
        else:
            self.launch_file_path = None


    def launch_selected_file(self):
        asset_type = self.asset_type.currentText()
        asset = self.asset.currentText()
        self.build_type_data = self.build_type.currentText()

        proj = os.path.join(self.BASE_PATH, asset_type, asset)

        if self.item_data.endswith('.mb') or asset.endswith('.ma'):
            if not self.launch_file_path is None:
                os.system(f'start maya -file {self.launch_file_path} -proj {proj}')

                self.statusBar_wgt.showMessage(f'Opening file {self.item_data}')

        elif self.item_data.endswith('.hip'):
            if not self.launch_file_path is None:

                os.system(f"cmd.exe /c start houdini {self.launch_file_path}")
        
        else:
            self.statusBar_wgt.showMessage('Selected file is not a valid file format')

    def launch_blank_command(self):
        asset_type = self.asset_type.currentText()
        asset = self.asset.currentText()
        self.build_type_data = self.build_type.currentText()
        
        # maya blank file
        if self.maya_blk_file.isChecked():

            self.path = os.path.join(self.BASE_PATH, asset_type, asset)

            os.system(f'cmd.exe /c start maya -proj {self.path}')

            self.statusBar_wgt.showMessage('Launching blank maya file', 3000)

        elif self.hou_blk_file.isChecked():
            path = os.path.join(self.BASE_PATH, asset_type, asset, self.build_type_data)
            os.chdir(path) 
            os.system("cmd.exe /c start houdini")
        
        else:
            print('wooo')


    def refresh_tree_widget(self):

        # get data from the combo boxes
        # asset type
        asset_type = self.asset_type.currentText()
        asset = self.asset.currentText()
        self.build_type_data = self.build_type.currentText()

        self.path = os.path.join(self.BASE_PATH, asset_type, asset)
        tree_view_path = os.path.join(self.path, self.build_type_data)

        style = '''
        <style>
        a{
            color:#EAB729;
        }
        </style>
        '''
        html = f'''
        {style}
        <p>Current treeview path on system:</p>
        <a href="{tree_view_path}">{tree_view_path}</a>
        <br>
        '''
        html = html.replace('\\', '/')
        self.output_log_wget.insertHtml(html)
        self.output_log_wget.setOpenExternalLinks(False)
        self.output_log_wget.setOpenLinks(False)
        # self.output_log_wget.append('')
        self.output_log_wget.moveCursor(QtGui.QTextCursor.End)





        # clear the iteam in tree widget
        self.tree_widget.clear()

        files_list = Files.get_files(self.path, self.build_type_data)
        master_list = Files.create_file_list(files_list)
        if master_list:
            for name in master_list:

                item  = QtWidgets.QTreeWidgetItem([name, Files.find_master_file_type(name,files_list)])
                print(master_list)


                # adding child elements
                children_list = Files.get_children(item.text(0), Files.get_files(self.path,self.build_type_data))

                if children_list:
                    only_version = Files.get_only_version(children_list)

                    for i,child in enumerate(only_version[0]):
                        child_element = QtWidgets.QTreeWidgetItem([child, Files.find_type(child)])
                        child_element.setData(QtCore.Qt.UserRole,0 ,only_version[1][i] )
                        item.addChild(child_element)


                self.tree_widget.addTopLevelItem(item) 
                self.statusBar_wgt.showMessage('Asset updated',2000)
        else:
            item = QtWidgets.QTreeWidgetItem(['No file found'])
            self.statusBar_wgt.showMessage('No file found in the given input.', 4000)
            html = 'No file found in the given input. Please check the directory'
            self.output_log_wget.insertHtml(html)
            self.output_log_wget.append('')
            self.tree_widget.addTopLevelItem(item)




    def asset_type_changed(self):
        asset_type = self.asset_type.currentText()
        if asset_type == "prop":
            self.asset.clear()

            path = os.path.join(self.BASE_PATH, asset_type)
            assets = os.listdir(path)

            self.asset.addItems(assets)

        elif asset_type == "char":
            self.asset.clear()

            path = os.path.join(self.BASE_PATH, asset_type)
            assets = os.listdir(path)

            self.asset.addItems(assets)

        elif asset_type == "env":
            self.asset.clear()

            path = os.path.join(self.BASE_PATH, asset_type)
            assets = os.listdir(path)

            self.asset.addItems(assets) 

        elif asset_type == "matte":
            self.asset.clear()

            path = os.path.join(self.BASE_PATH, asset_type)
            assets = os.listdir(path)

            self.asset.addItems(assets)

    def detail_changed(self):

        pass 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    # apply_stylesheet(app, theme='dark_amber.xml')
    window = AssetLauncher()



    # style_file = QtCore.QFile('dark.qss')
    # style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    # stream = QtCore.QTextStream(style_file)
    # app.setStyleSheet(stream.readAll())


    window.show()
    app.exec()