from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "harpy",
    version = "1.0.0",
    author = "Babyblue Robotics",
    author_email = "bshah@ieee.org",
    description = ("Python library to control real/simulated hardware and robotics."),
    url = "https://github.com/babyblue-robotics/harpy.git",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    install_requires=['numpy']
)