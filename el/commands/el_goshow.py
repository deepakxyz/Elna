import click
from el.utils.el import el
from el.func.goshow import GoShow


@click.command()
@click.argument('showname', required=False)
@click.option('-l','--list', is_flag=True)
def cli(list, showname):
    '''Go show'''

    # list all the shows with the option
    if list:
        click.echo('List shows')

    # move into the show
    elif showname:
        click.echo(showname)

    # only goshow
    else:
        click.echo('Currently/Moved under the "Shows" root directory')
        click.echo('''
        USEFUL COMMANDS:
        el goshow --list : To list all the show.
        el goshow [showname] : Move to the [showname] directory is [showname] exists.
        ''')
        GoShow.toRoot()

