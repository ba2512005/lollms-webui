from pathlib import Path
from typing import Union

setuptools = ...  # assuming you've imported setuptools correctly

README_MD_FILE = "README.md"
REQUIREMENTS_TXT_FILE = "requirements.txt"
REQUIREMENTS_DEV_TXT_FILE = "requirements_dev.txt"

def read_requirements(path: Union[str, Path]) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]

requirements = list(filter(None, read_requirements(REQUIREMENTS_TXT_FILE)))
requirements_dev = list(filter(None, read_requirements(REQUIREMENTS_DEV_TXT_FILE)))

def get_all_files(path: str) -> list:
    path = Path(path)
    file_list = []
    for file_path in path.rglob("*"):
        if file_path.is_file():
            relative_path = file_path.relative_to(path)
            if not (relative_path.name.startswith("__pycache__") or
                    relative_path.suffix == ".pyc" or
                    relative_path.name in ["local_config.yaml", ".installed", ".git", ".gitignore"]):
                file_list.append(str(relative_path))
    return file_list

with open(README_MD_FILE, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lollms",
    version="10.1.0",
    author="Saifeddine ALOUI (ParisNeo)",
    author_email="parisneo_ai@gmail.com",
    description="A python library for AI personality definition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ParisNeo/lollms",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': ['lollms-elf = lollms.server.elf:main'],
    },
    extras_require={"dev": requirements_dev},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)