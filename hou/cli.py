import click
import os


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("hou_"):
                commands.append(filename.replace("hou_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"hou.commands.hou_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli
        

@click.command(cls=ComplexCLI)
def cli():
    '''Welcome to Hou'''
    pass