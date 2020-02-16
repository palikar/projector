import os
import abc

from . import utils


class BaseProcessor:

    def __init__(self):
        self.data_dir = None

    def set_data_dir(self, data_dir):
        self.data_dir = data_dir

    @abc.abstractmethod
    def precoppy(self, prop, value):
        pass

    @abc.abstractmethod
    def postcoppy(self, prop, value, project_directory):
        pass

    @abc.abstractmethod
    def postrender(self, prop, value, project_directory):
        pass


class License(BaseProcessor):

    license_files = {
        'bsd2': 'LICENSE_BSD2.txt',
        'bsd3': 'LICENSE_BSD3.txt',
        'gpl2': 'LICENSE_GPL2.txt',
        'gpl3': 'LICENSE_GPL3.txt',
        'mit': 'LICENSE_MIT.txt',
        'apache2': 'LICENSE_APACHE2'
    }

    def __init__(self):
        BaseProcessor.__init__(self)

    def precoppy(self, prop, value):
        pass

    def postrender(self, prop, value, project_directory):
        pass

    def postcoppy(self, prop, value, project_directory):
        if prop != "license":
            return

        lic = value.lower()
        license_file = os.path.join(self.data_dir, self.license_files[lic])
        project_license_file = os.path.join(project_directory, 'LICENSE.txt')

        utils.copyfile(license_file, project_license_file)
