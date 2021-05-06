import os
from el.utils.read_dump import read_yaml
from el.utils.dir_utils import create_dir
from el.utils.el import el


# Create show Class method
class CreateShow():
    def __init__(self,path, name,type='Show'):
        self.path = path
        self.name = name
        self.type = type
        self.fullpath = os.path.join(self.path,self.name)

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
            else:
                print(f'WARNNING: The {self.fullpath} already exists.')
        else:
            print('WARNNING: The base directory does not exists.')
            print(f'{path}')

    # change working directory to the show folder
    def cwd(self):
        os.chdir(self.fullpath)
        os.system('/bin/bash')


        # create sub-directories

















def cwd(func):
    def wrapper(*args, **kwargs):
        arguments = kwargs
        path = os.path.join(arguments['path'],arguments['name'])
        os.chdir(path)
        os.system('/bin/bash')
        # return func()
    return wrapper

@create_dir
@cwd
def create_show(path,name,type='Show'):
    click.echo('Creating show')
    print('Creating show')
    create_show.full_path = os.path.join(path, name)

