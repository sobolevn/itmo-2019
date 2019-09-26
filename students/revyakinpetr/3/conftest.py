# -*- coding: utf-8 -*-

import os
import shutil

import pytest

SCOPE = 'module'
TESTTXT = 'test.txt'
TEST = 'test'
TESTDATE = '10-03-2019'


def create_file(filename):
    """Creation file."""
    open(filename, 'w').close()  # noqa: WPS515


@pytest.fixture(scope=SCOPE, params=[
    ('ls_empty', []),
    ('ls_files', [TESTTXT]),
    ('ls_directories', [TEST]),
    ('ls_files_directories', [TEST, TESTTXT]),
])
def ls_fixture(request):
    """Fixture for ls."""
    dirname, filelist = request.param
    os.mkdir(dirname)
    for fln in filelist:
        formatname = '{0}/{1}'.format(dirname, fln)
        if len(fln.split('.')) > 1:
            create_file(formatname)
        else:
            os.mkdir(formatname)

    yield request.param
    if os.path.exists(dirname):
        shutil.rmtree(dirname)


@pytest.fixture(scope=SCOPE, params=[
    (TESTTXT, False, True),
    ('тест.txt', False, True),
    (TESTTXT, True, True),
    ('test/..', False, False),
])
def mk_fixture(request):
    """Fixture for mk."""
    filename, pre_exist, post_exist = request.param
    if pre_exist:
        create_file(filename)

    yield request.param

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope=SCOPE, params=[
    (TESTTXT, True, False),
    ('nodirectory', False, False),
    ('test2.txt', False, False),
])
def rm_fixture(request):
    """Fixture for rm."""
    filename, pre_exist, post_exist = request.param
    if pre_exist:
        create_file(filename)

    yield request.param

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope=SCOPE, params=[
    ('тест.txt', ['code: 0']),
    ('wrong.txt', ['code: 1']),
    ('testdir', ['code: 1']),
])
def contains_fixture(request):
    """Fixture for contains."""
    filename, status = request.param
    if status == ['code: 0']:
        create_file(filename)

    yield request.param

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope=SCOPE, params=[
    ('since_empty', TESTDATE, []),
    ('since_files', TESTDATE, [TESTTXT]),
    ('since_directories_files', TESTDATE, [TEST, TESTTXT]),
    ('since_directories', TESTDATE, [TEST]),
    ('since_empty', '33-33-3333', []),
])
def since_fixture(request):
    """Fixture for since."""
    path, date, test_list = request.param

    os.mkdir(path)
    for fln in test_list:
        formatname = '{0}/{1}'.format(path, fln)
        if len(fln.split('.')) > 1:
            create_file(formatname)
        else:
            os.mkdir(formatname)

    yield request.param
    if os.path.exists(path):
        shutil.rmtree(path)


@pytest.fixture(scope=SCOPE, params=[
    ('ls', '', 0),
    ('mk', TESTTXT, 0),
    ('contains', TESTTXT, 0),
    ('since', TESTDATE, 0),
    ('rm', TESTTXT, 0),
])
def integration_fixture(request):
    """Fixture for integration."""
    yield request.param
