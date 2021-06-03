import click
import os
from el.utils.el import Path

path = '/mnt/y/pipeline/Shows/Mayday/asset_build'

@click.command()
def cli():
    '''Test'''
    h = Path.show_name(os.getcwd())