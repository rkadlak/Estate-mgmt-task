from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in estate_management/__init__.py
from estate_management import __version__ as version

setup(
	name="estate_management",
	version=version,
	description="estate management",
	author="rohit",
	author_email="rkadlak@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
