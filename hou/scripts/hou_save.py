import json
import objecttoolutils
import os
import hou

hou_file = 'hou'

# Read json
def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


# Dump json
def dump_json(json_file_path, data):
    with open(json_file_path, 'w') as wf:
        json.dump(data, wf, indent=4)
        
# read 'hou' file
data = read_json(hou_file)


current_file_path = hou.hipFile.name()
split = current_file_path.split('/')
current_file_name = split[-1]

list_dir = os.listdir(os.getcwd())
if current_file_name in list_dir:
    name = current_file_name
    hou.hipFile.save(name)
    
    
else:
    name = hou.ui.readInput("File Name", title="Save current file")[1]
    if len(name)>1:
        name = name.replace(" ","_")
        name = name + "_v001.hip"
        hou.hipFile.save(name)
        #log current file into hou.hip_files
        data['hip_files'].append(name)
        dump_json(hou_file,data)