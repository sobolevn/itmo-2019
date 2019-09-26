# -*- coding: utf-8 -*-

import os

from constants import FORMAT_CONSTANT, FOLDERS, FILES, FILE_NOT_FOUND, FILE_EXISTS, FILE, FOLDER  # noqa: E501, I001


def mk_dir(dirname):
    """Create folder specified by dirname."""
    if not os.path.exists(dirname):
        os.mkdir(dirname)


def mk_file(filename):
    """Create a file specified by filename."""
    if not os.path.exists(filename):
        open(filename, 'w').close()  # noqa: WPS515


def setup_ls(pc):
    """Set up the environment to test the ls function."""
    mk_dir(pc[0])
    for folder in pc[1][FOLDERS]:
        mk_dir(FORMAT_CONSTANT.format(pc[0], folder))
    for filee in pc[1][FILES]:
        mk_file(FORMAT_CONSTANT.format(pc[0], filee))


def setup_mk(pc):
    """Set up the environment to test the mk function."""
    filename, expected = pc
    if expected == FILE_EXISTS:
        mk_file(filename)


def setup_rm(pc):
    """Set up the environment to test the rm function."""
    object_type, object_name, exception = pc
    if exception != FILE_NOT_FOUND:
        if object_type == FOLDER:
            mk_dir(object_name)
        elif object_type == FILE:
            mk_file(object_name)


def setup_contains(pc):
    """Set up the environment to test the contains function."""
    object_type, object_name, expected = pc
    if object_type == FILE and expected == '1':
        mk_file(object_name)
    elif object_type == FOLDER:
        mk_dir(object_name)


def setup_since(pc):
    """Set up the environment to test the ls function."""
    setup_ls(pc)
