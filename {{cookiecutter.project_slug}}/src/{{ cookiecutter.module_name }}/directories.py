# pylint: skip-file
import os
from pathlib import Path

SHARED_DATA_DIRECTORY = "{{ cookiecutter.shared_data_directory}}"
EXPERIMENTS_DIRECTORY = Path(os.path.realpath(os.path.curdir))
while (EXPERIMENTS_DIRECTORY.name.lower() != "experiments" and
       not EXPERIMENTS_DIRECTORY.parent is None and
       EXPERIMENTS_DIRECTORY != EXPERIMENTS_DIRECTORY.parent):
    EXPERIMENTS_DIRECTORY = EXPERIMENTS_DIRECTORY.parent

if EXPERIMENTS_DIRECTORY == EXPERIMENTS_DIRECTORY.parent: # root directory reached
    raise ValueError("There is no experiments folder.")

if SHARED_DATA_DIRECTORY == '':
    DATA_DIRECTORY = os.path.join(EXPERIMENTS_DIRECTORY, os.pardir, os.pardir, 'data')
else:
    DATA_DIRECTORY = SHARED_DATA_DIRECTORY
