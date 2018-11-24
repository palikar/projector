#!/usr/bin/python


import sys
import os
import json
import argparse

from .property_reader import PropertyReader
from .generator import Generator
from .renderer import Renderer


            


def get_parser():
    parser = argparse.ArgumentParser(description='Generates boiler plate projects')
    parser.add_argument('generator', type=str, default="no_gen",nargs="?",
			help='The name of the template to be used for generating the new project')

    parser.add_argument('direcotry', type=str, default="~/code/",nargs="?",
			help='The direcotry where the new project will be created')
    parser.add_argument('--list-gen', action='store_true',
			help='List all the available generators')

    return parser


def main():

    config = None
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    config_file = os.path.join(os.path.dirname(__file__), "data", "config.json")
    if not os.path.isfile(config_file):
        print("Configuraion file is missing")
        exit(1)

    with open(config_file, "r") as config_file_fd:
        config = json.load(config_file_fd)
    
    parser = get_parser()
    args = parser.parse_args()



    if args.list_gen:
        print("Available generators:")
        for gen, gen_node in config.items():
            print(gen)
        exit(0)


    generator = args.generator    
    if not generator in config.keys():
        print("There is no defined generator with this name")
        exit(1)
    print("Generator in use: " + generator)


    reader = PropertyReader()
    renderer = Renderer()
    gen = Generator(config[generator], reader, renderer, data_dir = data_dir)
    gen(args.direcotry)

if __name__ == '__main__':
    main()






        
        

    
