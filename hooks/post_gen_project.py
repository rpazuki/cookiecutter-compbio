#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath)) 

def create_folder(folder):
    os.mkdir(os.path.join(PROJECT_DIRECTORY, folder))
        
def replace_brackets_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content.replace("[", "{").replace("]", "}")
    with open(filepath, 'w') as f:
        f.write(new_content)


if __name__ == '__main__':
    
    remove_file('experiments/.keep')
    replace_brackets_in_file('experiments/experiments_template/cookiecutter.json')
    create_folder('experiments/experiments_template/{{ cookiecutter.experiment_slug }}')
    remove_file('data/.keep')
    
    if '{{ cookiecutter.manuscript_format }}' != 'LaTeX':
         remove_file('doc/references.bib')

    

   

