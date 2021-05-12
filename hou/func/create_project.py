import os
from hou.utils.utils import echo, cwd

# create new houdini project
class CreateProject():
    def __init__(self,path,name,desc):
        self.path = path
        self.name = name
        self.fullpath = os.path.join(self.path,self.name) 
        self.desc = desc

        # exe
        self.check_create()


    # check if the project already exist
    def check_create(self):
        if not os.path.isdir(self.fullpath):
            # create directory
            os.mkdir(self.fullpath)
            return True

        else:
            echo(f"Project '{self.name}' already exists.")
            return False

