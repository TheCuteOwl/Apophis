import shutil
import base64
import colorama
from colorama import Fore, init
colorama.init()

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input


def IDToken():
    ID = input_centered(str(f'{Fore.GREEN}Enter an Discord ID {Fore.RESET}-> ')).encode()
    Token = base64.b64encode(ID)
    print(f'{Fore.GREEN}Discord{Fore.RESET} token start with {Fore.GREEN}{Token.decode()}{Fore.RESET}')
    input(f'\nPress Any Key To Leave{Fore.RESET}')