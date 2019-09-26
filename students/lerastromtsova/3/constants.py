# -*- coding: utf-8 -*-

from contextlib import contextmanager
from datetime import datetime

import pytest

TEST_DIR = 'test_dirs'
FORMAT_CONSTANT = '{0}/{1}'

SCOPE = 'module'
FOLDER = 'folder'
FILE = 'file'

FOLDERS = 'folders'
FILES = 'files'
FILE_NOT_FOUND = pytest.raises(FileNotFoundError)
FILE_EXISTS = pytest.raises(FileExistsError)
NOW = datetime.now()
TEST_DATE = NOW.replace(year=NOW.year - 3).strftime('%d.%m.%Y %H:%M:%S')


@contextmanager
def does_not_raise():
    """Empty function that is used to show there is no Exception."""
    yield
