import os
all_files = ['sphere_main_model_v001.mb', 'sphere_main_model_v002.mb', 'sphere_model_v001.hip']
master_files = ['sphere_main_model', 'sphere_model']


def test(master_file, all_files):
    print(master_file, all_files)
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




print(test(master_files[1], all_files))