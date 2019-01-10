from game_state import *
import install

def main():
    if gameState['install']['stage'] != -1:
        install.main()
