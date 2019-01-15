from cocos.text import HTMLLabel
from timer import setTimer

class TypeWriter:
    def __init__(self, parent, interval = 50):
        self.parent = parent
        self.interval = interval
        self.goal_list = []
        self.cursor = 0
        self.done = True
        self.label = HTMLLabel()
        parent.add(self.label)
    
    def type(self, text, interval = None):
        assert self.done, 'TypeWriter.type before last type job is done'
        self.done = False
        self.goal_list = []
        self.cursor = 0
        tag_builder = []
        iter_text = iter(text)
        for char in iter_text:
            if char == '<':
                tag_builder = ['<']
                for char in iter_text:
                    tag_builder.append(char)
                    if char == '>':
                        break
                else:
                    assert False, 'unclosed tag'
                self.goal_list.append(''.join(tag_builder))
            else:
                self.goal_list.append(char)
        interval = interval or self.interval
        setTimer(self.onTimer, interval)
    
    def onTimer(self, delay):
        self.cursor += 1
        buffer = []
        cursor = 0
        for i in goal_list:
            if len(i) == 1:
                if cursor < self.cursor:
                    buffer.append(i)
                cursor += 1
            else:
                buffer.append(i)
        label = HTMLLabel(''.join(buffer))
        self.parent.remove(self.label)
        self.parent.add(label)
        self.label = label
        if cursor == self.cursor:
            self.done = True
            return 0
        else:
            return delay
