import requests
import colorama
from colorama import Fore, init
colorama.init()
import shutil

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input


Yellow = Fore.YELLOW
Green = Fore.GREEN
Reset = Fore.RESET


def get_ip_info():
    ip_address = input_centered(f'Enter an {Green}IP Address{Reset} To Locate {Green}->{Reset} ')
    url = f"https://ipwhois.app/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        ip = data.get('ip', '')
        city = data.get('city', '')
        region = data.get('region', '')
        country = f"{data.get('country_name', '')} ({data.get('country_code', '')})"
        latitude = data.get('latitude', '')
        longitude = data.get('longitude', '')
        postal_code = data.get('postal', '')
        timezone = data.get('timezone_gmt', '')
        asn = data.get('asn', '')
        organization = data.get('isp', '')
        
        print(f"[{Green}+{Reset}] IP Address:{Green} {ip} {Reset}")
        print(f"[{Green}+{Reset}] City:{Green} {city} {Reset}")
        print(f"[{Green}+{Reset}] Region:{Green} {region} {Reset}")
        print(f"[{Green}+{Reset}] Country:{Green} {country} {Reset}")
        print(f"[{Green}+{Reset}] Latitude:{Green} {latitude} {Reset}")
        print(f"[{Green}+{Reset}] Longitude:{Green} {longitude} {Reset}")
        print(f"[{Green}+{Reset}] Postal Code:{Green} {postal_code} {Reset}")
        print(f"[{Green}+{Reset}] Timezone:{Green} {timezone} {Reset}")
        print(f"[{Green}+{Reset}] ASN:{Green} {asn} {Reset}")
        print(f"[{Green}+{Reset}] Organization :{Green} {organization} {Reset}")
    else:
        print(f"{Fore.RED}Error: {response.status_code}")
    input(f'[{Green}*{Reset}] Ended Press {Green}Any{Reset} Key To {Green}Leave{Reset}')
