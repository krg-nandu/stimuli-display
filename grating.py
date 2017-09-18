# previously psychopy_2b

from psychopy import visual, core, event, logging
import numpy as np
import time
import subprocess, sys

logging.console.setLevel(logging.WARNING)
log = logging.LogFile("run.log", level=logging.INFO,filemode='w')

globalClock = core.Clock()
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

				
			
white_duration=-1
duration_max=3600
switched=False
	
'''
Request for the duration of the capture from the user
'''
capture_duration=15
if (len(sys.argv) == 2):
	capture_duration=(int)(sys.argv[1])
print('Capture requested for %d seconds'%(capture_duration))

### 
speed=0.01
pix_per_cycle=160
duration_one=60
duration_two=60
# "+","-",None
direction="-"
###

mywin=visual.Window([1280,1024],monitor="Dell Inc. 17",units="pix",fullscr=True,screen=1)
#plate=visual.ImageStim(win=mywin,image="well_plate.png",size=(568*0.85,380*0.85),pos=[0,0])
plate=visual.Rect(win=mywin,size=(620*1.5,400*1.5),lineColor=[0,0,0],lineColorSpace="rgb255")
white=visual.ImageStim(win=mywin,image="Solid_white.png",size=(1280,1024),pos=[0,0])

#grating=visual.GratingStim(win=mywin,mask=None,size=(380*0.85,568*0.85),ori=270,color=[80,80,80],colorSpace="rgb255",pos=[0,0],sf=1.0/pix_per_cycle)
grating=visual.GratingStim(win=mywin,mask=None,size=(380*0.85,568*0.85),ori=270,color=[80,80,80],colorSpace="rgb255",pos=[0,0],sf=1.0/pix_per_cycle)
rad = visual.RadialStim(win=mywin,mask='circle',size=(20,20),pos=[20,20])
shape = visual.ShapeStim(mywin, units='', lineWidth=1.5, lineColor='black', lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', vertices=((-50, 0), (0, 50), (50, 0)), windingRule=None, closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=False)

log_file=[]
timer=core.Clock()

# display white
while True: 
	if white_duration<0 or (white_duration>=0 and timer.getTime()>=white_duration):
		white.draw()
		plate.draw()
	
	mywin.flip()
	if event.waitKeys(0.1)==["escape"] or (white_duration>=0 and timer.getTime()>=white_duration): 
		break	
	event.clearEvents()

'''
Link to (and initiate) capture from the camera and pause for a few (3) seconds before
displaying the stimuli on the screen
'''
#args = ("/usr/src/flycapture/bin/SaveImageToAviEx",str(capture_duration))
#p = subprocess.Popen(args)
#time.sleep(3)

'''
# display grating
timer.reset()
while timer.getTime()<=duration_max: 
	ta=time.time()
	#print timer.getTime()
	white.draw()
	if direction!=None:
		grating.setPhase(speed,direction)

		# switch by pressing "s"
		if duration_one<=0 and duration_two<=0:
			if event.waitKeys(0.005)==["s"]:
				if direction=="+":
					direction="-"
				else:
					direction="+"
		# switch by time 
		else:
			if switched==False and duration_one<=timer.getTime()<duration_one+duration_two:
				if direction=="+":
					direction="-"
					print "Switching From + to - at %.3fs" %timer.getTime() 

				elif direction=="-":
					direction="+"
					print "Switching From - to + at %.3fs" %timer.getTime() 

				switched=True
			if timer.getTime()>=duration_one+duration_two:
				break
	else:
		if timer.getTime()>=duration_one+duration_two:
			break
	grating.draw()
	mywin.flip()

	if event.waitKeys(0.005)==["escape"]: 
		break	
	event.clearEvents()
	tb=time.time()
	#print tb-ta
print "Grating Ends at %.3fs" %timer.getTime()

# end on white
while True: 
	white.draw()
	plate.draw()
	mywin.flip()
	if event.waitKeys(0.1)==["escape"]: 
		break	
	event.clearEvents()
'''

clock = core.Clock()
for frameN in range(200):
	white.draw()
	#grating.setPhase(0.1, '+')
	#grating.draw()
	#shape.setPhase(0.1,'+')
	shape.setOri(2,operation='+')
	shape.draw()
	mywin.logOnFlip(level=logging.EXP, msg='sent on actual flip')
	mywin.flip()


mywin.close()
core.quit()


