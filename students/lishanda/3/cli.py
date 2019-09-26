# -*- coding: utf-8 -*-

import argparse
import os
import sys

WRONG_ARGUMENT = 'wrong argument'


def main(commands, module):
    """Main."""
    if hasattr(module, commands[0]):  # noqa WPS421
        arg = commands[1] if len(commands) > 1 else None
        getattr(module, commands[0])(arg)  # noqa WPS421
    else:
        print('Unknown command passed')  # noqa T001


def ls(arg=None):
    """ls."""
    directory = os.getcwd() if arg is None else arg
    files = [file_object.name for file_object in os.scandir(directory) if file_object.is_file()]  # noqa E501
    dirs = [folder.name for folder in os.scandir(directory) if folder.is_dir()]
    return files + dirs


def mk(arg=None):
    """mk."""
    if not arg:
        return WRONG_ARGUMENT
    if os.path.exists(arg):
        return 'file already exists'
    try:
        open(arg, 'a').close()  # noqa WPS515
    except OSError:
        return 'invalid filename'
    return 'success'


def rm(arg=None):
    """rm."""
    if not arg:
        return 'wrong argument'
    if os.path.isdir(arg):
        return 'argument is dir'
    if not os.path.exists(arg):
        return 'file not found'
    os.remove(arg)
    return 'success'


def contains(arg=None):
    """contains."""
    if not arg:
        return WRONG_ARGUMENT
    if os.path.isdir(arg):
        return 'argument is dir'
    return 0 if arg in ls() else 1


def since(timestamp=None, directory=os.getcwd()):  # noqa WPS404, B008
    """since."""
    if not timestamp:
        return WRONG_ARGUMENT
    try:
        timestamp = int(timestamp)
    except Exception:
        return WRONG_ARGUMENT
    if not os.path.exists(directory):
        return 'dir not found'
    dir_content = ls(directory)
    if not dir_content:
        return 'dir is empty'
    return [
        item_object for item_object in dir_content if os.stat('{0}/{1}'.format(
            directory,
            item_object,
        )).st_ctime > timestamp
    ]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, nargs='*', help='Command')
    args = parser.parse_args()

    current_module = sys.modules[__name__]
    main(args.command, current_module)
