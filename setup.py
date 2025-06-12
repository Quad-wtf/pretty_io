from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pretty-io",
    version="1.0.1",
    author="Quad, Wtf",
    author_email="quad.business.inquirities@gmail.com",
    description="A Python module for pretty terminal input/output with ANSI styling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quad-wtf/pretty-io",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    keywords="terminal, ansi, colors, styling, input, output, cli",
    project_urls={
        "Bug Reports": "https://github.com/Quad-wtf/pretty-io/issues",
        "Source": "https://github.com/Quad-wtf/pretty-io",
    },
)
