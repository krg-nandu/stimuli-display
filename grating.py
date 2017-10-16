from psychopy import visual, core, event, logging
import numpy as np
import time
import subprocess, sys

# change the logger path as required
logging.console.setLevel(logging.CRITICAL)
log = logging.LogFile("/media/zfishlab/Data/FlyCapture/stimuli_timing.log", level=logging.CRITICAL,filemode='w')

globalClock = core.MonotonicClock(start_time=0)
logging.setDefaultClock(globalClock)

def write_file(output_name,list_name):
	csvfile = str(output_name)
	with open(csvfile,"w") as output:
		writer = csv.writer(output,lineterminator = '\n')
		for n in list_name:
			if isinstance(n,list):
				writer.writerow(n)
			elif isinstance(n,dict):	
				writer.writerow([n["x"],n["y"],n["t"]])
			else:
				writer.writerow([n])


# These are the dimensions of the plate.
# DO NOT CHANGE!
width_plate = 620*1.56
height_plate = 400*1.61

grating_width = 380*0.85
grating_height = 568*0.85

white_duration=-1
duration_max=3600
switched=False
	
'''
Request for the duration of the capture from the user
'''
capture_duration=15
if (len(sys.argv) == 2):
	capture_duration=(int)(sys.argv[1])
#print('Capture requested for %d seconds'%(capture_duration))

### 
speed=0.01
pix_per_cycle=160
duration_one=60
duration_two=60
# "+","-",None
direction="-"
###

scalingFactor = 70.0
wheel  = np.asarray([[-1,0],[0,0],[-1/np.sqrt(2),1/np.sqrt(2)],[0,0],[0,1],[0,0],[1/np.sqrt(2),1/np.sqrt(2)],[0,0],[1,0],[0,0],[1/np.sqrt(2),-1/np.sqrt(2)],[0,0],[0,-1],[0,0],[-1/np.sqrt(2),-1/np.sqrt(2)],[0,0],[-1,0]])

mywin=visual.Window([1280,1024],monitor="Dell Inc. 17",units="pix",fullscr=True,screen=1)
plate=visual.Rect(win=mywin,size=(width_plate,height_plate),lineColor=[0,0,0],lineColorSpace="rgb255",lineWidth=4)
white=visual.ImageStim(win=mywin,image="Solid_white.png",size=(1280,1024),pos=[0,0])

#background=visual.Circle(win=mywin,radius=1, fillColor='red')

rad = visual.RadialStim(win=mywin,mask='circle',size=(20,20),pos=[20,20])

log_file=[]
timer=core.Clock()

def startCamera(nframes):
	'''
	Link to (and initiate) capture from the camera and pause for a few (3) seconds before
	displaying the stimuli on the screen
	'''
	# the duration is in frames -- need to convert it into seconds based on the screen's
	# refresh rate
	nSec = nframes/60.0 # assuming 60 Hz emprically validated
	nSec = nSec + 10

	args = ("/usr/src/flycapture/bin/SaveImageToAviEx",str(nSec))
	p = subprocess.Popen(args)
	time.sleep(3)

