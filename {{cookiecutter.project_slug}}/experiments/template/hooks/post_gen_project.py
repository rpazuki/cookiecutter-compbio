#!/usr/bin/env python
import os
import platform
import subprocess
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
EXPERIMENTS_DIRECTORY = os.path.abspath(
    os.path.join(os.path.curdir, os.pardir))
MAIN_DIRECTORY = os.path.abspath(
    os.path.join(os.path.curdir, os.pardir, os.pardir))


def __run_command__(command: list) -> bool:
    result = subprocess.run(command,
                            shell=True,
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


def __get_last_experiment_dir__(experiments_dir, except_dir=None):
    # List all directories in experiments_dir
    dirs = [d for d in os.listdir(experiments_dir)
            if os.path.isdir(os.path.join(experiments_dir, d)) and
            d != os.path.basename(except_dir)]
    # Sort by modification time (most recent last)
    dirs.sort(key=lambda d: os.path.getmtime(os.path.join(experiments_dir, d)))
    # Return the most recent directory name, or None if none found
    return dirs[-1] if dirs else None


def __copy_directory_contents__(src_dir, dst_dir):
    """Copy all files and folders from src_dir to dst_dir, excluding names
    starting with a dot."""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for item in os.listdir(src_dir):
        if item.startswith('.'):
            continue
        s = os.path.join(src_dir, item)
        d = os.path.join(dst_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)


def __copy_file__(src_file, dst_file):
    """Move a file from src_file to dst_file."""
    shutil.copy2(src_file, dst_file)


def __replace_in_file__(filepath: str, pattern: str, replacement: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(pattern, replacement)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


def copy_default_files():
    """Copy default files to the new project"""
    src_file = os.path.join(EXPERIMENTS_DIRECTORY,
                            "template", "notebook_example.ipynb")
    dst_file = os.path.join(
        PROJECT_DIRECTORY, "notebooks", "notebook_example.ipynb")
    __copy_file__(src_file,
                  dst_file)
    #

    return True


def install_python_env() -> bool:
    """Create a local python environment"""
    if '{${ cookiecutter.create_python_env.lower().strip() }$}' == 'y':
        # Create a python environment
        print(
            "Begin creating a python environment in "
            "'{${ cookiecutter.python_env_name }$}' ...")
        # Create the python environment
        if __run_command__(["python", "-m",  "venv",
                            "{${ cookiecutter.python_env_name }$}"]):
            print("python environment is created.")
            return True
        else:
            return False

    return True


def install_requirements() -> bool:
    """Install packages that are listed in """
    if '{${ cookiecutter.install_packages.lower().strip() }$}' == 'y':
        # Activate the python requirements
        if platform.system() == "Windows":
            python_path = os.path.join(
                PROJECT_DIRECTORY,
                "{${ cookiecutter.python_env_name }$}",
                "Scripts",
                "python.exe")
        else:
            python_path = os.path.join(
                PROJECT_DIRECTORY,
                "{${ cookiecutter.python_env_name }$}",
                "bin",
                "python")
        # Updating pip
        print("Updating 'pip' ...")
        if not __run_command__([python_path, "-m",
                                "pip", "install", "-U", "pip"]):
            return False
        # Installing python packages from 'requirements.txt'
        req_path = os.path.join(EXPERIMENTS_DIRECTORY, "requirements.txt")
        print(f"Installing python packages from '{req_path}' ...")
        if __run_command__([python_path,
                            "-m",
                            "pip",
                            "install",
                            "-r",
                            req_path]):
            print("python packages are installed.")
            return True
        else:
            return False

    return True


def install_local_lib() -> bool:
    """Install the local library in editable mode in src folder"""
    # Activate the python environment
    if platform.system() == "Windows":
        python_path = os.path.join(
            PROJECT_DIRECTORY,
            "{${ cookiecutter.python_env_name }$}",
            "Scripts",
            "python.exe")
    else:
        python_path = os.path.join(
            PROJECT_DIRECTORY,
            "{${ cookiecutter.python_env_name }$}",
            "bin",
            "python")
    if platform.system() == "Windows":
        src_path = MAIN_DIRECTORY + "\\src\\" + \
            "{{ cookiecutter.module_name }}"
    else:
        src_path = MAIN_DIRECTORY + "/src/" + "{{ cookiecutter.module_name }}"

    print(f"Install local package '{src_path}' ...")
    return __run_command__([python_path,
                            "-m",
                            "pip",
                            "install",
                            "-e",
                            src_path])


def copy_last_experiment() -> bool:
    """copy all files from the last experiment to the new one"""
    if '{${ cookiecutter.copy_last_experiment.lower().strip() }$}' == 'n':
        return True

    # copy the last experiment files
    last_experiment = __get_last_experiment_dir__(
        EXPERIMENTS_DIRECTORY, PROJECT_DIRECTORY)
    if not last_experiment:
        print("No previous experiment directory found to copy from.")
        return True

    print(f"Copy the last experiment ('{last_experiment}') files ...")
    try:
        __copy_directory_contents__(os.path.join(
            EXPERIMENTS_DIRECTORY, last_experiment), PROJECT_DIRECTORY)
        return True
    except (OSError, shutil.Error) as e:
        print(
            f"Error copying files from '{last_experiment}' "
            f"to '{PROJECT_DIRECTORY}': {e}")
        return False


if __name__ == '__main__':
    commands = [copy_default_files,
                install_python_env,
                install_requirements,
                install_local_lib,
                copy_last_experiment]
    RET = True
    # Execute commands if the previous one was successful
    while RET is True and len(commands) > 0:
        c = commands.pop(0)
        RET = c()
