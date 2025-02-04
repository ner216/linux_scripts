#!/usr/bin/env python3

#script that copies scripts in /src/ directory to system

#Built in imports
import os
import subprocess
import sys

#Get user who is running script
SUDOER = os.environ.get('SUDO_USER')
USER = os.getlogin()
#Exit script if it is not run as sudo:
if not SUDOER or USER == "root":
    print("Script must be run as root or sudo.")
    exit()

#Constant variables
SCRIPTS_PATH = "src/"
INSTALL_PATH = "/usr/local/bin/"

def copy_scipts() -> None:
    for script in os.listdir(SCRIPTS_PATH):
        if script != ".gitignore":
            print(f" Copying {SCRIPTS_PATH}{script} to {INSTALL_PATH}{script}")
            os.popen(f"sudo cp {SCRIPTS_PATH}{script} {INSTALL_PATH}{script}")

def remove_scipts() -> None:
    for script in os.listdir(SCRIPTS_PATH):
        if script != ".gitignore":
            print(f" Removing {INSTALL_PATH}{script}")
            os.popen(f"sudo rm {INSTALL_PATH}{script}")

def main():
    print(f"This script is used to copy or remove scripts from the {INSTALL_PATH} directory.")
    #Flag variables
    install_arg = False
    uninstall_arg = False
    help_arg = False
    version_info_arg = False

    #Process arguments
    for arg in sys.argv:
        if str(arg) == "install":
            install_arg = True
        elif arg == "uninstall":
            uninstall_arg = True
        elif str(arg) == "help":
            help_arg = True
        elif str(arg) == "version" or arg == "ver":
            version_info_arg = True

    #Compute command based on given argument
    if help_arg == True:
        print("Commands: ")
        print(" -- Install scripts: install.py install")
        print(" -- uninstall scripts: install.py uninstall")
        print(" -- dry run the program: install.py dryrun")
        print(" -- Get this help message: install.py help")
        print(" -- Get version info: install.py [version/ver]")
        exit()
    elif version_info_arg == True:
        print("Version: 0.1")
        print("Creator: Nolan Provencher")
        print("GitHub: https://github.com/ner216/linux_scripts")
        exit()
    elif install_arg == True:
        print("Scipts that can be installed: ")
        for script in os.listdir(SCRIPTS_PATH):
            if script != ".gitignore":
                print(f" {script}")
        install_confirmation = input(f"Copy scripts to {INSTALL_PATH}?(y/N) ")
        if install_confirmation == "y":
            copy_scipts()
        else:
            exit()
    elif uninstall_arg == True:
        print("Scipts to be uninstalled: ")
        for script in os.listdir(SCRIPTS_PATH):
            if script != ".gitignore":
                print(f" {script}")
        uninstall_confirmation = input(f"Remove scripts from {INSTALL_PATH}?(y/N) ")
        if uninstall_confirmation == "y":
            remove_scipts()
        else:
            exit()
    else:
        print("Error, invalid arguments. Use `install.py help` for help.")
        exit()

main()

