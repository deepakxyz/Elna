# OS
import os
import shutil
import time


# maya
import maya.cmds as mc
import maya.OpenMaya as om


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


# Open current working directory for the file
def openPWD():
    path_details = current_file_details()
    toOpen = "explorer.exe {0}".format(path_details['current_directory'])
    os.system(toOpen)
    

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
            
        
path = current_file_details()
print(get_level_details(path))