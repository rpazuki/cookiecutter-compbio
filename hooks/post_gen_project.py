#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def move_folder(source_filepath, destination_filepath):
    
    shutil.copytree(os.path.join(PROJECT_DIRECTORY, source_filepath), 
                    os.path.join(PROJECT_DIRECTORY, destination_filepath))


if __name__ == '__main__':
    
    remove_file('experiments/.keep')
    remove_file('data/.keep')
    
    if '{{ cookiecutter.manuscript_format }}' != 'LaTeX':
         remove_file('doc/references.bib')

    move_folder('experiments_template', 'experiments')

