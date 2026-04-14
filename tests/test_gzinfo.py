import os
import pytest
import gzinfo as gz


FIXTURE = os.path.join(os.path.dirname(__file__), "bar.txt.gz")


def test_gzinfo_is_frozen():
    info = gz.GzInfo(fname="foo.txt", method=8, flag=8, last_mtime=0)
    with pytest.raises(Exception):
        info.fname = "bar.txt"
