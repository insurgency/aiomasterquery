#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='aioamasterquery',
    version=None,  # TODO
    author='insurgency.gg',
    url='https://github.com/insurgency/aioamasterquery',
    packages=find_packages(
        exclude=[
            'tests',
        ],
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Networking',
        'Typing :: Typed',
    ],
    license='MIT',
    python_requires='>=3.7',
    test_suite='tests',
    install_requires=[
        'git+https://github.com/insurgency/aioa2squery.git@5c9b43e37c78534b2074e5be8e736b6149c727ff#egg=aioa2squery',
    ],
    extras_require={
        'speedups': [
            'uvloop',
        ],
    },
    # Automatic Script Creation
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
    entry_points={
        'console_scripts': [
            # TODO
        ],
    },
)
