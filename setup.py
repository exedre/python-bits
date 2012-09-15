import os.path
import os
from setuptools import setup

version = "0.1.1"
version_files=(("src/bits/VERSION","%s\n"),)

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: End Users/Desktop",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Information Analysis",
    ]

distname = 'python-bits'

long_description = """

"""

def setup_package():
    setup(
        install_requires = 'numpy >= 1.5.0',
        name='bits',
        version=version,
        description=long_description,
        classifiers=classifiers,
        author="Emmanuele Somma",
        author_email="emmanuele.somma_AT_bancaditalia_DOT_it",
        maintainer = "Emmanuele Somma",
        maintainer_email="emmanuele.somma_AT_bancaditalia_DOT_it",        
        url="http://python-bits.org",
        license="BSD",
        package_dir = {'':'src'},
        platforms = ['Linux',
                     'Mac OS-X',
                     'Unix'],
        packages = ['bits',
                    'bits.tests',
                     ], 
#        entry_points = {
#            'console_scripts': [
#                'e4t = e4t.e4t:e4t',
#                'e4t-admin = e4t.e4t:e4t_admin',
#                ]},
          )

for (filename, template) in version_files:
    filename = os.path.join(os.path.dirname(__file__), filename)
    try:
        os.makedirs(os.path.dirname(filename))
    except:
        pass
    verfile = None
    try:
        verfile = open(filename, 'w')
        verfile.write(template % version)
        verfile.close()
    except:
        verfile.close()
        raise


if __name__=="__main__":
    setup_package()
