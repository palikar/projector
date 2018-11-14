

import os
from . import utils


class Generator:

    
    def __init__(self, config, reader, renderer, data_dir="../data"):
        self.reader = reader
        self.config = config
        self.rendrer = renderer
        self.data_dir = data_dir


    def __call__(self, path):
        
        template_dir = os.path.join(self.data_dir, self.config["root_dir"])
        template_dir = os.path.abspath(template_dir)

        
        properties = {}
        self.reader.load_properties(self.config["properties"])
        properties = self.reader.read()

    
        print("Final config: " + str(properties))


        proj_dir = os.path.join(path, properties["project_name"])
        proj_dir = os.path.abspath(proj_dir)

        if not os.path.isdir(proj_dir):
            os.makedirs(proj_dir)
        else:
            print("The direcotry already exists")

        print(f"Copying form {template_dir} to {proj_dir}")
        utils.copytree(template_dir, proj_dir)


        self.rendrer.process_tree(properties, proj_dir, file_names=True)


        
        

