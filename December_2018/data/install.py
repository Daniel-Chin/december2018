from .game_state import *
from time import sleep

def main():
    while gameState['install']['stage'] != len(STAGES):
        STAGES[gameState['install']['stage']]()
        gameState['install']['stage'] += 1
        saveState()
    gameState['install']['stage'] = -1
    saveState()

def greet():
    typeWrite('Thank you. ')
    sleep(2)
    typeWrite('Thank you for starting', end = ' ')
    sleep(1)
    typeWrite('to play this game. ')

def typeWrite(text, interval = 0.1, end = '\n'):
    for char in text:
        print(char, end = '', flush = True)
        sleep(interval)
    print('', end = end, flush = True)

STAGES = [
    greet, 
]
