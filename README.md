# Elna
Elna is (mostly) a command line tool to automate visual effects pipeline process, which incluedes,

    - Creating Projects with proper directories
    - Creating Assets and Shots with proper naming convention
    - Creating and Controlling Assets and Shots version.
    - Conneting the Projects and Assets with DCC's 

## Commands
To start and configure elna, use a command `el init` in a directory that you want all the projects to be located. 
> You can only initialize Elna at one location/directory, this is mainly to avoid data loss. Future develoment may allow you to create mutilple instances.
-  `el goshow`
-  `el goshow --list`
-  `el goshow --current`


# Hou
## Required Environment Varialbe

# V
`v` has a playback commands for both djv and rv viewer
- `v rv [fileindex]` : if fileindex is not mentioned it plays the first sequences. 
- `v rv --list`      : List all sequences with the index.