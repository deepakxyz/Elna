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
        Asset.asset_list()


    elif type and asset:
        Asset.go_asset(cat=type,asset_name=asset)
