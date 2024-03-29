#!/usr/bin/env python

import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='whom to say bye to')
options = arg_parser.parse_args()

print(f'bye {options.name}!')
