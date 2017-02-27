from setuptools import setup

setup(name = 'LightBox',
      version = "0.1",
      description = "Assignment 3 for comp30670",
      url = "",
      author = "Conan Martin",
      author_email = "conan.martin@ucdconnect.ie",
      licence = "XX",
      packages = ["src"],
      entry_points={
        'console_scripts':['LightBox=src.name:main']
        },
      install_requires=[
          '',
      ],
      )