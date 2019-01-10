'''
'''
import os
from os import path
os.chdir(path.dirname(__file__))
os.chdir('data')
import game_state
import sys
from time import sleep

def main():
    ...

if __name__ == '__main__':
    main()
    sys.exit(0)
else:
    print('What??? '); sleep(1)
    print('Why did you import my game? '); sleep(1)
    print('Dirty hacker! '); sleep(1)
    class DirtyHackerError(Exception):pass
    raise DirtyHackerError
