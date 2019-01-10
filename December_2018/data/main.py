from .game_state import *
import data.install as install
from .check_inet import checkInternet

def main():
    checkInternet()
    if gameState['install']['stage'] != -1:
        install.main()
