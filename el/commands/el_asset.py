import click
import os

from el.core.asset import Asset
from el.utils.el import el



@click.command()
@click.option('-l', '--list', is_flag=True)
@click.option('-t','--type', required=False)
@click.option('-a', '--asset', required=False)
def cli(list, type, asset):
    if list:
        if Asset.check():
            Asset.asset_list()

        else:
            el.echo('You must be at the project level to list all the existing assets.', lvl="WARNNING") 


    elif type and asset:
        Asset.go_asset(cat=type,asset_name=asset)
