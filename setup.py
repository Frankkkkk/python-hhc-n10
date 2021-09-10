from setuptools import setup


setup(
    name="python-hhc-n10",
    version="0.0.1",
    author="Frank Villaro-Dixon",
    author_email="frank@villaro-dixon.eu",
    description=("Interfaces with HHC-N10 (Ethernet Relay)"),
    license="MIT",
    keywords="ethernet relay hhc-n10",
    url="http://github.com/Frankkkkk/python-hhc-n10",
    packages=['hhcn10'],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
