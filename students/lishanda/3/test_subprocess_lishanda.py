# -*- coding: utf-8 -*-

import subprocess

from constants import CLISTR, PYSTR, TXT_FILENAME


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
