from setuptools import setup

description = """
Mhash ctypes bindings for Python.
"""

setup(
    name = "py-mhash",
    url = "https://github.com/niwibe/py-mhash",
    author = "Andrei Antoukh",
    author_email = "niwi@niwi.be",
    version='1.2',
    packages = [
        "mhashlib",
    ],
    description = description.strip(),
    zip_safe=False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        #"Operating System :: OS Independent",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
