#!/usr/bin/env python
# encoding: UTF-8

import ast
import os.path
import sys

from setuptools import setup

deps = [
    "Chameleon>=2.24",
    "ruamel.yaml>=0.10.12"
]
maj, min_, micro, rl, ser = sys.version_info
if (maj, min_) < (2, 7):
    deps += [
        "argparse>=1.4",
        "backport_collections>=0.1",
        "futures>=3.0.3"
    ]
if (maj, min_) < (3, 3):
    deps += [
        "requests-futures>=0.9.5"
    ]
if (maj, min_) == (3, 3):
    deps += [
        "asyncio>=3.4.3"
    ]
if (maj, min_) < (3, 4):
    deps += [
        "singledispatch>=3.4.0.3"
    ]
print(deps)

try:
    # For setup.py install
    from vjobs import __version__ as version
except ImportError:
    # For pip installations
    version = str(ast.literal_eval(
                open(os.path.join(os.path.dirname(__file__),
                "vjobs", "__init__.py"),
                'r').read().split("=")[-1].strip()))

__doc__ = open(os.path.join(os.path.dirname(__file__), "README.rst"),
               'r').read()

setup(
    name="vjobs",
    version=version,
    description="Link budget calculations for telecommunications engineers",
    author="D Haynes",
    author_email="dave@thuswise.co.uk",
    url="https://bitbucket.org/vjobs/vjobs",
    long_description=__doc__,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "License :: Other/Proprietary License",
    ],
    packages=[
        "vjobs",
        "vjobs.test",
    ],
    package_data={
        "vjobs": [
            "doc/*.rst",
            "doc/_templates/*.css",
            "doc/html/*.html",
            "doc/html/*.js",
            "doc/html/_sources/*",
            "doc/html/_static/css/*",
            "doc/html/_static/font/*",
            "doc/html/_static/js/*",
            "doc/html/_static/*.css",
            "doc/html/_static/*.gif",
            "doc/html/_static/*.js",
            "doc/html/_static/*.png",
        ],
    },
    install_requires=deps,
    extras_require={
        "docbuild": [
            "babel<=1.3,>2.0",
            "sphinx-argparse>=0.1.15",
            "sphinxcontrib-seqdiag>=0.8.4",
        ],
    },
    tests_require=[
    ],
    entry_points={
        "console_scripts": [
            "vjobs = vjobs.workflow.main:run",
        ],
    },
    zip_safe=False
)
