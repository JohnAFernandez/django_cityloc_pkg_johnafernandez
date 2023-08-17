from setuptools import setup, find_packages

# put the contents of your README file into the long_description
from pathlib import Path
this_directory = Path(__file__).parent

print(this_directory)
print(this_directory / "README.rst")

try:
    long_description = Path("/home/runner/work/django_cityloc_pkg_johnafernandez/README.rst").read_text()
except:
    try:
        long_description = Path(this_directory / "README.rst").read_text()
    except:
        long_description = "Yeah, it's not working champ."


setup(
    long_description=long_description
)