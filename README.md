# pyfile_to_module
Util for converting path filenames of python files into the appropriate python module name to assist with build systems. 

Functions a a CLI tool for converting path names to module names in a couple of different ways:
  * Straight swap of path names for periods and removing .py
  * Swap with optional prefix to remove leading path from filename
  * More intelligent python path walk to find best match for the module name and automatically strip off leading path names

## Installation via pip 

```bash
pip install pyfile_to_module
```

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

## Usage within sublime build system 

To set up a python build system that uses the python -m command line option to execute the module as a module (and avoid complaints about relative imports and packages, you can use a sublime build system something like this example, assuming a virtualenv setup. 

Note that this assumes that the pyfile_to_module tool is installed somewhere that the sublime python can access it.  
If you dont want to install it into the sublime python, you can just drop the pyfile_to_module.py script somewhere on your path and chmod +x it (if you dont remove the .py extension, adapt the example below to pyfile_to_module.py)

```json
	"build_systems": [
        {

            "name":"module virtualenv",
            "working_dir": "${project_path}",
            "shell" : true,
            "env" : {
                "PYTHONPATH" : "/Users/evansde77/Documents/cirrus:/Users/evansde77/Documents/cirrus/src"
            },
            "cmd":
            [
                ". ${project_path}/venv/bin/activate && ${project_path}/venv/bin/python -m `pyfile_to_module -w $file`"
            ]
        }

	]

```
