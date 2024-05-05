

import click
from rich import print
from rich.style import Style
from rich.text import Text

OUTPUT_COLORS = ["white", "black", "blue", "red", "yellow", "green"]

@click.command("color-echo", short_help='Output word to console.')
@click.option("--word",
             required=True,
             type=str,
             default=None,
             help="Soecify output word.")
@click.option("--color",
             required=False,
             type=click.Choice(OUTPUT_COLORS, case_sensitive=False),
             default="white",
             help="Soecify output color.")
def color_echo(word,color):
    text = Text()
    output_style = Style(color=color, blink=True, bold=True)
    text.append(word,style=output_style)
    
    print(text)