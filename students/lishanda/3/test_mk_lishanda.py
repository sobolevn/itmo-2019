# -*- coding: utf-8 -*-

import pytest  # noqa I003
from constants import M_NUMBER, TXT_FILENAME, INV_ARG, PYSTR, CLISTR  # noqa I001
from constants import DIRSTR, TXTSTR, earlier_than_now_timestamp, mkdir  # noqa F401, I001
from cli import mk


def test_mk_no_filename():
    """Test mk_no_filename."""
    assert mk() == INV_ARG


def test_mk_en_filename(tmp_path):
    """Test mk_en_filename."""
    filename = tmp_path / TXT_FILENAME
    assert mk(filename) == 'success'


def test_mk_ru_filename(tmp_path):
    """Test mk_ru_filename."""
    filename = tmp_path / 'файл.txt'
    assert mk(filename) == 'success'


def test_mk_duplicate(tmp_path):
    """Test mk_duplicate."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert mk(filename) == 'file already exists'


def test_mk_invalid_filename(tmp_path):
    """Test mk_invalid_filename."""
    filename = tmp_path / 'f/1/l/e.txt'
    assert mk(filename) == 'invalid filename'
