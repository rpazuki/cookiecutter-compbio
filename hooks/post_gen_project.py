#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def rename_file(old_filepath, new_filepath):
    os.rename(os.path.join(PROJECT_DIRECTORY, old_filepath),
              os.path.join(PROJECT_DIRECTORY, new_filepath))    
    
def replace_brackets_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content.replace("[", "{").replace("]", "}")
    with open(filepath, 'w') as f:
        f.write(new_content)

def move_folder(source_filepath, destination_filepath):
    
    shutil.copytree(os.path.join(PROJECT_DIRECTORY, source_filepath), 
                    os.path.join(PROJECT_DIRECTORY, destination_filepath))


if __name__ == '__main__':
    
    remove_file('experiments/.keep')
    replace_brackets_in_file('experiments/experiments_template/cookiecutter.json')
    rename_file('experiments/experiments_template/cookiecutter.experiment_slug',
                '{{ experiments/experiments_template/cookiecutter.experiment_slug }}')
    remove_file('data/.keep')
    
    if '{{ cookiecutter.manuscript_format }}' != 'LaTeX':
         remove_file('doc/references.bib')

    

   

