import click
import os


from el.core.create_shot import CreateShot


@click.command()
@click.argument('seq_num')
def cli(seq_num):
	if CreateShot.check():
		CreateShot.create_shot(seq_num)