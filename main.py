import argparse
import os
import shutil
import winreg


command_line = argparse.ArgumentParser(prog="FILE SYSTEM|REGISTRY MANAGEMENT BY CLI")
command_line.add_argument("--create", nargs=1, metavar="FILE", help="Create a new file", type=str)
command_line.add_argument("--remove", metavar="FILE", help="Remove a file", nargs=1, type=str)
command_line.add_argument("--write", metavar=("FILE", "TEXT"), help="Write to a file", nargs=2, type=str)
command_line.add_argument("--read", metavar="FILE", help="Read from a file", nargs=1, type=str)
command_line.add_argument("--copy", metavar=("FILE", "PATH1", "PATH2"), help="Copy FILE from PATH1 to PATH2 (folder without file name)", nargs=3, type=str)
command_line.add_argument("--rename", metavar=("OLD", "NEW"), help="Rename a file", nargs=2, type=str)
command_line.add_argument("--create-key", metavar="KEY", help="Create a new key", nargs=1, type=str)
command_line.add_argument("--remove-key", metavar="KEY", help="Remove a key", nargs=1, type=str)
command_line.add_argument("--write-key", metavar=("KEY", "NAME", "VALUE"), help="Write value to key", nargs=3, type=str)

args = command_line.parse_args()


