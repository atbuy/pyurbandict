from pathlib import Path

from setuptools import find_packages, setup

cwd = Path(__file__).parent
reqs_path = cwd.joinpath("requirements.txt")
readme_path = cwd.joinpath("README.md")

requirements = []
with open(reqs_path) as file:
    requirements = file.read().splitlines()

readme = ""
with open(readme_path) as file:
    readme = file.read()

setup(
    name="python-urbandict",
    version="0.2.2",
    license="MIT",
    author="Vitaman02",
    url="https://github.com/Vitaman02/pyurbandict",
    description="Python wrapper for the Urban Dictionary API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
