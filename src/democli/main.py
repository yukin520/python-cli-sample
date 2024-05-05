
import click

from democli.click_sample import edit_your_config_file
from democli.click_sample import input_your_params
from democli.click_sample import show_progress
from democli.echo import color_echo


@click.group()
def cli():
    """my demo cli program"""

def main():
    cli.add_command(color_echo)
    cli.add_command(edit_your_config_file)
    cli.add_command(input_your_params)
    cli.add_command(show_progress)

    cli()

if __name__ == "__main__":
    main()