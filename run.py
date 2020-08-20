#!/usr/bin/python3
# coding=utf-8

#######################################################
######################BlackMafia#######################
#######################################################

import shutil, platform

py_version = platform.python_version()

if py_version < '3.7':
    exit('WARNING you are using python version %s please upgrade to 3.7++'%(py_version))

cache = ['lib.py/__pycache__', 'MBF.py/__pycache__', 'store.py/__pycache__', 'app.py/__pycache__', 'CLI.py/__pycache__', 'http.py/__pycache__', 'login.py/__pycache__', 'brute.py/__pycache__', 'dump.py/__pycache__', 'fb.py/__pycache__']

for path in cache:
    try:
        shutil.rmtree(path)
    except:
        pass

__import__('login.app')
