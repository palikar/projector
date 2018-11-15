import re
import os
import pystache

from  . import utils


class Renderer:



    def __init__(self):
        self.mustacher = pystache.Renderer()
        
            

    def _process_file(self, tree, f, properties):
        new_content = self.mustacher.render_path(f, properties)
        with open(f, 'w') as file:
            file.write(new_content)
        
    


    def process_tree(self, properties, tree, file_names=True):
        for f in os.listdir(tree):
            f = os.path.join(tree, f)

            if file_names:
                mat = re.search(r'\{\{(.*)\}\}', f)
                if mat and mat.group(1) in properties.keys():
                    new_name = re.sub(r'\{\{(.*)\}\}', properties[mat.group(1)], f)
                    os.rename(f, new_name)
                    f = new_name

            if os.path.isfile(f):
                print(f)
            if os.path.isfile(f) and not utils.is_binary(f):
                self._process_file(tree, f, properties)
            elif os.path.isdir(f):
                self.process_tree(properties, f, file_names=file_names)

            
        
        
