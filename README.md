# Gzip Information
[![Build Status](https://travis-ci.com/PierreSelim/gzinfo.svg?branch=master)](https://travis-ci.com/PierreSelim/gzinfo)

Getting the original filename form gzip archive in Python (compatible with
Python 3.6, 3.7 and 3.8).

## Install
from github directly:

```
pip install git+https://github.com/PierreSelim/verysimplestats.git
```

## Usage

If you gzip a file called `foo.txt` and rename the archive `bar.txt` you can 
still retrive the original name from the header (per 
[RFC1952](https://tools.ietf.org/html/rfc1952))

```python
>>> import gzinfo
>>> info = gzinfo.read_gz_info('bar.txt.gz')
>>> info.fname
'foo.txt'
```
