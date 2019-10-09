import os 
from setuptools import find_packages, setup
from freight import __version__

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='aa-freight',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Alliance Auth plugin app for running an alliance freight service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/ErikKalkoken/aa-freight',
    author='Erik Kalkoken',
    author_email='erik.kalkoken@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',        
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[ 
        'requests'
    ]
)
