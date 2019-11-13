import sys
import readline


readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode emacs')


class PropertyReader:

    def __init__(self):
        self.props = []

    @staticmethod
    def _check_property(prop):
        binary = "y_n" in prop and prop["y_n"]
        choices = prop["choice"] if "choice" in prop else None

        if binary and choices is not None:
            print("Inconsisten property: " + prop["name"])
            sys.exit(1)

    @staticmethod
    def _process_prop(prop):

        default = prop["default"] if "default" in prop else None
        binary = "y_n" in prop and prop["y_n"]
        choices = prop["choice"] if "choice" in prop else None

        value = None
        if binary:

            while value is None:
                if default in ("n", "y"):
                    value = input(prop["name"] + "[y/n]("+default+") :")
                    if value.stip() == "":
                        value = default
                else:
                    value = input(prop["name"] + "[y/n]:")
                if value not in ("y", "n"):
                    value = None
                    print("Please type \'y\' or \'n\' ")

        elif choices is not None:

            while value is None:
                if default in choices:
                    value = input(prop["name"]
                                  + "\n[" + str(choices)
                                  + "]\n(" + default
                                  + ")\n:")
                    if value.stip() == "":
                        value = default
                else:
                    value = input(prop["name"]+"\n"+str(choices)+"\n:")
                    if value not in choices:
                        value = None
                        print("The value must be in the set of choices")

        else:

            while value is None:
                if default is not None:
                    value = input(prop["name"]+"("+prop["default"]+"): ")
                    if value.strip() == "":
                        value = prop["default"]
                else:
                    value = input(prop["name"]+": ")
                    if value.strip() == "":
                        continue
        return value

    def load_properties(self, props):
        for prop in props:
            if "name" not in prop.keys() or "token" not in prop.keys():
                print(prop)
                print("Invalid property. Name or token missing ")
                sys.exit(1)
            PropertyReader._check_property(prop)

        self.props = props

    def read(self):
        repl = {}
        for prop in self.props:
            value = PropertyReader._process_prop(prop)
            repl[prop["token"]] = value
        return repl
