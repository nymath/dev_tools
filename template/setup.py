from distutils.core import setup
from setuptools import find_packages
from Cython.Build import cythonize
import numpy
import glob

extensions = glob.glob("torchqtm/_C/*.pyx")
extensions.extend(glob.glob("torchqtm/window/*.pyx"))
extensions.extend(glob.glob("torchqtm/finance/*.pyx"))

install_requires = [
    'numpy',
    'pandas',
    'pandas_market_calendars',
    'cython',
]


def main():
    setup(
        ext_modules=cythonize(extensions, annotate=True),
        include_dirs=[numpy.get_include()],
        name="torchqtm",
        version="0.2.0",
        author="ny",
        author_email="nymath@163.com",
        install_requires=install_requires,
        description="None",
        long_description=open('README.md', 'r').read(),
        long_description_content_type="text/markdown",
        url="https://github.com/nymath/torchqtm",
        download_url="https://github.com/nymath/torchqtm/releases/tag/",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Unix",
        ],
        python_requires='>=3.9',
    )


if __name__ == "__main__":
    main()

## setup cython
# python setup.py build_ext --inplace
## setup package
# pip install twine
# python setup.py sdist bdist_wheel
# twine upload dist/*
# twine upload --skip-existing dist/*

# ny.math
# xxx
