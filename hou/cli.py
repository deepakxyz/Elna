import click
import os

from click.core import BaseCommand
from hou.globals import BASE_PATH, HOUDINI_JSON
from hou.utils.utils import cwd
from hou.utils.read_dump import read_json

from hou.func.create_project import CreateProject
from hou.func.gopro import GoPro


class Context:
    def __init__(self, base_path, houdini_json):
        self.name = "deepak"
        self.base_path = base_path
        self.houdini_json = houdini_json


    def getJsonData(self):
        file_path = os.path.join(self.base_path, self.houdini_json)
        data = read_json(file_path)
        return data


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Context(base_path=BASE_PATH,houdini_json=HOUDINI_JSON)



# create project with user input data
@cli.command()
def create_project():
    '''Create a new Houdini project with all the sub directories.'''
    pro_name = click.prompt('Name of the project')
    pro_name = pro_name.replace(' ', '_')
    pro_description = click.prompt('Project Description')

    fullpath = os.path.join(BASE_PATH, pro_name)
    check_dir = CreateProject.check_dir(fullpath)

    if check_dir:
        new_pro = CreateProject(path=BASE_PATH,name=pro_name, desc=pro_description)
        new_pro.add_to_json()
        new_pro.cwd()


# gopro function
# gopro --list : list all the data
@cli.command()
@click.argument('proname',required=False)
@click.option("--list", is_flag=True)
@click.pass_context
def gopro(ctx,proname, list):
    ''' Go to the project'''


    # List all the project with description
    if list:
        data = ctx.obj.getJsonData()
        for i in data['projects']:
            name = i['name']
            desc = i['description']
            otls = i['otls']
            print(f"{name}: {desc} | otls: {otls}")
    
    # move to the project
    elif proname:
        data = ctx.obj.getJsonData()
        projects = []
        for pro in data['projects']:
            projects.append(pro['name'])

        if proname in projects:
            cwd(os.path.join(BASE_PATH, proname))
        
        else:
            click.echo(f'Project "{proname} does not exists.')
            click.echo('Use "hou gopro --list to get all the existing projects.')

    else:
        gopro = GoPro.toRoot()