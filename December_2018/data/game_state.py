__all__ = ['gameState', 'saveState']

import pickle
import sys
from io import BytesIO

INIT_STATE = {
    install: {
        stage: 0,   # -1 for finish
    }, 
}

gameState = {}

def loadState():
    global gameState
    try:
        with open('file0', 'rb') as f0:
            with open('file1', 'rb') as f1:
                with open('file9', 'rb') as f9:
                    which = None
                    try:
                        which = f9.read()[0]
                        if which not in (0, 1):
                            which = None
                            raise IndexError
                        gameState = pickle.load((f0, f1)[which])
                        copy(f0, f1, which)
                    except IndexError:
                        try:
                            gameState = pickle.load(f0)
                            which = 0
                        except:
                            try:
                                gameState = pickle.load(f1)
                                which = 1
                            except:
                                print('Game save file corrupted - which is unbelievable, because Daniel wrote an entire python script dedicated to prevent this from happening. Contact Daniel, and tell him what heppened. Please. ')
                                input('Press Enter to exit game... ')
                                sys.exit(1207)
        assert which is not None
        f0.seek(0)
        f1.seek(0)
        if f0.read() != f1.read():
            goodFile = (f0, f1)[which]
            badFile = (f0, f1)[1 - which]
            goodFile.seek(0)
            data = goodFile.read()
            badFile.close()
            badFile = open('file' + str(1 - which), 'wb')
            badFile.write(data)
            badFile.close()
    except FileNotFoundError:
        gameState = INIT_STATE
        saveState()

def saveState():
    io = BytesIO()
    pickle.dump(gameState, io)
    data = io.read()
    io.close()
    with open('file9', 'wb+') as f:
        f.write(b'\x01')
    with open('file0', 'wb+') as f:
        f.write(data)
    with open('file9', 'wb+') as f:
        f.write(b'\x00')
    with open('file1', 'wb+') as f:
        f.write(data)

loadState()
