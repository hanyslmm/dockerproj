#! /usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello Hany!')

if __name__ == '__main__':
    hello()