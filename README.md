# Linux Scripts For Simple Tasks
### I created these scripts to assist with tedious tasks.

## Getting Started
The `/src/` directory in the repository contains my simple command scripts. Each script is a command.
### Manually copy scripts
You can copy files from `/src/` directory to your `/usr/local/bin` direcotory to make them accessable system wide.
### Copy all scripts with installer script
- Navigate to the root of the repository 
- Run the command `sudo ./install.py install`
    - The script will copy all scripts to the `/usr/local/bin` directory. 
### Installer details
- The installer copys all scripts in the `/src/` directory of the repository to your own `/usr/local/bin` directory.
- Installer must be run with sudo or root
- **To install (copy scripts)**
    - Run `sudo ./install.py install`
- **To uninstall (remove installed sripts)**
    - Run `sudo ./install.py uninstall`
## Scripts included
- ### gity
    - Runs a git command on all local git repositories at once.
    - To get started with gity, Run: `gity help`
    