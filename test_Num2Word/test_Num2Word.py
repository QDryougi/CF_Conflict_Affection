#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on June 09, 2023, at 20:18
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
expName = 'test_Num2Word'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Ryougi mana\\Desktop\\test_Num2Word\\test_Num2Word.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instrpage1 = visual.TextStim(win=win, name='instrpage1',
    text='Green = a\nRed = l',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "FixationRoutine"
FixationRoutineClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ChooseRTs"
ChooseRTsClock = core.Clock()
point = visual.ShapeStim(
    win=win, name='point',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
respChoRT = keyboard.Keyboard()

# Initialize components for Routine "blank1"
blank1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instrpage2 = visual.TextStim(win=win, name='instrpage2',
    text='space to go on',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "FixationRoutine"
FixationRoutineClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ChooseRTs"
ChooseRTsClock = core.Clock()
point = visual.ShapeStim(
    win=win, name='point',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
respChoRT = keyboard.Keyboard()

# Initialize components for Routine "blank1"
blank1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=feedbackcolor, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='take a rest\nspce out\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instr1Components = [instrpage1, key_resp]
for thisComponent in instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrpage1* updates
    if instrpage1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrpage1.frameNStart = frameN  # exact frame index
        instrpage1.tStart = t  # local t and not account for scr refresh
        instrpage1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrpage1, 'tStartRefresh')  # time at next scr refresh
        instrpage1.setAutoDraw(True)
    
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
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrpage1.started', instrpage1.tStartRefresh)
thisExp.addData('instrpage1.stopped', instrpage1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Study1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('color.xlsx', selection='3,5,8,23,67.9'),
    seed=None, name='Study1')
thisExp.addLoop(Study1)  # add the loop to the experiment
thisStudy1 = Study1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy1.rgb)
if thisStudy1 != None:
    for paramName in thisStudy1:
        exec('{} = thisStudy1[paramName]'.format(paramName))

for thisStudy1 in Study1:
    currentLoop = Study1
    # abbreviate parameter names if possible (e.g. rgb = thisStudy1.rgb)
    if thisStudy1 != None:
        for paramName in thisStudy1:
            exec('{} = thisStudy1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationRoutine"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationRoutineComponents = [Fixation]
    for thisComponent in FixationRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationRoutine"-------
    while continueRoutine:
        # get current time
        t = FixationRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + FixTime-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationRoutine"-------
    for thisComponent in FixationRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study1.addData('Fixation.started', Fixation.tStartRefresh)
    Study1.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "FixationRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ChooseRTs"-------
    continueRoutine = True
    # update component parameters for each repeat
    point.setFillColor(color)
    respChoRT.keys = []
    respChoRT.rt = []
    _respChoRT_allKeys = []
    # keep track of which components have finished
    ChooseRTsComponents = [point, respChoRT]
    for thisComponent in ChooseRTsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChooseRTsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ChooseRTs"-------
    while continueRoutine:
        # get current time
        t = ChooseRTsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChooseRTsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *point* updates
        if point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            point.frameNStart = frameN  # exact frame index
            point.tStart = t  # local t and not account for scr refresh
            point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(point, 'tStartRefresh')  # time at next scr refresh
            point.setAutoDraw(True)
        
        # *respChoRT* updates
        waitOnFlip = False
        if respChoRT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respChoRT.frameNStart = frameN  # exact frame index
            respChoRT.tStart = t  # local t and not account for scr refresh
            respChoRT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respChoRT, 'tStartRefresh')  # time at next scr refresh
            respChoRT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respChoRT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respChoRT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respChoRT.status == STARTED and not waitOnFlip:
            theseKeys = respChoRT.getKeys(keyList=['a', 'l'], waitRelease=False)
            _respChoRT_allKeys.extend(theseKeys)
            if len(_respChoRT_allKeys):
                respChoRT.keys = _respChoRT_allKeys[-1].name  # just the last key pressed
                respChoRT.rt = _respChoRT_allKeys[-1].rt
                # was this correct?
                if (respChoRT.keys == str(Ans)) or (respChoRT.keys == Ans):
                    respChoRT.corr = 1
                else:
                    respChoRT.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChooseRTsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ChooseRTs"-------
    for thisComponent in ChooseRTsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study1.addData('point.started', point.tStartRefresh)
    Study1.addData('point.stopped', point.tStopRefresh)
    # check responses
    if respChoRT.keys in ['', [], None]:  # No response was made
        respChoRT.keys = None
        # was no response the correct answer?!
        if str(Ans).lower() == 'none':
           respChoRT.corr = 1;  # correct non-response
        else:
           respChoRT.corr = 0;  # failed to respond (incorrectly)
    # store data for Study1 (TrialHandler)
    Study1.addData('respChoRT.keys',respChoRT.keys)
    Study1.addData('respChoRT.corr', respChoRT.corr)
    if respChoRT.keys != None:  # we had a response
        Study1.addData('respChoRT.rt', respChoRT.rt)
    # the Routine "ChooseRTs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank1"-------
    continueRoutine = True
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank1Components = [text_5]
    for thisComponent in blank1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank1"-------
    for thisComponent in blank1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study1.addData('text_5.started', text_5.tStartRefresh)
    Study1.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Study1'


# ------Prepare to start Routine "instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr2Components = [instrpage2, key_resp_2]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrpage2* updates
    if instrpage2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrpage2.frameNStart = frameN  # exact frame index
        instrpage2.tStart = t  # local t and not account for scr refresh
        instrpage2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrpage2, 'tStartRefresh')  # time at next scr refresh
        instrpage2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrpage2.started', instrpage2.tStartRefresh)
thisExp.addData('instrpage2.stopped', instrpage2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ChooseRTtrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('color.xlsx'),
    seed=None, name='ChooseRTtrials')
thisExp.addLoop(ChooseRTtrials)  # add the loop to the experiment
thisChooseRTtrial = ChooseRTtrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChooseRTtrial.rgb)
if thisChooseRTtrial != None:
    for paramName in thisChooseRTtrial:
        exec('{} = thisChooseRTtrial[paramName]'.format(paramName))

