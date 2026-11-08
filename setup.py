from setuptools import setup, PEP420PackageFinder

with open('requirements.txt', 'r') as infile:
    requirements = [line.strip() for line in infile.readlines()]

setup(
    name='XS A10',
    description='XS A10',
    author='barmedareyansh01@gmail.com',
    install_requires=requirements,
    include_package_data=True
)
