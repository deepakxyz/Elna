import os
from el.utils.read_dump import read_yaml
from el.utils.dir_utils import create_dir

path = '/mnt/x/Shows'

def cwd(func):
    def wrapper(*args, **kwargs):
        arguments = kwargs
        path = os.path.join(arguments['path'],arguments['name'])
        os.chdir(path)
        os.system('/bin/bash')
    return wrapper

@create_dir
@cwd
def create_show(path,name,type='Show'):
    create_show.full_path = os.path.join(path, name)

    # change current working diretory
    # os.chdir(full_path)
    # os.system('/bin/bash')
    # TODO:
    # 1. Create asset and sequences directory.
    # 2. 


