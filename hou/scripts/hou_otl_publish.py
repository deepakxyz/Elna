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
## Publish OTLS


selection = hou.selectedNodes()
if len(selection) == 1:

    hda_node = selection[0]
    definition = hda_node.type().definition()
    try:
        if definition.libraryFilePath():
            libFilePath = definition.libraryFilePath()
            full_current_name = hda_node.type().name()
            current_version_string = hda_node.type().nameComponents()
            
            all_otls=[]
            # loop at all the otls
            for otls in data['otls']:
                all_otls.append(otls['path'])
                
            if not libFilePath in all_otls:
                # get description from user input
                desc = hou.ui.readInput("Description", title="Otls Description")[1]
                new_otls = {"path":libFilePath,"description":desc}
                data['otls'].append(new_otls)
                # dump data  
                dump_json(hou_file, data)
                print('Otls published')
            
            
    except:
        print('Not a HDA / OTL')
