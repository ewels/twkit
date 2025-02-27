#!/usr/bin/env python

from setuptools import find_packages, setup

VERSION = "0.2.0"

with open("README.md") as f:
    readme = f.read()

setup(
    name="twkit",
    version=VERSION,
    description="Automate creation of Nextflow Tower resources",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=["nextflow", "bioinformatics", "workflow", "pipeline", "nextflow-tower"],
    author="Esha Joshi, Adam Talbot, Harshil Patel",
    author_email="esha.joshi@seqera.io, adam.talbot@seqera.io, harshil.patel@seqera.io",
    url="https://github.com/seqeralabs/twkit",
    license="MIT",
    entry_points={"console_scripts": ["twkit=twkit.cli:main"]},
    python_requires=">=3.8, <4",  # untested
    install_requires=["pyyaml>=6.0.0"],
    packages=find_packages(exclude=("docs")),
    include_package_data=True,
    zip_safe=False,
)
