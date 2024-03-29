
# Py3 Service Template

[![Build Status](https://travis-ci.com/AlcheraInc/py3-service-template.svg?branch=master)](https://travis-ci.com/AlcheraInc/py3-service-template)

Basic setup for service prototyping in Alchera Inc.

### References

* gRPC + Python 3
    * https://www.grpc.io/docs/tutorials/basic/python/
    * https://www.sandtable.com/using-ssl-with-grpc-in-python/
* Build
    * https://docs.travis-ci.com/user/languages/python/
    * https://blog.travis-ci.com/2019-08-07-extensive-python-testing-on-travis-ci

## Note

### Environment

* OS: Expect **Ubuntu Linux** for `master` branch
* Python 3.6 +
    * PIP 19 +

## [How To](./.travis.yml)

### Develop

Open documents with [MkDocs](https://www.mkdocs.org/).

```console
user@host:/py3-service-template$ mkdocs serve
INFO    -  Building documentation... 
INFO    -  Cleaning site directory 
[I 191101 12:03:15 server:296] Serving on http://127.0.0.1:8000
[I 191101 12:03:15 handlers:62] Start watching changes
[I 191101 12:03:15 handlers:64] Start detecting changes
...
```

### Test

Simply run PyTest

```console
user@host:/py3-service-template$ pytest .
================================ test session starts =================================
platform linux -- Python 3.7.3, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
...
```
