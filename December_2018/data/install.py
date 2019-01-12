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
<br>
Maybe you think they are stupid;
But that doesn't mean
they don't hear you. 
<br>
Play carefully.
<br>
Press ENTER to continue...'''
    lines = warn_text.split('\n')
    vertical_pad = int((height - len(lines)) / 2)
    print('\n' * (vertical_pad - 1))
    [printCenter(width, x) for x in lines]
    print('\n' * (vertical_pad - 1))
    input()
    terminal(cls)

def printCenter(terminal_width, text, and_sleep = 2):
    if text == '<br>':
        print()
    else:
        length = len(text)
        left_pad = int((terminal_width - length) / 2)
        left_pad = max(left_pad, 0)
        print(' ' * left_pad, end = '')
        print(text)
    if text != '' and '...' not in text: 
        sleep(and_sleep)

def greet():
    typeWrite('* Hi there! ')
    sleep(1.5)
    typeWrite('* Thank you for starting', end = ' ')
    sleep(1)
    typeWrite('to play this game. ')
    sleep(1)
    print()
    typeWrite('* This game needs some dependencies. ')
    sleep(1)
    typeWrite('* Let us install them one by one! ')
    sleep(1)

def getPip():
    typeWrite('* First of all, we need pip. ')
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
        typeWrite('* Would you kindly type "%s" and press ENTER, please? ' % desired)
        op = input(prompt)
    popen = Popen(op.split(' '))
    typeWrite('* Thank you! Now wait for it...')
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
    typeWrite('* Good job! I can sense that pip is fully operational. ')
    sleep(1)
    print()

def pipInstall(*packages):
    pip.main(['install'] + list(packages) + ['--user'])

def typeWrite(*args, interval = 0.05, end = '\n', sep = ' '):
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
    typeWrite('* Next, colors. Shall we add some colors to the terminal? ')
    sleep(1)
    typeWrite('* I will run "%s". ' % commandPreview('colorama'))
    sleep(1)
    getConsent()
    print(commandPreview('colorama'))
    pipInstall('colorama')
    importColor()
    print('Testing all colors... ')
    all_colors = [x for x in dir(Back) if x[0] != '_']
    for color in all_colors:
        print(Fore.RESET, ' ', Back.__getattribute__(color), color, end = '', flush = True, sep = '')
        sleep(0.1)
        print(Back.RESET, ' ', Fore.__getattribute__(color), color, end = '', flush = True, sep = '')
        sleep(0.1)
    print(Style.RESET_ALL)
    print('Testing success. ')
    print()
    print('*', Back.LIGHTCYAN_EX + Fore.BLACK + Style.DIM, end = '')
    typeWrite('Great!', end = '')
    print(Style.RESET_ALL, end = ' ')
    sleep(1)
    typeWrite('Look at all the ', end = '')
    show_off = [Back.RED, Back.LIGHTRED_EX, Back.YELLOW, Back.GREEN, Back.BLUE, Back.MAGENTA]
    print(Fore.WHITE, end = '')
    for char, color in zip('colors', show_off):
        print(color, end = '')
        typeWrite(char, end = '')
    print(Style.RESET_ALL, end = '')
    typeWrite(' I can use! ')
    sleep(1)
    print()

def getConsent():
    typeWrite('* Do you give consent? ')
    op = input('y/n: ').lower()
    while op not in ('y', 'n'):
        op = input('Please type either "y" or "n" and press Enter: ').lower()
    if op == 'y':
        typeWrite('* Okay! ')
    else:
        typeWrite('* I am sure ', end = '')
        sleep(0.6)
        typeWrite('you will come back again. ')
        sleep(1)
        sys.exit(0)

def welcomeBack():
    typeWrite('* Welcome back! \n  We shall continue. ')
    sleep(1)

def nop():
    pass

def getCocos():
    typeWrite('* Alright. ')
    sleep(1)
    typeWrite('* You must be tired of this ugly terminal already. ')
    sleep(1)
    typeWrite('* Frankly speaking, me too! ')
    sleep(1)
    typeWrite("* Why don't we install the main game engine")
    typeWrite('  so that we can have a proper graphical window? ')
    sleep(1)
    typeWrite('* I will run ', end = '')
    print(Back.BLACK + Fore.GREEN, end = '')
    typeWrite(commandPreview('cocos2d'), end = '')
    print(Style.RESET_ALL + '. ')
    sleep(1)
    getConsent()
    print(commandPreview('cocos2d'))
    pipInstall('cocos2d')
    importCocos()

def importCocos():
    import cocos

STAGES = [
    (warnAI, nop), 
    (greet, nop), 
    (getPip, nop), 
    (verifyPip, importPip),
    (nop, welcomeBack), 
    (getColor, importColor), 
    (getCocos, importCocos), 
]
