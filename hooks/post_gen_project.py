#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath:str):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath)) 

def create_folder(folder:str):
    os.mkdir(os.path.join(PROJECT_DIRECTORY, folder))

def rename_brackets_in_folder_name(folder:str, folder_name:str):    
    os.rename(os.path.join(PROJECT_DIRECTORY, folder, folder_name),
              os.path.join(PROJECT_DIRECTORY, folder, folder_name.replace('[', '{').replace(']', '}'))
              )
        
def replace_brackets_in_file(filepath:str):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content.replace('[', '{').replace(']', '}')
    with open(filepath, 'w') as f:
        f.write(new_content)


if __name__ == '__main__':    
    remove_file('experiments/.keep')
    
    # If the name of a folder contains '{{}}', the cookiecutter will try to change it. Since we need the
    # 'template' folder for calling the cookiecutter later, we uses '[]' inplace of
    # '{}', and change all of '[]' to '{}' eventually.
    # replace_brackets_in_file('experiments/template/cookiecutter.json')
    # create_folder('experiments/template/[[ cookiecutter.experiment_slug ]]')
    # rename_brackets_in_folder_name('experiments/template', '[[ cookiecutter.experiment_slug ]]')
    #
    remove_file('data/.keep')
    
    if '{{ cookiecutter.manuscript_format }}' != 'LaTeX':
        remove_file('doc/references.bib')

    

   

