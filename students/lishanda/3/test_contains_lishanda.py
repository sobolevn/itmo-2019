# -*- coding: utf-8 -*-


from cli import contains, mk, rm
from constants import DIRSTR, INV_ARG, TXT_FILENAME, mkdir


def test_contains_no_filename():
    """Test contains_no_filename."""
    assert contains() == INV_ARG


def test_contains_success():
    """Test contains_success."""
    mk(TXT_FILENAME)
    assert contains(TXT_FILENAME) == 0
    rm(TXT_FILENAME)


def test_contains_dir(tmp_path):
    """Test contains_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)  # noqa WPS204
    assert contains(directory) == 'argument is dir'


def test_contains_non_existing_file():
    """Test contains_non_existing_file."""
    assert contains('non_existing_FILENAME') == 1
