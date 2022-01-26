from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="my-py-package",
    version="0.0.1",
    author="Kerem Celik",
    author_email="celikerem@gmail.com",
    description="A sample package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/keremcelik/my-py-package",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
