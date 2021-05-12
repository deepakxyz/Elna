import click
import os
from hou.globals import BASE_PATH
from hou.func.gopro import GoPro

@click.command()
@click.argument('proname',required=False)
@click.option('-a','--all',is_flag=True)
@click.option('-l','--list',is_flag=True, help='List all the existing houdini projects.')
def cli(proname,all,list):
    gopro = GoPro.toRoot()

    click.echo(proname)
    if all == True:
        print('None')
    else:
        print('Noob')
    if list:
        print('This is all the list')
