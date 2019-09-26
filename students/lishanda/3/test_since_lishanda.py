# -*- coding: utf-8 -*-


from cli import since
from constants import (
    DIRSTR,
    INV_ARG,
    M_NUMBER,
    TXT_FILENAME,
    TXTSTR,
    mkdir,
)


def test_since_not_existing_dir(tmp_path):
    """Test since_not_existing_dir."""
    directory = tmp_path / DIRSTR
    assert since(M_NUMBER, directory) == 'dir not found'


def test_since_empty_dir(tmp_path):
    """Test since_empty_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)
    assert since(M_NUMBER, directory) == 'dir is empty'


def test_since_only_dirs(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_only_dirs."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    adirectory = directory / 'another dir'
    adirectory.mkdir()
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 1


def test_since_only_files(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_only_files."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    filename = directory / TXT_FILENAME
    filename.write_text('test')
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 1


def test_since_dirs_and_files(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_dirs_and_files."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    subdir = directory / 'subdir'
    subdir.mkdir()
    filename = directory / TXT_FILENAME
    filename.write_text(TXTSTR)
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 2


def test_since_invalid_date():
    """Test since_invalid_date."""
    assert since('abcd') == INV_ARG


def test_since_no_date():
    """Test since_no_date."""
    assert since() == INV_ARG