for thisChooseRTtrial in ChooseRTtrials:
    currentLoop = ChooseRTtrials
    # abbreviate parameter names if possible (e.g. rgb = thisChooseRTtrial.rgb)
    if thisChooseRTtrial != None:
        for paramName in thisChooseRTtrial:
            exec('{} = thisChooseRTtrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationRoutine"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationRoutineComponents = [Fixation]
    for thisComponent in FixationRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationRoutine"-------
    while continueRoutine:
        # get current time
        t = FixationRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + FixTime-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationRoutine"-------
    for thisComponent in FixationRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ChooseRTtrials.addData('Fixation.started', Fixation.tStartRefresh)
    ChooseRTtrials.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "FixationRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ChooseRTs"-------
    continueRoutine = True
    # update component parameters for each repeat
    point.setFillColor(color)
    respChoRT.keys = []
    respChoRT.rt = []
    _respChoRT_allKeys = []
    # keep track of which components have finished
    ChooseRTsComponents = [point, respChoRT]
    for thisComponent in ChooseRTsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChooseRTsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ChooseRTs"-------
    while continueRoutine:
        # get current time
        t = ChooseRTsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChooseRTsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *point* updates
        if point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            point.frameNStart = frameN  # exact frame index
            point.tStart = t  # local t and not account for scr refresh
            point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(point, 'tStartRefresh')  # time at next scr refresh
            point.setAutoDraw(True)
        
        # *respChoRT* updates
        waitOnFlip = False
        if respChoRT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respChoRT.frameNStart = frameN  # exact frame index
            respChoRT.tStart = t  # local t and not account for scr refresh
            respChoRT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respChoRT, 'tStartRefresh')  # time at next scr refresh
            respChoRT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respChoRT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respChoRT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respChoRT.status == STARTED and not waitOnFlip:
            theseKeys = respChoRT.getKeys(keyList=['a', 'l'], waitRelease=False)
            _respChoRT_allKeys.extend(theseKeys)
            if len(_respChoRT_allKeys):
                respChoRT.keys = _respChoRT_allKeys[-1].name  # just the last key pressed
                respChoRT.rt = _respChoRT_allKeys[-1].rt
                # was this correct?
                if (respChoRT.keys == str(Ans)) or (respChoRT.keys == Ans):
                    respChoRT.corr = 1
                else:
                    respChoRT.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChooseRTsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ChooseRTs"-------
    for thisComponent in ChooseRTsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ChooseRTtrials.addData('point.started', point.tStartRefresh)
    ChooseRTtrials.addData('point.stopped', point.tStopRefresh)
    # check responses
    if respChoRT.keys in ['', [], None]:  # No response was made
        respChoRT.keys = None
        # was no response the correct answer?!
        if str(Ans).lower() == 'none':
           respChoRT.corr = 1;  # correct non-response
        else:
           respChoRT.corr = 0;  # failed to respond (incorrectly)
    # store data for ChooseRTtrials (TrialHandler)
    ChooseRTtrials.addData('respChoRT.keys',respChoRT.keys)
    ChooseRTtrials.addData('respChoRT.corr', respChoRT.corr)
    if respChoRT.keys != None:  # we had a response
        ChooseRTtrials.addData('respChoRT.rt', respChoRT.rt)
    # the Routine "ChooseRTs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank1"-------
    continueRoutine = True
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank1Components = [text_5]
    for thisComponent in blank1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank1"-------
    for thisComponent in blank1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ChooseRTtrials.addData('text_5.started', text_5.tStartRefresh)
    ChooseRTtrials.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ChooseRTtrials'


