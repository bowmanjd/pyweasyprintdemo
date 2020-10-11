"""Package configuration."""
import setuptools

setuptools.setup(
    author="Jonathan Bowman",
    description="Examples for using [WeasyPrint] as a Python library",
    entry_points={"console_scripts": ["weasyprintdemo=weasyprintdemo:run"]},
    install_requires=["weasyprint"],
    name="weasyprintdemo",
    py_modules=["weasyprintdemo"],
    version="0.1.0",
)
