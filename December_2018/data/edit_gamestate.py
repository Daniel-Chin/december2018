'''
This is apparently a tool for debugging. 
'''
import game_state
game_state.gameState = {
    'install': {
        'stage': 3, 
    }, 
}
game_state.saveState()
input('ok')