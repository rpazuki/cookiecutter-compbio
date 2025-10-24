from setuptools import setup, find_packages
setup(
   name='{{ cookiecutter.module_name  }}',
   version='0.1',
   packages=find_packages(),
   install_requires=[
       # List your dependencies here
   ],
)