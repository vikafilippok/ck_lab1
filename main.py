import argparse
import os
import shutil
import winreg

def create(name):
    try:
        with open(name, "x") as file:
            print("File created")
    except FileExistsError:
        print("Error: file is already exist")
def remove(name):
    try:
        os.remove(name)
        print("File deleted")
    except FileNotFoundError:
        print("Error: file not found")
def write(name, value):
    try:
        with open(name, "w") as file:
            file.write(value)
            print("Written to file")
    except FileNotFoundError:
        print("Error: file not found")

def read(name):
    try:
        with open(name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: file not found")
def copy(full_path, directory):
    try:
        shutil.copy2(full_path, directory)
        print("File copied to another directory")
    except FileNotFoundError:
        print("Error: file not found")

#def rename(old_name, new_name):
#def create_key(key, name):
#def remove_key(key, name):
#def write_to_key(key, name, value):

########### PARSE #################
def parse():
    command_line = argparse.ArgumentParser(prog="FILE SYSTEM|REGISTRY MANAGEMENT BY CLI")
    command_line.add_argument("--create", metavar="FILE", help="Create a new file", nargs=1, type=str)
    command_line.add_argument("--remove", metavar="FILE", help="Remove a file", nargs=1, type=str)
    command_line.add_argument("--write", metavar=("FILE", "TEXT"), help="Write to a file", nargs=2, type=str)
    command_line.add_argument("--read", metavar="FILE", help="Read from a file", type=str)
    command_line.add_argument("--copy", metavar=("PATH1", "PATH2"), help="Copy file from PATH1 to PATH2", nargs=2, type=str)
    command_line.add_argument("--rename", metavar=("OLD", "NEW"), help="Rename a file", nargs=2, type=str)
    command_line.add_argument("--createKey", metavar=("KEY", "NAME"), help="Create a new key", nargs=2, type=str)
    command_line.add_argument("--removeKey", metavar=("KEY", "NAME"), help="Remove a key", nargs=2, type=str)
    command_line.add_argument("--writeToKey", metavar=("KEY", "NAME", "VALUE"), help="Write value to key", nargs=3, type=str)

    return command_line.parse_args()

############ MAIN ##################
arg = parse()

if arg.create:
    create(arg.create[0])
elif arg.remove:
    remove(arg.remove)
elif arg.write:
    write(arg.write[0], arg.write[1])
elif arg.read:
    read(arg.read)
elif arg.copy:
    copy(arg.copy[0], arg.copy[1])
elif arg.rename:
    rename(arg.rename[0], arg.rename[1])
elif arg.createKey:
    create_key(arg.createKey[0], arg.createKey[1])
elif arg.removeKey:
    remove_key(arg.removeKey[0], arg.removeKey[1])
elif arg.writeToKey:
    write_to_key(arg.writeToKey[0], arg.writeToKey[1], arg.writeToKey[2])

