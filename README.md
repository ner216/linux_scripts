# Linux Scripts For Simple Tasks
### A collection of basic linux scripts to simplify shell workflow

## Getting Started
The `/src/` directory in the repository contains my simple command scripts. Each script is a command.
### Manually copy scripts
You can copy files from `/src/` directory to your `/usr/local/bin` direcotory to make them accessable system wide.
### Copy all scripts with installer script:
- Navigate to the root of the repository 
- Run the command `sudo ./install.py`
    - The script will copy all scripts to the `/usr/local/bin` directory. 
### More information about the installer:
- The installer copys all scripts in the `/src/` directory of the repository to your own `/usr/local/bin` directory.
- Installer must be run with sudo or root
- **To install (copy scripts)**
    - Run `sudo ./install.py`
- **To uninstall (remove installed sripts)**
    - Run `sudo ./install.py uninstall`
## Scripts included:
- ### gity
    - Runs a specified git command on all local git repositories at once.
        - For example: run `gity status` to show `git status` of every repo on the system.
    - Use `gity help` to get basic command information
        - See **gity.md** for full documentation.
- ### cld
    - A Rclone wrapper that simplifies Rclone commands.
    - cld also reformats and simplifies rclone output to make it easier to read.
    - Use `cld help` to get basic command information.
        - See **cld.md** for full documentation.