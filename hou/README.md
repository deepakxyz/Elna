# Hou 
Hou is a command line tool to make a creating and managing Houdini project easier.

## Configure


## Commands
- `hou create-project`                     : Create a new project with sub directories.
- `hou gopro [OPTIONS] [PRONAME]`          : Go to the Houdini project directory.
    - `proname`                            : Go to the given project directory is the project exists.
    - `--list`                             : List all the Houdini projects.
    - `--last`                             : Go to the last opend houdini projects.
- `hou launch`                             : Launch latest working file of the project, if it is a new project it launches a blank file.
- `hou otls [OPTIONS]
    - `--list`                             : List all the otls
    - `--update`                           : Update newly added otls
    - `--force-update`                     : Force update otls on the current houdini projects.