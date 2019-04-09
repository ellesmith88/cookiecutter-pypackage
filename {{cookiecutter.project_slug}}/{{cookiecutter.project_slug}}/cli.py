# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""

__author__ = """{{ cookiecutter.full_name }}"""
__contact__ = "{{ cookiecutter.email }}"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "{{ cookiecutter.open_source_license }}"

import sys
import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
