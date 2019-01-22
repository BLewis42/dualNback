#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on November 19, 2018, at 16:02
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'dual n-back - Schweizer'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='S:\\Research\\Nixon\\People\\Ben Lewis\\Psychopy\\Dual N-Back Task\\dual n-back - Schweizer.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1080, 1080], fullscr=False, screen=1,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
back = 1
corr = []
audiocorr = []
oneback = []
twoback = []
threeback = []
fourback = []
fiveback = []
sixback = []
sevenback = []
eightback = []
twobackmovie = ''
color = [1,1,1]
audiooneback = []
audiotwoback = []
audiothreeback = []
audiofourback = []
audiofiveback = []
audiosixback = []
audiosevenback = []
audioeightback = []

polygon1 = visual.Rect(
    win=win, name='polygon1',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon2 = visual.Rect(
    win=win, name='polygon2',
    width=[2, .05][0], height=[2, .05][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon3 = visual.Rect(
    win=win, name='polygon3',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(1, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon4 = visual.Rect(
    win=win, name='polygon4',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon5 = visual.Rect(
    win=win, name='polygon5',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(-.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon6 = visual.Rect(
    win=win, name='polygon6',
    width=(2, 0.05)[0], height=(2, 0.05)[1],
    ori=0, pos=(0, .5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon7 = visual.Rect(
    win=win, name='polygon7',
    width=(2, 0.05)[0], height=(2, 0.05)[1],
    ori=0, pos=(0, -.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
polygon8 = visual.Rect(
    win=win, name='polygon8',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(-1, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
polygon9 = visual.Rect(
    win=win, name='polygon9',
    width=(0.05, 2)[0], height=(0.05, 2)[1],
    ori=0, pos=(1, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
polygon10 = visual.Rect(
    win=win, name='polygon10',
    width=(2, 0.05)[0], height=(2, 0.05)[1],
    ori=0, pos=(0, 1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
polygon11 = visual.Rect(
    win=win, name='polygon11',
    width=(2, 0.05)[0], height=(2, 0.05)[1],
    ori=0, pos=(0, -1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)

instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='default text',
    font='times new roman',
    pos=(0, 0), height=.08, wrapWidth=1.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "prestim"
prestimClock = core.Clock()

prestim_stimuli = visual.ImageStim(
    win=win, name='prestim_stimuli',
    image='singleblock.png', mask=None,
    ori=0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prestim_audiostimuli = sound.Sound('A', secs=-1, stereo=True)
prestim_audiostimuli.setVolume(1.0)
prestim_pause = visual.ImageStim(
    win=win, name='prestim_pause',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "trials"
trialsClock = core.Clock()

trials_stimuli = visual.ImageStim(
    win=win, name='trials_stimuli',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trials_audiostimuli = sound.Sound('A', secs=-1, stereo=True)
trials_audiostimuli.setVolume(1)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blockloop = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blockloop')
thisExp.addLoop(blockloop)  # add the loop to the experiment
thisBlockloop = blockloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
if thisBlockloop != None:
    for paramName in thisBlockloop:
        exec('{} = thisBlockloop[paramName]'.format(paramName))

for thisBlockloop in blockloop:
    currentLoop = blockloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
    if thisBlockloop != None:
        for paramName in thisBlockloop:
            exec('{} = thisBlockloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if back==0:
        back=1
    
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    polygon4.setAutoDraw(False)
    polygon5.setAutoDraw(False)
    polygon6.setAutoDraw(False)
    polygon7.setAutoDraw(False)
    polygon8.setAutoDraw(False)
    polygon9.setAutoDraw(False)
    polygon10.setAutoDraw(False)
    polygon11.setAutoDraw(False)
    
    (win.flip())
    
    instruction =('In each trial, you are now to press [SPACEBAR] on any trial '
        'in which the currently filled space is the SAME as the space that was '
        'filled {} trials back ({}-back task).').format(back, back)
    instructions_text.setText(instruction)
    instructions_keyresp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [instructions_text, instructions_keyresp]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instructions_text* updates
        if t >= 0.0 and instructions_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_text.tStart = t
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.setAutoDraw(True)
        
        # *instructions_keyresp* updates
        if t >= 0.0 and instructions_keyresp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_keyresp.tStart = t
            instructions_keyresp.frameNStart = frameN  # exact frame index
            instructions_keyresp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions_keyresp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prestimloop = data.TrialHandler(nReps=back, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='prestimloop')
    thisExp.addLoop(prestimloop)  # add the loop to the experiment
    thisPrestimloop = prestimloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrestimloop.rgb)
    if thisPrestimloop != None:
        for paramName in thisPrestimloop:
            exec('{} = thisPrestimloop[paramName]'.format(paramName))
    
    for thisPrestimloop in prestimloop:
        currentLoop = prestimloop
        # abbreviate parameter names if possible (e.g. rgb = thisPrestimloop.rgb)
        if thisPrestimloop != None:
            for paramName in thisPrestimloop:
                exec('{} = thisPrestimloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "prestim"-------
        t = 0
        prestimClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        polygon1.setAutoDraw(True)
        polygon2.setAutoDraw(True)
        polygon3.setAutoDraw(True)
        polygon4.setAutoDraw(True)
        polygon5.setAutoDraw(True)
        polygon6.setAutoDraw(True)
        polygon7.setAutoDraw(True)
        polygon8.setAutoDraw(True)
        polygon9.setAutoDraw(True)
        polygon10.setAutoDraw(True)
        polygon11.setAutoDraw(True)
        
        positions = [(-.75, .75), (-.25, .75), (.25, .75), (.75, .75),
            (-.75, .25), (-.25, .25), (.25, .25), (.75, .25),
            (-.75, -.25), (-.25, -.25), (.25, -.25), (.75, -.25), 
            (-.75, -.75), (-.25, -.75), (.25, -.75), (.75, -.75)]
        from random import choice
        position=choice(positions)
        
        sounds = [('A.wav'), ('B.wav'), ('C.wav'), ('D.wav'),
            ('E.wav'), ('F.wav'), ('G.wav'), ('H.wav'),
            ('I.wav'), ('J.wav'), ('K.wav'), ('L.wav'), 
            ('M.wav'), ('N.wav'), ('O.wav'), ('P.wav')]
            #('Q.wav'), ('R.wav'), ('S.wav'), ('T.wav'),
            #('U.wav'), ('V.wav'), ('X.wav'), ('Y.wav'),
            #('Z.wav')]
        from random import choice
        sound=choice(sounds)
        prestim_stimuli.setPos((position))
        prestim_audiostimuli.setSound(sound)
        prestim_audiostimuli.setVolume(1, log=False)
        # keep track of which components have finished
        prestimComponents = [prestim_stimuli, prestim_audiostimuli, prestim_pause]
        for thisComponent in prestimComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "prestim"-------
        while continueRoutine:
            # get current time
            t = prestimClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *prestim_stimuli* updates
            if t >= 0 and prestim_stimuli.status == NOT_STARTED:
                # keep track of start time/frame for later
                prestim_stimuli.tStart = t
                prestim_stimuli.frameNStart = frameN  # exact frame index
                prestim_stimuli.setAutoDraw(True)
            frameRemains = 0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if prestim_stimuli.status == STARTED and t >= frameRemains:
                prestim_stimuli.setAutoDraw(False)
            # start/stop prestim_audiostimuli
            if t >= .5 and prestim_audiostimuli.status == NOT_STARTED:
                # keep track of start time/frame for later
                prestim_audiostimuli.tStart = t
                prestim_audiostimuli.frameNStart = frameN  # exact frame index
                win.callOnFlip(prestim_audiostimuli.play)  # screen flip
            
            # *prestim_pause* updates
            if t >= 1 and prestim_pause.status == NOT_STARTED:
                # keep track of start time/frame for later
                prestim_pause.tStart = t
                prestim_pause.frameNStart = frameN  # exact frame index
                prestim_pause.setAutoDraw(True)
            frameRemains = 1 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if prestim_pause.status == STARTED and t >= frameRemains:
                prestim_pause.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prestimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prestim"-------
        for thisComponent in prestimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        eightback=sevenback
        sevenback=sixback
        sixback=fiveback
        fiveback=fourback
        fourback=threeback
        threeback=twoback
        twoback=oneback
        oneback=position
        
        audioeightback=audiosevenback
        audiosevenback=audiosixback
        audiosixback=audiofiveback
        audiofiveback=audiofourback
        audiofourback=audiothreeback
        audiothreeback=audiotwoback
        audiotwoback=audiooneback
        audiooneback=position
        
        prestim_audiostimuli.stop()  # ensure sound has stopped at end of routine
        # the Routine "prestim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed back repeats of 'prestimloop'
    
    
    # set up handler to look after randomisation of conditions etc
    trialsloop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.csv'),
        seed=None, name='trialsloop')
    thisExp.addLoop(trialsloop)  # add the loop to the experiment
    thisTrialsloop = trialsloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsloop.rgb)
    if thisTrialsloop != None:
        for paramName in thisTrialsloop:
            exec('{} = thisTrialsloop[paramName]'.format(paramName))
    
    for thisTrialsloop in trialsloop:
        currentLoop = trialsloop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsloop.rgb)
        if thisTrialsloop != None:
            for paramName in thisTrialsloop:
                exec('{} = thisTrialsloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trials"-------
        t = 0
        trialsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        if trialType=='Target':
            if back==8:
                position=eightback
            elif back==7:
                position=sevenback
            elif back==6:
                position=sixback
            elif back==5:
                position=fiveback
            elif back==4:
                position=fourback
            elif back==3:
                position=threeback
            elif back==2:
                position=twoback
            elif back==1:
                position=oneback
        
        elif trialType=='nonTarget':
            positions = [(-.75, .75), (-.25, .75), (.25, .75), (.75, .75),
            (-.75, .25), (-.25, .25), (.25, .25), (.75, .25),
            (-.75, -.25), (-.25, -.25), (.25, -.25), (.75, -.25), 
            (-.75, -.75), (-.25, -.75), (.25, -.75), (.75, -.75)]
            from random import choice
            position=choice(positions)
            if position==eightback and back==8:
                from random import choice
                position=choice(positions)
            elif position==sevenback and back==7:
                from random import choice
                position=choice(positions)
            elif position==sixback and back==6:
                from random import choice
                position=choice(positions)
            elif position==fiveback and back==5:
                from random import choice
                position=choice(positions)
            elif position==fourback and back==4:
                from random import choice
                position=choice(positions)
            elif position==threeback and back==3:
                from random import choice
                position=choice(positions)
            elif position==twoback and back==2:
                from random import choice
                position=choice(positions)
            elif position==oneback and back==1:
                from random import choice
                position=choice(positions)
        #double check that this random re-selection won't result in occasionally
        #producing a target trial despite a 'nonTarget' designation'
        
        if audiotrialType=='Target':
            if back==8:
                sound=audioeightback
            elif back==7:
                sound=audiosevenback
            elif back==6:
                sound=audiosixback
            elif back==5:
                sound=audiofiveback
            elif back==4:
                sound=audiofourback
            elif back==3:
                sound=audiothreeback
            elif back==2:
                sound=audiotwoback
            elif back==1:
                sound=audiooneback
        
        elif audiotrialType=='nonTarget':
            sounds = [('A.wav'), ('B.wav'), ('C.wav'), ('D.wav'),
            ('E.wav'), ('F.wav'), ('G.wav'), ('H.wav'),
            ('I.wav'), ('J.wav'), ('K.wav'), ('L.wav'), 
            ('M.wav'), ('N.wav'), ('O.wav'), ('P.wav')]
            #('Q.wav'), ('R.wav'), ('S.wav'), ('T.wav'),
            #('U.wav'), ('V.wav'), ('X.wav'), ('Y.wav'),
            #('Z.wav')]
            from random import choice
            sound=choice(sounds)
            if sound==audioeightback and back==8:
                from random import choice
                sound=choice(sounds)
            elif sound==audiosevenback and back==7:
                from random import choice
                sound=choice(sounds)
            elif sound==audiosixback and back==6:
                from random import choice
                sound=choice(sounds)
            elif sound==audiofiveback and back==5:
                from random import choice
                sound=choice(sounds)
            elif sound==audiofourback and back==4:
                from random import choice
                sound=choice(sounds)
            elif sound==audiothreeback and back==3:
                from random import choice
                sound=choice(sounds)
            elif sound==audiotwoback and back==2:
                from random import choice
                sound=choice(sounds)
            elif sound==audiooneback and back==1:
                from random import choice
                sound=choice(sounds)
        
        trials_stimuli.setOpacity(1)
        trials_stimuli.setPos((position))
        trials_stimuli.setSize((0.45, 0.45))
        trials_stimuli.setOri(0)
        trials_stimuli.setImage('singleblock.png')
        trials_keyresp = event.BuilderKeyResponse()
        trials_audiostimuli.setSound(sound)
        trials_audiostimuli.setVolume(1, log=False)
        trials_audiokeyresp = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        trialsComponents = [trials_stimuli, trials_keyresp, trials_audiostimuli, trials_audiokeyresp]
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trials"-------
        while continueRoutine:
            # get current time
            t = trialsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if trials_keyresp.corr:
                color = [1,-1,1]
            
            # *trials_stimuli* updates
            if t >= 0 and trials_stimuli.status == NOT_STARTED:
                # keep track of start time/frame for later
                trials_stimuli.tStart = t
                trials_stimuli.frameNStart = frameN  # exact frame index
                trials_stimuli.setAutoDraw(True)
            frameRemains = 0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trials_stimuli.status == STARTED and t >= frameRemains:
                trials_stimuli.setAutoDraw(False)
            if trials_stimuli.status == STARTED:  # only update if drawing
                trials_stimuli.setColor(color, colorSpace='rgb', log=False)
            
            # *trials_keyresp* updates
            if t >= 1 and trials_keyresp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trials_keyresp.tStart = t
                trials_keyresp.frameNStart = frameN  # exact frame index
                trials_keyresp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trials_keyresp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 1 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trials_keyresp.status == STARTED and t >= frameRemains:
                trials_keyresp.status = STOPPED
            if trials_keyresp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if trials_keyresp.keys == []:  # then this was the first keypress
                        trials_keyresp.keys = theseKeys[0]  # just the first key pressed
                        trials_keyresp.rt = trials_keyresp.clock.getTime()
                        # was this 'correct'?
                        if (trials_keyresp.keys == str(correctAns)) or (trials_keyresp.keys == correctAns):
                            trials_keyresp.corr = 1
                        else:
                            trials_keyresp.corr = 0
            # start/stop trials_audiostimuli
            if t >= 0.5 and trials_audiostimuli.status == NOT_STARTED:
                # keep track of start time/frame for later
                trials_audiostimuli.tStart = t
                trials_audiostimuli.frameNStart = frameN  # exact frame index
                win.callOnFlip(trials_audiostimuli.play)  # screen flip
            
            # *trials_audiokeyresp* updates
            if t >= 1 and trials_audiokeyresp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trials_audiokeyresp.tStart = t
                trials_audiokeyresp.frameNStart = frameN  # exact frame index
                trials_audiokeyresp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trials_audiokeyresp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 1 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trials_audiokeyresp.status == STARTED and t >= frameRemains:
                trials_audiokeyresp.status = STOPPED
            if trials_audiokeyresp.status == STARTED:
                theseKeys = event.getKeys(keyList=['right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if trials_audiokeyresp.keys == []:  # then this was the first keypress
                        trials_audiokeyresp.keys = theseKeys[0]  # just the first key pressed
                        trials_audiokeyresp.rt = trials_audiokeyresp.clock.getTime()
                        # was this 'correct'?
                        if (trials_audiokeyresp.keys == str(audiocorrectAns)) or (trials_audiokeyresp.keys == audiocorrectAns):
                            trials_audiokeyresp.corr = 1
                        else:
                            trials_audiokeyresp.corr = 0
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trials"-------
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        eightback=sevenback
        sevenback=sixback
        sixback=fiveback
        fiveback=fourback
        fourback=threeback
        threeback=twoback
        twoback=oneback
        oneback=position
        color = [1,1,1]
        
        audioeightback=audiosevenback
        audiosevenback=audiosixback
        audiosixback=audiofiveback
        audiofiveback=audiofourback
        audiofourback=audiothreeback
        audiothreeback=audiotwoback
        audiotwoback=audiooneback
        audiooneback=position
        
        
        
        # check responses
        if trials_keyresp.keys in ['', [], None]:  # No response was made
            trials_keyresp.keys=None
            # was no response the correct answer?!
            if str(correctAns).lower() == 'none':
               trials_keyresp.corr = 1;  # correct non-response
            else:
               trials_keyresp.corr = 0;  # failed to respond (incorrectly)
        # store data for trialsloop (TrialHandler)
        trialsloop.addData('trials_keyresp.keys',trials_keyresp.keys)
        trialsloop.addData('trials_keyresp.corr', trials_keyresp.corr)
        if trials_keyresp.keys != None:  # we had a response
            trialsloop.addData('trials_keyresp.rt', trials_keyresp.rt)
        trials_audiostimuli.stop()  # ensure sound has stopped at end of routine
        # check responses
        if trials_audiokeyresp.keys in ['', [], None]:  # No response was made
            trials_audiokeyresp.keys=None
            # was no response the correct answer?!
            if str(audiocorrectAns).lower() == 'none':
               trials_audiokeyresp.corr = 1;  # correct non-response
            else:
               trials_audiokeyresp.corr = 0;  # failed to respond (incorrectly)
        # store data for trialsloop (TrialHandler)
        trialsloop.addData('trials_audiokeyresp.keys',trials_audiokeyresp.keys)
        trialsloop.addData('trials_audiokeyresp.corr', trials_audiokeyresp.corr)
        if trials_audiokeyresp.keys != None:  # we had a response
            trialsloop.addData('trials_audiokeyresp.rt', trials_audiokeyresp.rt)
        if trials_keyresp.corr:
            corr.append(1)
        if trials_audiokeyresp.corr:
            audiocorr.append(1)
        # the Routine "trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsloop'
    
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
    if sum(corr) > 16 and sum(audiocorr) > 16:
        twobackmsg = '{} visual items correct and {} auditory items correct. TRIPLE KILL!!'.format(sum(corr), sum(audiocorr))
        twobackmovie = 'great job.gif'
        back=back+1
    elif sum(corr) > 12 and sum(audiocorr) > 12:
        twobackmsg = '{} visual items correct and {} auditory items correct. Not too shabby.'.format(sum(corr), sum(audiocorr))
        twobackmovie = 'great job.gif'
    else:
        twobackmsg = 'This is only a two-back task. You got {} visual and {} auditory items. Don\'t strain yourself.'.format(sum(corr), sum(audiocorr))
        twobackmovie = 'getsomehelp.gif'
        back=back-1
    
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    polygon4.setAutoDraw(False)
    polygon5.setAutoDraw(False)
    polygon6.setAutoDraw(False)
    polygon7.setAutoDraw(False)
    polygon8.setAutoDraw(False)
    polygon9.setAutoDraw(False)
    polygon10.setAutoDraw(False)
    polygon11.setAutoDraw(False)
    (win.flip())
    
    feedback_movie = visual.MovieStim3(
        win=win, name='feedback_movie',
        noAudio = True,
        filename=twobackmovie,
        ori=0, pos=(0, -.5), opacity=1,
        depth=-1.0,
        )
        # keep track of which components have finished
    text_3 = visual.TextStim(win=win, name='text_3',
        text=twobackmsg,
        font='times new roman',
        pos=(0, -.8), height=0.1, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', alignHoriz='center',
        depth=-1.0);
    
    feedbackComponents = [feedback_movie, text_3]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    
    # -------Start Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *feedback_movie* updates
        if t >= 0 and text_3.status == NOT_STARTED:
            text_3.setAutoDraw(True)
        # check if all components have finished
        if t >= 0.0 and feedback_movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_movie.setAutoDraw(True)
        if feedback_movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
            # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    corr = [0]
    audiocorr = [0]
    # keep track of which components have finished
    feedbackComponents = []
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'blockloop'






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
