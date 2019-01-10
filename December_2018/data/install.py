from .game_state import *
from time import sleep
from subprocess import Popen
import sys
import platform
from os import system as terminal
from .terminalsize import get_terminal_size

if platform.system() == 'Windows':
    prompt = '> '
    cls = 'cls'
else:
    prompt = '$ '
    cls = 'clear'

def main():
    for i in range(gameState['install']['stage']):
        STAGES[i][1]()
    while gameState['install']['stage'] != len(STAGES):
        STAGES[gameState['install']['stage']][0]()
        gameState['install']['stage'] += 1
        saveState()
    gameState['install']['stage'] = -1
    saveState()

def warnAI():
    width, height = get_terminal_size()
    warn_text = '''
-= Warning =-

The NPCs in this game are sentient AIs.
They have emotions, goals, and intentions.
They remember what you say.
|
Maybe you think they are stupid;
But that doesn't mean
they don't hear you. 
|
Play carefully.
|
Press ENTER to continue...'''
    lines = warn_text.split('\n')
    vertical_pad = int((height - len(lines)) / 2)
    print('\n' * (vertical_pad - 1))
    [printCenter(width, x) for x in lines]
    print('\n' * (vertical_pad - 1))
    input()
    terminal(cls)

def printCenter(terminal_width, text, and_sleep = 2):
    length = len(text)
    left_pad = int((terminal_width - length) / 2)
    left_pad = max(left_pad, 0)
    print(' ' * left_pad, end = '')
    print(text)
    if text != '' and '...' not in text: 
        sleep(and_sleep)

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
            input('Press Enter to exit game... ')
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

def importPip():
    global pip
    import pip
    if not hasattr(pip, 'main'):
        import pip._internal as pip

def verifyPip():
    try:
        importPip()
    except:
        print('Fatal Error: Failed to install pip! ')
        input('Press Enter to exit game... ')
        import pip
        sys.exit(4685)
    print()
    typeWrite('* Good job. '.upper())

def pipInstall(*packages):
    pip.main(['install'] + list(packages) + ['--user'])

def typeWrite(*args, interval = 0.1, end = '\n', sep = ' '):
    for char in sep.join(args):
        print(char, end = '', flush = True)
        sleep(interval)
    print('', end = end, flush = True)

def commandPreview(*packages):
    return '%spip install %s --user' % (prompt, ' '.join(packages))

def importColor():
    global Fore, Back, Style
    from colorama import Fore, Back, Style, init
    init()

def getColor():
    typeWrite('* Next, colors. '.upper())
    sleep(1)
    typeWrite('* I WILL RUN "%s". ' % commandPreview('colorama'))
    sleep(1)
    typeWrite('* Do you give consent? '.upper())
    if getConsent():
        print(commandPreview('colorama'))
        pipInstall('colorama')
        importColor()
        print()
        print(Fore.RED, Back.WHITE, end = '')
        typeWrite('* Great. '.upper(), end = '')
        print(Style.RESET_ALL)
    else:
        typeWrite('* I am sure '.upper(), end = '')
        sleep(0.6)
        typeWrite('you will come back again. '.upper())
        sys.exit(0)

def getConsent():
    op = input('y/n: ').lower()
    while op not in ('y', 'n'):
        op = input('Please type either "y" or "n" and press Enter: ').lower()
    return op == 'y'

def welcomeBack():
    typeWrite('* Welcome back. \n  We shall continue. '.upper())

def nop():
    pass

STAGES = [
    (warnAI, nop), 
    (greet, nop), 
    (getPip, nop), 
    (verifyPip, importPip),
    (nop, welcomeBack), 
    (getColor, importColor), 
]
