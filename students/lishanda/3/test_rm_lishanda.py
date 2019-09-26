# -*- coding: utf-8 -*-

import pytest  # noqa I003
from constants import M_NUMBER, TXT_FILENAME, INV_ARG, PYSTR, CLISTR  # noqa I001
from constants import DIRSTR, TXTSTR, earlier_than_now_timestamp, mkdir  # noqa F401, I001
from cli import rm


def test_rm_success(tmp_path):
    """Test rm_success."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert rm(filename) == 'success'


def test_rm_dir(tmp_path):
    """Test rm_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)  # noqa WPS204
    assert rm(directory) == 'argument is dir'


def test_rm_fail(tmp_path):
    """Test rm_fail."""
    filename = tmp_path / 'someFILENAME'
    assert rm(filename) == 'file not found'


def test_rm_no_filename():
    """Test rm_no_filename."""
    assert rm() == INV_ARG
