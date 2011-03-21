#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
import os, sys

version = '0.1.0'

install_requires = [
    "instapaperlib>=0.4.0",
]

setup(
    name="instayc",
    version=version,
    description="Python tool for auto adding hacker news articles to
    instapaper.",
    long_description=(open("README.md").read()),
    author="Jarod Luebbert",
    author_email="jarodluebbert@gmail.com",
    url="http://github.com/jarodl/instayc",
    packages=["instayc"],
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
    entry_points="""
    # -*- Entry points: -*-
    [console scripts]
    instayc=instayc.cmdline:main
    """,
    license="MIT",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    )
)
