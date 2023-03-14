def Gen():
    import colorama
    from colorama import Fore, init
    colorama.init()
    import ctypes
    import random
    import string
    import sys
    import shutil

    Yellow = Fore.YELLOW
    Green = Fore.GREEN
    Reset = Fore.RESET

    def input_centered(prompt):
        console_width, _ = shutil.get_terminal_size()
        prompt_lines = prompt.split('\n')
        padding = (console_width - max(len(line) for line in prompt_lines)) // 2
        centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
        user_input = input(centered_prompt)

    def print_centered(text):
        console_width, _ = shutil.get_terminal_size()
        padding = (console_width - len(text)) // 2
        print(' ' * padding + text)
    char = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
    number = 0
    Result = ''

    import sys

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

    set_terminal_title("NITROGEN | Made by https://github.com/TheCuteOwl Code Generated : 0")

    print_centered(f'''{Green}
    ███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗
    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝{Reset}''')

    print_centered(f'You will need {Green}checker{Reset} to {Green}check{Reset} the code')
    gen = input(f'How many code do you want to {Green}generate{Reset} ? : ')
    with open('result.txt', 'w') as f:
        for i in range(int(gen)):
            Result += f'https://discord.gift/{"".join(random.choices(char, k=16))}'
            number += 1
            set_terminal_title('Nitro Gen | Made by https://github.com/TheCuteOwl Code Generated : ' + str(number))
            print(f"[{Green}Gen{Reset}] | {Result}")
            f.write(Result+ '\n')
            Result = ''
    input_centered(f'\n\n\nSuccesfully {Green}Generated{Reset}, Saved into result.txt file, Press {Green}enter{Reset} to close')
