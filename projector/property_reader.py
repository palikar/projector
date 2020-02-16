import sys
import readline


readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode emacs')


class OptionsCompleter():

    def __init__(self, options):
        self.options = sorted(options)
        self.matches = []

    def get_matches(self):
        return self.matches

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)]
            else:
                self.matches = self.options[:]

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None

        return response


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
    def _process_binary(prop, default):
        value = None
        while value is None:
            if default in ("n", "y"):
                value = input(prop["name"] + "[y/n]("+default+") :")
                if value.stip() == "":
                    value = default
            else:
                value = input(prop["name"] + "[y/n]:")
            if value.lower() not in ("y", "n", "yes", "no"):
                value = None
                print("Please type \'y\' or \'n\' ")

        return value in ("y", "yes")

    @staticmethod
    def _process_choices(prop, default, choices):
        readline.set_completer(
            OptionsCompleter(choices).complete)
        value = None
        while value is None:
            if default in choices:
                value = input(prop["name"]
                              + "\n" + str(choices)
                              + "\n(" + default
                              + ")\n:")
                if value.stip() == "":
                    value = default
            else:
                value = input(prop["name"]+str(choices)+":")
                if value not in choices:
                    value = None
                    print("The value must be in the set of choices")

        readline.set_completer(None)
        return value

    @staticmethod
    def _process_text(prop, default):
        value = None
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

    @staticmethod
    def _process_prop(prop):

        default = prop["default"] if "default" in prop else None
        binary = "y_n" in prop and prop["y_n"]
        choices = prop["choice"] if "choice" in prop else None

        value = None
        if binary:
            return PropertyReader._process_binary(prop, default)
        elif choices is not None:
            return PropertyReader._process_choices(prop, default, choices)
        else:
            return PropertyReader._process_text(prop, default)

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
