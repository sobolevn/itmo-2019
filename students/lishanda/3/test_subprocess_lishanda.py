# -*- coding: utf-8 -*-

import pytest  # noqa I003
import subprocess  # noqa S404
from constants import M_NUMBER, TXT_FILENAME, INV_ARG, PYSTR, CLISTR  # noqa I001

from constants import DIRSTR, TXTSTR, earlier_than_now_timestamp, mkdir  # noqa F401, I001


def test_ls_integration():
    """Test ls_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'ls']) == 0


def test_contains_integration():
    """Test contains_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'contains', TXT_FILENAME]) == 0


def test_mk_integration():
    """Test mk_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'mk', TXT_FILENAME]) == 0


def test_rm_integration():
    """Test rm_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'rm', 'someFILENAME']) == 0


def test_since_integration():
    """Test since_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'since', '0']) == 0
