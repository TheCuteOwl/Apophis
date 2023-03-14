import requests
import time
import colorama
from colorama import Fore, init
import shutil
import sys, subprocess
colorama.init()


Yellow = Fore.YELLOW
Green = Fore.GREEN
Reset = Fore.RESET

def clear_console():
    if sys.platform.startswith('win'):
        _ = subprocess.call('cls', shell=True)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        _ = subprocess.call('clear', shell=True)
    else:
        print('Unsupported platform. Cannot clear console.')


def print_centered(text):
    console_width, _ = shutil.get_terminal_size()
    padding = (console_width - len(text)) // 2
    print(' ' * padding + text)

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input


def SpammingCustom():
    url = input_centered(f'{Green}Webhook{Reset} URL : ')
    messages = input_centered((f'{Green}Message{Reset} To Spam : '))
    timetospam = input_centered(f'How many {Green}time{Reset} do you want to send the {Green}message{Reset}? : ')
    message = messages
    data = {
    "content" : message,
    "username" : "Spam Moment"
}


    for i in range(int(timetospam)):
        result = requests.post(url, json = data)
        time.sleep(0.2)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print_centered(f"{Fore.RED}Error {Reset}retrying...")
        else:
          print_centered(f"{Green}Send{Reset} successfully")

    input_centered(f'{Green}Ended.{Reset} Press Any {Green}Key{Reset} to Leave')

def delete():
    webhook = input_centered(f'{Green}Webhook{Reset} URL -> ')
    requests.delete(webhook)
    print_centered(f'{Green}Successfully{Reset} Deleted')
    input_centered(f'Press any {Green}key{Reset} to quit')

def main():
    inputmain = input_centered(f'''
    Which {Green}webhook{Reset} tools you want to use ?
    
    [{Green}1{Reset}] {Green}Webhook Spammer{Reset}
    [{Green}2{Reset}] {Green}Webhook Deleter{Reset}
    
    -> ''')

    if inputmain == '1':
        clear_console()
        SpammingCustom()
    elif inputmain == '2':
        clear_console()
        delete()
    else:
        clear_console()
        print_centered(f'{Fore.RED}Wrong{Reset} Input')
        time.sleep(1)
        clear_console()
        main()

