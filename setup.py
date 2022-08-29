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
    name="pyurbandict",
    version="0.1.1",
    license="MIT",
    description="Python Urban Dictionary scraper",
    author="Vitaman02",
    url="https://github.com/Vitaman02/pyurbandict",
    description=readme,
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.10",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
