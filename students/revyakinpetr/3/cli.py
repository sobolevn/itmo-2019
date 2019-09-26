# -*- coding: utf-8 -*-

import argparse
import os
from datetime import datetime


def create_parser():
    """Creates parser for command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, nargs='*', help='sd')
    return parser


def ls(pathname):
    """Command ls."""
    if pathname == '':
        pathname = '.'
    return set(os.listdir(pathname))  # noqa: C405


def mk(filename):
    """Command mk."""
    file_exists = os.path.isfile(filename)

    if file_exists:
        return ['error']

    try:
        open(filename, 'w').close()  # noqa: WPS515
    except Exception:
        return ['error']

    return ['create {0}'.format(filename)]


def rm(filename):
    """Command rm."""
    file_exists = os.path.isfile(filename)
    if file_exists:
        os.remove(filename)
        return ['remove {0}'. format(filename)]

    forder_exist = os.path.isdir(filename)
    if forder_exist:
        os.rmdir(filename)
        return ['remove {0}'. format(filename)]

    return ['no file or directory to remove']


def contains(path):
    """Command contains."""
    if path in os.listdir():
        return ['code: 0']
    return ['code: 1']


def since(date, path='.'):
    """Command since."""
    try:
        date = datetime.strptime(date, '%d-%m-%Y')
    except Exception:
        return set([])  # noqa: C405
    if os.path.isdir(path):
        listdir = os.listdir(path)
        return set([  # noqa: C403
            itm for itm in listdir
            if date < datetime.fromtimestamp(
                os.path.getctime('{0}/{1}'.format(path, itm)),
            )
        ])
    return set([])  # noqa: C405


def main():
    """Command to start."""
    console_input = create_parser().parse_args().command
    if len(console_input) == 1:
        command = console_input[0]
        argument = ''
    else:
        command, argument = console_input

    command_result = globals()[command](argument)  # noqa: WPS421
    for res in command_result:
        print(res)  # noqa: T001


if __name__ == '__main__':
    main()
