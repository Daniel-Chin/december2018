from .game_state import *
import pip
if not hasattr(pip, 'main'):
    import pip._internal as pip
import cocos

def main():
    cocos.director.director.init()
    root = Root()
    cocos.director.director.run(cocos.scene.Scene(root))

class Root(cocos.layer.Layer):
    def __init__(self):
        super(__class__, self).__init__()
        label = cocos.text.HTMLLabel(
            '<font color="white">hhh,</font>', 
            #font_size=32,
            #font_name='Lucida Console',
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)
        self.remove(label)
        self.add(label)
