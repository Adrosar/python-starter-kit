#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dokumentacja http://www.pyinvoke.org
"""

from invoke import task, run
from shutil import rmtree

if __name__ == "__main__":
    exit()


@task
def clean(_):
    rmtree("./.mypy_cache", ignore_errors=True)
    rmtree("./app/__pycache__", ignore_errors=True)
    print("-> CLEAN :)")


@task
def start(_):
    print("-> Start app/main.py")
    run("\"venv/Scripts/python\" app/main.py")
