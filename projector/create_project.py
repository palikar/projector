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
    parser.add_argument('generator', type=str,nargs="?", default='no_gen',
			help='The name of the template to be used for generating the new project')

    parser.add_argument('direcotry', type=str, default="~/code/",nargs="?",
			help='The direcotry where the new project will be created')
    parser.add_argument('--list-gen', action='store_true',
			help='List all the available generators')

    parser.add_argument('--config', dest='config_dir', action='store',default=None,
			help='A custom configuraion directory')

    return parser


def main():

    parser = get_parser()
    args = parser.parse_args()

    data_dir = None
    config_file = None

    if args.config_dir is not None:

        if not os.path.isdir(args.config_dir):
            print(f'{args.config_dir} is not a directory!')
            exit(1)

        if not os.path.isfile(os.path.join(args.config_dir, 'config.json')):
            print(f'There is no \'config.json\' in {args.config_dir}!')
            exit(1)
        
        data_dir = os.path.abspath(args.config_dir )
        config_file = os.path.join(args.config_dir, 'config.json')

    else:
        
        config = None
        data_dir = os.path.expanduser('~/.config/projector')
        config_file = os.path.join(data_dir, "config.json")

        if not os.path.isdir(data_dir):
            print(f"Configuraion direcotry is missing. {data_dir} is not a file!")
            exit(1)

        if not os.path.isfile(config_file):
            print(f"Configuraion file is missing. {config_file} is not a file!")
            exit(1)


    with open(config_file, 'r') as config_file_fd:
        config = json.load(config_file_fd)
    



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






        
        

    
