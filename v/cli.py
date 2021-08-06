import click
import os

from click.decorators import argument
from v.core.utils import base_dir_to_win_dir
from v.core.playback import get_sequences
from v.core.txconvert import converter


@click.group()
def cli():
    pass


@cli.command()
@click.argument('fileindex', required=False)
@click.option('--list','-l',is_flag=True, help="List all the sequences")
def rv(fileindex,list):
    ''' Play the sequences using RV viewer'''
    seq = get_sequences()
    if list:
        for i, j in enumerate(seq):
            print(f'{i} : {j}') 
    else:
        if not fileindex:
            fileindex = 0
        os.system(f'cmd.exe /c start rv {seq[int(fileindex)]}')

@cli.command()
@click.argument('fileindex', required=False)
@click.option('--list','-l',is_flag=True, help="List all the sequences")
def djv(fileindex,list):
    ''' Play the sequences using djv viewer'''
    seq = get_sequences()
    if list:
        for i, j in enumerate(seq):
            print(f'{i} : {j}') 
    else:
        if not fileindex:
            fileindex = 0
        os.system(f'cmd.exe /c start djv {seq[int(fileindex)]}')



@cli.command()
@click.argument('filename', required=False)
@click.option('--all', '-a', is_flag=True, help="Convert all the files in the directory")
def txconvert(filename, all):
    if all:
        converter(all=True)
    
    if filename:
        converter(name=filename, all=False)