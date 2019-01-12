from .game_state import *
import data.install as install
from .check_inet import checkInternet

def main():
    checkInternet()
    if gameState['install']['stage'] != -1:
        install.main()
    if gameState['install']['2_stage'] != -1:
        import data.install_2 as install_2
        install_2.main()
