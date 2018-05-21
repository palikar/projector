- [Abstract](#orgef3b9c3)
- [Instalation and basic usage](#org072d394)
- [Config file](#org550c195)
  - [Mandatory property for each project.](#org3c5ff68)
    - [Add new top level property for the folder name](#orgc3f5b29)



<a id="orgef3b9c3"></a>

# Abstract

A handy utility that (for now) helps me create my project in a simple manner, without copying and pasting a whole directory of an existing project and then going through the files and replacing the necessary files and file contents with new words. This *python* scripts automates exactly this process. Custom project-templates can be added as easily as just adding a new project-template folder and specifying the file names that should be changed. Then trough the configuration file everything about the new project-template could setup.


<a id="org072d394"></a>

# Instalation and basic usage

Clone the repo with

    git clone https://github.com/palikar/projector

You will probably have to do something like

    cd projector
    chmod +x create_project.py

Then you can run the script like:

    ./create_project.py cmake ~/code/

This will create new *cmake*-project and will place the root directory of the project in the folder `~/code` of your system. If you don't like the structure of the setup of any of the templates, feel free to change them. The templates' folders are in the root of the repo and are specified through the `root_dir` property of each generator in the config file.


<a id="org550c195"></a>

# Config file

The file that defines all the projects that can be created is `config.json`.


<a id="org3c5ff68"></a>

## Mandatory property for each project.

`project_name` - this should be always there as the scripts use this to create the folder for the project.


<a id="orgc3f5b29"></a>

### TODO Add new top level property for the folder name
