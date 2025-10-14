#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    
    remove_file('experiment/.keep')
    remove_file('data/.keep')
    

    # if '{{ cookiecutter.language }}' == 'Python':
    #     remove_file('src/main_analysis.rmd')
    #     remove_file('src/helpers/utils.R')
    

    # if '{{ cookiecutter.manuscript_format }}' == 'LaTeX':
    #     remove_file('doc/main.rmd')

    # if '{{ cookiecutter.manuscript_format }}' == 'Other':
    #     remove_file('doc/main.rmd')
    #     remove_file('doc/main.tex')
    #     remove_file('doc/references.bib')
