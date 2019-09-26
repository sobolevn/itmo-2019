# -*- coding: utf-8 -*-

import argparse
import os
from datetime import datetime


def create_parser():
    """Creates parser for command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        type=str,
        help='ls/mk/rm/contains/since',
    )
    return parser


def ls(path: str) -> dict:
    """Returns folders in files in specified path."""
    if not path:
        path = '.'
    full_path = '{0}/{1}'.format(os.getcwd(), path)
    _, dirs, files = next(os.walk(full_path), (None, [], []))  # noqa: WPS221
    return {'folders': set(dirs), 'files': set(files)}


def mk(filename: str) -> dict:
    """Creates a file with filename if it does not exist."""
    if os.path.exists(filename):
        raise FileExistsError
    else:
        open(filename, 'w').close()  # noqa: WPS515
    return {'filename': {filename}}


def rm(filename: str) -> dict:
    """Removes the specified file."""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        raise FileNotFoundError
    return {'removed': {filename}}


def contains(filename: str) -> dict:
    """Shows if the specified file is present in the current directory."""
    if os.path.isfile(filename):
        if os.path.exists(filename):
            return {'result': '1'}
    return {'result': '0'}


def since(pathname, time):  # noqa: WPS210
    """Returns all the files and dirs from cd created after specified date."""
    target_time = datetime.strptime(time, '%d.%m.%Y %H:%M:%S')
    inside_contents = ls(pathname)
    created_after = {'files': set(), 'folders': set()}
    for key, filee in inside_contents.items():
        for it in filee:
            birth_time = datetime.utcfromtimestamp(os.path.getctime(pathname))
            if birth_time > target_time:
                created_after[key].add(it)
    return created_after


def display_results(to_display: dict):
    """Displays dict in a human-readable form."""
    for key, word in to_display.items():
        if word:
            print('{0}:'.format(key.upper()))  # noqa: T001
            print('\n'.join(word))  # noqa: T001


if __name__ == '__main__':
    raw_input = create_parser().parse_args().command
    if len(raw_input.split()) == 1:
        command, argument = raw_input, ''
    else:
        command, argument = raw_input.split()
    display_results(locals()[command](argument))  # noqa: WPS421
