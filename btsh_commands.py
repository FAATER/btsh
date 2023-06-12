#!/usr/bin/env python3

import os
import sys

COLOR_DEFAULT = "\033[0m"
COLOR_DIRECTORY = "\033[1;34m"  # Azul brillante
COLOR_EXECUTABLE = "\033[1;32m"  # Verde brillante
COLOR_FILE = "\033[0;36m"  # Cian para archivos (extensiones generales)

version = "alpha 1"
help_command = (
    "version | see version app\n"
    "clear | clear history console\n"
    "info | check info app\n"
    "exit | exit app\n"
    "ext_command | execute external commands\n"
    "ls | see files on directory\n"
    "help | see help\n"
)

def mt_version():
    print(version)

def cd(directory):
    try:
        if directory == "..":
            os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
        else:
            os.chdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except NotADirectoryError:
        print(f"'{directory}' is not a valid directory.")
    except PermissionError:
        print(f"You don't have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def mt_help():
    print(help_command)

def clear():
    os.system("clear")

def info():
    print("MultiOs Terminal version Prototype\nJune 4 2023")

def exit_app():
    sys.exit()

def ext_command():
    exte_command = input("Please enter external command >> ")
    os.system(exte_command)

def ls():
    files = os.listdir()
    for file in files:
        path = os.path.join(os.getcwd(), file)
        if os.path.isdir(path):
            print(f"{COLOR_DIRECTORY}{file}{COLOR_DEFAULT}")
        elif os.access(path, os.X_OK):
            print(f"{COLOR_EXECUTABLE}{file}{COLOR_DEFAULT}")
        else:
            print(f"{COLOR_FILE}{file}{COLOR_DEFAULT}")

def check_command(arg1):
    cadena = arg1
    primera_letra = cadena[0]
    palabras = cadena.split()
    primera_palabra = palabras[0]
    resto_cadena = ' '.join(palabras[1:])
    if primera_palabra == "ls":
        ls()
    elif primera_palabra == "cd":
        cd(resto_cadena)
    elif primera_palabra == "exit":
        exit_app()
    elif primera_letra == "/":
        os.system(primera_palabra+" "+resto_cadena)
    else:
        os.system("/bin/"+primera_palabra+" "+resto_cadena)

if __name__ == "__main__":
    print("Please open: multios-terminal.py")
