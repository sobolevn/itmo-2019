# -*- coding: utf-8 -*-


from cli import ls
from constants import TXT_FILENAME, TXTSTR, mkdir


def test_ls_empty_dir(tmp_path):
    """Test ls_empty_dir."""
    assert not ls(tmp_path)


def test_ls_only_dirs(tmp_path):
    """Test ls_only_dirs."""
    directory = tmp_path / 'another_dir'
    mkdir(directory)
    assert len(ls(tmp_path)) == 1


def test_ls_only_files(tmp_path):
    """Test ls_only_files."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert filename.read_text() == TXTSTR
    assert len(ls(tmp_path)) == 1


def test_ls_files_and_dirs(tmp_path):
    """Test ls_files_and_dirs."""
    directory = tmp_path / 'sub'
    mkdir(directory)
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert len(ls(tmp_path)) == 2
