import os
from el.utils.read_dump import read_yaml
from el.utils.dir_utils import create_dir

path = '/mnt/x/Shows'

# Create show Class method
class CreateShow():
    def __init__(self,path, name,type='Show'):
        self.path = path
        self.name = name
        self.type = type
        self.fullpath = os.path.join(self.path,self.name)

    def create_dir(self):
        if os.path.isdir(self.path):
            if not os.path.isdir(self.fullpath):
                os.mkdir(self.fullpath)
            else:
                print(f'WARNNING: The {self.fullpath} already exists.')
        else:
            print('WARNNING: The base directory does not exists.')
            print(f'{path}')

    def cwd(self):
        os.chdir(self.fullpath)
        os.system('/bin/bash')







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

    # change current working diretory
    # os.chdir(full_path)
    # os.system('/bin/bash')
    # TODO:
    # 1. Create asset and sequences directory.
    # 2. 


