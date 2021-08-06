import click
import os

from el.core.create_shot import CreateSeq


@click.command()
@click.argument('seq_name', nargs=-1)
def cli(seq_name):
	if len(seq_name) > 0:
		seq_name = list(seq_name)
		seq_name = seq_name[0]
	else:
		seq_name = None

	if CreateSeq.check():

		CreateSeq.create_seq(seq_name=seq_name)