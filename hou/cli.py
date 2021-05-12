import click
import os
from hou.func.create_project import CreateProject

@click.group()
def cli():
    '''Create new houdini project'''
    click.echo('Create new project')
    pass


@cli.command()
def create_project():
    '''This is create command'''
    pro_name = click.prompt('Name of the project')
    pro_name = pro_name.replace(' ', '_')
    pro_description = click.prompt('Proejct Description')

    new_pro = CreateProject()
