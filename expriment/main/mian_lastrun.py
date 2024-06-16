#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on June 06, 2024, at 23:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'mian'  # from the Builder filename that created this script
expInfo = {'姓名': '', '性别': '', '年龄（周岁）': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['姓名'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Ryougi mana\\Desktop\\CF_DDM\\expriment\\main\\mian_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "GeneInstr"
GeneInstrClock = core.Clock()
GeneInstr_p = visual.ImageStim(
    win=win,
    name='GeneInstr_p', 
    image='pic/GenInstr.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instrNum"
instrNumClock = core.Clock()
Numinstr_p = visual.ImageStim(
    win=win,
    name='Numinstr_p', 
    image='pic/NumInstr.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respNumPrac = keyboard.Keyboard()

# Initialize components for Routine "num2Word"
num2WordClock = core.Clock()
frame = visual.ImageStim(
    win=win,
    name='frame', 
    image='frame.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
respNum2word = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
frame2 = visual.ImageStim(
    win=win,
    name='frame2', 
    image='frame.png', mask=None,
    ori=0.0, pos=(0,0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
textFBNum = visual.TextStim(win=win, name='textFBNum',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "endPracNum"
endPracNumClock = core.Clock()
NumEndPrac = visual.ImageStim(
    win=win,
    name='NumEndPrac', 
    image='pic/NumEndPrac.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respEndNumP = keyboard.Keyboard()

# Initialize components for Routine "inter"
interClock = core.Clock()
frame3 = visual.ImageStim(
    win=win,
    name='frame3', 
    image='frame.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "num2Word"
num2WordClock = core.Clock()
frame = visual.ImageStim(
    win=win,
    name='frame', 
    image='frame.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
respNum2word = keyboard.Keyboard()

# Initialize components for Routine "restNum"
restNumClock = core.Clock()
NumRest = visual.ImageStim(
    win=win,
    name='NumRest', 
    image='pic/NumRest.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respRest = keyboard.Keyboard()

# Initialize components for Routine "num2Word"
num2WordClock = core.Clock()
frame = visual.ImageStim(
    win=win,
    name='frame', 
    image='frame.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
respNum2word = keyboard.Keyboard()

# Initialize components for Routine "AffInstr"
AffInstrClock = core.Clock()
AffInsr_P = visual.ImageStim(
    win=win,
    name='AffInsr_P', 
    image='pic/AffInstr.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respAffInstr = keyboard.Keyboard()

# Initialize components for Routine "intervals"
intervalsClock = core.Clock()
times = [0.3,0.5,0.4,0.35,0.45]
fixTime=[]
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.6, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AFF_S1"
AFF_S1Clock = core.Clock()
flanker_p = visual.ImageStim(
    win=win,
    name='flanker_p', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
target_p = visual.ImageStim(
    win=win,
    name='target_p', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
respFlanker = keyboard.Keyboard()

# Initialize components for Routine "AFF_S2"
AFF_S2Clock = core.Clock()
# 积极词表
positiveWords = [
    "畅销", "诚恳", "充裕", "典雅",
    "丰满", "奉献", "富丽", "富足",
    "公平", "瑰丽", "豪放", "吉祥",
    "精致", "敬佩", "俊秀", "廉洁",
    "留恋", "前进", "清秀", "热切",
    "如愿", "生动", "圣洁", "舒畅",
    "爽朗", "顽强", "旺盛", "鲜艳",
    "羡慕", "享受", "雄厚", "秀丽",
    "永恒", "优雅", "有利", "赞成",
    "珍藏", "振作", "正直", "卓越"
]
# 消极词表
negativeWords = [
    "悲观", "别扭", "嘲笑", "处罚",
    "丢失", "堵塞", "罚款", "烦恼",
    "孤单", "黑暗", "胡涂", "怀疑",
    "慌忙", "假冒", "焦躁", "禁止",
    "沮丧", "懒惰", "浪费", "冷笑",
    "鲁莽", "落后", "闷热", "排斥",
    "轻率", "穷苦", "缺乏", "撒谎",
    "伤心", "失意", "损害", "逃避",
    "消沉", "心慌", "厌恶", "忧虑",
    "郁闷", "杂乱", "争吵", "自卑"
]
AffWord = visual.TextStim(win=win, name='AffWord',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
respAffWord = keyboard.Keyboard()

# Initialize components for Routine "endPracAff"
endPracAffClock = core.Clock()
endPracA_p = visual.ImageStim(
    win=win,
    name='endPracA_p', 
    image='pic/AffEndPrac.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
respEndPracA = keyboard.Keyboard()

# Initialize components for Routine "intervals"
intervalsClock = core.Clock()
times = [0.3,0.5,0.4,0.35,0.45]
fixTime=[]
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.6, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AFF_S1"
AFF_S1Clock = core.Clock()
flanker_p = visual.ImageStim(
    win=win,
    name='flanker_p', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
target_p = visual.ImageStim(
    win=win,
    name='target_p', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
respFlanker = keyboard.Keyboard()

# Initialize components for Routine "AFF_S2"
AFF_S2Clock = core.Clock()
# 积极词表
positiveWords = [
    "畅销", "诚恳", "充裕", "典雅",
    "丰满", "奉献", "富丽", "富足",
    "公平", "瑰丽", "豪放", "吉祥",
    "精致", "敬佩", "俊秀", "廉洁",
    "留恋", "前进", "清秀", "热切",
    "如愿", "生动", "圣洁", "舒畅",
    "爽朗", "顽强", "旺盛", "鲜艳",
    "羡慕", "享受", "雄厚", "秀丽",
    "永恒", "优雅", "有利", "赞成",
    "珍藏", "振作", "正直", "卓越"
]
# 消极词表
negativeWords = [
    "悲观", "别扭", "嘲笑", "处罚",
    "丢失", "堵塞", "罚款", "烦恼",
    "孤单", "黑暗", "胡涂", "怀疑",
    "慌忙", "假冒", "焦躁", "禁止",
    "沮丧", "懒惰", "浪费", "冷笑",
    "鲁莽", "落后", "闷热", "排斥",
    "轻率", "穷苦", "缺乏", "撒谎",
    "伤心", "失意", "损害", "逃避",
    "消沉", "心慌", "厌恶", "忧虑",
    "郁闷", "杂乱", "争吵", "自卑"
]
AffWord = visual.TextStim(win=win, name='AffWord',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
respAffWord = keyboard.Keyboard()

# Initialize components for Routine "restAff"
restAffClock = core.Clock()
AffRest = visual.ImageStim(
    win=win,
    name='AffRest', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
respRest_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "GeneInstr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
GeneInstrComponents = [GeneInstr_p, key_resp]
for thisComponent in GeneInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GeneInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GeneInstr"-------
while continueRoutine:
    # get current time
    t = GeneInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GeneInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GeneInstr_p* updates
    if GeneInstr_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GeneInstr_p.frameNStart = frameN  # exact frame index
        GeneInstr_p.tStart = t  # local t and not account for scr refresh
        GeneInstr_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GeneInstr_p, 'tStartRefresh')  # time at next scr refresh
        GeneInstr_p.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GeneInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GeneInstr"-------
for thisComponent in GeneInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "GeneInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
returnPractice = data.TrialHandler(nReps=99.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='returnPractice')
thisExp.addLoop(returnPractice)  # add the loop to the experiment
thisReturnPractice = returnPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReturnPractice.rgb)
if thisReturnPractice != None:
    for paramName in thisReturnPractice:
        exec('{} = thisReturnPractice[paramName]'.format(paramName))

for thisReturnPractice in returnPractice:
    currentLoop = returnPractice
    # abbreviate parameter names if possible (e.g. rgb = thisReturnPractice.rgb)
    if thisReturnPractice != None:
        for paramName in thisReturnPractice:
            exec('{} = thisReturnPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrNum"-------
    continueRoutine = True
    # update component parameters for each repeat
    respNumPrac.keys = []
    respNumPrac.rt = []
    _respNumPrac_allKeys = []
    # keep track of which components have finished
    instrNumComponents = [Numinstr_p, respNumPrac]
    for thisComponent in instrNumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrNumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrNum"-------
    while continueRoutine:
        # get current time
        t = instrNumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrNumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Numinstr_p* updates
        if Numinstr_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numinstr_p.frameNStart = frameN  # exact frame index
            Numinstr_p.tStart = t  # local t and not account for scr refresh
            Numinstr_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numinstr_p, 'tStartRefresh')  # time at next scr refresh
            Numinstr_p.setAutoDraw(True)
        
        # *respNumPrac* updates
        waitOnFlip = False
        if respNumPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respNumPrac.frameNStart = frameN  # exact frame index
            respNumPrac.tStart = t  # local t and not account for scr refresh
            respNumPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respNumPrac, 'tStartRefresh')  # time at next scr refresh
            respNumPrac.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respNumPrac.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respNumPrac.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respNumPrac.status == STARTED and not waitOnFlip:
            theseKeys = respNumPrac.getKeys(keyList=['space'], waitRelease=False)
            _respNumPrac_allKeys.extend(theseKeys)
            if len(_respNumPrac_allKeys):
                respNumPrac.keys = _respNumPrac_allKeys[-1].name  # just the last key pressed
                respNumPrac.rt = _respNumPrac_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrNumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrNum"-------
    for thisComponent in instrNumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instrNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pracNum = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('NumPractise.xlsx', selection='0:1'),
        seed=None, name='pracNum')
    thisExp.addLoop(pracNum)  # add the loop to the experiment
    thisPracNum = pracNum.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracNum.rgb)
    if thisPracNum != None:
        for paramName in thisPracNum:
            exec('{} = thisPracNum[paramName]'.format(paramName))
    
    for thisPracNum in pracNum:
        currentLoop = pracNum
        # abbreviate parameter names if possible (e.g. rgb = thisPracNum.rgb)
        if thisPracNum != None:
            for paramName in thisPracNum:
                exec('{} = thisPracNum[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "num2Word"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        stimulus.setPos(Position)
        stimulus.setText(target)
        respNum2word.keys = []
        respNum2word.rt = []
        _respNum2word_allKeys = []
        # keep track of which components have finished
        num2WordComponents = [frame, stimulus, respNum2word]
        for thisComponent in num2WordComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        num2WordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "num2Word"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = num2WordClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=num2WordClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *frame* updates
            if frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                frame.frameNStart = frameN  # exact frame index
                frame.tStart = t  # local t and not account for scr refresh
                frame.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(frame, 'tStartRefresh')  # time at next scr refresh
                frame.setAutoDraw(True)
            if frame.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > frame.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    frame.tStop = t  # not accounting for scr refresh
                    frame.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(frame, 'tStopRefresh')  # time at next scr refresh
                    frame.setAutoDraw(False)
            
            # *stimulus* updates
            if stimulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(True)
            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus.tStartRefresh + 4.5-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                    stimulus.setAutoDraw(False)
            
            # *respNum2word* updates
            waitOnFlip = False
            if respNum2word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                respNum2word.frameNStart = frameN  # exact frame index
                respNum2word.tStart = t  # local t and not account for scr refresh
                respNum2word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respNum2word, 'tStartRefresh')  # time at next scr refresh
                respNum2word.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respNum2word.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respNum2word.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respNum2word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respNum2word.tStartRefresh + 4.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respNum2word.tStop = t  # not accounting for scr refresh
                    respNum2word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(respNum2word, 'tStopRefresh')  # time at next scr refresh
                    respNum2word.status = FINISHED
            if respNum2word.status == STARTED and not waitOnFlip:
                theseKeys = respNum2word.getKeys(keyList=['a', 'l'], waitRelease=False)
                _respNum2word_allKeys.extend(theseKeys)
                if len(_respNum2word_allKeys):
                    respNum2word.keys = _respNum2word_allKeys[-1].name  # just the last key pressed
                    respNum2word.rt = _respNum2word_allKeys[-1].rt
                    # was this correct?
                    if (respNum2word.keys == str(CorAns)) or (respNum2word.keys == CorAns):
                        respNum2word.corr = 1
                    else:
                        respNum2word.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in num2WordComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "num2Word"-------
        for thisComponent in num2WordComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if respNum2word.keys in ['', [], None]:  # No response was made
            respNum2word.keys = None
            # was no response the correct answer?!
            if str(CorAns).lower() == 'none':
               respNum2word.corr = 1;  # correct non-response
            else:
               respNum2word.corr = 0;  # failed to respond (incorrectly)
        # store data for pracNum (TrialHandler)
        pracNum.addData('respNum2word.keys',respNum2word.keys)
        pracNum.addData('respNum2word.corr', respNum2word.corr)
        if respNum2word.keys != None:  # we had a response
            pracNum.addData('respNum2word.rt', respNum2word.rt)
        if respNum2word.corr:
            feedbacktext = "√"
            feedbackcolor = "green"
        else:
            feedbacktext = "×"
            feedbackcolor = "red"
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        textFBNum.setColor(feedbackcolor, colorSpace='rgb')
        textFBNum.setPos(Position)
        textFBNum.setText(feedbacktext)
        # keep track of which components have finished
        feedbackComponents = [frame2, textFBNum]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *frame2* updates
            if frame2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                frame2.frameNStart = frameN  # exact frame index
                frame2.tStart = t  # local t and not account for scr refresh
                frame2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(frame2, 'tStartRefresh')  # time at next scr refresh
                frame2.setAutoDraw(True)
            if frame2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > frame2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    frame2.tStop = t  # not accounting for scr refresh
                    frame2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(frame2, 'tStopRefresh')  # time at next scr refresh
                    frame2.setAutoDraw(False)
            
            # *textFBNum* updates
            if textFBNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFBNum.frameNStart = frameN  # exact frame index
                textFBNum.tStart = t  # local t and not account for scr refresh
                textFBNum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFBNum, 'tStartRefresh')  # time at next scr refresh
                textFBNum.setAutoDraw(True)
            if textFBNum.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFBNum.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textFBNum.tStop = t  # not accounting for scr refresh
                    textFBNum.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFBNum, 'tStopRefresh')  # time at next scr refresh
                    textFBNum.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'pracNum'
    
    # get names of stimulus parameters
    if pracNum.trialList in ([], [None], None):
        params = []
    else:
        params = pracNum.trialList[0].keys()
    # save data for this loop
    pracNum.saveAsExcel(filename + '.xlsx', sheetName='pracNum',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "endPracNum"-------
    continueRoutine = True
    # update component parameters for each repeat
    respEndNumP.keys = []
    respEndNumP.rt = []
    _respEndNumP_allKeys = []
    # keep track of which components have finished
    endPracNumComponents = [NumEndPrac, respEndNumP]
    for thisComponent in endPracNumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endPracNumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "endPracNum"-------
    while continueRoutine:
        # get current time
        t = endPracNumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endPracNumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumEndPrac* updates
        if NumEndPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumEndPrac.frameNStart = frameN  # exact frame index
            NumEndPrac.tStart = t  # local t and not account for scr refresh
            NumEndPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumEndPrac, 'tStartRefresh')  # time at next scr refresh
            NumEndPrac.setAutoDraw(True)
        
        # *respEndNumP* updates
        waitOnFlip = False
        if respEndNumP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respEndNumP.frameNStart = frameN  # exact frame index
            respEndNumP.tStart = t  # local t and not account for scr refresh
            respEndNumP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respEndNumP, 'tStartRefresh')  # time at next scr refresh
            respEndNumP.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respEndNumP.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respEndNumP.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respEndNumP.status == STARTED and not waitOnFlip:
            theseKeys = respEndNumP.getKeys(keyList=['q', 'p'], waitRelease=False)
            _respEndNumP_allKeys.extend(theseKeys)
            if len(_respEndNumP_allKeys):
                respEndNumP.keys = _respEndNumP_allKeys[-1].name  # just the last key pressed
                respEndNumP.rt = _respEndNumP_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endPracNumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endPracNum"-------
    for thisComponent in endPracNumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if respEndNumP.keys == "p":
        returnPractice.finished = True # 循环结束
    else:
        returnPractice.finished = False
    # the Routine "endPracNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'returnPractice'

# get names of stimulus parameters
if returnPractice.trialList in ([], [None], None):
    params = []
else:
    params = returnPractice.trialList[0].keys()
# save data for this loop
returnPractice.saveAsExcel(filename + '.xlsx', sheetName='returnPractice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "inter"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
interComponents = [frame3]
for thisComponent in interComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
interClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inter"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = interClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=interClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *frame3* updates
    if frame3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        frame3.frameNStart = frameN  # exact frame index
        frame3.tStart = t  # local t and not account for scr refresh
        frame3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(frame3, 'tStartRefresh')  # time at next scr refresh
        frame3.setAutoDraw(True)
    if frame3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > frame3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            frame3.tStop = t  # not accounting for scr refresh
            frame3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(frame3, 'tStopRefresh')  # time at next scr refresh
            frame3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in interComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inter"-------
for thisComponent in interComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
NumBlock1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NumCon.xlsx', selection='0:1'),
    seed=None, name='NumBlock1')
thisExp.addLoop(NumBlock1)  # add the loop to the experiment
thisNumBlock1 = NumBlock1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNumBlock1.rgb)
if thisNumBlock1 != None:
    for paramName in thisNumBlock1:
        exec('{} = thisNumBlock1[paramName]'.format(paramName))

for thisNumBlock1 in NumBlock1:
    currentLoop = NumBlock1
    # abbreviate parameter names if possible (e.g. rgb = thisNumBlock1.rgb)
    if thisNumBlock1 != None:
        for paramName in thisNumBlock1:
            exec('{} = thisNumBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "num2Word"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    stimulus.setPos(Position)
    stimulus.setText(target)
    respNum2word.keys = []
    respNum2word.rt = []
    _respNum2word_allKeys = []
    # keep track of which components have finished
    num2WordComponents = [frame, stimulus, respNum2word]
    for thisComponent in num2WordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    num2WordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "num2Word"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = num2WordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=num2WordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *frame* updates
        if frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            frame.frameNStart = frameN  # exact frame index
            frame.tStart = t  # local t and not account for scr refresh
            frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame, 'tStartRefresh')  # time at next scr refresh
            frame.setAutoDraw(True)
        if frame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > frame.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                frame.tStop = t  # not accounting for scr refresh
                frame.frameNStop = frameN  # exact frame index
                win.timeOnFlip(frame, 'tStopRefresh')  # time at next scr refresh
                frame.setAutoDraw(False)
        
        # *stimulus* updates
        if stimulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.tStart = t  # local t and not account for scr refresh
            stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
            stimulus.setAutoDraw(True)
        if stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                stimulus.tStop = t  # not accounting for scr refresh
                stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(False)
        
        # *respNum2word* updates
        waitOnFlip = False
        if respNum2word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respNum2word.frameNStart = frameN  # exact frame index
            respNum2word.tStart = t  # local t and not account for scr refresh
            respNum2word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respNum2word, 'tStartRefresh')  # time at next scr refresh
            respNum2word.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respNum2word.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respNum2word.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respNum2word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respNum2word.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                respNum2word.tStop = t  # not accounting for scr refresh
                respNum2word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respNum2word, 'tStopRefresh')  # time at next scr refresh
                respNum2word.status = FINISHED
        if respNum2word.status == STARTED and not waitOnFlip:
            theseKeys = respNum2word.getKeys(keyList=['a', 'l'], waitRelease=False)
            _respNum2word_allKeys.extend(theseKeys)
            if len(_respNum2word_allKeys):
                respNum2word.keys = _respNum2word_allKeys[-1].name  # just the last key pressed
                respNum2word.rt = _respNum2word_allKeys[-1].rt
                # was this correct?
                if (respNum2word.keys == str(CorAns)) or (respNum2word.keys == CorAns):
                    respNum2word.corr = 1
                else:
                    respNum2word.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in num2WordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "num2Word"-------
    for thisComponent in num2WordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respNum2word.keys in ['', [], None]:  # No response was made
        respNum2word.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           respNum2word.corr = 1;  # correct non-response
        else:
           respNum2word.corr = 0;  # failed to respond (incorrectly)
    # store data for NumBlock1 (TrialHandler)
    NumBlock1.addData('respNum2word.keys',respNum2word.keys)
    NumBlock1.addData('respNum2word.corr', respNum2word.corr)
    if respNum2word.keys != None:  # we had a response
        NumBlock1.addData('respNum2word.rt', respNum2word.rt)
    if respNum2word.corr:
        feedbacktext = "√"
        feedbackcolor = "green"
    else:
        feedbacktext = "×"
        feedbackcolor = "red"
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NumBlock1'

# get names of stimulus parameters
if NumBlock1.trialList in ([], [None], None):
    params = []
else:
    params = NumBlock1.trialList[0].keys()
# save data for this loop
NumBlock1.saveAsExcel(filename + '.xlsx', sheetName='NumBlock1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "restNum"-------
continueRoutine = True
# update component parameters for each repeat
respRest.keys = []
respRest.rt = []
_respRest_allKeys = []
# keep track of which components have finished
restNumComponents = [NumRest, respRest]
for thisComponent in restNumComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restNumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "restNum"-------
while continueRoutine:
    # get current time
    t = restNumClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restNumClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NumRest* updates
    if NumRest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NumRest.frameNStart = frameN  # exact frame index
        NumRest.tStart = t  # local t and not account for scr refresh
        NumRest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NumRest, 'tStartRefresh')  # time at next scr refresh
        NumRest.setAutoDraw(True)
    
    # *respRest* updates
    waitOnFlip = False
    if respRest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respRest.frameNStart = frameN  # exact frame index
        respRest.tStart = t  # local t and not account for scr refresh
        respRest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respRest, 'tStartRefresh')  # time at next scr refresh
        respRest.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respRest.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respRest.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respRest.status == STARTED and not waitOnFlip:
        theseKeys = respRest.getKeys(keyList=['space'], waitRelease=False)
        _respRest_allKeys.extend(theseKeys)
        if len(_respRest_allKeys):
            respRest.keys = _respRest_allKeys[-1].name  # just the last key pressed
            respRest.rt = _respRest_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restNumComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "restNum"-------
for thisComponent in restNumComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "restNum" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NumBlock2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NumCon.xlsx', selection='80:81'),
    seed=None, name='NumBlock2')
thisExp.addLoop(NumBlock2)  # add the loop to the experiment
thisNumBlock2 = NumBlock2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNumBlock2.rgb)
if thisNumBlock2 != None:
    for paramName in thisNumBlock2:
        exec('{} = thisNumBlock2[paramName]'.format(paramName))

for thisNumBlock2 in NumBlock2:
    currentLoop = NumBlock2
    # abbreviate parameter names if possible (e.g. rgb = thisNumBlock2.rgb)
    if thisNumBlock2 != None:
        for paramName in thisNumBlock2:
            exec('{} = thisNumBlock2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "num2Word"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    stimulus.setPos(Position)
    stimulus.setText(target)
    respNum2word.keys = []
    respNum2word.rt = []
    _respNum2word_allKeys = []
    # keep track of which components have finished
    num2WordComponents = [frame, stimulus, respNum2word]
    for thisComponent in num2WordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    num2WordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "num2Word"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = num2WordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=num2WordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *frame* updates
        if frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            frame.frameNStart = frameN  # exact frame index
            frame.tStart = t  # local t and not account for scr refresh
            frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame, 'tStartRefresh')  # time at next scr refresh
            frame.setAutoDraw(True)
        if frame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > frame.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                frame.tStop = t  # not accounting for scr refresh
                frame.frameNStop = frameN  # exact frame index
                win.timeOnFlip(frame, 'tStopRefresh')  # time at next scr refresh
                frame.setAutoDraw(False)
        
        # *stimulus* updates
        if stimulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.tStart = t  # local t and not account for scr refresh
            stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
            stimulus.setAutoDraw(True)
        if stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                stimulus.tStop = t  # not accounting for scr refresh
                stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(False)
        
        # *respNum2word* updates
        waitOnFlip = False
        if respNum2word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respNum2word.frameNStart = frameN  # exact frame index
            respNum2word.tStart = t  # local t and not account for scr refresh
            respNum2word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respNum2word, 'tStartRefresh')  # time at next scr refresh
            respNum2word.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respNum2word.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respNum2word.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respNum2word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respNum2word.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                respNum2word.tStop = t  # not accounting for scr refresh
                respNum2word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respNum2word, 'tStopRefresh')  # time at next scr refresh
                respNum2word.status = FINISHED
        if respNum2word.status == STARTED and not waitOnFlip:
            theseKeys = respNum2word.getKeys(keyList=['a', 'l'], waitRelease=False)
            _respNum2word_allKeys.extend(theseKeys)
            if len(_respNum2word_allKeys):
                respNum2word.keys = _respNum2word_allKeys[-1].name  # just the last key pressed
                respNum2word.rt = _respNum2word_allKeys[-1].rt
                # was this correct?
                if (respNum2word.keys == str(CorAns)) or (respNum2word.keys == CorAns):
                    respNum2word.corr = 1
                else:
                    respNum2word.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in num2WordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "num2Word"-------
    for thisComponent in num2WordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respNum2word.keys in ['', [], None]:  # No response was made
        respNum2word.keys = None
        # was no response the correct answer?!
        if str(CorAns).lower() == 'none':
           respNum2word.corr = 1;  # correct non-response
        else:
           respNum2word.corr = 0;  # failed to respond (incorrectly)
    # store data for NumBlock2 (TrialHandler)
    NumBlock2.addData('respNum2word.keys',respNum2word.keys)
    NumBlock2.addData('respNum2word.corr', respNum2word.corr)
    if respNum2word.keys != None:  # we had a response
        NumBlock2.addData('respNum2word.rt', respNum2word.rt)
    if respNum2word.corr:
        feedbacktext = "√"
        feedbackcolor = "green"
    else:
        feedbacktext = "×"
        feedbackcolor = "red"
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NumBlock2'

# get names of stimulus parameters
if NumBlock2.trialList in ([], [None], None):
    params = []
else:
    params = NumBlock2.trialList[0].keys()
# save data for this loop
NumBlock2.saveAsExcel(filename + '.xlsx', sheetName='NumBlock2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
returnPrac = data.TrialHandler(nReps=99.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='returnPrac')
thisExp.addLoop(returnPrac)  # add the loop to the experiment
thisReturnPrac = returnPrac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReturnPrac.rgb)
if thisReturnPrac != None:
    for paramName in thisReturnPrac:
        exec('{} = thisReturnPrac[paramName]'.format(paramName))

for thisReturnPrac in returnPrac:
    currentLoop = returnPrac
    # abbreviate parameter names if possible (e.g. rgb = thisReturnPrac.rgb)
    if thisReturnPrac != None:
        for paramName in thisReturnPrac:
            exec('{} = thisReturnPrac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AffInstr"-------
    continueRoutine = True
    # update component parameters for each repeat
    respAffInstr.keys = []
    respAffInstr.rt = []
    _respAffInstr_allKeys = []
    # keep track of which components have finished
    AffInstrComponents = [AffInsr_P, respAffInstr]
    for thisComponent in AffInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AffInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AffInstr"-------
    while continueRoutine:
        # get current time
        t = AffInstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AffInstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AffInsr_P* updates
        if AffInsr_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AffInsr_P.frameNStart = frameN  # exact frame index
            AffInsr_P.tStart = t  # local t and not account for scr refresh
            AffInsr_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffInsr_P, 'tStartRefresh')  # time at next scr refresh
            AffInsr_P.setAutoDraw(True)
        
        # *respAffInstr* updates
        waitOnFlip = False
        if respAffInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respAffInstr.frameNStart = frameN  # exact frame index
            respAffInstr.tStart = t  # local t and not account for scr refresh
            respAffInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respAffInstr, 'tStartRefresh')  # time at next scr refresh
            respAffInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respAffInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respAffInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respAffInstr.status == STARTED and not waitOnFlip:
            theseKeys = respAffInstr.getKeys(keyList=['space'], waitRelease=False)
            _respAffInstr_allKeys.extend(theseKeys)
            if len(_respAffInstr_allKeys):
                respAffInstr.keys = _respAffInstr_allKeys[-1].name  # just the last key pressed
                respAffInstr.rt = _respAffInstr_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AffInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AffInstr"-------
    for thisComponent in AffInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "AffInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracAff = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('AFFPrac.xlsx'),
        seed=None, name='PracAff')
    thisExp.addLoop(PracAff)  # add the loop to the experiment
    thisPracAff = PracAff.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracAff.rgb)
    if thisPracAff != None:
        for paramName in thisPracAff:
            exec('{} = thisPracAff[paramName]'.format(paramName))
    
    for thisPracAff in PracAff:
        currentLoop = PracAff
        # abbreviate parameter names if possible (e.g. rgb = thisPracAff.rgb)
        if thisPracAff != None:
            for paramName in thisPracAff:
                exec('{} = thisPracAff[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "intervals"-------
        continueRoutine = True
        # update component parameters for each repeat
        fixTime = Math.random(times);
        # keep track of which components have finished
        intervalsComponents = [text, blank]
        for thisComponent in intervalsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intervalsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "intervals"-------
        while continueRoutine:
            # get current time
            t = intervalsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intervalsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + fixTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intervalsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intervals"-------
        for thisComponent in intervalsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracAff.addData('text.started', text.tStartRefresh)
        PracAff.addData('text.stopped', text.tStopRefresh)
        PracAff.addData('blank.started', blank.tStartRefresh)
        PracAff.addData('blank.stopped', blank.tStopRefresh)
        # the Routine "intervals" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AFF_S1"-------
        continueRoutine = True
        routineTimer.add(1.700000)
        # update component parameters for each repeat
        flanker_p.setImage(flankerPic)
        target_p.setImage(targetPic)
        respFlanker.keys = []
        respFlanker.rt = []
        _respFlanker_allKeys = []
        # keep track of which components have finished
        AFF_S1Components = [flanker_p, target_p, respFlanker]
        for thisComponent in AFF_S1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AFF_S1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AFF_S1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AFF_S1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AFF_S1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *flanker_p* updates
            if flanker_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                flanker_p.frameNStart = frameN  # exact frame index
                flanker_p.tStart = t  # local t and not account for scr refresh
                flanker_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_p, 'tStartRefresh')  # time at next scr refresh
                flanker_p.setAutoDraw(True)
            if flanker_p.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_p.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_p.tStop = t  # not accounting for scr refresh
                    flanker_p.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_p, 'tStopRefresh')  # time at next scr refresh
                    flanker_p.setAutoDraw(False)
            
            # *target_p* updates
            if target_p.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                target_p.frameNStart = frameN  # exact frame index
                target_p.tStart = t  # local t and not account for scr refresh
                target_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_p, 'tStartRefresh')  # time at next scr refresh
                target_p.setAutoDraw(True)
            if target_p.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_p.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target_p.tStop = t  # not accounting for scr refresh
                    target_p.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target_p, 'tStopRefresh')  # time at next scr refresh
                    target_p.setAutoDraw(False)
            
            # *respFlanker* updates
            waitOnFlip = False
            if respFlanker.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                respFlanker.frameNStart = frameN  # exact frame index
                respFlanker.tStart = t  # local t and not account for scr refresh
                respFlanker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respFlanker, 'tStartRefresh')  # time at next scr refresh
                respFlanker.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respFlanker.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respFlanker.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respFlanker.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respFlanker.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respFlanker.tStop = t  # not accounting for scr refresh
                    respFlanker.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(respFlanker, 'tStopRefresh')  # time at next scr refresh
                    respFlanker.status = FINISHED
            if respFlanker.status == STARTED and not waitOnFlip:
                theseKeys = respFlanker.getKeys(keyList=['a', 's'], waitRelease=False)
                _respFlanker_allKeys.extend(theseKeys)
                if len(_respFlanker_allKeys):
                    respFlanker.keys = _respFlanker_allKeys[-1].name  # just the last key pressed
                    respFlanker.rt = _respFlanker_allKeys[-1].rt
                    # was this correct?
                    if (respFlanker.keys == str(corAnsF)) or (respFlanker.keys == corAnsF):
                        respFlanker.corr = 1
                    else:
                        respFlanker.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AFF_S1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AFF_S1"-------
        for thisComponent in AFF_S1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if respFlanker.keys in ['', [], None]:  # No response was made
            respFlanker.keys = None
            # was no response the correct answer?!
            if str(corAnsF).lower() == 'none':
               respFlanker.corr = 1;  # correct non-response
            else:
               respFlanker.corr = 0;  # failed to respond (incorrectly)
        # store data for PracAff (TrialHandler)
        PracAff.addData('respFlanker.keys',respFlanker.keys)
        PracAff.addData('respFlanker.corr', respFlanker.corr)
        if respFlanker.keys != None:  # we had a response
            PracAff.addData('respFlanker.rt', respFlanker.rt)
        
        # ------Prepare to start Routine "AFF_S2"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        AffWord.setText(thisWord)
        respAffWord.keys = []
        respAffWord.rt = []
        _respAffWord_allKeys = []
        # keep track of which components have finished
        AFF_S2Components = [AffWord, respAffWord]
        for thisComponent in AFF_S2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AFF_S2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AFF_S2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AFF_S2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AFF_S2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AffWord* updates
            if AffWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AffWord.frameNStart = frameN  # exact frame index
                AffWord.tStart = t  # local t and not account for scr refresh
                AffWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AffWord, 'tStartRefresh')  # time at next scr refresh
                AffWord.setAutoDraw(True)
            if AffWord.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AffWord.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    AffWord.tStop = t  # not accounting for scr refresh
                    AffWord.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AffWord, 'tStopRefresh')  # time at next scr refresh
                    AffWord.setAutoDraw(False)
            
            # *respAffWord* updates
            waitOnFlip = False
            if respAffWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respAffWord.frameNStart = frameN  # exact frame index
                respAffWord.tStart = t  # local t and not account for scr refresh
                respAffWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respAffWord, 'tStartRefresh')  # time at next scr refresh
                respAffWord.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respAffWord.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respAffWord.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respAffWord.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respAffWord.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respAffWord.tStop = t  # not accounting for scr refresh
                    respAffWord.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(respAffWord, 'tStopRefresh')  # time at next scr refresh
                    respAffWord.status = FINISHED
            if respAffWord.status == STARTED and not waitOnFlip:
                theseKeys = respAffWord.getKeys(keyList=['l', 'k'], waitRelease=False)
                _respAffWord_allKeys.extend(theseKeys)
                if len(_respAffWord_allKeys):
                    respAffWord.keys = _respAffWord_allKeys[-1].name  # just the last key pressed
                    respAffWord.rt = _respAffWord_allKeys[-1].rt
                    # was this correct?
                    if (respAffWord.keys == str(corAnsA)) or (respAffWord.keys == corAnsA):
                        respAffWord.corr = 1
                    else:
                        respAffWord.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AFF_S2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AFF_S2"-------
        for thisComponent in AFF_S2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("thisWord",thisWord)
        # check responses
        if respAffWord.keys in ['', [], None]:  # No response was made
            respAffWord.keys = None
            # was no response the correct answer?!
            if str(corAnsA).lower() == 'none':
               respAffWord.corr = 1;  # correct non-response
            else:
               respAffWord.corr = 0;  # failed to respond (incorrectly)
        # store data for PracAff (TrialHandler)
        PracAff.addData('respAffWord.keys',respAffWord.keys)
        PracAff.addData('respAffWord.corr', respAffWord.corr)
        if respAffWord.keys != None:  # we had a response
            PracAff.addData('respAffWord.rt', respAffWord.rt)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'PracAff'
    
    # get names of stimulus parameters
    if PracAff.trialList in ([], [None], None):
        params = []
    else:
        params = PracAff.trialList[0].keys()
    # save data for this loop
    PracAff.saveAsExcel(filename + '.xlsx', sheetName='PracAff',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "endPracAff"-------
    continueRoutine = True
    # update component parameters for each repeat
    respEndPracA.keys = []
    respEndPracA.rt = []
    _respEndPracA_allKeys = []
    # keep track of which components have finished
    endPracAffComponents = [endPracA_p, respEndPracA]
    for thisComponent in endPracAffComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endPracAffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "endPracAff"-------
    while continueRoutine:
        # get current time
        t = endPracAffClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endPracAffClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endPracA_p* updates
        if endPracA_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endPracA_p.frameNStart = frameN  # exact frame index
            endPracA_p.tStart = t  # local t and not account for scr refresh
            endPracA_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endPracA_p, 'tStartRefresh')  # time at next scr refresh
            endPracA_p.setAutoDraw(True)
        
        # *respEndPracA* updates
        waitOnFlip = False
        if respEndPracA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respEndPracA.frameNStart = frameN  # exact frame index
            respEndPracA.tStart = t  # local t and not account for scr refresh
            respEndPracA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respEndPracA, 'tStartRefresh')  # time at next scr refresh
            respEndPracA.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respEndPracA.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respEndPracA.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respEndPracA.status == STARTED and not waitOnFlip:
            theseKeys = respEndPracA.getKeys(keyList=['p', 'q'], waitRelease=False)
            _respEndPracA_allKeys.extend(theseKeys)
            if len(_respEndPracA_allKeys):
                respEndPracA.keys = _respEndPracA_allKeys[-1].name  # just the last key pressed
                respEndPracA.rt = _respEndPracA_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endPracAffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endPracAff"-------
    for thisComponent in endPracAffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if respEndPracA.keys == "p":
        returnPrac.finished = True # 循环结束
    else:
        returnPrac.finished = False
    
    positiveWords = [
        "畅销", "诚恳", "充裕", "典雅",
        "丰满", "奉献", "富丽", "富足",
        "公平", "瑰丽", "豪放", "吉祥",
        "精致", "敬佩", "俊秀", "廉洁",
        "留恋", "前进", "清秀", "热切",
        "如愿", "生动", "圣洁", "舒畅",
        "爽朗", "顽强", "旺盛", "鲜艳",
        "羡慕", "享受", "雄厚", "秀丽",
        "永恒", "优雅", "有利", "赞成",
        "珍藏", "振作", "正直", "卓越"
    ]
    # 消极词表
    negativeWords = [
        "悲观", "别扭", "嘲笑", "处罚",
        "丢失", "堵塞", "罚款", "烦恼",
        "孤单", "黑暗", "胡涂", "怀疑",
        "慌忙", "假冒", "焦躁", "禁止",
        "沮丧", "懒惰", "浪费", "冷笑",
        "鲁莽", "落后", "闷热", "排斥",
        "轻率", "穷苦", "缺乏", "撒谎",
        "伤心", "失意", "损害", "逃避",
        "消沉", "心慌", "厌恶", "忧虑",
        "郁闷", "杂乱", "争吵", "自卑"
    ]
    # the Routine "endPracAff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'returnPrac'

