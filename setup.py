import os
from setuptools import setup

here = os.path.dirname(__file__)

about = {}
with open(os.path.join(here, 'vsdbg', '__about__.py')) as fobj:
    exec(fobj.read(), about)

setup(
    name='vsdbg',
    version=about['__version__'],
    packages = ['vsdbg'],
    install_requires=['debugpy'],
    entry_points='''
        [console_scripts]
        vsdbg=vsdbg:dbg
    ''',
    include_package_data = True,
    author               = about['__author__'],
    author_email         = about['__author_email__'],
    maintainer           = about['__author__'],
    maintainer_email     = about['__author_email__'],
    description          = about['__description__'],
    url                  = about['__url__'],
)