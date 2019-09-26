# -*- coding: utf-8 -*-

import os
import subprocess

from cli import ls, mk, rm, contains, since  # noqa: I001


def test_ls(ls_fixture):
    """Testing ls command."""
    pathname, test_list = ls_fixture
    assert ls(pathname) == set(test_list)  # noqa: C405


def test_mk(mk_fixture):
    """Testing mk command."""
    filename, pre_exist, post_exist = mk_fixture
    assert os.path.isfile(filename) == pre_exist
    mk(filename)
    assert os.path.isfile(filename) == post_exist


def test_rm(rm_fixture):
    """Testing rm command."""
    filename, pre_exist, post_exist = rm_fixture
    assert os.path.isfile(filename) == pre_exist
    rm(filename)
    assert os.path.isfile(filename) == post_exist


def test_contains(contains_fixture):
    """Testing contains command."""
    filename, status = contains_fixture
    assert contains(filename) == status


def test_since(since_fixture):
    """Testing since command."""
    path, date, test_list = since_fixture
    assert since(date, path) == set(test_list)  # noqa: C405


def test_integration(integration_fixture):
    """Testing integration command."""
    comand, argument, code = integration_fixture
    format_str = 'python students/revyakinpetr/3/cli.py {0} {1}'
    comand_str = format_str.format(comand, argument)
    assert subprocess.call(comand_str, shell=True) == code  # noqa: S602
