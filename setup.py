import os
from setuptools import setup

here = os.path.dirname(__file__)

about = {}
with open(os.path.join(here, 'vsdbg', '__about__.py')) as fobj:
    exec(fobj.read(), about)

setup(
    name='vsdbg',
    version=about['__version__'],
    py_modules=['vsdbg'],
    install_requires=['debugpy'],
    entry_points='''
        [console_scripts]
        vsdbg=vsdbg:dbg
    ''',
)