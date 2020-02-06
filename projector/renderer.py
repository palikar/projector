import re
import os
import pystache

import utils


class Renderer:

    def __init__(self):
        self.mustacher = pystache.Renderer()

    def _process_file(self, tree, file, properties):
        new_content = self.mustacher.render_path(file, properties)
        with open(file, 'w') as file_hd:
            file_hd.write(new_content)

    def process_tree(self, properties, tree, file_names=True):
        for file in os.listdir(tree):
            file = os.path.join(tree, file)

            if file_names:
                mat = re.search(r'\{\{(.*)\}\}', file)
                if mat and mat.group(1) in properties.keys():
                    new_name = re.sub(r'\{\{(.*)\}\}',
                                      properties[mat.group(1)], file)
                    os.rename(file, new_name)
                    file = new_name

            if os.path.isfile(file):
                print(file)
            if os.path.isfile(file) and not utils.is_binary(file):
                self._process_file(tree, file, properties)
            elif os.path.isdir(file):
                self.process_tree(properties, file, file_names=file_names)

    def process_file(self, properties, file, file_names=True):
        if file_names:
            mat = re.search(r'\{\{(.*)\}\}', file)
            if mat and mat.group(1) in properties.keys():
                new_name = re.sub(r'\{\{(.*)\}\}',
                                  properties[mat.group(1)], file)
                os.rename(file, new_name)
                file = new_name

        if os.path.isfile(file) and not utils.is_binary(file):
            self._process_file(file, file, properties)
