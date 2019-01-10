from .game_state import *
import data.install as install

def main():
    if gameState['install']['stage'] != -1:
        install.main()
