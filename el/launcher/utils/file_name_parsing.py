import os

files = ['maya_modeling_v001.mb','maya_modeling_v002.mb','maya_modeling_v003.mb',
'head_model_v001.mb','head_model_v002.mb','head_model_v003.mb','head_model_v004.mb']



def create_file_list(files):
    files_list = []
    for file in files:
        name , ext = os.path.splitext(file)
        name = name.split('_')
        del name[-1]
        name = "_".join(name)
        if name not in files_list:
            files_list.append(name)

    return files_list


def get_version(files, file_names):
    for file in files:
        for parent in file_names:
            if file.startswith(parent):
                print(file)
        # if file in file_names:
            # print(file)

        
file_names = (create_file_list(files))

get_version(files, file_names)