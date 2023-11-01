from setuptools import setup, find_packages
from bokger import __version__
setup(
    name='bokger',
    packages=find_packages(where='src',),
    package_data={        
        'bokger.models' : ['DownloadCsv.js',
                           'DownloadTxt.js',
                           'CopyToClipboard',
                           ]
        },
    version=__version__,
    description='A logging package that generates debugging information in html.',
    author='chaoweichen26@gmail.com',
    license='',    
    python_requires='>=3',
    setup_requires=[
        'wheel',    
        'pytest-runner',
    ],
    install_requires=[        
        "bokeh",
        "numpy",
        "pydecor",
    ],
    tests_require=[
        'pytest',
        'junit2html',
    ],
)

