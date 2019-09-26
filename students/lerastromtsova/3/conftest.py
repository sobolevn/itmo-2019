# -*- coding: utf-8 -*-

import os
import shutil

import pytest

from setups import mk_dir, setup_ls, setup_mk, setup_rm, setup_contains, setup_since  # noqa: E501, I001
from constants import does_not_raise, TEST_DIR, FOLDERS, FILES, FOLDER, FILE, SCOPE, FILE_NOT_FOUND, FILE_EXISTS, TEST_DATE  # noqa: E501, I001


@pytest.fixture(scope=SCOPE, params=[
    ('{0}/empty_dir-ls'.format(TEST_DIR), {FOLDERS: set(), FILES: set()}),
    ('{0}/folders-ls'.format(TEST_DIR), {FOLDERS: {FOLDER}, FILES: set()}),
    ('{0}/files-ls'.format(TEST_DIR), {FOLDERS: set(), FILES: {FILE}}),
    (
        '{0}/files_folders-ls'.format(TEST_DIR),
        {FOLDERS: {'dir1', 'dir2'}, FILES: {'file1', 'file2'}},
    ),
])
def fixture_ls(request):
    """A fixture to test the ls function."""
    mk_dir(TEST_DIR)
    setup_ls(request.param)
    yield request.param


def teardown():
    """Delete the test folder after tests execution."""
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)


@pytest.fixture(scope=SCOPE, params=[
    ('{0}/тест-мк.txt'.format(TEST_DIR), does_not_raise()),
    ('{0}/test-mk.txt'.format(TEST_DIR), does_not_raise()),
    ('{0}/test-mk.txt'.format(TEST_DIR), FILE_EXISTS),
    ('{0}/..'.format(TEST_DIR), pytest.raises(Exception)),
])
def fixture_mk(request):
    """A fixture to test the mk function."""
    mk_dir(TEST_DIR)
    setup_mk(request.param)
    yield request.param


@pytest.fixture(scope=SCOPE, params=[
    (FILE, '{0}/test-rm.txt'.format(TEST_DIR), does_not_raise()),
    (FOLDER, '{0}/folder-rm'.format(TEST_DIR), pytest.raises(Exception)),
    (FILE, '{0}/nonexistent-rm.txt'.format(TEST_DIR), FILE_NOT_FOUND),
])
def fixture_rm(request):
    """A fixture to test the rm function."""
    mk_dir(TEST_DIR)
    setup_rm(request.param)
    yield request.param


@pytest.fixture(scope=SCOPE, params=[
    (FILE, '{0}/test-contains.txt'.format(TEST_DIR), '1'),
    (FILE, '{0}/nonexistent-contains.txt'.format(TEST_DIR), '0'),
    (FOLDER, '{0}/test-contains'.format(TEST_DIR), '0'),
])
def fixture_contains(request):
    """A fixture to test the contains function."""
    mk_dir(TEST_DIR)
    setup_contains(request.param)
    yield request.param


@pytest.fixture(scope=SCOPE, params=[
    (
        '{0}/empty_dir-since'.format(TEST_DIR),
        {FOLDERS: set(), FILES: set()},
        TEST_DATE,
        does_not_raise(),
    ),
    (
        '{0}/folders-since'.format(TEST_DIR),
        {FOLDERS: {FOLDER}, FILES: set()},
        TEST_DATE,
        does_not_raise(),
    ),
    (
        '{0}/files-since'.format(TEST_DIR),
        {FOLDERS: set(), FILES: {FILE}},
        TEST_DATE,
        does_not_raise(),
    ),
    (
        '{0}/files_folders-since'.format(TEST_DIR),
        {FOLDERS: {'dir1', 'dir2'}, FILES: {'file1', 'file2'}},
        TEST_DATE,
        does_not_raise(),
    ),
    (
        '{0}/other-since'.format(TEST_DIR),
        {FOLDERS: set(), FILES: set()},
        'not-valid-date',
        pytest.raises(Exception),
    ),
])
def fixture_since(request):
    """A fixture to test the ls function."""
    mk_dir(TEST_DIR)
    setup_since(request.param)
    yield request.param


@pytest.fixture(scope=SCOPE, params=[
    # command, argument, expected result
    ('ls', '', 0),
    ('mk', 'test.py', 0),
    ('contains', 'test.py', 0),
    ('since', TEST_DATE, 0),
    ('rm', 'test.py', 0),
])
def fixture_integration(request):
    """A fixture to perform integration testing."""
    yield request.param
    teardown()