# ------Prepare to start Routine "instr3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr3Components = [text]
for thisComponent in instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
study2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practise.xlsx'),
    seed=None, name='study2')
thisExp.addLoop(study2)  # add the loop to the experiment
thisStudy2 = study2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy2.rgb)
if thisStudy2 != None:
    for paramName in thisStudy2:
        exec('{} = thisStudy2[paramName]'.format(paramName))

for thisStudy2 in study2:
    currentLoop = study2
    # abbreviate parameter names if possible (e.g. rgb = thisStudy2.rgb)
    if thisStudy2 != None:
        for paramName in thisStudy2:
            exec('{} = thisStudy2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "num2Word"-------
    continueRoutine = True
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
    while continueRoutine:
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
            if tThisFlipGlobal > stimulus.tStartRefresh + 3-frameTolerance:
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
    # store data for study2 (TrialHandler)
    study2.addData('respNum2word.keys',respNum2word.keys)
    study2.addData('respNum2word.corr', respNum2word.corr)
    if respNum2word.keys != None:  # we had a response
        study2.addData('respNum2word.rt', respNum2word.rt)
    feedbackcolor = "green"
    if respNum2word.corr:
        feedbacktext = "√"
        feedbackcolor = "green"
    else:
        feedbacktext = "×"
        feedbackcolor = "red"
    # the Routine "num2Word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    text_4.setText(feedbacktext)
    # keep track of which components have finished
    feedbackComponents = [frame2, text_4]
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
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
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
    study2.addData('frame2.started', frame2.tStartRefresh)
    study2.addData('frame2.stopped', frame2.tStopRefresh)
    study2.addData('text_4.started', text_4.tStartRefresh)
    study2.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'study2'


# ------Prepare to start Routine "instr4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr4Components = [text_2]
for thisComponent in instr4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate1.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Num2wordtrials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('mainbody.xlsx', selection=Rows),
        seed=None, name='Num2wordtrials')
    thisExp.addLoop(Num2wordtrials)  # add the loop to the experiment
    thisNum2wordtrial = Num2wordtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNum2wordtrial.rgb)
    if thisNum2wordtrial != None:
        for paramName in thisNum2wordtrial:
            exec('{} = thisNum2wordtrial[paramName]'.format(paramName))
    
    for thisNum2wordtrial in Num2wordtrials:
        currentLoop = Num2wordtrials
        # abbreviate parameter names if possible (e.g. rgb = thisNum2wordtrial.rgb)
        if thisNum2wordtrial != None:
            for paramName in thisNum2wordtrial:
                exec('{} = thisNum2wordtrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "num2Word"-------
        continueRoutine = True
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
        while continueRoutine:
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
                if tThisFlipGlobal > stimulus.tStartRefresh + 3-frameTolerance:
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
        # store data for Num2wordtrials (TrialHandler)
        Num2wordtrials.addData('respNum2word.keys',respNum2word.keys)
        Num2wordtrials.addData('respNum2word.corr', respNum2word.corr)
        if respNum2word.keys != None:  # we had a response
            Num2wordtrials.addData('respNum2word.rt', respNum2word.rt)
        feedbackcolor = "green"
        if respNum2word.corr:
            feedbacktext = "√"
            feedbackcolor = "green"
        else:
            feedbacktext = "×"
            feedbackcolor = "red"
        # the Routine "num2Word" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Num2wordtrials'
    
    
    # ------Prepare to start Routine "instr5"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    instr5Components = [text_3, key_resp_3]
    for thisComponent in instr5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr5"-------
    while continueRoutine:
        # get current time
        t = instr5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr5"-------
    for thisComponent in instr5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('text_3.started', text_3.tStartRefresh)
    blocks.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    blocks.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        blocks.addData('key_resp_3.rt', key_resp_3.rt)
    blocks.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    blocks.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "instr5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


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
