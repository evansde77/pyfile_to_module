# pyfile_to_module
Util for converting path filenames of python files into the appropriate python module name to assist with build systems

## Installation via pip 

TBD

## Installation from source repo

```bash 
git clone 
cd pyfile_to_module
virtualenv venv 
. venv/bin/activate 
python setup.py develop 

```

## Usage

The package contains an entry point that defines the pyfile_to_module commandline tool, usage can be seen via the -h option:

```bash
pyfile_to_module -h
usage: pyfile_to_module [-h] [--prefix PREFIX] [--walk-pythonpath] filename

CLI util for converting filenames to module names

positional arguments:
  filename              filename to convert to modulename

optional arguments:
  -h, --help            show this help message and exit
  --prefix PREFIX, -p PREFIX
                        dir prefix to strip from the filename
  --walk-pythonpath, -w
                        walk python path entries to find matching prefix
                        instead of supplying it

```

### Examples 

Dumb conversion of a python filename to module format:

```bash
pyfile_to_module `pwd`/src/pyfile_to_module/pyfile_to_module.py 
Users.evansde77.Documents.pyfile_to_module.src.pyfile_to_module.pyfile_to_module
```
Stripping a leading path prefix from a module name: 

```bash
pyfile_to_module `pwd`/src/pyfile_to_module/pyfile_to_module.py --prefix=/Users/evansde77/Documents/pyfile_to_module/src
pyfile_to_module.pyfile_to_module
```

Using python path to find the best match for a module name 
```bash
pyfile_to_module `pwd`/src/pyfile_to_module/pyfile_to_module.py -w 
pyfile_to_module.pyfile_to_module
```
