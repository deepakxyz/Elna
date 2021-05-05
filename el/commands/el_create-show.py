import click
import os
from el.func.create_show import create_show

base_path = '/mnt/x/Shows'

@click.command()
@click.argument('show_name')
def cli(show_name):
    '''Create show'''
    create_show(path=base_path, name=show_name,type='Show')


