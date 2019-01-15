__all__ = ['setTimer']

from cocos.actions.instant_actions import CallFunc
from cocos.actions import Delay
from cocos.director import director
from cocos.cocosnode import CocosNode

wrapperNode = CocosNode()
currentScene = None
directorSceneStack = []

def setTimer(callback, delay, *args, **kw):
    wrapperNode.do(
        Delay(delay) + 
        CallFunc(callbackCaller, callback, delay, *args, **kw)
    )

def callbackCaller(callback, delay, *args, **kw):
    new_delay = callback(delay, *args, **kw)
    if new_delay != 0:
        setTimer(callback, new_delay, *args, **kw)

def onNewScene(newScene):
    global currentScene
    if currentScene:
        currentScene.remove(wrapperNode)
    newScene.add(wrapperNode)
    currentScene = newScene

def onPush(scene):
    directorSceneStack.append(currentScene)
    onNewScene(scene)

def onPop():
    onNewScene(directorSceneStack.pop(-1))

def run(scene):
    onNewScene(scene)
    saved_run(scene)

def replace(scene):
    onNewScene(scene)
    saved_replace(scene)

director.on_push = onPush
director.on_pop = onPop
saved_run = director.run
director.run = run
saved_replace = director.replace
director.replace = replace