# get names of stimulus parameters
if returnPrac.trialList in ([], [None], None):
    params = []
else:
    params = returnPrac.trialList[0].keys()
# save data for this loop
returnPrac.saveAsExcel(filename + '.xlsx', sheetName='returnPrac',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
AffBlocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('AffLoop.xlsx'),
    seed=None, name='AffBlocks')
thisExp.addLoop(AffBlocks)  # add the loop to the experiment
thisAffBlock = AffBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAffBlock.rgb)
if thisAffBlock != None:
    for paramName in thisAffBlock:
        exec('{} = thisAffBlock[paramName]'.format(paramName))

for thisAffBlock in AffBlocks:
    currentLoop = AffBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisAffBlock.rgb)
    if thisAffBlock != None:
        for paramName in thisAffBlock:
            exec('{} = thisAffBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    AffBlock1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('AFFcon.xlsx'),
        seed=None, name='AffBlock1')
    thisExp.addLoop(AffBlock1)  # add the loop to the experiment
    thisAffBlock1 = AffBlock1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAffBlock1.rgb)
    if thisAffBlock1 != None:
        for paramName in thisAffBlock1:
            exec('{} = thisAffBlock1[paramName]'.format(paramName))
    
    for thisAffBlock1 in AffBlock1:
        currentLoop = AffBlock1
        # abbreviate parameter names if possible (e.g. rgb = thisAffBlock1.rgb)
        if thisAffBlock1 != None:
            for paramName in thisAffBlock1:
                exec('{} = thisAffBlock1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "intervals"-------
        continueRoutine = True
        # update component parameters for each repeat
        fixTime = Math.random(times);
        # keep track of which components have finished
        intervalsComponents = [text, blank]
        for thisComponent in intervalsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intervalsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "intervals"-------
        while continueRoutine:
            # get current time
            t = intervalsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intervalsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + fixTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intervalsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intervals"-------
        for thisComponent in intervalsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AffBlock1.addData('text.started', text.tStartRefresh)
        AffBlock1.addData('text.stopped', text.tStopRefresh)
        AffBlock1.addData('blank.started', blank.tStartRefresh)
        AffBlock1.addData('blank.stopped', blank.tStopRefresh)
        # the Routine "intervals" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AFF_S1"-------
        continueRoutine = True
        routineTimer.add(1.700000)
        # update component parameters for each repeat
        flanker_p.setImage(flankerPic)
        target_p.setImage(targetPic)
        respFlanker.keys = []
        respFlanker.rt = []
        _respFlanker_allKeys = []
        # keep track of which components have finished
        AFF_S1Components = [flanker_p, target_p, respFlanker]
        for thisComponent in AFF_S1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AFF_S1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AFF_S1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AFF_S1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AFF_S1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *flanker_p* updates
            if flanker_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                flanker_p.frameNStart = frameN  # exact frame index
                flanker_p.tStart = t  # local t and not account for scr refresh
                flanker_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_p, 'tStartRefresh')  # time at next scr refresh
                flanker_p.setAutoDraw(True)
            if flanker_p.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_p.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_p.tStop = t  # not accounting for scr refresh
                    flanker_p.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_p, 'tStopRefresh')  # time at next scr refresh
                    flanker_p.setAutoDraw(False)
            
            # *target_p* updates
            if target_p.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                target_p.frameNStart = frameN  # exact frame index
                target_p.tStart = t  # local t and not account for scr refresh
                target_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_p, 'tStartRefresh')  # time at next scr refresh
                target_p.setAutoDraw(True)
            if target_p.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_p.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target_p.tStop = t  # not accounting for scr refresh
                    target_p.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target_p, 'tStopRefresh')  # time at next scr refresh
                    target_p.setAutoDraw(False)
            
            # *respFlanker* updates
            waitOnFlip = False
            if respFlanker.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                respFlanker.frameNStart = frameN  # exact frame index
                respFlanker.tStart = t  # local t and not account for scr refresh
                respFlanker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respFlanker, 'tStartRefresh')  # time at next scr refresh
                respFlanker.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respFlanker.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respFlanker.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respFlanker.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respFlanker.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respFlanker.tStop = t  # not accounting for scr refresh
                    respFlanker.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(respFlanker, 'tStopRefresh')  # time at next scr refresh
                    respFlanker.status = FINISHED
            if respFlanker.status == STARTED and not waitOnFlip:
                theseKeys = respFlanker.getKeys(keyList=['a', 's'], waitRelease=False)
                _respFlanker_allKeys.extend(theseKeys)
                if len(_respFlanker_allKeys):
                    respFlanker.keys = _respFlanker_allKeys[-1].name  # just the last key pressed
                    respFlanker.rt = _respFlanker_allKeys[-1].rt
                    # was this correct?
                    if (respFlanker.keys == str(corAnsF)) or (respFlanker.keys == corAnsF):
                        respFlanker.corr = 1
                    else:
                        respFlanker.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AFF_S1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AFF_S1"-------
        for thisComponent in AFF_S1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if respFlanker.keys in ['', [], None]:  # No response was made
            respFlanker.keys = None
            # was no response the correct answer?!
            if str(corAnsF).lower() == 'none':
               respFlanker.corr = 1;  # correct non-response
            else:
               respFlanker.corr = 0;  # failed to respond (incorrectly)
        # store data for AffBlock1 (TrialHandler)
        AffBlock1.addData('respFlanker.keys',respFlanker.keys)
        AffBlock1.addData('respFlanker.corr', respFlanker.corr)
        if respFlanker.keys != None:  # we had a response
            AffBlock1.addData('respFlanker.rt', respFlanker.rt)
        
        # ------Prepare to start Routine "AFF_S2"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        AffWord.setText(thisWord)
        respAffWord.keys = []
        respAffWord.rt = []
        _respAffWord_allKeys = []
        # keep track of which components have finished
        AFF_S2Components = [AffWord, respAffWord]
        for thisComponent in AFF_S2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AFF_S2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AFF_S2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AFF_S2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AFF_S2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AffWord* updates
            if AffWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AffWord.frameNStart = frameN  # exact frame index
                AffWord.tStart = t  # local t and not account for scr refresh
                AffWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AffWord, 'tStartRefresh')  # time at next scr refresh
                AffWord.setAutoDraw(True)
            if AffWord.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AffWord.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    AffWord.tStop = t  # not accounting for scr refresh
                    AffWord.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AffWord, 'tStopRefresh')  # time at next scr refresh
                    AffWord.setAutoDraw(False)
            
            # *respAffWord* updates
            waitOnFlip = False
            if respAffWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respAffWord.frameNStart = frameN  # exact frame index
                respAffWord.tStart = t  # local t and not account for scr refresh
                respAffWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respAffWord, 'tStartRefresh')  # time at next scr refresh
                respAffWord.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respAffWord.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respAffWord.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respAffWord.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respAffWord.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    respAffWord.tStop = t  # not accounting for scr refresh
                    respAffWord.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(respAffWord, 'tStopRefresh')  # time at next scr refresh
                    respAffWord.status = FINISHED
            if respAffWord.status == STARTED and not waitOnFlip:
                theseKeys = respAffWord.getKeys(keyList=['l', 'k'], waitRelease=False)
                _respAffWord_allKeys.extend(theseKeys)
                if len(_respAffWord_allKeys):
                    respAffWord.keys = _respAffWord_allKeys[-1].name  # just the last key pressed
                    respAffWord.rt = _respAffWord_allKeys[-1].rt
                    # was this correct?
                    if (respAffWord.keys == str(corAnsA)) or (respAffWord.keys == corAnsA):
                        respAffWord.corr = 1
                    else:
                        respAffWord.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AFF_S2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AFF_S2"-------
        for thisComponent in AFF_S2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("thisWord",thisWord)
        # check responses
        if respAffWord.keys in ['', [], None]:  # No response was made
            respAffWord.keys = None
            # was no response the correct answer?!
            if str(corAnsA).lower() == 'none':
               respAffWord.corr = 1;  # correct non-response
            else:
               respAffWord.corr = 0;  # failed to respond (incorrectly)
        # store data for AffBlock1 (TrialHandler)
        AffBlock1.addData('respAffWord.keys',respAffWord.keys)
        AffBlock1.addData('respAffWord.corr', respAffWord.corr)
        if respAffWord.keys != None:  # we had a response
            AffBlock1.addData('respAffWord.rt', respAffWord.rt)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'AffBlock1'
    
    # get names of stimulus parameters
    if AffBlock1.trialList in ([], [None], None):
        params = []
    else:
        params = AffBlock1.trialList[0].keys()
    # save data for this loop
    AffBlock1.saveAsExcel(filename + '.xlsx', sheetName='AffBlock1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "restAff"-------
    continueRoutine = True
    # update component parameters for each repeat
    AffRest.setImage(RestPic)
    respRest_2.keys = []
    respRest_2.rt = []
    _respRest_2_allKeys = []
    # keep track of which components have finished
    restAffComponents = [AffRest, respRest_2]
    for thisComponent in restAffComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restAffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "restAff"-------
    while continueRoutine:
        # get current time
        t = restAffClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restAffClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AffRest* updates
        if AffRest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AffRest.frameNStart = frameN  # exact frame index
            AffRest.tStart = t  # local t and not account for scr refresh
            AffRest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffRest, 'tStartRefresh')  # time at next scr refresh
            AffRest.setAutoDraw(True)
        
        # *respRest_2* updates
        waitOnFlip = False
        if respRest_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respRest_2.frameNStart = frameN  # exact frame index
            respRest_2.tStart = t  # local t and not account for scr refresh
            respRest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respRest_2, 'tStartRefresh')  # time at next scr refresh
            respRest_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respRest_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respRest_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respRest_2.status == STARTED and not waitOnFlip:
            theseKeys = respRest_2.getKeys(keyList=['space'], waitRelease=False)
            _respRest_2_allKeys.extend(theseKeys)
            if len(_respRest_2_allKeys):
                respRest_2.keys = _respRest_2_allKeys[-1].name  # just the last key pressed
                respRest_2.rt = _respRest_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restAffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "restAff"-------
    for thisComponent in restAffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # 积极词表
    positiveWords = [
        "畅销", "诚恳", "充裕", "典雅",
        "丰满", "奉献", "富丽", "富足",
        "公平", "瑰丽", "豪放", "吉祥",
        "精致", "敬佩", "俊秀", "廉洁",
        "留恋", "前进", "清秀", "热切",
        "如愿", "生动", "圣洁", "舒畅",
        "爽朗", "顽强", "旺盛", "鲜艳",
        "羡慕", "享受", "雄厚", "秀丽",
        "永恒", "优雅", "有利", "赞成",
        "珍藏", "振作", "正直", "卓越"
    ]
    # 消极词表
    negativeWords = [
        "悲观", "别扭", "嘲笑", "处罚",
        "丢失", "堵塞", "罚款", "烦恼",
        "孤单", "黑暗", "胡涂", "怀疑",
        "慌忙", "假冒", "焦躁", "禁止",
        "沮丧", "懒惰", "浪费", "冷笑",
        "鲁莽", "落后", "闷热", "排斥",
        "轻率", "穷苦", "缺乏", "撒谎",
        "伤心", "失意", "损害", "逃避",
        "消沉", "心慌", "厌恶", "忧虑",
        "郁闷", "杂乱", "争吵", "自卑"
    ]
    # the Routine "restAff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'AffBlocks'

# get names of stimulus parameters
if AffBlocks.trialList in ([], [None], None):
    params = []
else:
    params = AffBlocks.trialList[0].keys()
# save data for this loop
AffBlocks.saveAsExcel(filename + '.xlsx', sheetName='AffBlocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
