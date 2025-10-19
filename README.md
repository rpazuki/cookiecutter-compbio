# Cookiecutter CompBio

A [rpazuki/cookiecutter-compbio](https://github.com/rpazuki/cookiecutter-compbio) template for computational biology projects.


# Quickstart

* Install cookiecutter

`pip install -U cookiecutter`

Or:

`conda install -c conda-forge cookiecutter`

* Initialize the project

`cookiecutter https://github.com/rpazuki/cookiecutter-compbio.git`

* Create the enviroment and start working!

`conda env create --file environment.yml`

* for each new numerical experiment, enter the experiments folder, and create a new one

`cd expriments`

`cookiecutter template`

* To use the newer version of the template on old projects, use
`cookiecutter https://github.com/rpazuki/cookiecutter-compbio.git --replay  -f`
