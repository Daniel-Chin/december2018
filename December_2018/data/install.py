from .game_state import *
from time import sleep
from subprocess import Popen
import sys
import platform
from os import system as terminal

if platform.system() == 'Windows':
    prompt = '> '
else:
    prompt = '$ '

def main():
    if gameState['install']['stage'] > 2:
        typeWrite('* Welcome back. \n  We shall continue. '.upper())
    while gameState['install']['stage'] != len(STAGES):
        STAGES[gameState['install']['stage']]()
        gameState['install']['stage'] += 1
        saveState()
    gameState['install']['stage'] = -1
    saveState()

def greet():
    typeWrite('* Thank you. '.upper())
    sleep(1.5)
    typeWrite('* Thank you for starting'.upper(), end = ' ')
    sleep(1)
    typeWrite('to play this game. '.upper())
    sleep(1)
    print()
    typeWrite('* This game needs some dependencies. '.upper())
    sleep(1)
    typeWrite('* Let us install them one by one. '.upper())
    sleep(1)

def getPip():
    typeWrite('* First of all, we need pip. '.upper())
    sleep(1)
    try:
        python_name = 'python3'
        Popen([python_name, '-V'], stdout = open('temp', 'w+'))
    except FileNotFoundError:
        try:
            python_name = 'python'
            Popen([python_name, '-V'], stdout = open('temp', 'w+'))
        except FileNotFoundError:
            print('Fatal Error: cannot call python from terminal. Add python to path, please! ')
            input('Press Enter to exit game. ')
            sys.exit(7482)
    desired = python_name + ' get-pip.py --user'
    op = ''
    while op != desired:
        typeWrite('* PLEASE TYPE "%s" AND PRESS ENTER. ' % desired)
        op = input(prompt)
    popen = Popen(op.split(' '))
    typeWrite('* Now wait...'.upper())
    popen.wait()
    gameState['install']['stage'] += 1
    saveState()
    terminal(python_name + ' ../December_2018.py')
    sys.exit(0)

def verifyPip():
    global pip
    try:
        import pip
        if not hasattr(pip, 'main'):
            import pip._internal as pip
    except:
        print('Fatal Error: Failed to install pip! ')
        input('Press Enter to exit game. ')
        import pip
        sys.exit(4685)
    print()
    typeWrite('* Good job. '.upper())

def pipInstall(*packages):
    pip.main(['install'] + packages + ['--user'])

def typeWrite(*args, interval = 0.1, end = '\n', sep = ' '):
    for char in sep.join(args):
        print(char, end = '', flush = True)
        sleep(interval)
    print('', end = end, flush = True)

def commandPreview(*packages):
    return '%spip install %s --user' % (prompt, ' '.join(packages))

def getColor():
    global colorama
    typeWrite('* Next, colors. '.upper())
    sleep(1)
    typeWrite('* I WILL RUN "%s". ' % commandPreview('colorama'))
    sleep(1)
    typeWrite('* Do you give consent? '.upper())
    if getConsent():
        print(commandPreview('colorama'))
        pipInstall('colorama')
        import colorama
        from colorama import Fore, Back, Style
        colorama.init()
        print(Fore.RED, Back.WHITE, Style.DIM)
        typeWrite('* Great. '.upper(), end = '')
        print(Style.RESET_ALL)
    else:
        typeWrite('* I am sure '.upper(), end = '')
        sleep(0.6)
        typeWrite(' you will come back again. '.upper())
        sys.exit(0)

def getConsent():
    op = input('y/n: ').lower()
    while op not in ('y', 'n'):
        op = input('Please type either "y" or "n" and press Enter: ').lower()
    return op == 'y'

STAGES = [
    greet, 
    getPip, 
    verifyPip, 
]
