# -*- coding: utf-8 -*-

import pytest  # noqa I003

M_NUMBER = 123
TXT_FILENAME = 'file.txt'
INV_ARG = 'wrong argument'
PYSTR = 'python'
CLISTR = 'students/lishanda/3/cli.py'
DIRSTR = 'dir'
TXTSTR = ''


@pytest.fixture
def earlier_than_now_timestamp():
    """Timestamp."""
    from datetime import datetime  # noqa WPS433
    return int(datetime.timestamp(datetime.now())) - 10


def mkdir(directory):
    """Mkdir func."""
    directory.mkdir()
