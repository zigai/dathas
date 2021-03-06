import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text()

setup(
    name="dathas",
    version="0.0.5",
    description=" Enhance your Python dataclasses",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ziga Ivansek",
    author_email="ziga.ivansek@gmail.com",
    url="https://github.com/zigai/dathas",
    python_requires=">=3.10",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
