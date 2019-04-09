#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

__author__ = """{{ cookiecutter.full_name }}"""
__contact__ = "{{ cookiecutter.email }}"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "{{ cookiecutter.open_source_license }}"
__version__ = "{{ cookiecutter.version }}"


from setuptools import setup, find_packages

# One strategy for storing the overall version is to put it in the top-level
# package's __init__ but Nb. __init__.py files are not needed to declare
# packages in Python 3
from ceda_example import __version__ as _package_version

# Populate long description setting with content of README
#
# Use markdown format read me file as GitHub will render it automatically
# on package page
with open("README.md") as readme_file:
    _long_description = readme_file.read()


requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %} ]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %} ]


setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',

    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description="{{ cookiecutter.project_short_description }}",

    license='BSD - See LICENSE file for details',

    # This qualifier can be used to selectively exclude Python versions -
    # in this case early Python 2 and 3 releases
    python_requires='>=3.5.0',

    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
    long_description=_long_description,
    long_description_content_type='text/markdown',

    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
