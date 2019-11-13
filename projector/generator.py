

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

        if os.path.isdir(template_dir):

            proj_dir = os.path.join(path, properties["project_name"])
            proj_dir = os.path.abspath(proj_dir)

            print("Copying from to {}".format(proj_dir))
            
            if not os.path.isdir(proj_dir):
                os.makedirs(proj_dir)
            else:
                print("The directory already exists")
                
            utils.copytree(template_dir, proj_dir)
            self.rendrer.process_tree(properties, proj_dir, file_names=True)
        elif os.path.isfile(template_dir):
            utils.copyfile(template_dir, path+'/')
            self.rendrer.process_file(properties,
                                      os.path.join(path, os.path.basename(template_dir)),
                                      file_names=True)
        




        
        

