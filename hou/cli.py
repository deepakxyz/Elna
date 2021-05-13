import click
import os

from click.core import BaseCommand
from hou.globals import BASE_PATH, HOUDINI_JSON, LOG_JSON
from hou.utils.utils import cwd, log
from hou.utils.read_dump import read_json, dump_json

from hou.func.create_project import CreateProject
from hou.func.gopro import GoPro
from hou.func.project import Launch


class Context:
    def __init__(self, base_path, houdini_json, log_json):
        self.name = "deepak"
        self.base_path = base_path
        self.houdini_json = houdini_json
        self.log_json = log_json


    def getJsonData(self):
        file_path = os.path.join(self.base_path, self.houdini_json)
        data = read_json(file_path)
        return data


    def log_getShow(self):
        log_file_path = os.path.join(self.base_path,self.log_json)
        log_data = read_json(log_file_path)
        last_show = log_data['last_show']
        return last_show

    def log_lastShow(self,proname):
        log_file_path = os.path.join(self.base_path,self.log_json)
        log_data = read_json(log_file_path)
        log_data['last_show'] = proname

        # dump the data
        dump_json(log_file_path, log_data)





@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Context(base_path=BASE_PATH,houdini_json=HOUDINI_JSON,log_json=LOG_JSON)



# create project with user input data
@cli.command()
@click.pass_context
def create_project(ctx):
    '''Create a new Houdini project with all the sub directories.'''
    pro_name = click.prompt('Name of the project')
    pro_name = pro_name.replace(' ', '_')
    pro_description = click.prompt('Project Description')

    fullpath = os.path.join(BASE_PATH, pro_name)
    check_dir = CreateProject.check_dir(fullpath)

    if check_dir:
        new_pro = CreateProject(path=BASE_PATH,name=pro_name, desc=pro_description)
        new_pro.add_to_json()
        # log last_show
        ctx.obj.log_lastShow(pro_name)
        new_pro.cwd()


# gopro function
# gopro --list : list all the data
@cli.command()
@click.argument('proname',required=False)
@click.option("--list", is_flag=True)
@click.option("--last", is_flag=True)
@click.pass_context
def gopro(ctx,proname, list, last):
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
            # log the last gopro project
            ctx.obj.log_lastShow(proname=proname)

            # change directory into project directory
            cwd(os.path.join(BASE_PATH, proname))
        
        else:
            click.echo(f'Project "{proname} does not exists.')
            click.echo('Use "hou gopro --list to get all the existing projects.')


    elif last:
        # read log data
        last_show = ctx.obj.log_getShow()
        # check working directory
        cwd(os.path.join(BASE_PATH, last_show))

    else:
        gopro = GoPro.toRoot()



# command runs inside houdini project folder
@cli.command()
def launch():
    # check if the folder is a houdini project
    dir = os.getcwd()
    hou_file =os.path.join(dir,'hou')
    if os.path.isfile(hou_file):
        print('You are fucking inside the project directory. Good')
        h = Launch.check_if_hip_exists(cwd=dir)


    else:
        click.echo("WARRNING: You are not inside the Houdini project to run this command.")