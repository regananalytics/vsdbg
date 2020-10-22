from setuptools import setup
from vsdbg import __about__

setup(
    name='vsdbg',
    version=__about__.__version__,
    py_modules=['vsdbg'],
    install_requires=['debugpy'],
    entry_points='''
        [console_scripts]
        vsdbg=vsdbg:dbg
    ''',
)