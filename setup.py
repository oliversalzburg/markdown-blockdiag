from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="blockdiag-fences",
    version="0.0.2",
    packages=find_packages(),
    url="https://github.com/oliversalzburg/markdown-blockdiag",
    license="MIT",
    install_requires=[
        "Markdown",
        "mkdocs",
        "superfences",
        "actdiag",
        "blockdiag",
        "nwdiag",
        "packetdiag",
        "rackdiag",
        "seqdiag",
    ],
    author="Oliver Salzburg",
    author_email="oliver.salzburg@gmail.com",
    description="blockdiag extension for Python Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
