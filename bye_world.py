#!/usr/bin/env python

import argparse
import greetings

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='whom to say bye to')
options = arg_parser.parse_args()

greetings.bye(options.name)