def displayCircularStimuli(directions,colors,colors_wheel,thicknesses,speeds,duration):
	ops = []
	for d in directions:
		if d == 'Clockwise':
			ops.append('+')
		else:
			ops.append('-')	

	shape1 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[0], lineColor=colors_wheel[0], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(-width_plate/6.4,height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape1b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[0],pos=(-width_plate/6.4,height_plate/8.2))

	shape2 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[1], lineColor=colors_wheel[1], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(0,height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape2b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[1],pos=(0,height_plate/8.2))

	shape3 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[2], lineColor=colors_wheel[2], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(width_plate/6.4,height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape3b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[2],pos=(width_plate/6.4,height_plate/8.2))

	shape4 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[3], lineColor=colors_wheel[3], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(-width_plate/6.4,-height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape4b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[3],pos=(-width_plate/6.4,-height_plate/8.2))

	shape5 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[4], lineColor=colors_wheel[4], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(0,-height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape5b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[4],pos=(0,-height_plate/8.2))

	shape6 = visual.ShapeStim(mywin,units='', lineWidth=thicknesses[5], lineColor=colors_wheel[5], lineColorSpace='rgb', fillColor='red', fillColorSpace='rgb', vertices=np.multiply(wheel,scalingFactor), windingRule=None, closeShape=True, pos=(width_plate/6.4,-height_plate/8.2), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

	shape6b = visual.Circle(mywin,radius=scalingFactor,fillColor=colors[5],pos=(width_plate/6.4,-height_plate/8.2))

	mywin.winHandle.maximize()
	mywin.winHandle.set_fullscreen(True) 
	mywin.winHandle.activate()

    	# display white
	while True: 
		white.draw()
		plate.draw()
		mywin.flip()
		if event.waitKeys(0.5)==["escape"]:
			break	
	event.clearEvents()
	#startCamera(duration)
	clock = core.Clock()
	for frameN in range(duration):
		white.draw()
		plate.draw()

		shape1.setOri(speeds[0],operation=ops[0])
		shape1b.draw()
		shape1.draw()


		shape2.setOri(speeds[1],operation=ops[1])
		shape2b.draw()
		shape2.draw()
	
		shape3.setOri(speeds[2],operation=ops[2])
		shape3b.draw()
		shape3.draw()

		shape4.setOri(speeds[3],operation=ops[3])
		shape4b.draw()
		shape4.draw()

		shape5.setOri(speeds[4],operation=ops[4])
		shape5b.draw()
		shape5.draw()

		shape6.setOri(speeds[5],operation=ops[5])
		shape6b.draw()
		shape6.draw()
	
		mywin.logOnFlip(level=logging.CRITICAL, msg='sent on actual flip')
		mywin.flip()

	for frameN in range(300):
		white.draw()
		plate.draw()
		mywin.flip()

	mywin.close()
	core.quit()

def displayGrating(grating,t1,speed1,dir1,t2,speed2,dir2):
	mywin.winHandle.maximize()
	mywin.winHandle.set_fullscreen(True) 
	mywin.winHandle.activate()

    	# display white
	while True: 
		white.draw()
		plate.draw()
		mywin.flip()
		if event.waitKeys(0.5)==["escape"]:
			break	
	event.clearEvents()

	startCamera(t1+t2)

	t=0
	while (t < (t1+t2)):
		white.draw()
		if (t < t1):
			grating.setPhase(speed1,dir1)
		else:
			grating.setPhase(speed2,dir2)
		grating.draw()
		if (t==0) or (t==t1) or (t==(t1+t2-1)):
			mywin.logOnFlip(level=logging.CRITICAL, msg='sent on actual flip')
		mywin.flip()
		t=t+1

	for frameN in range(300):
		white.draw()
		plate.draw()
		mywin.flip()

	mywin.close()

def displayHorizontalGrating(t1,speed1,dir1,t2,speed2,dir2,thickness):
	#startCamera(t1+t2)
	grating=visual.GratingStim(win=mywin,mask=None,size=(grating_width,grating_height),ori=270,color=[80,80,80],colorSpace="rgb255",pos=[0,0],sf=(1.0/pix_per_cycle)*thickness)
	displayGrating(grating,t1,speed1,dir1,t2,speed2,dir2)

def displayVerticalGrating(t1,speed1,dir1,t2,speed2,dir2,thickness):
	#startCamera(t1+t2)
	grating=visual.GratingStim(win=mywin,mask=None,size=(grating_height,grating_width),ori=0,color=[80,80,80],colorSpace="rgb255",pos=[0,0],sf=(1.0/pix_per_cycle)*thickness)
	displayGrating(grating,t1,speed1,dir1,t2,speed2,dir2)

def displayNoStimuli(duration):
	mywin.winHandle.maximize()
	mywin.winHandle.set_fullscreen(True) 
	mywin.winHandle.activate()

    	# display white
	while True: 
		white.draw()
		plate.draw()
		mywin.flip()
		if event.waitKeys(0.5)==["escape"]:
			break	
	event.clearEvents()
	startCamera(duration)
	t=0
	while (t < duration):
		white.draw()
		plate.draw()
		mywin.flip()
		t=t+1
	mywin.close()
