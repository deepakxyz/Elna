import click
import os
from v.func.utils import base_dir_to_win_dir
from v.func.playback import get_sequences


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
    