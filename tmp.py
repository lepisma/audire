#!/usr/bin/env python

"""
Bootup script
"""

import os, sys
import argparse
from src.display import Display

parser = argparse.ArgumentParser(description = "Tmp is a voice assistance for people with hearing disability")

parser.add_argument("-d",
                    "--diagnose",
                    action = "store_true",
                    help = "Run diagnosis tests and exit")

args = parser.parse_args()

if args.diagnose:
    display = Display()
    display.alert()
    display.show("Hello stalker !")
    display.show("Write few tests and run me again.")










