import click
import os
from el.func.create_show import create_show, CreateShow

base_path = '/mnt/x/Shows'

@click.command()
@click.argument('show_name')
@click.option('--stay',is_flag=True, help='Stay in the current working directory')
def cli(show_name,stay):
    '''Create a new Show under the base directory and the show can be accessed from other DCC'''
    # create_show(path=base_path, name=show_name,type='Show')
    show = CreateShow(path=base_path, name=show_name)
    show.create_dir()
    if not stay:
        show.cwd()


