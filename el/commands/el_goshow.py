import click
from el.utils.el import el
from el.core.goshow import GoShow


@click.command()
@click.argument('showname', required=False)
@click.option('-l','--list', is_flag=True)
def cli(list, showname):
    '''Go show'''

    # list all the shows with the option
    if list:
        GoShow.goshow_list()

    # move into the show
    elif showname:
        GoShow.goshow(showname=showname)

    # only goshow
    else:
        click.echo('Currently/Moved under the "Shows" root directory')
        click.echo('''
        USEFUL COMMANDS:
        el goshow --list : To list all the show.
        el goshow [showname] : Move to the [showname] directory is [showname] exists.
        ''')
        GoShow.toRoot()

