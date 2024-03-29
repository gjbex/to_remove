#!/usr/bin/env python

import argparse
import greetings
import sys

arg_parser = argparse.ArgumentParser('Hello world app')
arg_parser.add_argument('name', help='name to say hello to')
options = arg_parser.parse_args()
greetings.hello()
