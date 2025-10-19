#!/usr/bin/env python
import os
import platform
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
IS_WINDOWS = platform.system() == "Windows"


def __run_command__(command: list) -> bool:
    result = subprocess.run(command,
                            shell=IS_WINDOWS,
                            capture_output=True,
                            text=True,
                            check=False)
    # Print the output
    if result.stderr == "":
        print(result.stdout)
        return True
    else:
        print(result.stderr)
        return False


def remove_file(filepath: str):
    """Remove a file given its relative path from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def create_folder(folder: str):
    """Create a folder given its relative path from the project directory."""
    # If the folder already exists, do nothing
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, folder)):
        os.mkdir(os.path.join(PROJECT_DIRECTORY, folder))


def rename_brackets_in_folder_name(folder: str, folder_name: str):
    """Rename a folder by removing '$' from its name."""
    # Rename the folder by removing '$' from its name
    os.rename(os.path.join(PROJECT_DIRECTORY, folder, folder_name),
              os.path.join(PROJECT_DIRECTORY, folder,
                           folder_name.replace('$', ''))
              )


def remove_dollar_sign_in_file(filepath: str):
    """Remove 'dollar_sign' from a file given its relative path."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('$', '')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


if __name__ == '__main__':
    #
    remove_file('experiments/.keep')
    if '{{ cookiecutter.manuscript_format }}' != 'LaTeX':
        remove_file('doc/references.bib')
    # mapp the data folder to a shared folder if specified
    if '{{ cookiecutter.shared_data_folder.lower().strip() }}' != '':
        if IS_WINDOWS:
            if not __run_command__(["cmd",
                                    "/c",
                                    "mklink",
                                    "/D",
                                    "data",
                                    '{{ cookiecutter.shared_data_folder }}']):
                print("Failed to create a symbolic link. "
                      "Please run the command below in the command prompt "
                      "(cmd) as an administrator:")
                print(
                    f'mklink /D "{os.path.join(PROJECT_DIRECTORY,"data")}" '
                    f'"{os.path.abspath("{{ cookiecutter.shared_data_folder }}")}"')
        else:
            os.symlink(os.path.abspath('{{ cookiecutter.shared_data_folder }}'),
                       os.path.join(PROJECT_DIRECTORY, 'data'),
                       target_is_directory=True)
    else:
        create_folder('data')
    #
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY,
                                       'experiments/template/{{cookiecutter.experiment_slug}}')):

        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}')
        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}/reports')
        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}/reports/figures')
        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}/models')
        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}/notebooks')
        create_folder(
            'experiments/template/{${cookiecutter.experiment_slug}$}/processed')
        rename_brackets_in_folder_name(
            'experiments/template', '{${cookiecutter.experiment_slug}$}')

    # If the name of a folder contains '{}', the cookiecutter will try
    # to change it. Since we need the
    # 'template' folder for calling the cookiecutter later,
    # we uses '$' around the '{}', and remove them eventually.
    remove_dollar_sign_in_file('experiments/template/cookiecutter.json')

    remove_dollar_sign_in_file(
        'experiments/template/hooks/post_gen_project.py')
    #
