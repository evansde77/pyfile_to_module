#!/usr/bin/env python
"""
installer

CLI util to install the pyfile_to_module script as a binary executable
in a specified location so that it can be found on PATH etc without requiring
a virtualenv etc

"""
import os
import sys
import inspect
import argparse
import subprocess


def build_parser():
    """build command line parser and process CLI options"""
    parser = argparse.ArgumentParser(description='CLI util for installing pyfile_to_module binary')
    parser.add_argument(
        '--location', '-l',
        dest='location',
        default='~/bin/',
        help='path location to install the pyfile_to_module tool'
    )
    args = parser.parse_args()
    return args


def main():
    """
    command to locate the pyfile_to_module script and install it
    as an executable in a location specified by the CLI opts

    """
    opts = build_parser()

    loc = os.path.expandvars(os.path.expanduser(opts.location))
    if not os.path.exists(loc):
        try:
            os.makedirs(loc)
        except OSError as ex:
            msg = "Unable to create {} due to error {}".format(loc, ex)
            print(msg)
            sys.exit(1)

    src_dir = os.path.dirname(inspect.getsourcefile(build_parser))
    src_code = os.path.join(src_dir, 'pyfile_to_module.py')
    target = os.path.join(loc, 'pyfile_to_module')

    # copy the script
    command = ["/bin/cp", src_code, target]
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as ex:
        msg = "Error copying pyfile_to_module script to {}: Error: {}".format(target, ex)
        print(msg)
        sys.exit(1)

    # make it executable
    command = ['chmod', 'a+x', target]
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as ex:
        msg = "Error setting permissions on pyfile_to_module script to {}: Error: {}".format(target, ex)
        print(msg)
        sys.exit(1)

    msg = "pyfile_to_module installed as executable in {}".format(target)
    print(msg)
    sys.exit(0)


if __name__ == '__main__':
    main()
