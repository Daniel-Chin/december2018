import sys
from time import sleep
import os
from os import path

if __name__ == '__main__':
    os.chdir(path.dirname(__file__))
    os.chdir('data')
    from main import main
    main()
    sys.exit(0)
else:
    print('What??? '); sleep(1)
    print('Why did you import my game? '); sleep(1)
    print('Dirty hacker! '); sleep(1)
    class DirtyHackerError(Exception):pass
    raise DirtyHackerError
