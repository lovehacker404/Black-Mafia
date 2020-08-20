#!/usr/bin/python3
# coding=utf-8
#Python version : 3.8+                               #
#######################################################
#################################################

import shutil, platform

py_version = platform.python_version()

if py_version < '3.7':
    exit('WARNING anda menggunakan python version %s silahkan upgrade ke 3.7++'%(py_version))

cache = ['src/__pycache__', 'src/data/__pycache__']

for path in cache:
    try:
        shutil.rmtree(path)
    except:
        pass

__import__('src.app')
