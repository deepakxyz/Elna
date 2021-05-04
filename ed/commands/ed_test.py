import click
import os

@click.command()
def cli():
    '''Test'''
    os.chdir('/mnt/y/Shows')
    os.system('/bin/bash')

