from socket import socket
import sys

def checkInternet():
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        print('Debugging. Skip internet checking. ')
        return
    s = socket()
    s.settimeout(1)
    try:
        s.connect(('8.8.8.8', 53))
        s.close()
    except:
        print('Sorry, this game requires internet access. ')
        input('Press Enter to quit game...')
        sys.exit(8468)
