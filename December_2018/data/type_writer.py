from cocos.text import HTMLLabel
from cocos.audio.SDL.timer import SDL_AddTimer as addTimer
from io import StringIO

class Tag:
    def __init__(self, raw = None):
        self.opening = ''
        self.closing = ''
        self.content = []
        if raw is not None:
            self.raw = raw
            io = StringIO()
            io.write('root>')
            io.write(raw)
            io.write('</root>')
            io.seek(0)
            self.loadIO(io)
    
    def loadIO(self, io):
        buffer = ['<']
        while buffer[-1] != '>':
            buffer.append(io.read(1))
        self.opening = ''.join(buffer)
        while True:
            char = io.read(1)
            if char == '<':
                char = io.read(1)
                if char == '/':
                    buffer = ['<', '/']
                    while buffer[-1] != '>':
                        buffer.append(io.read(1))
                    self.closing = ''.join(buffer)
                    return
                else:
                    io.seek(io.tell() - 1)
                    self.content.append(Tag())
                    self.content[-1].loadIO(io)
            else:
                self.content.append(char)
    
    def __repr__(self):
        return self.opening + ''.join([str(x) for x in self.content]) + self.closing
    
    def __str__(self):
        return self.__repr__()

class TypeWriter:
    def __init__(self, parent, interval = 0.05):
        self.parent = parent
        self.interval = interval
        self.text = StringIO()
        self.to_type = []
        self.done = True
        self.label = HTMLLabel()
        parent.add(self.label)
    
    def type(self, text, interval = None):
        self.done = False
        interval = interval or self.interval
        
        addTimer(interval, self.onTimer)
    
    def onTimer(self):
        self.text.write(self.to_type.read(1))
        self.text.seek(0)
        self.parent
    
    def readOneCharAndTags(self):
        ...
    