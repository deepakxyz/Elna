import os
from hou.utils.utils import echo, cwd
from hou.utils.read_dump import read_json, dump_json
from time import gmtime, strftime

from hou.globals import PRO_SUB_DIR

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
            echo(f"Project '{fullpath}' already exists.",lvl="ERROR")
            print(f'''
                Sorry!, the project already exists.
                Try creating a new project with a another name or if your looking for the
                particular project use `hou goshow [project-name]` to move in the show.
            ''')
            return False


    # check if the project already exist
    def create_dir(self):
            # create directory
            os.mkdir(self.fullpath)
            echo("Project successfull created.")
            print(f'''
                - The project is created in the hou home directory.
                - It also created the following sub-directories
                {PRO_SUB_DIR}
                - Use `hou launch` to launch a blank houdini file.
            ''')
            
            # create sub dirctory
            self.create_sub_dir()


    # change directory
    def cwd(self):
        os.chdir(self.fullpath)
        os.system('/bin/bash')


    # add data to json file
    def add_to_json(self):
        time = strftime("%d %b %Y", gmtime())
        data = {"name":self.name, "description":self.desc,"path":self.fullpath ,"created-on":time,"otls":[]}

        path = os.path.join(self.path, 'houdini.json')
        read_data = read_json(path)
        read_data['projects'].append(data)
        dump_json(path, read_data)


    # create sub-dir 
    def create_sub_dir(self):
        dirs = PRO_SUB_DIR
        for dir in dirs:
            path = os.path.join(self.fullpath, dir)
            os.mkdir(path)

        # create hou file
        hou_data = {"name":self.name, "status":"WIP","hip_files":[],"last_working_file":None,'level':"project","otls":[]}
        # save file
        file_path = os.path.join(self.fullpath, 'hou')
        dump_json(file_path,hou_data)


    # create hip file
    def create_houdini_file(self):
        os.system('cmd /c ')
        pass
        

