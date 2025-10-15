#!/usr/bin/env python
import os
import platform
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
EXPERIMENTS_DIRECTORY = os.path.abspath(os.path.join(os.path.curdir, os.pardir))

def __run_command__(command:list) -> bool:
    result = subprocess.run(command,
                            shell=True,
                            capture_output=True,
                            text=True)        
    # Print the output
    if result.stderr == "":
        print(result.stdout)        
        return True
    else:
        print(result.stderr)
        return False



def install_python_env() -> bool:
    """Create a local python environment"""
    if '{${ cookiecutter.create_python_env.lower().strip() }$}' == 'y':
        # Create a python environment
        print("Begin creating a python environment in '{${ cookiecutter.python_env_name }$}' ...")
        # IMPROTANT: do not remove the list. Since brackets turn into curly bracket, we need it here.
        if __run_command__(["python", "-m",  "venv", "{${ cookiecutter.python_env_name }$}"]):        
            print("python environment is created.")
            return True
        else:
            return False
        
    return False

def install_environment() -> bool:
    """Install packages that are listed in """
    if '{${ cookiecutter.install_packages.lower().strip() }$}' == 'y':
       # Activate the python environment
       if platform.system()  == "Windows":
           python_path = os.path.join(PROJECT_DIRECTORY,"{${ cookiecutter.python_env_name }$}", "Scripts", "python.exe")
       else:
           python_path = os.path.join(PROJECT_DIRECTORY,"{${ cookiecutter.python_env_name }$}", "bin", "python")
       # Updating pip
       print("Updating 'pip' ...")       
       if __run_command__([python_path, "-m", "pip", "install",  "-U", "pip"]) == False:
           return False
       # Installing python packages from 'requirements.txt'                
       req_path = os.path.join(EXPERIMENTS_DIRECTORY,"requirements.txt")
       print(f"Installing python packages from '{req_path}' ...")
       if __run_command__([python_path, "-m", "pip", "install",  "-r", req_path]):        
           print("python packages are installed.")
           return True
       else:
           return False
        
    return False

if __name__ == '__main__':
    commands = [install_python_env,
                install_environment]
    ret = True
    # Execute commands if the previous one was successful
    while ret == True and len(commands) > 0:
        c = commands.pop(0)
        ret = c()
        
     
            
        
   

    

   

