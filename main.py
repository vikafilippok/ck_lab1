import argparse
import os
import shutil
import winreg


########## CREATE FILE #########################
def create(name):
    try:
        with open(name, "x") as file:
            print("File created")
    except FileExistsError:
        print("Error: file is already exist")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")

########## REMOVE #########################
def remove(name):
    try:
        os.remove(name)
        print("File deleted")
    except FileNotFoundError:
        print("Error: file not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## WRITE #########################
def write(name, value):
    try:
        with open(name, "w") as file:
            file.write(value)
            print("Written to file")
    except FileNotFoundError:
        print("Error: file not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## READ #########################
def read(name):
    try:
        with open(name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: file not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


def copy(full_path, directory):
    try:
        shutil.copy2(full_path, directory)
        print("File copied to another directory")
    except FileNotFoundError:
        print("Error: file not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## RENAME #########################
def rename(old_name, new_name):
    try:
        os.renames(old_name, new_name)
        print("File|Directory renamed from", old_name, "to", new_name)
    except FileNotFoundError:
        print("Error: file not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## CREATE KEY #########################
def create_key(Hkey, sub_key):
    try:
        if Hkey == "HKEY_CLASSES_ROOT":
            winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_CURRENT_USER":
            winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_LOCAL_MACHINE":
            winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_USERS":
            winreg.CreateKeyEx(winreg.HKEY_USERS, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_CURRENT_CONFIG":
            winreg.CreateKeyEx(winreg.HKEY_CURRENT_CONFIG, sub_key, 0, winreg.KEY_ALL_ACCESS)
        print("The key has been created")
    except PermissionError:
        print("Access error. Administrator rights are required to create a registry key.")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## REMOVE KEY #########################
def remove_key(Hkey, sub_key):
    try:
        if Hkey == "HKEY_CLASSES_ROOT":
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, sub_key)
        elif Hkey == "HKEY_CURRENT_USER":
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, sub_key)
        elif Hkey == "HKEY_LOCAL_MACHINE":
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, sub_key)
        elif Hkey == "HKEY_USERS":
            winreg.DeleteKey(winreg.HKEY_USERS, sub_key)
        elif Hkey == "HKEY_CURRENT_CONFIG":
            winreg.DeleteKey(winreg.HKEY_CURRENT_CONFIG, sub_key)
        print("The key removed successfully")
    except FileNotFoundError:
        print("The key was not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########## WRITE TO KEY #########################
def write_value_to_key(Hkey, sub_key, name, value):
    try:
        if Hkey == "HKEY_CLASSES_ROOT":
            key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_CURRENT_USER":
            key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_LOCAL_MACHINE":
            key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_USERS":
            key = winreg.OpenKeyEx(winreg.HKEY_USERS, sub_key, 0, winreg.KEY_ALL_ACCESS)
        elif Hkey == "HKEY_CURRENT_CONFIG":
            key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_CONFIG, sub_key, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        use_value = winreg.QueryValueEx(key, name)
        print("A value has been added to the key:", use_value)
    except FileNotFoundError:
        print("The key was not found")
    except Exception as e:
        print(f"An error occurred while creating the key: {e}")


########### PARSE #################
def parse():
    command_line = argparse.ArgumentParser(prog="FILE SYSTEM|REGISTRY MANAGEMENT BY CLI")
    command_line.add_argument("--create", metavar="FILE", help="Create a new file", nargs=1, type=str)
    command_line.add_argument("--remove", metavar="FILE", help="Remove a file", nargs=1, type=str)
    command_line.add_argument("--write", metavar=("FILE", "TEXT"), help="Write to a file", nargs=2, type=str)
    command_line.add_argument("--read", metavar="FILE", help="Read from a file", type=str)
    command_line.add_argument("--copy", metavar=("PATH1", "PATH2"), help="Copy file from PATH1 to PATH2", nargs=2,
                              type=str)
    command_line.add_argument("--rename", metavar=("OLD", "NEW"), help="Rename a file", nargs=2, type=str)
    command_line.add_argument("--createKey", metavar=("KEY", "SUB_KEY"), help="Create a new SUB_KEY in KEY", nargs=2, type=str)
    command_line.add_argument("--removeKey", metavar=("KEY", "SUB_KEY"), help="Remove a key", nargs=2, type=str)
    command_line.add_argument("--writeToKey", metavar=("KEY", "SUB_KEY", "NAME", "VALUE"), help="Write value to key", nargs=4, type=str)

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
    write_value_to_key(arg.writeToKey[0], arg.writeToKey[1], arg.writeToKey[2], arg.writeToKey[3])
