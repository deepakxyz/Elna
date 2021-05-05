import os
from el.utils.read_dump import read_yaml
from el.utils.dir_utils import create_dir

path = '/mnt/x/Shows'

@create_dir
def create_show(path,name):
    print('Show create')
    
create_show(path=path, name='Hello')