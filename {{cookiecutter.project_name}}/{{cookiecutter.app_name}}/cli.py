# vim: set fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 softtabstop=4:
import logging
import os
import sys

import click

from __version__ import __version__


def setup_logger(quiet=False, verbose=False):
	"""日志初始化

	Args:
		args (Dict[string, string]): 命令行参数
	"""
	log_format = u'%(asctime)s %(levelname)s %(message)s'

	if quiet:
		logging.basicConfig(level=logging.WARNING, format=log_format)
	elif verbose:
		logging.basicConfig(level=logging.DEBUG, format=log_format)
	else:
		logging.basicConfig(level=logging.INFO, format=log_format)


@click.command()
@click.version_option(
    prog_name='{{cookiecutter.app_name}}', version=__version__
)
@click.option(
    '--quiet',
    '-q',
    is_flag=True,
    default=False,
    help="Quiet mode."
)
@click.option(
    '--verbose',
    '-v',
    is_flag=True,
    default=False,
    help="Verbose mode."
)
@click.argument('argument')
def cli(
        argument,
        help=False,
        quiet=False,
        verbose=False
):
    setup_logger(quiet=quiet, verbose=verbose)


if __name__ == '__main__':
    cli()
