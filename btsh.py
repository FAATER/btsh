#!/usr/bin/env python3

from btsh_commands import *
import os
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import prompt

color_code = 34  # Código de color ANSI para azul

def print_welcome_message():
    os.system("clear")
    global color_code
    color = f"\033[{color_code}m"  # Secuencia de escape ANSI para cambiar el color del texto
    print(f"{color}Beautiful_SH is running")
    print(f"version: {version}\033[0m")  # Se restaura el color original al finalizar

def print_current_directory():
    current_dir = os.getcwd()
    root_dir = os.path.abspath(os.sep)
    levels = len(current_dir.split(os.sep)) - len(root_dir.split(os.sep))
    global color_code
    color = f"\033[{color_code}m"  # Secuencia de escape ANSI para cambiar el color del texto
    prompt_text = f"{color}╭─({current_dir})"
    print(prompt_text)

if __name__ == "__main__":
    print_welcome_message()

    # Configurar autocompletado
    executables = os.listdir('/bin')
    completer = WordCompleter(executables)

    # Configurar estilo del prompt
    style = Style.from_dict({
        "prompt": "fg:blue",
    })

    while True:
        try:
            print_current_directory()
            ejecucion = prompt("╰─❯ ", completer=completer, style=style)
            check_command(ejecucion)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
