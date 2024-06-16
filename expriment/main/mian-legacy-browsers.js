/************* 
 * Mian Test *
 *************/


// store info about the experiment session:
let expName = 'mian';  // from the Builder filename that created this script
let expInfo = {};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(GeneInstrRoutineBegin());
flowScheduler.add(GeneInstrRoutineEachFrame());
flowScheduler.add(GeneInstrRoutineEnd());
const returnPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(returnPracticeLoopBegin(returnPracticeLoopScheduler));
flowScheduler.add(returnPracticeLoopScheduler);
flowScheduler.add(returnPracticeLoopEnd);
flowScheduler.add(interRoutineBegin());
flowScheduler.add(interRoutineEachFrame());
flowScheduler.add(interRoutineEnd());
const NumBlock1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NumBlock1LoopBegin(NumBlock1LoopScheduler));
flowScheduler.add(NumBlock1LoopScheduler);
flowScheduler.add(NumBlock1LoopEnd);
flowScheduler.add(restNumRoutineBegin());
flowScheduler.add(restNumRoutineEachFrame());
flowScheduler.add(restNumRoutineEnd());
const NumBlock2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NumBlock2LoopBegin(NumBlock2LoopScheduler));
flowScheduler.add(NumBlock2LoopScheduler);
flowScheduler.add(NumBlock2LoopEnd);
const returnPracLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(returnPracLoopBegin(returnPracLoopScheduler));
flowScheduler.add(returnPracLoopScheduler);
flowScheduler.add(returnPracLoopEnd);
const AffBlocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AffBlocksLoopBegin(AffBlocksLoopScheduler));
flowScheduler.add(AffBlocksLoopScheduler);
flowScheduler.add(AffBlocksLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'pic/NumInstr.png', 'path': 'pic/NumInstr.png'},
    {'name': 'pic/NumRest.png', 'path': 'pic/NumRest.png'},
    {'name': 'NumPractise.xlsx', 'path': 'NumPractise.xlsx'},
    {'name': 'pic/AffEndPrac.png', 'path': 'pic/AffEndPrac.png'},
    {'name': 'AFFPrac.xlsx', 'path': 'AFFPrac.xlsx'},
    {'name': 'pic/GenInstr.png', 'path': 'pic/GenInstr.png'},
    {'name': 'pic/AffRest2.png', 'path': 'pic/AffRest2.png'},
    {'name': 'pic/AffRest1.png', 'path': 'pic/AffRest1.png'},
    {'name': 'pic/flanker4.png', 'path': 'pic/flanker4.png'},
    {'name': 'pic/AffRest3.png', 'path': 'pic/AffRest3.png'},
    {'name': 'frame.png', 'path': 'frame.png'},
    {'name': 'pic/flanker3.png', 'path': 'pic/flanker3.png'},
    {'name': 'AFFcon.xlsx', 'path': 'AFFcon.xlsx'},
    {'name': 'pic/flanker6.png', 'path': 'pic/flanker6.png'},
    {'name': 'pic/NumEndPrac.png', 'path': 'pic/NumEndPrac.png'},
    {'name': 'pic/EndExp.png', 'path': 'pic/EndExp.png'},
    {'name': 'pic/flanker2.png', 'path': 'pic/flanker2.png'},
    {'name': 'AffLoop.xlsx', 'path': 'AffLoop.xlsx'},
    {'name': 'NumCon.xlsx', 'path': 'NumCon.xlsx'},
    {'name': 'pic/flanker5.png', 'path': 'pic/flanker5.png'},
    {'name': 'pic/AffInstr.png', 'path': 'pic/AffInstr.png'},
    {'name': 'pic/flanker1.png', 'path': 'pic/flanker1.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var GeneInstrClock;
var GeneInstr_p;
var key_resp;
var instrNumClock;
var Numinstr_p;
var respNumPrac;
var num2WordClock;
var frame;
var stimulus;
var respNum2word;
var feedbackClock;
var frame2;
var textFBNum;
var endPracNumClock;
var NumEndPrac;
var respEndNumP;
var interClock;
var frame3;
var restNumClock;
var NumRest;
var respRest;
var AffInstrClock;
var AffInsr_P;
var respAffInstr;
var intervalsClock;
var times;
var text;
var blank;
var AFF_S1Clock;
var flanker_p;
var target_p;
var respFlanker;
var AFF_S2Clock;
var positiveWords;
var negativeWords;
var AffWord;
var respAffWord;
var endPracAffClock;
var endPracA_p;
var respEndPracA;
var restAffClock;
var AffRest;
var respRest_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "GeneInstr"
  GeneInstrClock = new util.Clock();
  GeneInstr_p = new visual.ImageStim({
    win : psychoJS.window,
    name : 'GeneInstr_p', units : undefined, 
    image : 'pic/GenInstr.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrNum"
  instrNumClock = new util.Clock();
  Numinstr_p = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Numinstr_p', units : undefined, 
    image : 'pic/NumInstr.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  respNumPrac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "num2Word"
  num2WordClock = new util.Clock();
  frame = new visual.ImageStim({
    win : psychoJS.window,
    name : 'frame', units : undefined, 
    image : 'frame.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 1.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  stimulus = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimulus',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  respNum2word = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  frame2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'frame2', units : undefined, 
    image : 'frame.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 1.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  textFBNum = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFBNum',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "endPracNum"
  endPracNumClock = new util.Clock();
  NumEndPrac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'NumEndPrac', units : undefined, 
    image : 'pic/NumEndPrac.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  respEndNumP = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "inter"
  interClock = new util.Clock();
  frame3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'frame3', units : undefined, 
    image : 'frame.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 1.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "restNum"
  restNumClock = new util.Clock();
  NumRest = new visual.ImageStim({
    win : psychoJS.window,
    name : 'NumRest', units : undefined, 
    image : 'pic/NumRest.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  respRest = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AffInstr"
  AffInstrClock = new util.Clock();
  AffInsr_P = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AffInsr_P', units : undefined, 
    image : 'pic/AffInstr.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  respAffInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intervals"
  intervalsClock = new util.Clock();
  times = [0.3, 0.5, 0.4, 0.35, 0.45];
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '+',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.6,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AFF_S1"
  AFF_S1Clock = new util.Clock();
  flanker_p = new visual.ImageStim({
    win : psychoJS.window,
    name : 'flanker_p', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.8],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  target_p = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_p', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.8],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  respFlanker = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AFF_S2"
  AFF_S2Clock = new util.Clock();
  positiveWords = ["\u7545\u9500", "\u8bda\u6073", "\u5145\u88d5", "\u5178\u96c5", "\u4e30\u6ee1", "\u5949\u732e", "\u5bcc\u4e3d", "\u5bcc\u8db3", "\u516c\u5e73", "\u7470\u4e3d", "\u8c6a\u653e", "\u5409\u7965", "\u7cbe\u81f4", "\u656c\u4f69", "\u4fca\u79c0", "\u5ec9\u6d01", "\u7559\u604b", "\u524d\u8fdb", "\u6e05\u79c0", "\u70ed\u5207", "\u5982\u613f", "\u751f\u52a8", "\u5723\u6d01", "\u8212\u7545", "\u723d\u6717", "\u987d\u5f3a", "\u65fa\u76db", "\u9c9c\u8273", "\u7fa1\u6155", "\u4eab\u53d7", "\u96c4\u539a", "\u79c0\u4e3d", "\u6c38\u6052", "\u4f18\u96c5", "\u6709\u5229", "\u8d5e\u6210", "\u73cd\u85cf", "\u632f\u4f5c", "\u6b63\u76f4", "\u5353\u8d8a"];
  negativeWords = ["\u60b2\u89c2", "\u522b\u626d", "\u5632\u7b11", "\u5904\u7f5a", "\u4e22\u5931", "\u5835\u585e", "\u7f5a\u6b3e", "\u70e6\u607c", "\u5b64\u5355", "\u9ed1\u6697", "\u80e1\u6d82", "\u6000\u7591", "\u614c\u5fd9", "\u5047\u5192", "\u7126\u8e81", "\u7981\u6b62", "\u6cae\u4e27", "\u61d2\u60f0", "\u6d6a\u8d39", "\u51b7\u7b11", "\u9c81\u83bd", "\u843d\u540e", "\u95f7\u70ed", "\u6392\u65a5", "\u8f7b\u7387", "\u7a77\u82e6", "\u7f3a\u4e4f", "\u6492\u8c0e", "\u4f24\u5fc3", "\u5931\u610f", "\u635f\u5bb3", "\u9003\u907f", "\u6d88\u6c89", "\u5fc3\u614c", "\u538c\u6076", "\u5fe7\u8651", "\u90c1\u95f7", "\u6742\u4e71", "\u4e89\u5435", "\u81ea\u5351"];
  
  var thisWord, fixTime
  
  Array.prototype.removeByValue = function (val) {
    for (var i = 0; i < this.length; i++) {
      if (this[i] === val) {
        this.splice(i, 1);
        i--;
      }
    }
    return this;
  }
  AffWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'AffWord',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  respAffWord = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "endPracAff"
  endPracAffClock = new util.Clock();
  endPracA_p = new visual.ImageStim({
    win : psychoJS.window,
    name : 'endPracA_p', units : undefined, 
    image : 'pic/AffEndPrac.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  respEndPracA = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "restAff"
  restAffClock = new util.Clock();
  AffRest = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AffRest', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.33, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  respRest_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var GeneInstrComponents;
function GeneInstrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'GeneInstr'-------
    t = 0;
    GeneInstrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    GeneInstrComponents = [];
    GeneInstrComponents.push(GeneInstr_p);
    GeneInstrComponents.push(key_resp);
    
    GeneInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function GeneInstrRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'GeneInstr'-------
    // get current time
    t = GeneInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *GeneInstr_p* updates
    if (t >= 0.0 && GeneInstr_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GeneInstr_p.tStart = t;  // (not accounting for frame time here)
      GeneInstr_p.frameNStart = frameN;  // exact frame index
      
      GeneInstr_p.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    GeneInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GeneInstrRoutineEnd() {
  return async function () {
    //------Ending Routine 'GeneInstr'-------
    GeneInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp.stop();
    // the Routine "GeneInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var returnPractice;
var currentLoop;
function returnPracticeLoopBegin(returnPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    returnPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 99, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'returnPractice'
    });
    psychoJS.experiment.addLoop(returnPractice); // add the loop to the experiment
    currentLoop = returnPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    returnPractice.forEach(function() {
      const snapshot = returnPractice.getSnapshot();
    
      returnPracticeLoopScheduler.add(importConditions(snapshot));
      returnPracticeLoopScheduler.add(instrNumRoutineBegin(snapshot));
      returnPracticeLoopScheduler.add(instrNumRoutineEachFrame());
      returnPracticeLoopScheduler.add(instrNumRoutineEnd());
      const pracNumLoopScheduler = new Scheduler(psychoJS);
      returnPracticeLoopScheduler.add(pracNumLoopBegin(pracNumLoopScheduler, snapshot));
      returnPracticeLoopScheduler.add(pracNumLoopScheduler);
      returnPracticeLoopScheduler.add(pracNumLoopEnd);
      returnPracticeLoopScheduler.add(endPracNumRoutineBegin(snapshot));
      returnPracticeLoopScheduler.add(endPracNumRoutineEachFrame());
      returnPracticeLoopScheduler.add(endPracNumRoutineEnd());
      returnPracticeLoopScheduler.add(endLoopIteration(returnPracticeLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var pracNum;
function pracNumLoopBegin(pracNumLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pracNum = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'NumPractise.xlsx',
      seed: undefined, name: 'pracNum'
    });
    psychoJS.experiment.addLoop(pracNum); // add the loop to the experiment
    currentLoop = pracNum;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    pracNum.forEach(function() {
      const snapshot = pracNum.getSnapshot();
    
      pracNumLoopScheduler.add(importConditions(snapshot));
      pracNumLoopScheduler.add(num2WordRoutineBegin(snapshot));
      pracNumLoopScheduler.add(num2WordRoutineEachFrame());
      pracNumLoopScheduler.add(num2WordRoutineEnd());
      pracNumLoopScheduler.add(feedbackRoutineBegin(snapshot));
      pracNumLoopScheduler.add(feedbackRoutineEachFrame());
      pracNumLoopScheduler.add(feedbackRoutineEnd());
      pracNumLoopScheduler.add(endLoopIteration(pracNumLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function pracNumLoopEnd() {
  psychoJS.experiment.removeLoop(pracNum);

  return Scheduler.Event.NEXT;
}


async function returnPracticeLoopEnd() {
  psychoJS.experiment.removeLoop(returnPractice);

  return Scheduler.Event.NEXT;
}


var NumBlock1;
function NumBlock1LoopBegin(NumBlock1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    NumBlock1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'NumCon.xlsx', '0:80'),
      seed: undefined, name: 'NumBlock1'
    });
    psychoJS.experiment.addLoop(NumBlock1); // add the loop to the experiment
    currentLoop = NumBlock1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    NumBlock1.forEach(function() {
      const snapshot = NumBlock1.getSnapshot();
    
      NumBlock1LoopScheduler.add(importConditions(snapshot));
      NumBlock1LoopScheduler.add(num2WordRoutineBegin(snapshot));
      NumBlock1LoopScheduler.add(num2WordRoutineEachFrame());
      NumBlock1LoopScheduler.add(num2WordRoutineEnd());
      NumBlock1LoopScheduler.add(endLoopIteration(NumBlock1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function NumBlock1LoopEnd() {
  psychoJS.experiment.removeLoop(NumBlock1);

  return Scheduler.Event.NEXT;
}


var NumBlock2;
function NumBlock2LoopBegin(NumBlock2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    NumBlock2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'NumCon.xlsx', '80:160'),
      seed: undefined, name: 'NumBlock2'
    });
    psychoJS.experiment.addLoop(NumBlock2); // add the loop to the experiment
    currentLoop = NumBlock2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    NumBlock2.forEach(function() {
      const snapshot = NumBlock2.getSnapshot();
    
      NumBlock2LoopScheduler.add(importConditions(snapshot));
      NumBlock2LoopScheduler.add(num2WordRoutineBegin(snapshot));
      NumBlock2LoopScheduler.add(num2WordRoutineEachFrame());
      NumBlock2LoopScheduler.add(num2WordRoutineEnd());
      NumBlock2LoopScheduler.add(endLoopIteration(NumBlock2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function NumBlock2LoopEnd() {
  psychoJS.experiment.removeLoop(NumBlock2);

  return Scheduler.Event.NEXT;
}


var returnPrac;
function returnPracLoopBegin(returnPracLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    returnPrac = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 99, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'returnPrac'
    });
    psychoJS.experiment.addLoop(returnPrac); // add the loop to the experiment
    currentLoop = returnPrac;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    returnPrac.forEach(function() {
      const snapshot = returnPrac.getSnapshot();
    
      returnPracLoopScheduler.add(importConditions(snapshot));
      returnPracLoopScheduler.add(AffInstrRoutineBegin(snapshot));
      returnPracLoopScheduler.add(AffInstrRoutineEachFrame());
      returnPracLoopScheduler.add(AffInstrRoutineEnd());
      const PracAffLoopScheduler = new Scheduler(psychoJS);
      returnPracLoopScheduler.add(PracAffLoopBegin(PracAffLoopScheduler, snapshot));
      returnPracLoopScheduler.add(PracAffLoopScheduler);
      returnPracLoopScheduler.add(PracAffLoopEnd);
      returnPracLoopScheduler.add(endPracAffRoutineBegin(snapshot));
      returnPracLoopScheduler.add(endPracAffRoutineEachFrame());
      returnPracLoopScheduler.add(endPracAffRoutineEnd());
      returnPracLoopScheduler.add(endLoopIteration(returnPracLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var PracAff;
function PracAffLoopBegin(PracAffLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PracAff = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'AFFPrac.xlsx',
      seed: undefined, name: 'PracAff'
    });
    psychoJS.experiment.addLoop(PracAff); // add the loop to the experiment
    currentLoop = PracAff;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    PracAff.forEach(function() {
      const snapshot = PracAff.getSnapshot();
    
      PracAffLoopScheduler.add(importConditions(snapshot));
      PracAffLoopScheduler.add(intervalsRoutineBegin(snapshot));
      PracAffLoopScheduler.add(intervalsRoutineEachFrame());
      PracAffLoopScheduler.add(intervalsRoutineEnd());
      PracAffLoopScheduler.add(AFF_S1RoutineBegin(snapshot));
      PracAffLoopScheduler.add(AFF_S1RoutineEachFrame());
      PracAffLoopScheduler.add(AFF_S1RoutineEnd());
      PracAffLoopScheduler.add(AFF_S2RoutineBegin(snapshot));
      PracAffLoopScheduler.add(AFF_S2RoutineEachFrame());
      PracAffLoopScheduler.add(AFF_S2RoutineEnd());
      PracAffLoopScheduler.add(endLoopIteration(PracAffLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function PracAffLoopEnd() {
  psychoJS.experiment.removeLoop(PracAff);

  return Scheduler.Event.NEXT;
}


async function returnPracLoopEnd() {
  psychoJS.experiment.removeLoop(returnPrac);

  return Scheduler.Event.NEXT;
}


var AffBlocks;
function AffBlocksLoopBegin(AffBlocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    AffBlocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'AffLoop.xlsx',
      seed: undefined, name: 'AffBlocks'
    });
    psychoJS.experiment.addLoop(AffBlocks); // add the loop to the experiment
    currentLoop = AffBlocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    AffBlocks.forEach(function() {
      const snapshot = AffBlocks.getSnapshot();
    
      AffBlocksLoopScheduler.add(importConditions(snapshot));
      const AffBlock1LoopScheduler = new Scheduler(psychoJS);
      AffBlocksLoopScheduler.add(AffBlock1LoopBegin(AffBlock1LoopScheduler, snapshot));
      AffBlocksLoopScheduler.add(AffBlock1LoopScheduler);
      AffBlocksLoopScheduler.add(AffBlock1LoopEnd);
      AffBlocksLoopScheduler.add(restAffRoutineBegin(snapshot));
      AffBlocksLoopScheduler.add(restAffRoutineEachFrame());
      AffBlocksLoopScheduler.add(restAffRoutineEnd());
      AffBlocksLoopScheduler.add(endLoopIteration(AffBlocksLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var AffBlock1;
function AffBlock1LoopBegin(AffBlock1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    AffBlock1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'AFFcon.xlsx',
      seed: undefined, name: 'AffBlock1'
    });
    psychoJS.experiment.addLoop(AffBlock1); // add the loop to the experiment
    currentLoop = AffBlock1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    AffBlock1.forEach(function() {
      const snapshot = AffBlock1.getSnapshot();
    
      AffBlock1LoopScheduler.add(importConditions(snapshot));
      AffBlock1LoopScheduler.add(intervalsRoutineBegin(snapshot));
      AffBlock1LoopScheduler.add(intervalsRoutineEachFrame());
      AffBlock1LoopScheduler.add(intervalsRoutineEnd());
      AffBlock1LoopScheduler.add(AFF_S1RoutineBegin(snapshot));
      AffBlock1LoopScheduler.add(AFF_S1RoutineEachFrame());
      AffBlock1LoopScheduler.add(AFF_S1RoutineEnd());
      AffBlock1LoopScheduler.add(AFF_S2RoutineBegin(snapshot));
      AffBlock1LoopScheduler.add(AFF_S2RoutineEachFrame());
      AffBlock1LoopScheduler.add(AFF_S2RoutineEnd());
      AffBlock1LoopScheduler.add(endLoopIteration(AffBlock1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function AffBlock1LoopEnd() {
  psychoJS.experiment.removeLoop(AffBlock1);

  return Scheduler.Event.NEXT;
}


async function AffBlocksLoopEnd() {
  psychoJS.experiment.removeLoop(AffBlocks);

  return Scheduler.Event.NEXT;
}


var _respNumPrac_allKeys;
var instrNumComponents;
function instrNumRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instrNum'-------
    t = 0;
    instrNumClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respNumPrac.keys = undefined;
    respNumPrac.rt = undefined;
    _respNumPrac_allKeys = [];
    // keep track of which components have finished
    instrNumComponents = [];
    instrNumComponents.push(Numinstr_p);
    instrNumComponents.push(respNumPrac);
    
    instrNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrNumRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instrNum'-------
    // get current time
    t = instrNumClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Numinstr_p* updates
    if (t >= 0.0 && Numinstr_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Numinstr_p.tStart = t;  // (not accounting for frame time here)
      Numinstr_p.frameNStart = frameN;  // exact frame index
      
      Numinstr_p.setAutoDraw(true);
    }

    
    // *respNumPrac* updates
    if (t >= 0.0 && respNumPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respNumPrac.tStart = t;  // (not accounting for frame time here)
      respNumPrac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respNumPrac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respNumPrac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respNumPrac.clearEvents(); });
    }

    if (respNumPrac.status === PsychoJS.Status.STARTED) {
      let theseKeys = respNumPrac.getKeys({keyList: ['space'], waitRelease: false});
      _respNumPrac_allKeys = _respNumPrac_allKeys.concat(theseKeys);
      if (_respNumPrac_allKeys.length > 0) {
        respNumPrac.keys = _respNumPrac_allKeys[_respNumPrac_allKeys.length - 1].name;  // just the last key pressed
        respNumPrac.rt = _respNumPrac_allKeys[_respNumPrac_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrNumRoutineEnd() {
  return async function () {
    //------Ending Routine 'instrNum'-------
    instrNumComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    respNumPrac.stop();
    // the Routine "instrNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respNum2word_allKeys;
var num2WordComponents;
function num2WordRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'num2Word'-------
    t = 0;
    num2WordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    stimulus.setPos(Position);
    stimulus.setText(target);
    respNum2word.keys = undefined;
    respNum2word.rt = undefined;
    _respNum2word_allKeys = [];
    // keep track of which components have finished
    num2WordComponents = [];
    num2WordComponents.push(frame);
    num2WordComponents.push(stimulus);
    num2WordComponents.push(respNum2word);
    
    num2WordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function num2WordRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'num2Word'-------
    // get current time
    t = num2WordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *frame* updates
    if (t >= 0 && frame.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame.tStart = t;  // (not accounting for frame time here)
      frame.frameNStart = frameN;  // exact frame index
      
      frame.setAutoDraw(true);
    }

    frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (frame.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      frame.setAutoDraw(false);
    }
    
    // *stimulus* updates
    if (t >= 0.5 && stimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulus.tStart = t;  // (not accounting for frame time here)
      stimulus.frameNStart = frameN;  // exact frame index
      
      stimulus.setAutoDraw(true);
    }

    frameRemains = 0.5 + 4.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stimulus.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimulus.setAutoDraw(false);
    }
    
    // *respNum2word* updates
    if (t >= 0.5 && respNum2word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respNum2word.tStart = t;  // (not accounting for frame time here)
      respNum2word.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respNum2word.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respNum2word.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respNum2word.clearEvents(); });
    }

    frameRemains = 0.5 + 4.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (respNum2word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      respNum2word.status = PsychoJS.Status.FINISHED;
  }

    if (respNum2word.status === PsychoJS.Status.STARTED) {
      let theseKeys = respNum2word.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _respNum2word_allKeys = _respNum2word_allKeys.concat(theseKeys);
      if (_respNum2word_allKeys.length > 0) {
        respNum2word.keys = _respNum2word_allKeys[_respNum2word_allKeys.length - 1].name;  // just the last key pressed
        respNum2word.rt = _respNum2word_allKeys[_respNum2word_allKeys.length - 1].rt;
        // was this correct?
        if (respNum2word.keys == CorAns) {
            respNum2word.corr = 1;
        } else {
            respNum2word.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    num2WordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feedbacktext;
var feedbackcolor;
function num2WordRoutineEnd() {
  return async function () {
    //------Ending Routine 'num2Word'-------
    num2WordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (respNum2word.keys === undefined) {
      if (['None','none',undefined].includes(CorAns)) {
         respNum2word.corr = 1;  // correct non-response
      } else {
         respNum2word.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('respNum2word.keys', respNum2word.keys);
    psychoJS.experiment.addData('respNum2word.corr', respNum2word.corr);
    if (typeof respNum2word.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respNum2word.rt', respNum2word.rt);
        routineTimer.reset();
        }
    
    respNum2word.stop();
    if (respNum2word.corr) {
        feedbacktext = "\u221a";
        feedbackcolor = "green";
    } else {
        feedbacktext = "\u00d7";
        feedbackcolor = "red";
    }
    
    return Scheduler.Event.NEXT;
  };
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    textFBNum.setColor(new util.Color(feedbackcolor));
    textFBNum.setPos(Position);
    textFBNum.setText(feedbacktext);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(frame2);
    feedbackComponents.push(textFBNum);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *frame2* updates
    if (t >= 0 && frame2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame2.tStart = t;  // (not accounting for frame time here)
      frame2.frameNStart = frameN;  // exact frame index
      
      frame2.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (frame2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      frame2.setAutoDraw(false);
    }
    
    // *textFBNum* updates
    if (t >= 0.0 && textFBNum.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textFBNum.tStart = t;  // (not accounting for frame time here)
      textFBNum.frameNStart = frameN;  // exact frame index
      
      textFBNum.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textFBNum.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textFBNum.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd() {
  return async function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _respEndNumP_allKeys;
var endPracNumComponents;
function endPracNumRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'endPracNum'-------
    t = 0;
    endPracNumClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respEndNumP.keys = undefined;
    respEndNumP.rt = undefined;
    _respEndNumP_allKeys = [];
    // keep track of which components have finished
    endPracNumComponents = [];
    endPracNumComponents.push(NumEndPrac);
    endPracNumComponents.push(respEndNumP);
    
    endPracNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endPracNumRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'endPracNum'-------
    // get current time
    t = endPracNumClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NumEndPrac* updates
    if (t >= 0.0 && NumEndPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NumEndPrac.tStart = t;  // (not accounting for frame time here)
      NumEndPrac.frameNStart = frameN;  // exact frame index
      
      NumEndPrac.setAutoDraw(true);
    }

    
    // *respEndNumP* updates
    if (t >= 0.0 && respEndNumP.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respEndNumP.tStart = t;  // (not accounting for frame time here)
      respEndNumP.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respEndNumP.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respEndNumP.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respEndNumP.clearEvents(); });
    }

    if (respEndNumP.status === PsychoJS.Status.STARTED) {
      let theseKeys = respEndNumP.getKeys({keyList: ['q', 'p'], waitRelease: false});
      _respEndNumP_allKeys = _respEndNumP_allKeys.concat(theseKeys);
      if (_respEndNumP_allKeys.length > 0) {
        respEndNumP.keys = _respEndNumP_allKeys[_respEndNumP_allKeys.length - 1].name;  // just the last key pressed
        respEndNumP.rt = _respEndNumP_allKeys[_respEndNumP_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endPracNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endPracNumRoutineEnd() {
  return async function () {
    //------Ending Routine 'endPracNum'-------
    endPracNumComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    respEndNumP.stop();
    if ((respEndNumP.keys === "p")) {
        returnPractice.finished = true;
    } else {
        returnPractice.finished = false;
    }
    
    // the Routine "endPracNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var interComponents;
function interRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'inter'-------
    t = 0;
    interClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    interComponents = [];
    interComponents.push(frame3);
    
    interComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function interRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'inter'-------
    // get current time
    t = interClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *frame3* updates
    if (t >= 0.0 && frame3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame3.tStart = t;  // (not accounting for frame time here)
      frame3.frameNStart = frameN;  // exact frame index
      
      frame3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (frame3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      frame3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    interComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function interRoutineEnd() {
  return async function () {
    //------Ending Routine 'inter'-------
    interComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _respRest_allKeys;
var restNumComponents;
function restNumRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'restNum'-------
    t = 0;
    restNumClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respRest.keys = undefined;
    respRest.rt = undefined;
    _respRest_allKeys = [];
    // keep track of which components have finished
    restNumComponents = [];
    restNumComponents.push(NumRest);
    restNumComponents.push(respRest);
    
    restNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restNumRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'restNum'-------
    // get current time
    t = restNumClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NumRest* updates
    if (t >= 0.0 && NumRest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NumRest.tStart = t;  // (not accounting for frame time here)
      NumRest.frameNStart = frameN;  // exact frame index
      
      NumRest.setAutoDraw(true);
    }

    
    // *respRest* updates
    if (t >= 0.0 && respRest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respRest.tStart = t;  // (not accounting for frame time here)
      respRest.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respRest.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respRest.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respRest.clearEvents(); });
    }

    if (respRest.status === PsychoJS.Status.STARTED) {
      let theseKeys = respRest.getKeys({keyList: ['space'], waitRelease: false});
      _respRest_allKeys = _respRest_allKeys.concat(theseKeys);
      if (_respRest_allKeys.length > 0) {
        respRest.keys = _respRest_allKeys[_respRest_allKeys.length - 1].name;  // just the last key pressed
        respRest.rt = _respRest_allKeys[_respRest_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restNumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restNumRoutineEnd() {
  return async function () {
    //------Ending Routine 'restNum'-------
    restNumComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    respRest.stop();
    // the Routine "restNum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respAffInstr_allKeys;
var AffInstrComponents;
function AffInstrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'AffInstr'-------
    t = 0;
    AffInstrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respAffInstr.keys = undefined;
    respAffInstr.rt = undefined;
    _respAffInstr_allKeys = [];
    // keep track of which components have finished
    AffInstrComponents = [];
    AffInstrComponents.push(AffInsr_P);
    AffInstrComponents.push(respAffInstr);
    
    AffInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AffInstrRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'AffInstr'-------
    // get current time
    t = AffInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AffInsr_P* updates
    if (t >= 0.0 && AffInsr_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AffInsr_P.tStart = t;  // (not accounting for frame time here)
      AffInsr_P.frameNStart = frameN;  // exact frame index
      
      AffInsr_P.setAutoDraw(true);
    }

    
    // *respAffInstr* updates
    if (t >= 0.0 && respAffInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respAffInstr.tStart = t;  // (not accounting for frame time here)
      respAffInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respAffInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respAffInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respAffInstr.clearEvents(); });
    }

    if (respAffInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = respAffInstr.getKeys({keyList: ['space'], waitRelease: false});
      _respAffInstr_allKeys = _respAffInstr_allKeys.concat(theseKeys);
      if (_respAffInstr_allKeys.length > 0) {
        respAffInstr.keys = _respAffInstr_allKeys[_respAffInstr_allKeys.length - 1].name;  // just the last key pressed
        respAffInstr.rt = _respAffInstr_allKeys[_respAffInstr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AffInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AffInstrRoutineEnd() {
  return async function () {
    //------Ending Routine 'AffInstr'-------
    AffInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    respAffInstr.stop();
    // the Routine "AffInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixTime;
var intervalsComponents;
function intervalsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intervals'-------
    t = 0;
    intervalsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    fixTime = Math.random(times);
    // keep track of which components have finished
    intervalsComponents = [];
    intervalsComponents.push(text);
    intervalsComponents.push(blank);
    
    intervalsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function intervalsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intervals'-------
    // get current time
    t = intervalsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 1.2 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 1.2 + fixTime - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *blank* updates
    if (t >= 0.0 && blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank.tStart = t;  // (not accounting for frame time here)
      blank.frameNStart = frameN;  // exact frame index
      
      blank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    intervalsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intervalsRoutineEnd() {
  return async function () {
    //------Ending Routine 'intervals'-------
    intervalsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "intervals" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respFlanker_allKeys;
var AFF_S1Components;
function AFF_S1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'AFF_S1'-------
    t = 0;
    AFF_S1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.700000);
    // update component parameters for each repeat
    flanker_p.setImage(flankerPic);
    target_p.setImage(targetPic);
    respFlanker.keys = undefined;
    respFlanker.rt = undefined;
    _respFlanker_allKeys = [];
    // keep track of which components have finished
    AFF_S1Components = [];
    AFF_S1Components.push(flanker_p);
    AFF_S1Components.push(target_p);
    AFF_S1Components.push(respFlanker);
    
    AFF_S1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AFF_S1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'AFF_S1'-------
    // get current time
    t = AFF_S1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *flanker_p* updates
    if (t >= 0.0 && flanker_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      flanker_p.tStart = t;  // (not accounting for frame time here)
      flanker_p.frameNStart = frameN;  // exact frame index
      
      flanker_p.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (flanker_p.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      flanker_p.setAutoDraw(false);
    }
    
    // *target_p* updates
    if (t >= 0.2 && target_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_p.tStart = t;  // (not accounting for frame time here)
      target_p.frameNStart = frameN;  // exact frame index
      
      target_p.setAutoDraw(true);
    }

    frameRemains = 0.2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_p.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_p.setAutoDraw(false);
    }
    
    // *respFlanker* updates
    if (t >= 0.2 && respFlanker.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respFlanker.tStart = t;  // (not accounting for frame time here)
      respFlanker.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respFlanker.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respFlanker.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respFlanker.clearEvents(); });
    }

    frameRemains = 0.2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (respFlanker.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      respFlanker.status = PsychoJS.Status.FINISHED;
  }

    if (respFlanker.status === PsychoJS.Status.STARTED) {
      let theseKeys = respFlanker.getKeys({keyList: ['a', 's'], waitRelease: false});
      _respFlanker_allKeys = _respFlanker_allKeys.concat(theseKeys);
      if (_respFlanker_allKeys.length > 0) {
        respFlanker.keys = _respFlanker_allKeys[_respFlanker_allKeys.length - 1].name;  // just the last key pressed
        respFlanker.rt = _respFlanker_allKeys[_respFlanker_allKeys.length - 1].rt;
        // was this correct?
        if (respFlanker.keys == corAnsF) {
            respFlanker.corr = 1;
        } else {
            respFlanker.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AFF_S1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AFF_S1RoutineEnd() {
  return async function () {
    //------Ending Routine 'AFF_S1'-------
    AFF_S1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (respFlanker.keys === undefined) {
      if (['None','none',undefined].includes(corAnsF)) {
         respFlanker.corr = 1;  // correct non-response
      } else {
         respFlanker.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('respFlanker.keys', respFlanker.keys);
    psychoJS.experiment.addData('respFlanker.corr', respFlanker.corr);
    if (typeof respFlanker.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respFlanker.rt', respFlanker.rt);
        routineTimer.reset();
        }
    
    respFlanker.stop();
    return Scheduler.Event.NEXT;
  };
}


var thisWord;
var _respAffWord_allKeys;
var AFF_S2Components;
function AFF_S2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'AFF_S2'-------
    t = 0;
    AFF_S2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    if ((AffValue === 1)) {
        thisWord = positiveWords[Math.floor(Math.random() * positiveWords.length)];
        positiveWords.removeByValue(thisWord);
    } else {
        thisWord = negativeWords[Math.floor(Math.random() * negativeWords.length)];
        negativeWords.removeByValue(thisWord);
    }
    AffWord.setText(thisWord);
    respAffWord.keys = undefined;
    respAffWord.rt = undefined;
    _respAffWord_allKeys = [];
    // keep track of which components have finished
    AFF_S2Components = [];
    AFF_S2Components.push(AffWord);
    AFF_S2Components.push(respAffWord);
    
    AFF_S2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AFF_S2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'AFF_S2'-------
    // get current time
    t = AFF_S2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AffWord* updates
    if (t >= 0.0 && AffWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AffWord.tStart = t;  // (not accounting for frame time here)
      AffWord.frameNStart = frameN;  // exact frame index
      
      AffWord.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AffWord.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AffWord.setAutoDraw(false);
    }
    
    // *respAffWord* updates
    if (t >= 0.0 && respAffWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respAffWord.tStart = t;  // (not accounting for frame time here)
      respAffWord.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respAffWord.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respAffWord.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respAffWord.clearEvents(); });
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (respAffWord.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      respAffWord.status = PsychoJS.Status.FINISHED;
  }

    if (respAffWord.status === PsychoJS.Status.STARTED) {
      let theseKeys = respAffWord.getKeys({keyList: ['l', 'k'], waitRelease: false});
      _respAffWord_allKeys = _respAffWord_allKeys.concat(theseKeys);
      if (_respAffWord_allKeys.length > 0) {
        respAffWord.keys = _respAffWord_allKeys[_respAffWord_allKeys.length - 1].name;  // just the last key pressed
        respAffWord.rt = _respAffWord_allKeys[_respAffWord_allKeys.length - 1].rt;
        // was this correct?
        if (respAffWord.keys == corAnsA) {
            respAffWord.corr = 1;
        } else {
            respAffWord.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AFF_S2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AFF_S2RoutineEnd() {
  return async function () {
    //------Ending Routine 'AFF_S2'-------
    AFF_S2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("thisWord", thisWord);
    
    // was no response the correct answer?!
    if (respAffWord.keys === undefined) {
      if (['None','none',undefined].includes(corAnsA)) {
         respAffWord.corr = 1;  // correct non-response
      } else {
         respAffWord.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('respAffWord.keys', respAffWord.keys);
    psychoJS.experiment.addData('respAffWord.corr', respAffWord.corr);
    if (typeof respAffWord.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respAffWord.rt', respAffWord.rt);
        routineTimer.reset();
        }
    
    respAffWord.stop();
    return Scheduler.Event.NEXT;
  };
}


var _respEndPracA_allKeys;
var endPracAffComponents;
function endPracAffRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'endPracAff'-------
    t = 0;
    endPracAffClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respEndPracA.keys = undefined;
    respEndPracA.rt = undefined;
    _respEndPracA_allKeys = [];
    // keep track of which components have finished
    endPracAffComponents = [];
    endPracAffComponents.push(endPracA_p);
    endPracAffComponents.push(respEndPracA);
    
    endPracAffComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endPracAffRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'endPracAff'-------
    // get current time
    t = endPracAffClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endPracA_p* updates
    if (t >= 0.0 && endPracA_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endPracA_p.tStart = t;  // (not accounting for frame time here)
      endPracA_p.frameNStart = frameN;  // exact frame index
      
      endPracA_p.setAutoDraw(true);
    }

    
    // *respEndPracA* updates
    if (t >= 0.0 && respEndPracA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respEndPracA.tStart = t;  // (not accounting for frame time here)
      respEndPracA.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respEndPracA.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respEndPracA.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respEndPracA.clearEvents(); });
    }

    if (respEndPracA.status === PsychoJS.Status.STARTED) {
      let theseKeys = respEndPracA.getKeys({keyList: ['p', 'q'], waitRelease: false});
      _respEndPracA_allKeys = _respEndPracA_allKeys.concat(theseKeys);
      if (_respEndPracA_allKeys.length > 0) {
        respEndPracA.keys = _respEndPracA_allKeys[_respEndPracA_allKeys.length - 1].name;  // just the last key pressed
        respEndPracA.rt = _respEndPracA_allKeys[_respEndPracA_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endPracAffComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endPracAffRoutineEnd() {
  return async function () {
    //------Ending Routine 'endPracAff'-------
    endPracAffComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((respEndPracA.keys === "p")) {
        returnPrac.finished = true;
    } else {
        returnPrac.finished = false;
    }
    positiveWords = ["\u7545\u9500", "\u8bda\u6073", "\u5145\u88d5", "\u5178\u96c5", "\u4e30\u6ee1", "\u5949\u732e", "\u5bcc\u4e3d", "\u5bcc\u8db3", "\u516c\u5e73", "\u7470\u4e3d", "\u8c6a\u653e", "\u5409\u7965", "\u7cbe\u81f4", "\u656c\u4f69", "\u4fca\u79c0", "\u5ec9\u6d01", "\u7559\u604b", "\u524d\u8fdb", "\u6e05\u79c0", "\u70ed\u5207", "\u5982\u613f", "\u751f\u52a8", "\u5723\u6d01", "\u8212\u7545", "\u723d\u6717", "\u987d\u5f3a", "\u65fa\u76db", "\u9c9c\u8273", "\u7fa1\u6155", "\u4eab\u53d7", "\u96c4\u539a", "\u79c0\u4e3d", "\u6c38\u6052", "\u4f18\u96c5", "\u6709\u5229", "\u8d5e\u6210", "\u73cd\u85cf", "\u632f\u4f5c", "\u6b63\u76f4", "\u5353\u8d8a"];
    negativeWords = ["\u60b2\u89c2", "\u522b\u626d", "\u5632\u7b11", "\u5904\u7f5a", "\u4e22\u5931", "\u5835\u585e", "\u7f5a\u6b3e", "\u70e6\u607c", "\u5b64\u5355", "\u9ed1\u6697", "\u80e1\u6d82", "\u6000\u7591", "\u614c\u5fd9", "\u5047\u5192", "\u7126\u8e81", "\u7981\u6b62", "\u6cae\u4e27", "\u61d2\u60f0", "\u6d6a\u8d39", "\u51b7\u7b11", "\u9c81\u83bd", "\u843d\u540e", "\u95f7\u70ed", "\u6392\u65a5", "\u8f7b\u7387", "\u7a77\u82e6", "\u7f3a\u4e4f", "\u6492\u8c0e", "\u4f24\u5fc3", "\u5931\u610f", "\u635f\u5bb3", "\u9003\u907f", "\u6d88\u6c89", "\u5fc3\u614c", "\u538c\u6076", "\u5fe7\u8651", "\u90c1\u95f7", "\u6742\u4e71", "\u4e89\u5435", "\u81ea\u5351"];
    
    respEndPracA.stop();
    // the Routine "endPracAff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respRest_2_allKeys;
var restAffComponents;
function restAffRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'restAff'-------
    t = 0;
    restAffClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    AffRest.setImage(RestPic);
    respRest_2.keys = undefined;
    respRest_2.rt = undefined;
    _respRest_2_allKeys = [];
    // keep track of which components have finished
    restAffComponents = [];
    restAffComponents.push(AffRest);
    restAffComponents.push(respRest_2);
    
    restAffComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restAffRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'restAff'-------
    // get current time
    t = restAffClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AffRest* updates
    if (t >= 0.0 && AffRest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AffRest.tStart = t;  // (not accounting for frame time here)
      AffRest.frameNStart = frameN;  // exact frame index
      
      AffRest.setAutoDraw(true);
    }

    
    // *respRest_2* updates
    if (t >= 0.0 && respRest_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respRest_2.tStart = t;  // (not accounting for frame time here)
      respRest_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respRest_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respRest_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respRest_2.clearEvents(); });
    }

    if (respRest_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = respRest_2.getKeys({keyList: ['space'], waitRelease: false});
      _respRest_2_allKeys = _respRest_2_allKeys.concat(theseKeys);
      if (_respRest_2_allKeys.length > 0) {
        respRest_2.keys = _respRest_2_allKeys[_respRest_2_allKeys.length - 1].name;  // just the last key pressed
        respRest_2.rt = _respRest_2_allKeys[_respRest_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restAffComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restAffRoutineEnd() {
  return async function () {
    //------Ending Routine 'restAff'-------
    restAffComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    positiveWords = ["\u7545\u9500", "\u8bda\u6073", "\u5145\u88d5", "\u5178\u96c5", "\u4e30\u6ee1", "\u5949\u732e", "\u5bcc\u4e3d", "\u5bcc\u8db3", "\u516c\u5e73", "\u7470\u4e3d", "\u8c6a\u653e", "\u5409\u7965", "\u7cbe\u81f4", "\u656c\u4f69", "\u4fca\u79c0", "\u5ec9\u6d01", "\u7559\u604b", "\u524d\u8fdb", "\u6e05\u79c0", "\u70ed\u5207", "\u5982\u613f", "\u751f\u52a8", "\u5723\u6d01", "\u8212\u7545", "\u723d\u6717", "\u987d\u5f3a", "\u65fa\u76db", "\u9c9c\u8273", "\u7fa1\u6155", "\u4eab\u53d7", "\u96c4\u539a", "\u79c0\u4e3d", "\u6c38\u6052", "\u4f18\u96c5", "\u6709\u5229", "\u8d5e\u6210", "\u73cd\u85cf", "\u632f\u4f5c", "\u6b63\u76f4", "\u5353\u8d8a"];
    negativeWords = ["\u60b2\u89c2", "\u522b\u626d", "\u5632\u7b11", "\u5904\u7f5a", "\u4e22\u5931", "\u5835\u585e", "\u7f5a\u6b3e", "\u70e6\u607c", "\u5b64\u5355", "\u9ed1\u6697", "\u80e1\u6d82", "\u6000\u7591", "\u614c\u5fd9", "\u5047\u5192", "\u7126\u8e81", "\u7981\u6b62", "\u6cae\u4e27", "\u61d2\u60f0", "\u6d6a\u8d39", "\u51b7\u7b11", "\u9c81\u83bd", "\u843d\u540e", "\u95f7\u70ed", "\u6392\u65a5", "\u8f7b\u7387", "\u7a77\u82e6", "\u7f3a\u4e4f", "\u6492\u8c0e", "\u4f24\u5fc3", "\u5931\u610f", "\u635f\u5bb3", "\u9003\u907f", "\u6d88\u6c89", "\u5fc3\u614c", "\u538c\u6076", "\u5fe7\u8651", "\u90c1\u95f7", "\u6742\u4e71", "\u4e89\u5435", "\u81ea\u5351"];
    
    respRest_2.stop();
    // the Routine "restAff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
