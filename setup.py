#!/usr/bin/env python

from distutils.core import setup

setup(name='pmap',
      version='1.2dev',
      description=('map and starmap implementations passing additional',
                   'arguments and parallelizing if possible'),
      author='Sergio Oller',
      license='APACHE-2.0',
      author_email='sergioller@gmail.com',
      url='https://github.com/zeehio/pmap',
      py_modules=['pmap'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
      ],
)