import requests
import colorama
from colorama import Fore, init
import shutil
colorama.init()


Yellow = Fore.YELLOW
Green = Fore.GREEN
Reset = Fore.RESET

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input



def Finder():
    username = input_centered(f'{Green}Input an Username {Reset}-> ')

    def github(username):
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return False
        elif response.status_code == 404:
            return True
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
        

    if github(username):
        pass
    else:      
        print(f'[{Green}+{Reset}] {Green}Github - {Reset}https://github.com/{username}')
    # -------------
    def deviantart(username):
        url = f"https://www.deviantart.com/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return False
        return True

    if deviantart(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}DeviantArt - {Reset}https://www.deviantart.com/{username}')
    # -------------
    def flickr(username):
        url = f"https://www.flickr.com/photos/{username}"
        r = requests.get(url)
        if r.status_code == 200:
            return False
        elif r.status_code == 404:
            return True
        
    if flickr(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}Flickr - {Reset}https://www.flickr.com/photos/{username}')
    # -------------
    def speedrun(username):
        url = f'https://www.speedrun.com/api/v1/users?lookup={username}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                return False
            else:
                return True
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')

    if speedrun(username):
        pass
    else:
      print(f'[{Green}+{Reset}] {Green}Speedrun.com - {Reset}https://www.speedrun.com/user/{username}')
    # -------------
    def patreon(username):
        url = f"https://www.patreon.com/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return False
        return True
    
    if patreon(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}Patreon - {Reset}https://www.patreon.com/{username}')
    # -------------
    def behance(username):
        url = f"https://www.behance.net/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return False
        return True

    if behance(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}Behance - {Reset}https://www.behance.net/{username}')
    # -------------
    def dribbble(username):
        url = f"https://dribbble.com/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return False
        return True
    if dribbble(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}Dribbble - {Reset}https://dribbble.com/{username}')
    # -------------
    def Itchio(username):
        url = f"https://itch.io/profile/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return False
        return True

    if Itchio(username):
        pass
    else:
        print(f'[{Green}+{Reset}] {Green}Itch.io - {Reset}https://itch.io/profile/{username}')

    input(f'[{Green}*{Reset}] {Green}Ended.{Reset} Press any {Green}key{Reset} to leave')