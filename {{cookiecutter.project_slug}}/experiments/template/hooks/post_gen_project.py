#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if __name__ == '__main__':
     if '{${ cookiecutter.python_env.lower().strip() }$}' == 'y':
        # Create a python environment
        print("Begin creating a python environment in '{${ cookiecutter.python_env_name }$}' ...")
        # IMPROTANT: do not remove the list. Since brackets turn into curly bracket, we need it here.
        result = subprocess.run(["python", "-m",  "venv", "{${ cookiecutter.python_env_name }$}"],
                                shell=True,
                                capture_output=True,
                                text=True)        
        # Print the output
        if result.stderr == "":
            print(result.stdout)
            print("python environment is created.")
        else:
            print(result.stderr)
   

    

   

