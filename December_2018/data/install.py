from .game_state import *
from time import sleep
from subprocess import Popen
import sys
import platform

def main():
    while gameState['install']['stage'] != len(STAGES):
        STAGES[gameState['install']['stage']]()
        gameState['install']['stage'] += 1
        saveState()
    gameState['install']['stage'] = -1
    saveState()

def greet():
    typeWrite('Thank you. ', interval = 0.1)
    sleep(1.5)
    typeWrite('Thank you for starting', end = ' ', interval = 0.1)
    sleep(1)
    typeWrite('to play this game. ', interval = 0.1)
    sleep(1)
    print()
    typeWrite('For this game to run, let us install some dependencies. ')
    sleep(1)
    typeWrite('First of all, we need pip. ')
    try:
        Popen('python3 -V', stdout = 0)
        desired = 'python3'
    except FileNotFoundError:
        try:
            Popen('python -V', stdout = 0)
            desired = 'python'
        except FileNotFoundError:
            print('Fatal Error: cannot call python from terminal. Add python to path, please! ')
            input('Press Enter to exit game. ')
            sys.exit(7482)
    desired += ' get-pip.py'
    if platform.system() == 'Windows':
        prompt = '> '
    else:
        prompt = '$ '
    op = ''
    while op != desired:
        typeWrite('Please type "%s" and press Enter: ' % desired)
        op = input(prompt)
    Popen(op)
    import pip
    input('ok')

def typeWrite(*args, interval = 0.06, end = '\n', sep = ' '):
    for char in sep.join(args):
        print(char, end = '', flush = True)
        sleep(interval)
    print('', end = end, flush = True)

STAGES = [
    greet, 
]
