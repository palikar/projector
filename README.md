# Projector


## Abstract

![img](./demo_pic.png) A handy utility that (for now) helps me easily create my project, without copying and pasting a whole directory of an existing project and then going through the files and replacing the necessary files and file contents with new words. This *python* scripts automates exactly this process. Custom project-templates can be added as easily as just adding a new project-template folder and specifying the file names that should be changed. Then trough the configuration file everything about the new project-template could setup.


## Instalation and basic usage

Clone the repository and install it through the supplied `setup.py` file

```sh
git clone https://github.com/palikar/projector
python setup.py install
```



After that you should run able to run something like:

```sh
projector cmake-simple ~/code/new_project
```

This will create new *cmake*-project and will place the root directory of the project in the folder `~/code` of your system. If you don't like the structure of the setup of any of the templates, feel free to change them. The templates' folders are in the root of the repo and are specified through the `root_dir` property of each generator in the config file.



In any file of the project-template you can use text like `%property_name%`. The script will go through all the files, find these fields and replace them with the inputs collected on running the script. This also works for file names. The contents of binary files will be skipped but their names can be changed. In the configuration file for each generator a set of such properties is specified. Those tell the script what to expect from the user and which fields to replace in the template upon copying it in the given directory. More on the configuration file in the next section.



You can also list the available generators by calling:

```sh
projector --list-gen
```


## Config file

`config.json` is the file that defines all the projects that can be created. Each top-level object name of the JSON is the name of a new *generator*. The *projector* executable has to be invoked by passing one of these generators as its first argument. `root_dir` of a given generator tells the script which is the project-template folder. This folder will be copied in the given location and then traversed to expand the specified properties. The `properties` field of a generator is an array of property objects. Each object specifies:

-   `name` - The text with which the user will be prompted to enter a value for the given property.
-   `token` - The text that will be replaced with the collected value. This happens in the copied template directory. The tokens inside the cipied template folder are expanded to the user supplied values.
-   `default` - Optional field. Tells the script what is the default value for this property and if the user provides empty input, this value will be used in the token-expansion step.

projector uses [mustache](https://mustache.github.io/) (or a python [port](https://github.com/defunkt/pystache) of mustache) for the definition of its templates. This means that every file is processed as mustache template and `{{token_name}}` is replaced with the value given by the user while invoking projector.
