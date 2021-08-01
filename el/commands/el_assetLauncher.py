import click
import os
from el.utils.el import Path, current_show, el
from el.core.levels import Level

path = '/mnt/y/pipeline/Shows/Mayday/asset_build'

@click.command()
def cli():
    '''Asset Launcher'''
    if Level.check('show'):

        os.system('cmd.exe /c python  Z:/Elna/el/app/assetLauncher.py')
    else:
        os.system('el goshow --current')