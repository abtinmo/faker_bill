from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='faker_bill',
    version='0.1.0',
    description='add bill methods to faker package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='faker bill data test mock generator',
    author='abtinmo',
    author_email='abtin@riseup.net',
    url='https://github.com/abtinmo/faker_bill',
    license='MIT License',
    platforms=["any"],
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.5",
    install_requires=[
        "faker",
    ],
        classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
)