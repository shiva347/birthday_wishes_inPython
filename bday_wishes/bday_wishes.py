#!/usr/bin/python3

import os, random
from threading import Thread
from time import sleep
from playsound import playsound
from termcolor import colored
from bday_setup import *
art = __import__(f'{bday_decorated_file_name}', globals(), locals(), ['*'])


def replace_multiple_string(main_string, replace_string, new_string):
    """[Replace a set of multiple sub strings with a new string]

    Args:
        main_string ([string]): [String in which the replacement will be done]
        replace_string ([list]): [A list which elements will be replaced by a new_string]
        new_string ([string]): [A string which will be replaced in place of elements of replace]

    Returns:
        [string]: [Return the main string where the element of replace is replaced by new_string]
    """

    # Iterate over the list to be replaced
    for elem in replace_string:
        # Check if the element is in the main string
        if elem in main_string:
            # Replace the string
            main_string = main_string.replace(elem, new_string)

    return main_string


def art_print(art, time):
    color_used = [random.choice(color)]
    color_attribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
            # Color attr set to blink if 9
            if art[i] == '⑨':
                color_attribute = [colorCodes[art[i]]]
            # color attr none if 10
            elif art[i] == '⑩':
                color_attribute = []
            # Random color if R
            elif art[i] == '®':
                color_used = color
            else:
                color_used = [colorCodes[art[i]]]

        print(colored(replace_multiple_string(art[i], colorCodes, ''), random.choice(color_used), attrs=color_attribute), sep='',
              end='', flush=True);
        sleep(time)


def audio_play():
    if play_audio:
        playsound(audio)


def print_code():
    # Print the code before wishing
    if code_print:
        for i in range(len(art.code)):
            print(art.code[i], sep='', end='', flush=True);
            sleep(coding_speed)
        input('\n\n' + colored('python3', 'blue') + colored(' birthdaywishes_from_shiva.py', 'yellow'))
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input()


# Clearing terminal
os.system('cls' if os.name == 'nt' else 'clear')
print_code()
Thread(target=audio_play).start()
Thread(target=art_print, args=(art.birthday_art, speed)).start()
input()
