


class PropertyReader:
    def __init__(self):
        pass


    def _check_property(self, prop):
        default = prop["default"] if "default" in prop else None
        binary = "y_n" in prop and prop["y_n"]
        choices = prop["choice"] if "choice" in prop else None

        if binary and choices is not None:
            print("Inconsisten property: " + prop["name"])
            exit(1)
        
    
    def _process_prop(self, prop):


        
        default = prop["default"] if "default" in prop else None
        binary = "y_n" in prop and prop["y_n"]
        choices = prop["choice"] if "choice" in prop else None

        value = None
        if binary:

            while value is None:
                if default == "y" or default == "n":
                    value = input(prop["name"] + "[y/n]("+default+") :") 
                    if value.stip() is "":
                        value = default
                else:
                    value = input(prop["name"] + "[y/n]:")
                if  value != "n" and value != "y":
                    value = None
                    print("Please type \'y\' or \'n\' ")
                    
        elif choices is not None:

            while value is None:
                if default in choices:
                    value = input(prop["name"]+"\n["+str(choices)+"]\n("+default+")\n:")
                    if value.stip() is "":
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
                exit(1)
            self._check_property(prop)

        self.props = props

        
    def read(self):
        repl = {}
        for prop in  self.props:
            value = self._process_prop(prop)
            repl[prop["token"]] = value
        return repl





    
