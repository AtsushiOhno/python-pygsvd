from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages
from codecs import open

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="pygsvd",
    version="0.0.1",
    description="",
    license="MIT",
    url="https://github.com/AtsushiOhno/python-pygsvd",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    install_requires=_requires_from_file("requirements.txt"),
    dependency_links=[],
    python_requires='~=3.3',
)