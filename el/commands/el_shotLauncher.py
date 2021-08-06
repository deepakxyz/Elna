import click
import os
from el.utils.el import Path, current_show, el
from el.core.levels import Level


@click.command()
def cli():
    '''Asset Launcher'''
    if Level.check('show'):

        os.system('cmd.exe /c python  Z:/Elna/el/app/shotLauncher.py')
    else:
        os.system('el goshow --current')