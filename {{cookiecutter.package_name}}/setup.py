from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
   requirements = f.readlines()

setup(
    name='{{cookiecutter.package_name}}',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[req for req in requirements if req[:2] != "# "],
)