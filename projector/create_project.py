#!/usr/bin/env python
import os
import json
import argparse
import sys
import termtables

from projector.property_reader import PropertyReader
from projector.generator import Generator
from projector.renderer import Renderer

def list_projects(config):
    print("Available generators:")
    rows = []
    for gen, props in config.items():
        rows.append([gen, props.get('root_dir', ''), props.get('description', '')])

    string = termtables.to_string(
        rows,
        header=['Project' , 'Root folder', 'Description'],
        style=termtables.styles.ascii_thin_double,
        padding=(0, 1),
        alignment="lcc")
    print(string)
    exit(0)
    

def get_parser():
    parser = argparse.ArgumentParser(
        description='Generates boiler plate projects')
    parser.add_argument('generator',
                        type=str, nargs="?", default='no_gen',
                        help='The name of the template to be\
 used for generating the new project')

    parser.add_argument('direcotry',
                        type=str, default="~/code/", nargs="?",
                        help='The direcotry where the\
new project will be created')

    parser.add_argument('--list-gen', action='store_true',
                        help='List all the available generators')

    parser.add_argument('--config', dest='config_dir',
                        action='store', default=None,
                        help='A custom configuraion directory')

    return parser


def main():

    parser = get_parser()
    args = parser.parse_args()

    data_dir = None
    config_file = None

    if args.config_dir is not None:

        if not os.path.isdir(args.config_dir):
            print('{} is not a directory!'.format(args.config_dir))
            sys.exit(1)

        if not os.path.isfile(os.path.join(args.config_dir, 'config.json')):
            print('There is no \'config.json\' in {}!'.format(args.config_dir))
            sys.exit(1)

        data_dir = os.path.abspath(args.config_dir)
        config_file = os.path.join(args.config_dir, 'config.json')

    else:

        config = None
        data_dir = os.path.expanduser('~/.config/projector')
        config_file = os.path.join(data_dir, "config.json")

        if not os.path.isdir(data_dir):
            print("Configuraion direcotry is missing.\
 {} is not a file!".format(data_dir))
            sys.exit(1)

        if not os.path.isfile(config_file):
            print("Configuraion file is missing.\
 {} is not a file!".format(config_file))
            sys.exit(1)

    with open(config_file, 'r') as config_file_fd:
        config = json.load(config_file_fd)

    if args.list_gen:
        list_projects(config)

    generator = args.generator
    if generator not in config.keys():
        print("There is no defined generator with this name")
        sys.exit(1)
    print("Generator in use: " + generator)

    reader = PropertyReader()
    renderer = Renderer()
    gen = Generator(config[generator], reader, renderer, data_dir=data_dir)
    gen.gen(args.direcotry)


if __name__ == '__main__':
    main()
