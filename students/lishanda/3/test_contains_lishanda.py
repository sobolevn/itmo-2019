# -*- coding: utf-8 -*-

import pytest  # noqa I003
from constants import M_NUMBER, TXT_FILENAME, INV_ARG, PYSTR, CLISTR  # noqa I001
from constants import DIRSTR, TXTSTR, earlier_than_now_timestamp, mkdir  # noqa F401, I001
from cli import contains, mk, rm


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
