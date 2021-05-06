import os
from el.utils.read_dump import read_yaml, read_json, dump_json
from el.utils.dir_utils import create_dir
from el.utils.el import el
from time import gmtime, strftime


# Create show Class method
class CreateShow():
    def __init__(self,path, name,short_name, desc,type='Show'):
        self.path = path
        self.name = name
        self.type = type
        self.fullpath = os.path.join(self.path,self.name)
        self.short_name = short_name
        self.desc = desc # description

    # if the current directory as a file main.config and the base_show_path attribute
    # then run the other commands
    @staticmethod
    def check_cwd(path):
        # read main.config file
        try:
            config_read = read_yaml(os.path.join(path,"main.config"))
            if config_read['base_show_path'] == path:
                return True
            
            else:
                el.echo("You cannot create a new show unless your in the root directory","WARNING:")
                el.echo("Use `el goshow` command to move to the root directory.")
                return False
        except:
            el.echo("You cannot create a new show unless your in the root directory","WARNING:")
            el.echo("Use `el goshow` command to move to the root directory.")
            return False

    # create main show folder
    def create_dir(self):
        if os.path.isdir(self.path):
            if not os.path.isdir(self.fullpath):
                os.mkdir(self.fullpath)

                return True
                # add data to json file
            else:
                print(f'ERROR: The your trying to create "{self.name}" already exists.')
                return False
        else:
            print('ERROR: The base directory does not exists.')
            print(f'{path}')
            return False


    # change working directory to the show folder
    def cwd(self):
        os.chdir(self.fullpath)
        os.system('/bin/bash')


    def add_to_json(self):
        time = strftime("%d %b %Y", gmtime())
        data = {"name":self.name, "short-name":self.short_name, "description":self.desc, "created-on":time}

        path = os.path.join(self.path, 'Shows.json')
        read_data = read_json(path)
        read_data['shows'].append(data)
        dump_json(path, read_data)


