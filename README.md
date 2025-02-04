# Linux Scripts For Simple Tasks
### I created these scripts to assist my command line workflow.

## Getting Started
The `/src/` directory in the repository contains the command scripts. Each
script is a command.
### Manual install
You can copy these files to your `/usr/local/bin` direcotory to make them accessable
system wide.
### Install with installer
- Navigate to the root of the repository 
- Run the command `sudo ./install install`
    - The script will copy all scripts to the `/usr/local/bin` directory. 
### Installer details
- Installer must be run with sudo or root
- The installer can install (copy scripts)
    - Run `sudo ./install install`
- This installer can uninstall (remove installed sripts)
    - Run `sudo ./install uninstall`
## Scripts included
- ### gity
    - Runs a git command on all local git repositories at once.
    - Run git status on all repos: `gity status`
    