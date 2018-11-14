import re








class FileProcessor:



    def __init__(self, rapl):
        self.env = repl





    def _replace_tokens(self, tree, f):
        temp = os.path.join(tree, "temp")
        self._replace_tokens(f, replacements, temp)
        os.remove(f)
        os.rename(temp, f)


        
    def _eval_expressions(self, tree, f):
        copy_if_regex = "\{%\{\s*\(\s*copy-if\s*\)\s*\((.*)\s*==\s*\"(.*)\"\s*\)\s*}%\}"
        if_else_regex
        = "\{%\{\s*\(\s*if\s*\)\s*\(\s*%(.*)%\s*==\s*\"(.*)\"\s*\)\s*\}%\}\s*((.|\n)*)\s*\{%\{\s*\(\s*else\s*\)\s*\}%\}\n*((.|\n)*)\n*\{%\{\s*\(\s*endif\s*\)\s*\}%\}"
        
        with open(f, "r+") as file_handle:
            content = file_handle.read()
            copy_match = re.search(copy_if_regex, content, flags=re.IGNORECASE)
            if copy_match:
                token = copy_match.group(1)
                value = copy_match.group(2)
                if self.env[token] != value:
                    #delete file
                    return 
                    
            
            
        
        
        

    def _process_file(self, tree, f):
        self._eval_expressions(tree, f)

        self._replace_tokens(tree, f)
    


    def process_tree(self, replacements, tree, file_names=False):
    for f in os.listdir(tree):
        f = os.path.join(tree, f)
        if file_names:
            for key, val in replacements.items():
                if key in str(f):
                    os.rename(f, str(f).replace(key,val))
                    f = str(f).replace(key,val)
                    break            

        if os.path.isfile(f) and not bon.is_binary(f) :
            self._process_file(tree,f)
        elif os.path.isdir(f):
            self.process_tree(replacements, f, file_names=file_names)

            
        
        
