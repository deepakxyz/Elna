import os
from hou.utils.utils import echo, cwd
from hou.utils.read_dump import read_json, dump_json
from time import gmtime, strftime

# create new houdini project
class CreateProject():
    def __init__(self,path,name,desc):
        self.path = path
        self.name = name
        self.fullpath = os.path.join(self.path,self.name) 
        self.desc = desc

        self.create_dir()

    @staticmethod
    def check_dir(fullpath):
        if not os.path.isdir(fullpath):
            return True
        else:
            echo(f"Project '{fullpath}' already exists.")
            return False


    # check if the project already exist
    def create_dir(self):
            # create directory
            os.mkdir(self.fullpath)
            echo("Project successfull created.")
            
            # create sub dirctory
            self.create_sub_dir()


    # change directory
    def cwd(self):
        os.chdir(self.fullpath)
        os.system('/bin/bash')


    # add data to json file
    def add_to_json(self):
        time = strftime("%d %b %Y", gmtime())
        data = {"name":self.name, "description":self.desc,"path":self.fullpath ,"created-on":time}

        path = os.path.join(self.path, 'houdini.json')
        read_data = read_json(path)
        read_data['projects'].append(data)
        dump_json(path, read_data)


    # create sub-dir 
    def create_sub_dir(self):
        dirs = ['hip','geo','cache','image','render','had','scripts']
        for dir in dirs:
            path = os.path.join(self.fullpath, dir)
            os.mkdir(path)

