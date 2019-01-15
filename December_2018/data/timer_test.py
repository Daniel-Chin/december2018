import cocos
cocos.director.director.init()
from timer import setTimer

class Root(cocos.layer.Layer):
    def __init__(self):
        super(__class__, self).__init__()
        label = cocos.text.Label()
        self.add(label)
        self.label = label
        self.i = 0
        setTimer(self.onTimer, 1)
        setTimer(self.onTimer, 1.1)
    
    def setText(self, text):
        self.remove(self.label)
        label = cocos.text.Label(text)
        label.position = 320, 240
        self.add(label)
        self.label = label
    
    def onTimer(self, delay):
        print('onTimer')
        self.setText(str(self.i))
        self.i += 1
        return delay

root = Root()
mainScene = cocos.scene.Scene(root)
cocos.director.director.run(mainScene)
