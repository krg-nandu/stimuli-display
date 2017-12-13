from psychopy import visual, core, event, logging
import numpy as np
import time
import subprocess, sys

# change the logger path as required
logging.console.setLevel(logging.CRITICAL)
# log = logging.LogFile("/media/zfishlab/Data/FlyCapture/stimuli_timing.log", level=logging.CRITICAL,filemode='w')

globalClock = core.MonotonicClock(start_time=0)
logging.setDefaultClock(globalClock)


def write_file(output_name, list_name):
    csvfile = str(output_name)
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for n in list_name:
            if isinstance(n, list):
                writer.writerow(n)
            elif isinstance(n, dict):
                writer.writerow([n["x"], n["y"], n["t"]])
            else:
                writer.writerow([n])


# These are the dimensions of the plate.
# DO NOT CHANGE!
width_plate = 620 * 1.56
height_plate = 400 * 1.61

grating_width = 380 * 0.85
grating_height = 568 * 0.85

white_duration = -1
duration_max = 3600
switched = False

'''
Request for the duration of the capture from the user
'''
#capture_duration = 15
#if (len(sys.argv) == 2):
#    capture_duration = (int)(sys.argv[1])

scalingFactor = 70.0
mywin=visual.Window([1280,1024],monitor="Dell Inc. 17",units="pix",fullscr=True,screen=1)
plate=visual.Rect(win=mywin,size=(width_plate,height_plate),lineColor=[0,0,0],lineColorSpace="rgb255",lineWidth=4)
white=visual.ImageStim(win=mywin,image="Solid_white.png",size=(1280,1024),pos=[0,0])
log_file = []
timer = core.Clock()


def startCamera(nframes):
    '''
    Link to (and initiate) capture from the camera and pause for a few (3) seconds before
    displaying the stimuli on the screen
    '''
    # the duration is in frames -- need to convert it into seconds based on the screen's
    # refresh rate
    nSec = nframes / 60.0  # assuming 60 Hz emprically validated
    nSec = nSec + 10

    args = ("/usr/src/flycapture/bin/SaveImageToAviEx", str(nSec))
    p = subprocess.Popen(args)
    time.sleep(3)


def startleDisplayProtocol(t1, t2, t3, speed, color):
    # note that here t1, t2, t3 are in frames
    mywin.winHandle.maximize()
    mywin.winHandle.set_fullscreen(True)
    mywin.winHandle.activate()

    radDisc = scalingFactor/2.5
    shape1 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(-width_plate / 6.4, (scalingFactor/2.) + height_plate / 8.2))
    shape2 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(0, (scalingFactor/2.) + height_plate / 8.2))
    shape3 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(width_plate / 6.4, (scalingFactor/2.) +height_plate / 8.2))
    shape4 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(-width_plate / 6.4, (scalingFactor/2.) + -height_plate / 8.2))
    shape5 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(0, (scalingFactor/2.) + -height_plate / 8.2))
    shape6 = visual.Circle(mywin, radius=radDisc, fillColor=color,pos=(width_plate / 6.4, (scalingFactor/2.) + -height_plate / 8.2))

    shape1b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(-width_plate / 6.4, height_plate / 8.2))
    shape2b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(0, height_plate / 8.2))
    shape3b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(width_plate / 6.4, height_plate / 8.2))
    shape4b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(-width_plate / 6.4, -height_plate / 8.2))
    shape5b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(0, -height_plate / 8.2))
    shape6b = visual.Circle(mywin, radius=scalingFactor, lineWidth=2., lineColor='black',pos=(width_plate / 6.4, -height_plate / 8.2))

    # This is before the start of the experiment. Position the wells, add larvae, top up wells with water
    # and focus the camera! Press 'ESC' to start the experiment
    while True:
        white.draw()
        plate.draw()
        shape1b.draw()
        shape2b.draw()
        shape3b.draw()
        shape4b.draw()
        shape5b.draw()
        shape6b.draw()

        mywin.flip()
        if event.waitKeys(0.5) == ["escape"]:
            break
    event.clearEvents()

    # start the camera here, and start recording
    #startCamera(t1+t2+t3)

    # This is the acclimatization phase
    for frameN in range(t1):
        white.draw()
        plate.draw()

        shape1b.draw()
        shape2b.draw()
        shape3b.draw()
        shape4b.draw()
        shape5b.draw()
        shape6b.draw()

        #mywin.logOnFlip(level=logging.CRITICAL, msg='sent on actual flip')
        mywin.flip()

    initpos = [-width_plate / 6.4, height_plate / 8.2]
    ops='+'

    # This is the startle phase
    for frameN in range(t2):
        white.draw()
        plate.draw()

        shape1.draw()
        shape2.draw()
        shape3.draw()
        shape4.draw()
        shape5.draw()
        shape6.draw()

        if (shape1.pos[0]-radDisc) <= (initpos[0]-scalingFactor):
            ops='+'
        elif (shape1.pos[0]+radDisc) >= (initpos[0]+scalingFactor):
            ops = '-'
        shape1.setPos([speed,0], operation=ops)
        shape2.setPos([speed, 0], operation=ops)
        shape3.setPos([speed, 0], operation=ops)
        shape4.setPos([speed, 0], operation=ops)
        shape5.setPos([speed, 0], operation=ops)
        shape6.setPos([speed, 0], operation=ops)

        shape1b.draw()
        shape2b.draw()
        shape3b.draw()
        shape4b.draw()
        shape5b.draw()
        shape6b.draw()

        #mywin.logOnFlip(level=logging.CRITICAL, msg='sent on actual flip')
        mywin.flip()

    # This is the recovery phase
    for frameN in range(t3):
        white.draw()
        plate.draw()
        shape1b.draw()
        shape2b.draw()
        shape3b.draw()
        shape4b.draw()
        shape5b.draw()
        shape6b.draw()

        #mywin.logOnFlip(level=logging.CRITICAL, msg='sent on actual flip')
        mywin.flip()

    for frameN in range(300):
        white.draw()
        plate.draw()
        mywin.flip()

    mywin.close()
    core.quit()