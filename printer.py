import time
import sys
from colorama import Style
from config import CHAR_DELAY

def print_smoothly(text, delay=CHAR_DELAY):
    """Печатает текст плавно, символ за символом."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def countdown(seconds=3):
    """Обратный отсчет перед началом."""
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)