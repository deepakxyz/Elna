import click
import os
from el.func.initialize import Init



@click.command()
def cli():
    ''' Initialize Elna and setup database '''
    # get current working directory
    cwd = os.getcwd()
    init = Init(cwd)