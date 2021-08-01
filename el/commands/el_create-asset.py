import click
import os

from el.core.asset import CreateAsset, Asset



@click.command()
@click.argument('asset_name')
def cli(asset_name):
    if CreateAsset.check():

        create_asset = CreateAsset()

        # get and check project type
        click.echo('Must be from the following type')
        click.echo(create_asset.asset_types)
        type = click.prompt('Asset type')
        if type in create_asset.asset_types:


            if create_asset.check_if_exists(asset_name, type):


                # get asset description
                desc = click.prompt('Asset description')

                # create asset build directory
                create_asset.create_directory(asset_name,type, desc)

                # create asset directory
                create_asset.create_asset_directory(asset_name, type, desc)


                # move to asset
                Asset.go_asset(cat=type, asset_name=asset_name)
            
            else:

                # Asset already exists
                click.echo(f'Asset "{asset_name}" already exists in the type "{type}"')
        
        else:
            click.echo(f'"{type}" is not a valid type')

    else:
        msg = '''
        You must be inside any show to create new asset.
        '''
        print(msg)