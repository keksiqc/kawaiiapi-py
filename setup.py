from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kawaiiapi',
    version='1.2.2',
    author='Keksiqc',
    author_email='cotact@keksi.me',
    license='MIT',
    description='The kawaii api from Error44 as python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "aiohttp >= 3.6"
    ],
    url='https://github.com/keksiqc/kawaiiapi-py',
    py_modules=['kawaiiapi'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
