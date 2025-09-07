import time
from colorama import init, Style  # ← ДОБАВЬ Style ЗДЕСЬ
from config import HEART_COLOR, TITLE_COLOR, INTRO_DELAY
from lyrics import lyrics, heart_art
from printer import print_smoothly, countdown

def main():
    init()  # Инициализация colorama

    # Заставка с сердечком
    print(HEART_COLOR + heart_art + Style.RESET_ALL)
    print(TITLE_COLOR + "               ♡ FOR MY GIRL ♡")
    print("\n" + "═" * 50 + Style.RESET_ALL)

    time.sleep(INTRO_DELAY)

    # Обратный отсчет
    print(TITLE_COLOR + "\nЗапуск через...")
    countdown()
    print("\n" + Style.RESET_ALL)

    try:
        # Печать текста песни
        for line, pause_after in lyrics:
            print_smoothly(line)
            time.sleep(pause_after)

        # Финальное сообщение
        print(HEART_COLOR + "\n" + "♡" * 30)
        print("by my girl")
        print("♡" * 30 + Style.RESET_ALL)

    except KeyboardInterrupt:
        print('\n\nStopped with love...')

if __name__ == "__main__":
    main()