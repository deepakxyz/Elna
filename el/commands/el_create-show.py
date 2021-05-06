import click
import os
from el.func.create_show import  CreateShow


@click.command()
@click.argument('show_name')
@click.option('--stay',is_flag=True, help='Stay in the current working directory')
def cli(show_name,stay):
    '''Create a new Show under the base directory and the show can be accessed from other DCC'''
    base_path = os.getcwd()
    # check if your under show root dir
    check = CreateShow.check_cwd(base_path)
    if check:
        show = CreateShow(path=base_path, name=show_name)
        show.create_dir()
        if not stay:
            show.cwd()


