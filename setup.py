from setuptools import setup, find_packages

# put the contents of your README file into the long_description
from pathlib import Path
this_directory = Path(__file__).parent

print(this_directory)
print(this_directory / "README.rst")

long_description = (this_directory / "README.rst").read_text()

setup(
    long_description=long_description
)