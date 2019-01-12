'''
This is apparently a tool for debugging. 
'''
import game_state
game_state.gameState = {
    'install': {
        'stage': 6, 
        '2_stage': 0,
    }, 
}
game_state.saveState()
input('ok')
