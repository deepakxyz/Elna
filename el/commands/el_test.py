import click
import os
from el.utils.el import Path, current_show, el
from el.core.levels import Level

path = '/mnt/y/pipeline/Shows/Mayday/asset_build'

@click.command()
def cli():
    '''Test'''
    if Level.check('show'):
        os.system('cmd.exe /c python  Z:/Elna/el/app/asset.py')
    else:
        print('You are not at the show level')