"""
refs:
    - setup tools: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages
    - https://stackoverflow.com/questions/70295885/how-does-one-install-pytorch-and-related-tools-from-within-the-setup-py-install
"""
from setuptools import setup
from setuptools import find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SHED-Shapley-Based-Automated-Dataset-Refinement',  # project name
    version='0.0.1',
    description="Brandos Shed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TODO",
    author='Brando Miranda',
    author_email='brandojazz@gmail.com',
    python_requires='>=3.11',
    license='Apache 2.0',

    packages=find_packages(include=['src', 'src.*', 'utils', 'utils.*']),
    package_dir={
        'src': 'src',
        'utils': 'utils'
    },

    install_requires=[
        "accelerate",
        "appdirs",
        "loralib",
        "bitsandbytes",
        "black",
        "black[jupyter]",
        "datasets",
        "fire",
        "gradio",
        "sentencepiece",
        "peft==0.9.0", 
        "transformers",
        "requests",
        'sentence-transformers',
        'nvidia-htop',
    ]
)

