import time
import sys
from colorama import Fore, Back, Style, init

init()

#Текст песни
lyrics = [
    (Fore.RED + "All I want is you now", 0.2),
    (Fore.RED + "All I wanna do now", 0.2),
    (Fore.RED + "Is wait for you to call me", 0.2),
    (Fore.RED + "Baby, I'm so sorry", 0.2),
    (Fore.YELLOW + "Do you wanna hurt me?", 0.2),
    (Fore.YELLOW + "Are you gonna hurt me?", 0.2),
    (Fore.RED + "Please don't desert me", 0.2),
    (Fore.RED + "Please don't desert me", 0.2),
    (Fore.YELLOW + "All I want is you now", 0.2),
    (Fore.YELLOW + "All I wanna do now", 0.2),
    (Fore.RED + "Is wait for you to call me", 0.2),
    (Fore.BLUE + "Baby, I'm so sorry", 0.2),
    (Fore.YELLOW + "Do you wanna hurt me?", 0.2),
    (Fore.YELLOW + "Are you gonna hurt me?", 0.2),
    (Fore.RED + "Please don't desert me", 0.2),
    (Fore.RED + Style.BRIGHT + "Please don't desert me" + Style.RESET_ALL, 0.5),
]

def print_smoothly(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def main():
    # ASCII-заставка
    print(Fore.MAGENTA + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⡄⠖⠘⠈⠚⠞⢅⠄
⠀⠔⠎⢁⠱⠑⠥⣁⠀⡄⠀⠀⠄⠉⠁⠀⠀⠀⠀⠈⠃⠇
⢐⠅⣐⠃⠀⠀⠀⠀⠒⣄⡰⠉⠇⠀⠀⠀⠀⠀⠀⠡⢉⠀
⠠⡡⠂⠀⠀⠀⠀⠀⠀⠉⠫⡅⠀⠀⠀⠀⠀⠀⠂⡂⠀⠀
⠀⠱⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡒⠁⠀⠀
⠀⠀⠍⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠔⠁⠀⠀⠀
⠀⠀⠈⠠⠈⠙⡔⠠⠀⠀⠀⠀⠀⠀⠀⠠⠌⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠂⡀⠉⠎⡂⠄⠀⠀⠀⡠⠍⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠢⠌⡙⣧⡢⡰⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡿⠅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁
""" + Style.RESET_ALL)

    print(Fore.WHITE + "")

    time.sleep(2)
    try:
        for line, pause_after in lyrics:
            print_smoothly(line, delay=0.055)
            time.sleep(pause_after)


        print(Fore.WHITE + "by" + Fore.RED + " my girl")

    except KeyboardInterrupt:
        print(Fore.YELLOW + '\n\nStopped with love...' + Style.RESET_ALL)

if __name__ == "__main__":
    main()