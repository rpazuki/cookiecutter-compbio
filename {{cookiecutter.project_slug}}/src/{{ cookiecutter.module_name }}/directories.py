# pylint: skip-file
import os

SHARED_DATA_DIRECTORY = "{{ cookiecutter.shared_data_directory}}"
EXPERIMENTS_DIRECTORY = os.path.realpath(os.path.curdir)

if SHARED_DATA_DIRECTORY == '':
    DATA_DIRECTORY = os.path.join(EXPERIMENTS_DIRECTORY, os.pardir, os.pardir, 'data')
else:
    DATA_DIRECTORY = SHARED_DATA_DIRECTORY
