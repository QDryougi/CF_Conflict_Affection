#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 05, 2024, at 21:25
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
expInfo = {'您的名称(不必实名)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['您的名称(不必实名)'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Ryougi mana\\Desktop\\CF_DDM\\test_Num2Word\\test_Num2Word_lastrun.py',
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

# Initialize components for Routine "instrNum"
instrNumClock = core.Clock()
image_instr = visual.ImageStim(
    win=win,
    name='image_instr', 
    image='pic/pic1.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

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
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "endPracNum"
endPracNumClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='pic/pic5.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

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
key_resp_3 = keyboard.Keyboard()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='pic/pic6.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

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

# Initialize components for Routine "End"
EndClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='pic/pic7.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.33,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    instrNumComponents = [image_instr, key_resp_5]
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
        
        # *image_instr* updates
        if image_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_instr.frameNStart = frameN  # exact frame index
            image_instr.tStart = t  # local t and not account for scr refresh
            image_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_instr, 'tStartRefresh')  # time at next scr refresh
            image_instr.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
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
        trialList=data.importConditions('practise.xlsx', selection='0:5'),
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
        text_4.setColor(feedbackcolor, colorSpace='rgb')
        text_4.setPos(Position)
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
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'pracNum'
    
    
    # ------Prepare to start Routine "endPracNum"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    endPracNumComponents = [image_5, key_resp_6]
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
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['q', 'p'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
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
    if key_resp_6.keys == "p":
        returnPractice.finished = True # 循环结束
    else:
        returnPractice.finished = False
    # the Routine "endPracNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'returnPractice'


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
    trialList=data.importConditions('mainbody.xlsx', selection='0:5'),
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


# ------Prepare to start Routine "restNum"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
restNumComponents = [key_resp_3, image_6]
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
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
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
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "restNum" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NumBlock2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mainbody.xlsx', selection='80:85'),
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


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
EndComponents = [key_resp_7, image_7]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
