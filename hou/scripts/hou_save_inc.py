import json
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

hou.hipFile.saveAndIncrementFileName()
current_file_path = hou.hipFile.name()
split = current_file_path.split('/')
current_file_name = split[-1]
data['hip_files'].append(current_file_name)
# dump data
dump_json(hou_file, data)
