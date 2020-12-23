#import vsdbg_ez
import os
import sys
import debugpy
import shutil
import subprocess
from contextlib import contextmanager
from tempfile import TemporaryDirectory

PORT = 5678

def dbg(port=PORT, wait=True):
    debugpy.listen(port)
    if wait: debugpy.wait_for_client()



## CLI STUFF

@contextmanager
def temp_copy(filename):
    with TemporaryDirectory() as t:
        try:
            temp_path = os.path.join(t, filename)
            shutil.copy(filename, temp_path)
            yield temp_path
        finally:
            os.remove(filename)
            shutil.copy(temp_path, filename)

@contextmanager
def append_vsdbg(arg_dict):
    is_module = False
    if arg_dict['flags']:
        if '-m' in arg_dict['flags']:
            # handle module
            pymod = arg_dict['py']
            is_module = True
    else:
        pyfile = arg_dict['py']
    # Assume pyfile for now
    with temp_copy(pyfile) as t:
        try:
            if is_module:
                pass
            else:
                prepend(pyfile, 'import vsdbg_ez')
            yield pyfile
        finally:
            pass


def prepend(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line + '\n' + content)


def parse_args():
    arg_dict = {'self':None, 'flags':[], 'py':[], 'out':None}
    args = sys.argv
    arg_dict['self'] = args[0]
    is_module = False
    for arg in args[1:]:
        if arg.endswith('.py') or is_module:
            is_module = False
            arg_dict.update({'py':arg})
        elif arg.startswith('-'):
            if arg == '-m':
                is_module = True
            arg_dict.update({'flags':arg_dict['flags'].append(arg)})
    return args, arg_dict

def main():
    # Get args
    args, arg_dict = parse_args()
    print(f'Dict: {arg_dict}')
    cmd = f'python {" ".join(args[1:])}'
    print(f'CMD: {cmd}')
    with append_vsdbg(arg_dict) as py:
        subprocess.run(cmd, shell=True)
