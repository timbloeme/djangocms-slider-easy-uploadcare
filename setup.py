#!/usr/bin/env python
import os
import djangocms_slideshow

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_slideshow.__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

INSTALL_REQUIRES = [
    "django>=1.8.0, <1.9",
    "django-cms>=3.0",
    "sorl-thumbnail",
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Natural Language :: Dutch',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name="djangocms-slideshow",
    version=version,
    author="Urga Creatieve Communicatie",
    author_email="dries@urga.be",
    description="A simple django cms slideshow plugin",
    license="BSD",
    keywords=["slideshow", "django", "cms", "plugin"],
    url="https://github.com/urga/djangocms-slideshow",
    packages=['djangocms_slideshow', ],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    long_description=read('README.md'),
    include_package_data=True,
    zip_safe=False
)
