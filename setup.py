# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('boardgame/boardgame.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "boardgame",
    packages = ["boardgame"],
    entry_points = {
        "console_scripts": ['boardgame = boardgame.boardgame:main']
        },
    version = version,
    description = "Python command line application to simulate board game.",
    long_description = long_descr,
    author = "Leo Benkel",
    author_email = "leo.benkel@gmail.com",
    url = "",
    )