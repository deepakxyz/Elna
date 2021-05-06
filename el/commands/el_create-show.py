import click
import os
from el.func.create_show import  CreateShow


@click.command()
# @click.argument('show_name')
@click.option('--stay',is_flag=True, help='Stay in the current working directory')
def cli(stay):
    '''Create a new Show under the base directory and the show can be accessed from other DCC'''

    # Input data from the user
    show_name = click.prompt('Name of the show', type=str)

    click.echo('Short name must be only 3 character in length.')
    short_name = click.prompt('Short Name')
    if len(short_name) >= 4:
        click.echo('Short name is longer, please make it only 3 or less characters.')
        short_name = click.prompt('Short Name')

    description = click.prompt('Show description:')

    base_path = os.getcwd()
    # check if your under show root dir
    check = CreateShow.check_cwd(base_path)
    if check:
        show = CreateShow(path=base_path, name=show_name, short_name=short_name, desc=description)
        req = show.create_dir()
        # if only the directory got created 
        if req:
            show.add_to_json()
            if not stay:
                show.cwd()


