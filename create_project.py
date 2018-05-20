#!/usr/bin/python


import sys, os, json

def main():
    config = None
    with open(os.path.dirname(sys.argv[0])+"/config.json", "r") as config_file:
        config = json.load(config_file)
        
    

    generator = sys.argv[1]
    
    print("Generator in use: " + generator)
    if not generator in config:
        print("There is no defined generator with this name")
        exit(1)


    template_dir = (os.path.dirname(sys.argv[0]))+"/"+ config[generator]["root_dir"]
    replacements = {}
    for prop in  config[generator]["properties"]:
        while True:
            if "default" in prop:
                value = input(prop["name"]+"("+prop["default"]+"): ")
                if value.strip() == "":
                    value = prop["default"]
            else:
                value = input(prop["name"]+": ")
                if value.strip() == "":
                    continue
            replacements["%" + prop["name"] + "%"] = value
            break
    print("Final config: " + str(replacements).replace("%", ""))
    location = sys.argv[2]
    if not os.path.isdir(location):
        os.makedirs(location)


    





if __name__ == '__main__':
    main()
    
