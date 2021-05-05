import yaml
import json

# Read yaml
def read_yaml(file_path):
    with open(file_path, 'r') as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        return data

# Dump yaml
def dump_yaml(file_path,data):
    with open(file_path, 'w') as r:
        json.dump(data, wf)


# Read json
def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


# Dump json
def write_json(json_file_path, data):
    with open(json_file_path, 'w') as wf:
        json.dump(data, wf, indent=4)

