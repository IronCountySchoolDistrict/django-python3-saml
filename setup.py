import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_python3_saml',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD 3-Clause License',  # example license
    description='Django SAML auth plugin for python 3',
    long_description=README,
    url='https://github.com/IronCountySchoolDistrict/django-python3-saml',
    author='Issac Gable',
    author_email='issac.gable@ironmail.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 4 - Beta',
    ],
    install_requires=[
        'python3-saml',
        'django-environ',
    ]
)