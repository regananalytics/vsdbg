import os
import sys
import click
import debugpy
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

PORT = 5678

def dbg(port=PORT, wait=True):
    debugpy.listen(port)
    if wait:
        print('VSDBG: Waiting for Debug Session to Continue...')
        debugpy.wait_for_client()


## CLI STUFF

@contextmanager
def temp_copy(fullfile):
    if not isinstance(fullfile, Path):
        Path(fullfile)
    file = fullfile.stem + fullfile.suffix
    path = fullfile.parent
    with TemporaryDirectory() as t:
        try:
            temp_path = os.path.join(t, file)
            shutil.copy(fullfile, temp_path)
            yield temp_path
        finally:
            pass
            os.remove(fullfile)
            shutil.copy(temp_path, fullfile)

@contextmanager
def append_vsdbg(arg_dict):
    path = Path.cwd()
    if arg_dict['mod']:
        # This is a python module, find __init__.py
        modparts = arg_dict['cmd'][0].split('.')
        path = Path(os.path.join(path, *modparts))
        if not os.path.isdir(path):
            raise Exception(f'VSDBG:  Could not find module at {path}')
        fullfile = path / '__init__.py'
        if not os.path.isfile(fullfile):
            raise Exception(f'VSDBG:  Could not find __init__.py at {path}')
    else:
        fullfile = path / arg_dict['cmd'][0]
    with temp_copy(fullfile) as t:
        try:
            prepend(fullfile, 'import vsdbg_ez')
            yield fullfile
        finally:
            pass


def prepend(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line + '\n' + content)


@click.command()
@click.argument('cmd', nargs=-1)
@click.option('--bin', '-b', is_flag=True)
@click.option('--mod', '-m', is_flag=True)
def main(**kwargs):
    if kwargs['bin']:
        cmd = ' '
    else:
        cmd = f"python {'-m' if kwargs['mod'] else ''} {' '.join(kwargs['cmd'])}"
    with append_vsdbg(kwargs) as py:
        pass
        subprocess.run(cmd, shell=True)
