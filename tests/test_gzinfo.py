import os
import pathlib

import pytest

import gzinfo as gz



FIXTURE_FILENAME = pathlib.Path(os.path.dirname(__file__)) / "bar.txt.gz"


def test_read_gz_info_returns_correct_fname():
    info = gz.read_gz_info(FIXTURE_FILENAME)
    assert info is not None
    assert info.fname == "foo.txt"


def test_gzinfo_is_frozen():
    info = gz.GzInfo(fname="foo.txt", method=8, flag=8, last_mtime=0)
    with pytest.raises(Exception):
        info.fname = "bar.txt"
