# Linux Scripts For Simple Tasks
### A collection of linux scripts to simplify shell workflow

## Getting Started
The `/src/` directory in the repository contains my simple command scripts. Each script is a command.

### Manually Copy Scripts
You can copy files from `/src/` directory to your `/usr/local/bin` direcotory to make them accessable system wide.

### Installer Script:
- Navigate to the root of the repository 
- Run the command `sudo ./install.py`
    - The script will copy all scripts to the `/usr/local/bin` directory.
    - You can enter script names as arguments to install specific scripts. Ex. `sudo ./install.py lsgit`

### More information about the installer:
- The installer copies all/specified scripts in the `/src/` directory of the repository to your own `/usr/local/bin` directory.
- Installer must be run with sudo or root
- **To install (copy scripts)**
    - Run `sudo ./install.py`
- **To uninstall (remove installed sripts)**
    - Run `sudo ./install.py uninstall`

## Scripts included:
- gity
    - Python script that runs a specified git command on all local git repositories at once.
        - For example: run `gity status` to show `git status` of every repo in the directories that gity searches.
    - Use `gity help` to get basic command information
- lsgit
	- Bash script that will list repos on the system or show git status for each repo.
	- Use `lsgit -h` for more info.
- awake
	- Bash script that displays amount of time since last suspend.
	- Will also display a breakdown of time spend awake and suspended.
	- See `awake -h` for more info.
- cld
    - A Rclone wrapper that simplifies Rclone commands.
    - cld also reformats and simplifies rclone output to make it easier to read.
    - Use `cld help` to get basic command information.