# -*- coding: utf-8 -*-


from cli import rm
from constants import DIRSTR, INV_ARG, TXT_FILENAME, TXTSTR, mkdir


def test_rm_success(tmp_path):
    """Test rm_success."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert rm(filename) == 'success'


def test_rm_dir(tmp_path):
    """Test rm_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)
    assert rm(directory) == 'argument is dir'


def test_rm_fail(tmp_path):
    """Test rm_fail."""
    filename = tmp_path / 'someFILENAME'
    assert rm(filename) == 'file not found'


def test_rm_no_filename():
    """Test rm_no_filename."""
    assert rm() == INV_ARG
