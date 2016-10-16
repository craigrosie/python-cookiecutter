"""
setup.py for zephyr.

The version of the package made from `pip wheel --no-deps .` is taken from the
`package_version` environment variable.
"""

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements(
    'requirements.txt',
    session=PipSession()
)
install_reqs = [str(req.req) for req in install_reqs]

setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    packages=find_packages('.'),
    description='{{cookiecutter.project_description}}',
    author='{{cookiecutter.author}}',
    install_requires=install_reqs,
    classifiers=[]
)
