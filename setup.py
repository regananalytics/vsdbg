from setuptools import setup
import __about__

setup(
    name='vsdbg',
    version=__about__.__version__,
    packages = [
        'vsdbg', 
        'vsdbg_ez'
    ],
    install_requires=[
        'debugpy >= 1.0.0',
        'setuptools >= 50.3.2'
    ],
    entry_points={
        'console_scripts': [
            'vsdbg = vsdbg.vsdbg:main',
        ]
    },
    include_package_data = True,
    author               = __about__.__author__,
    author_email         = __about__.__author_email__,
    maintainer           = __about__.__author__,
    maintainer_email     = __about__.__author_email__,
    description          = __about__.__description__,
    url                  = __about__.__url__,
)