from cocos.text import HTMLLabel

class TypeWriter:
    def __init__(self, parent, interval = 50):
        self.parent = parent
        self.interval = interval
        self.goal_list = []
        self.now_list = []
        self.done = True
        self.label = HTMLLabel()
        parent.add(self.label)
    
    def type(self, text, interval = None):
        assert self.done, 'TypeWriter.type before last type job is done'
        self.done = False
        self.goal_list = []
        self.now_list = []
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
        addTimer(interval, f, ['no'])
    
    def onTimer(self, interval, param):
        return 0
    
    def readOneCharAndTags(self):
        ...
    