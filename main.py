import subprocess
import sys
import shutil
import time
import colorama
from colorama import Fore, init
colorama.init()

def set_terminal_title(title):
        if sys.platform.startswith('linux'):
            sys.stdout.write(f"\x1b]2;{title}\x07")
        elif sys.platform.startswith('darwin'):
            sys.stdout.write(f"\033]0;{title}\007")
        elif sys.platform.startswith('win'):
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            raise ValueError("Unsupported platform")
        
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


banner = Fore.GREEN + f"""
                     
                                         #*                                     
                                                                                
                                        @@@@                                    
                                       @@@@@@                                   
                                      @@@@@@@@                                  
                                       @@@@@@                                   
                                        @@@@%                                   
                                       @@@@@                                    
                                       @@@@@                                    
                                     ,@@@@@.                                    
                                   @@@@@@@*                                     
                              @@@@@@@@@@@                                       
                           @@@@@@@@@@(              @@@@@@*                     
                         @@@@@@@@              @@@@@@@@@@@@@@@,                 
                        ,@@@@@@@           @@@@@@@@@@@@@@@@@@@@@%               
                        /@@@@@@@@.    &@@@@@@@@@@@      @@@@@@@@@@              
                         @@@@@@@@@@@@@@@@@@@,              @@@@@@@@             
                           @@@@@@@@@@@@@                    @@@@@@@             
                                                           &@@@@@@@             
                                 .@@@@@@@@@@@@@@@(       *@@@@@@@@              
                            .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                       @@@@@@@@%               @@@@@@@@@@@@@&                   
                     *@@@@@@          ,@@@@@@@@#                                
                    @@@@@@         *@@@@@@@@@@@@@@                              
                   (@@@@@         @@@@@       @@@@                              
                   @@@@@*       @@@@@&        @@@@                              
                   @@@@@@      @@@@@         @@@@,                              
                   @@@@@@@@@@@@@@@@       @@@@@@                                
                    @@@@@@@@@@@@@     @@@@@@,                                   
                      ,@@@@@@@@     @@@                                         
                                   @@                                           
                                  @@                                            
                                  &@                                            
                                   @@                                           
                                     @                                                                                                                              
{Fore.RESET}"""
set_terminal_title('Apophis')
print(banner)

input_centered(f'Press any key to start using {Fore.GREEN}Apophis{Fore.RESET}...')
clear_console()

while True:
    set_terminal_title('Apophis | Made by TheCuteOwl')
    Category = input_centered(Fore.RESET +f'''
Which category of {Fore.GREEN}tools{Fore.RESET} do you want to use ?

[{Fore.GREEN}1{Fore.RESET}] {Fore.GREEN}Information Tools{Fore.RESET}
[{Fore.GREEN}2{Fore.RESET}] {Fore.GREEN}Discord Tools{Fore.RESET}

-> ''')

    if Category == '1':
        clear_console()
        while True:
            set_terminal_title('Apophis - Information | Made by TheCuteOwl')
            Information_Choice = input_centered(f"""
            Information {Fore.GREEN}Tools{Fore.RESET} List : 
        [{Fore.GREEN}1{Fore.RESET}] {Fore.GREEN}Social Media Accounts Hunter{Fore.RESET}
        [{Fore.GREEN}2{Fore.RESET}] {Fore.GREEN}Locate An IP{Fore.RESET}
        [{Fore.GREEN}99{Fore.RESET}] {Fore.GREEN}Back{Fore.RESET}
        ->  """)

        

            if Information_Choice == "1":
                clear_console()
                from utils.Social.SocialHunter import Finder
                Finder()
                clear_console()
            
            if Information_Choice == "2":
                clear_console()
                from utils.Social.IPLocate import get_ip_info
                get_ip_info()
                clear_console()

            elif Information_Choice == "99":
                clear_console()
                break
            else:
                clear_console()
            
    elif Category == '2':
        clear_console()
        while True:
            set_terminal_title('Apophis - Discord | Made by TheCuteOwl')
            Discord_Choice = input_centered(f"""
        Discord Tools List : 
        [{Fore.GREEN}1{Fore.RESET}] {Fore.GREEN}ID To Token (Only get the first part){Fore.RESET}
        [{Fore.GREEN}2{Fore.RESET}] {Fore.GREEN}Nitro Generator (Unchecked){Fore.RESET}
        [{Fore.GREEN}3{Fore.RESET}] {Fore.GREEN}Webhook Spammer And Deleter{Fore.RESET}
        [{Fore.GREEN}99{Fore.RESET}] {Fore.GREEN}To go back{Fore.RESET}
        ->  """)
            if Discord_Choice == '1':
                clear_console()
                from utils.Discord.IdToken import IDToken
                IDToken()
                clear_console()

            elif Discord_Choice == '2':
                clear_console()
                from utils.Discord.NitroGenerator import Gen
                Gen()
                clear_console()

            elif Discord_Choice == '3':
                clear_console()
                from utils.Discord.Webhooker import main
                main()
                clear_console()

            elif Discord_Choice == '99':
                clear_console()
                break

            else:
                pass
            

    else:
        clear_console()
