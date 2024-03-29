#!/usr/bin/env python

import argparse
import sys

arg_parser = argparse.ArgumentParser('Hello world app')
arg_parser.add_argument('name', help='name to say hello to')
options = arg_parser.parse_args()
print(f'hello {options.name}!')
