import click
import os
from hou.globals import BASE_PATH

from hou.func.create_project import CreateProject
from hou.func.gopro import GoPro




@click.command()
def cli():
    '''This is create command'''
    pro_name = click.prompt('Name of the project')
    pro_name = pro_name.replace(' ', '_')
    pro_description = click.prompt('Project Description')

    fullpath = os.path.join(BASE_PATH, pro_name)
    check_dir = CreateProject.check_dir(fullpath)

    if check_dir:
        new_pro = CreateProject(path=BASE_PATH,name=pro_name, desc=pro_description)
        new_pro.add_to_json()
        new_pro.cwd()

