import os

from . import utils
from .processors import License


class Generator:

    processors = [License()]

    def __init__(self, config, reader, renderer, data_dir="../data"):
        self.reader = reader
        self.config = config
        self.rendrer = renderer
        self.data_dir = data_dir

        for proc in self.processors:
            proc.set_data_dir(data_dir)

    def get_template_dir(self):
        template_dir = os.path.join(self.data_dir, self.config["root_dir"])
        return os.path.abspath(template_dir)

    def generate(self, path):
        template_dir = self.get_template_dir()
        properties = {}

        self.reader.load_properties(self.config["properties"])
        properties = self.reader.read()

        proj_dir = os.path.join(path, properties["project_name"])
        proj_dir = os.path.abspath(proj_dir)

        for proc in self.processors:
            for prop, value in properties.items():
                proc.precoppy(prop, value)

        if os.path.isdir(template_dir):
            print("Copying from to {}".format(proj_dir))
            if not os.path.isdir(proj_dir):
                os.makedirs(proj_dir)
            else:
                print("The directory already exists")
            utils.copytree(template_dir, proj_dir)
        elif os.path.isfile(template_dir):
            utils.copyfile(template_dir, path+'/')

        for proc in self.processors:
            for prop, value in properties.items():
                proc.postcoppy(prop, value, proj_dir)

        if os.path.isdir(template_dir):
            self.rendrer.process_tree(properties, proj_dir, file_names=True)
        elif os.path.isfile(template_dir):
            self.rendrer.process_file(properties,
                                      os.path.join(path,
                                                   os.path.basename(
                                                       template_dir)),
                                      file_names=True)

        for proc in self.processors:
            for prop, value in properties.items():
                proc.postrender(prop, value, proj_dir)
