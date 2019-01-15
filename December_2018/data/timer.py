__all__ = ['setTimer']

from cocos.actions.instant_actions import CallFunc
from cocos.actions import Delay
from cocos.director import director
from cocos.cocosnode import CocosNode

wrapperNode = None
currentScene = None
directorSceneStack = []

def setTimer(callback, delay, *args, **kw):
    wrapperNode.do(
        Delay(delay) + 
        CallFunc(callbackCaller, callback, *args, **kw)
    )

def callbackCaller(callback, *args, **kw):
    new_delay = callback(*args, **kw)
    if new_delay != 0:
        setTimer(callback, new_delay, *args, **kw)

def onNewScene(newScene):
    global wrapperNode, currentScene
    if currentScene:
        currentScene.remove(wrapperNode)
    wrapperNode = CocosNode()
    newScene.add(wrapperNode)
    currentScene = newScene

def onPush(self, scene):
    directorSceneStack.append(currentScene)
    onNewScene(scene)

def onPop(self):
    onNewScene(directorSceneStack.pop(-1))

def run(self, scene):
    onNewScene(scene)
    saved_run(self, scene)

def replace(scene):
    onNewScene(scene)
    saved_replace(self, scene)

director.on_push = onPush
director.on_pop = onPop
saved_run = director.run
director.run = run
saved_replace = director.replace
director.replace = replace
