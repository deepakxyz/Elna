import os

from hou.globals import PRO_SUB_DIR

# lauch a blank file if there is not any .hip file
# if there is any, lauch the latest version of the .hip file

class Launch():

    @classmethod
    def check_if_hip_exists(cls,cwd):
        # list directory
        for file in os.listdir(cwd):
            if not file in PRO_SUB_DIR:
                raw, ext = os.path.splitext(file)
                if ext == '.hip':
                    name = raw.split('_')
                    del name[-1:]
                    print(name)
        