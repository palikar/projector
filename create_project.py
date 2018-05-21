#!/usr/bin/python


import sys, os, json
import shutil
import binaryornot.check as bon


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def replace_in_file(input_file_name, replacements, output_file_name):
     with open(input_file_name, "r") as input_template, open(output_file_name, "w") as final:
         for line in input_template:
            for src, target in replacements.items():
                line = line.replace(src, str(target))
            final.write(line)

            

def replace_in_tree(replacements, tree, file_names=False):
    for f in os.listdir(tree):
        f = os.path.join(tree, f)
        if file_names:
            for key, val in replacements.items():
                if key in str(f):
                    os.rename(f, str(f).replace(key,val))
                    f = str(f).replace(key,val)
                    break            

        if os.path.isfile(f) and not bon.is_binary(f) :
            temp = os.path.join(tree, "temp")
            replace_in_file(f, replacements, temp)
            os.remove(f)
            os.rename(temp, f)
        elif os.path.isdir(f):
            replace_in_tree(replacements, f, file_names=file_names)

            









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
    proj_dir = os.path.join(location, replacements["%project_name%"])
    if not os.path.isdir(proj_dir):
        os.makedirs(proj_dir)
    copytree(template_dir, proj_dir)

    replace_in_tree(replacements, proj_dir, file_names=True)






if __name__ == '__main__':
    main()
    
