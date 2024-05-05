
import os
import time

import click


@click.command("edit-file", short_help='You can edit file that spcified by you.')
@click.option('--file-path', prompt='input file path  that you want edit', type=str)
def edit_your_config_file(file_path):
    if not os.path.exists(file_path):
        click.secho(f'Do not found file that you specified. >> {file_path}', fg='red', err=True)

    click.echo(f'You can edit this file. >> {file_path}/n')

    click.edit(filename=file_path)

    with open(file_path, "r") as f:
        lines = f.read()
        click.echo_via_pager(lines)

    click.echo('Command finished.')


@click.command("show-progress", short_help="You can show progress time that specified by --seconds option.")
@click.option('--total-seconds', type=int, prompt='input seconds which belong to you want to show progress.')
@click.option('--between-seconds', 
              type=int, 
              prompt='input seconds which wait betwwen progress.',
              required=False,
              default=1)
def show_progress(total_seconds, between_seconds):
    with click.progressbar(range(1, total_seconds, between_seconds)) as bar:
        for x in bar:
            click.echo(f'  sleep({x}/{total_seconds})...')
            time.sleep(between_seconds)

    click.secho('\n Finished command!!' , fg='blue')


@click.command("show-param", short_help='show sample parametors.')
@click.option('--param', prompt='input your param')
def input_your_params(param):
    click.secho(f'Your param is >> {param}', fg='green')

    click.echo('Continue? [y/n] ', nl=False)
    c = click.getchar()
    click.echo()
    if c == 'y':
        click.echo('We will go on')
    elif c == 'n':
        click.echo('Abort!')
        return
    else:
        click.echo('Invalid input :(')
        return
    
    click.echo('\nYou must enter any key to continue.')
    click.pause()