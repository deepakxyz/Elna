import click
import os
from el.core.create_show import CreateShow
from el.config.config_data import Config

from el.utils.el import el


@click.command()
@click.argument('show_name')
# @click.option('--stay',is_flag=True, help='Stay in the current working directory')
def cli(show_name):

    # get base directory
    base = Config.base()
    # check and create show


    if CreateShow.check(base, show_name):

        path = os.path.join(base, show_name)
        # create show
        new_show = CreateShow(base, show_name)

        # get  short name
        click.echo('Must be only two letters')
        short_name = click.prompt('Short name of the project')

        # get desc
        desc = click.prompt("Project description")

        # create level files
        new_show.create_level_files()

        # add data to main shows json file
        new_show.add_to_json(short_name=short_name, desc=desc)

        # display message
        new_show.msg()

        # change directory once all the directories gets created.
        el.cwd(path)


    


