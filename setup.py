from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='raptus.torii.ipython',
      version=version,
      description="extends raptus.torii with ipython",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Raptus AG',
      author_email='sriolo@raptus.com',
      url='http://raptus.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus', 'raptus.torii'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'ipython',
          'Twisted>=8.0.1'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
