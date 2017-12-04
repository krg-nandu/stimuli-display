from Tkinter import *
from grating import *

class Application(Frame):

    def createWidgets(self,master):

	'''
	**************
	Linear Stimuli
	**************
	'''
	row_num=0
	# set the linear stimuli label
	self.heading1 = Label(master,fg='red',bd=10,highlightbackground='red')
	self.heading1.grid(row=row_num,column=0,columnspan=3,sticky='ew')
        self.hgvar = IntVar() 
	self.hgratbutton = Checkbutton(self.heading1,text='Horizontal Gratings',variable=self.hgvar,command=self.selectHGratings)
	self.hgratbutton.grid(row=row_num,column=0,columnspan=3,sticky='ew')

	###
	self.hthick_label = Label(self.heading1, text='Thickness : ')
	self.hthick_label.grid(row=row_num+1,column=0)
	self.hthick_val = Entry(self.heading1)
	self.hthick_val.grid(row=row_num+1,column=1)

	'''
	Layout for the first stimulus: Direction, duration, speed
	'''
	self.direction1_label = Label(self.heading1, text='Initial Direction : ')
	self.direction1_label.grid(row=row_num+2,column=0)

	self._dir1PlusSet = IntVar()
	self._dir1MinusSet = IntVar()
	self.dir1_plus = Checkbutton(self.heading1,text='+',variable=self._dir1PlusSet)
	self.dir1_plus.grid(row=(row_num+2),column=1)

	self.dir1_minus = Checkbutton(self.heading1,text='-',variable=self._dir1MinusSet)
	self.dir1_minus.grid(row=(row_num+2),column=2)
	
	self.duration1_label = Label(self.heading1, text='Duration (in frames) : ')
	self.duration1_label.grid(row=(row_num+3),column=0)

	self.duration1_val = Entry(self.heading1)
	self.duration1_val.grid(row=(row_num+3),column=1)

	self.speed1_label = Label(self.heading1, text='Speed : ')
	self.speed1_label.grid(row=(row_num+4),column=0)
	self.speed1_val = Entry(self.heading1)
	self.speed1_val.grid(row=(row_num+4),column=1)

	'''
	Layout for the second stimulus: Direction, duration, speed
	'''
	self.direction2_label = Label(self.heading1, text='Direction shift: ')
	self.direction2_label.grid(row=(row_num+5),column=0)

	self._dir2PlusSet = IntVar()
	self._dir2MinusSet = IntVar()
	self.dir2_plus = Checkbutton(self.heading1,text='+',variable=self._dir2PlusSet)
	self.dir2_plus.grid(row=(row_num+5),column=1)
	self.dir2_minus = Checkbutton(self.heading1,text='-',variable=self._dir2MinusSet)
	self.dir2_minus.grid(row=(row_num+5),column=2)
	
	self.duration2_label = Label(self.heading1, text='Duration (in frames) : ')
	self.duration2_label.grid(row=(row_num+6),column=0)
	self.duration2_val = Entry(self.heading1)
	self.duration2_val.grid(row=(row_num+6),column=1)

	self.speed2_label = Label(self.heading1, text='Speed : ')
	self.speed2_label.grid(row=(row_num+7),column=0)
	self.speed2_val = Entry(self.heading1)
	self.speed2_val.grid(row=(row_num+7),column=1)


	'''
	**************
	Vertical Grating
	**************
	'''
	# set the linear stimuli label
	self.heading3 = Label(master,fg='red',bd=10,highlightbackground='red')
	self.heading3.grid(row=row_num,column=3,columnspan=3,sticky='ew')
        self.vgvar = IntVar() 
	self.vgratbutton = Checkbutton(self.heading3,text='Vertical Gratings',variable=self.vgvar,command=self.selectVGratings)
	self.vgratbutton.grid(row=row_num,column=3,columnspan=3,sticky='ew')

	self.vthick_label = Label(self.heading3, text='Thickness : ')
	self.vthick_label.grid(row=row_num+1,column=3)
	self.vthick_val = Entry(self.heading3)
	self.vthick_val.grid(row=row_num+1,column=4)

	'''
	Layout for the first stimulus: Direction, duration, speed
	'''
	self.direction1b_label = Label(self.heading3, text='Initial Direction : ')
	self.direction1b_label.grid(row=row_num+2,column=3)

	self._dir1bPlusSet = IntVar()
	self._dir1bMinusSet = IntVar()
	self.dir1b_plus = Checkbutton(self.heading3,text='+',variable=self._dir1bPlusSet)
	self.dir1b_plus.grid(row=row_num+2,column=4)
	self.dir1b_minus = Checkbutton(self.heading3,text='-',variable=self._dir1bMinusSet)
	self.dir1b_minus.grid(row=row_num+2,column=5)
	
	self.duration1b_label = Label(self.heading3, text='Duration (in frames) : ')
	self.duration1b_label.grid(row=row_num+3,column=3)
	self.duration1b_val = Entry(self.heading3)
	self.duration1b_val.grid(row=row_num+3,column=4)

	self.speed1b_label = Label(self.heading3, text='Speed : ')
	self.speed1b_label.grid(row=row_num+4,column=3)
	self.speed1b_val = Entry(self.heading3)
	self.speed1b_val.grid(row=row_num+4,column=4)

	'''
	Layout for the second stimulus: Direction, duration, speed
	'''
	self.direction2b_label = Label(self.heading3, text='Direction shift: ')
	self.direction2b_label.grid(row=row_num+5,column=3)

	self._dir2bPlusSet = IntVar()
	self._dir2bMinusSet = IntVar()
	self.dir2b_plus = Checkbutton(self.heading3,text='+',variable=self._dir2bPlusSet)
	self.dir2b_plus.grid(row=row_num+5,column=4)

	self.dir2b_minus = Checkbutton(self.heading3,text='-',variable=self._dir2bMinusSet)
	self.dir2b_minus.grid(row=row_num+5,column=5)
	
	self.duration2b_label = Label(self.heading3, text='Duration (in frames) : ')
	self.duration2b_label.grid(row=row_num+6,column=3)

	self.duration2b_val = Entry(self.heading3)
	self.duration2b_val.grid(row=row_num+6,column=4)

	self.speed2b_label = Label(self.heading3, text='Speed : ')
	self.speed2b_label.grid(row=row_num+7,column=3)
	self.speed2b_val = Entry(self.heading3)
	self.speed2b_val.grid(row=row_num+7,column=4)

	'''
	**************
	Radial Stimuli
	**************
	'''
	self.COLOR_OPTIONS = ["White","Gray","Red","Green","Blue","Yellow"]
	self.DIR_OPTIONS = ["Clockwise","Anti-Clockwise"]

	row_num = 9
	# set the radial stimuli label
	self.heading2 = Label(master,fg='red')
	self.heading2.grid(row=8,column=0,columnspan=9,sticky='ew')
	self.radVar = IntVar() 
	self.radButton = Checkbutton(self.heading2,text='Spinning Stimuli',variable=self.radVar,command=self.selectRad)
	self.radButton.grid(row=8,column=0,columnspan=9,sticky='ew')

	self.radDurationLabel = Label(self.heading2,text='Duration (in frames)').grid(row=row_num,column=0,columnspan=2)
	self.radDuration_val = Entry(self.heading2)
	self.radDuration_val.grid(row=row_num,column=2,columnspan=2,sticky='ew')

	# apply option to all wells
	self.appall = IntVar()
	self.applyAll = Checkbutton(self.heading2, text='Apply option to all wells',variable=self.appall,command=self.apply_all)
	self.applyAll.grid(row=row_num+1,column=0,columnspan=9,sticky='ew')

	row_num=row_num+2
	####################
	self.well1_label = Label(self.heading2, text='Well 1',fg='white',bg='gray').grid(row=row_num,column=0,columnspan=2)
	self.th1_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=0)
	self.th1_val = Entry(self.heading2)
	self.th1_val.grid(row=row_num+1,column=1)

	self.sp1_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=0)
	self.sp1_val = Entry(self.heading2)
	self.sp1_val.grid(row=row_num+2,column=1)

	self.color1_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=0)

	self.color1_val = StringVar(self.heading2)
	self.color1_val.set(self.COLOR_OPTIONS[0])
	self.color1_menu = apply(OptionMenu, (self.heading2, self.color1_val) + tuple(self.COLOR_OPTIONS))
	self.color1_menu.grid(row=row_num+3,column=1,sticky="ew")

	self.color1wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=0)

	self.color1wh_val = StringVar(self.heading2)
	self.color1wh_val.set(self.COLOR_OPTIONS[0])
	self.color1wh_menu = apply(OptionMenu, (self.heading2, self.color1wh_val) + tuple(self.COLOR_OPTIONS))
	self.color1wh_menu.grid(row=row_num+4,column=1,sticky="ew")

	self.dr1_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=0)
	self.dr1_val = StringVar(self.heading2)
	self.dr1_val.set(self.DIR_OPTIONS[0])
	self.dr1_menu = apply(OptionMenu, (self.heading2, self.dr1_val) + tuple(self.DIR_OPTIONS))
	self.dr1_menu.grid(row=row_num+5,column=1,sticky="ew")
	
	####################
	self.well2_label = Label(self.heading2, text='Well 2',fg='white',bg='gray').grid(row=row_num,column=2,columnspan=2)
	self.th2_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=2,sticky=E)
	self.th2_var = StringVar()
	self.th2_val = Entry(self.heading2,textvariable=self.th2_var)
	self.th2_val.grid(row=row_num+1,column=3)
	self.color2_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=2,sticky=E)

	self.sp2_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=2,sticky=E)
	self.sp2_var = StringVar()
	self.sp2_val = Entry(self.heading2,textvariable=self.sp2_var)
	self.sp2_val.grid(row=row_num+2,column=3)

	self.color2_val = StringVar(self.heading2)
	self.color2_val.set(self.COLOR_OPTIONS[0])
	self.color2_menu = apply(OptionMenu, (self.heading2, self.color2_val) + tuple(self.COLOR_OPTIONS))
	self.color2_menu.grid(row=row_num+3,column=3,sticky="ew")

	self.color2wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=2,sticky=E)
	self.color2wh_val = StringVar(self.heading2)
	self.color2wh_val.set(self.COLOR_OPTIONS[0])
	self.color2wh_menu = apply(OptionMenu, (self.heading2, self.color2wh_val) + tuple(self.COLOR_OPTIONS))
	self.color2wh_menu.grid(row=row_num+4,column=3,sticky="ew")

	self.dr2_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=2,sticky=E)
	self.dr2_val = StringVar(self.heading2)
	self.dr2_val.set(self.DIR_OPTIONS[0])
	self.dr2_menu = apply(OptionMenu, (self.heading2, self.dr2_val) + tuple(self.DIR_OPTIONS))
	self.dr2_menu.grid(row=row_num+5,column=3,sticky="ew")
	####################

	self.well3_label = Label(self.heading2, text='Well 3',fg='white',bg='gray').grid(row=row_num,column=4,columnspan=2)

	self.th3_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=4,sticky=E)
	self.th3_var = StringVar()
	self.th3_val = Entry(self.heading2,textvariable=self.th3_var)
	self.th3_val.grid(row=row_num+1,column=5)

	self.sp3_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=4,sticky=E)
	self.sp3_var = StringVar()
	self.sp3_val = Entry(self.heading2,textvariable=self.sp3_var)
	self.sp3_val.grid(row=row_num+2,column=5)

	self.color3_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=4,sticky=E)
	self.color3_val = StringVar(self.heading2)
	self.color3_val.set(self.COLOR_OPTIONS[0])
	self.color3_menu = apply(OptionMenu, (self.heading2, self.color3_val) + tuple(self.COLOR_OPTIONS))
	self.color3_menu.grid(row=row_num+3,column=5,sticky="ew")

	self.color3wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=4,sticky=E)
	self.color3wh_val = StringVar(self.heading2)
	self.color3wh_val.set(self.COLOR_OPTIONS[0])
	self.color3wh_menu = apply(OptionMenu, (self.heading2, self.color3wh_val) + tuple(self.COLOR_OPTIONS))
	self.color3wh_menu.grid(row=row_num+4,column=5,sticky="ew")

	self.dr3_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=4,sticky=E)
	self.dr3_val = StringVar(self.heading2)
	self.dr3_val.set(self.DIR_OPTIONS[0])
	self.dr3_menu = apply(OptionMenu, (self.heading2, self.dr3_val) + tuple(self.DIR_OPTIONS))
	self.dr3_menu.grid(row=row_num+5,column=5,sticky="ew")
	####################

	row_num=row_num+6
	self.well4_label = Label(self.heading2, text='Well 4',fg='white',bg='gray').grid(row=row_num,column=0,columnspan=2)

	self.th4_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=0)
	self.th4_var = StringVar()
	self.th4_val = Entry(self.heading2,textvariable=self.th4_var)
	self.th4_val.grid(row=row_num+1,column=1)

	self.sp4_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=0)
	self.sp4_var = StringVar()
	self.sp4_val = Entry(self.heading2,textvariable=self.sp4_var)
	self.sp4_val.grid(row=row_num+2,column=1)

	self.color4_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=0)
	self.color4_val = StringVar(self.heading2)
	self.color4_val.set(self.COLOR_OPTIONS[0])
	self.color4_menu = apply(OptionMenu, (self.heading2, self.color4_val) + tuple(self.COLOR_OPTIONS))
	self.color4_menu.grid(row=row_num+3,column=1,sticky="ew")

	self.color4wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=0)
	self.color4wh_val = StringVar(self.heading2)
	self.color4wh_val.set(self.COLOR_OPTIONS[0])
	self.color4wh_menu = apply(OptionMenu, (self.heading2, self.color4wh_val) + tuple(self.COLOR_OPTIONS))
	self.color4wh_menu.grid(row=row_num+4,column=1,sticky="ew")

	self.dr4_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=0)
	self.dr4_val = StringVar(self.heading2)
	self.dr4_val.set(self.DIR_OPTIONS[0])
	self.dr4_menu = apply(OptionMenu, (self.heading2, self.dr4_val) + tuple(self.DIR_OPTIONS))
	self.dr4_menu.grid(row=row_num+5,column=1,sticky="ew")
	####################

	self.well5_label = Label(self.heading2, text='Well 5',fg='white',bg='gray').grid(row=row_num,column=2,columnspan=2)
	self.th5_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=2,sticky=E)
	self.th5_var = StringVar()
	self.th5_val = Entry(self.heading2,textvariable=self.th5_var)
	self.th5_val.grid(row=row_num+1,column=3)

	self.sp5_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=2,sticky=E)
	self.sp5_var = StringVar()
	self.sp5_val = Entry(self.heading2,textvariable=self.sp5_var)
	self.sp5_val.grid(row=row_num+2,column=3)

	self.color5_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=2,sticky=E)
	self.color5_val = StringVar(self.heading2)
	self.color5_val.set(self.COLOR_OPTIONS[0])
	self.color5_menu = apply(OptionMenu, (self.heading2, self.color5_val) + tuple(self.COLOR_OPTIONS))
	self.color5_menu.grid(row=row_num+3,column=3,sticky="ew")

	self.color5wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=2,sticky=E)
	self.color5wh_val = StringVar(self.heading2)
	self.color5wh_val.set(self.COLOR_OPTIONS[0])
	self.color5wh_menu = apply(OptionMenu, (self.heading2, self.color5wh_val) + tuple(self.COLOR_OPTIONS))
	self.color5wh_menu.grid(row=row_num+4,column=3,sticky="ew")

	self.dr5_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=2,sticky=E)
	self.dr5_val = StringVar(self.heading2)
	self.dr5_val.set(self.DIR_OPTIONS[0])
	self.dr5_menu = apply(OptionMenu, (self.heading2, self.dr5_val) + tuple(self.DIR_OPTIONS))
	self.dr5_menu.grid(row=row_num+5,column=3,sticky="ew")
	####################

	self.well6_label = Label(self.heading2, text='Well 6',fg='white',bg='gray').grid(row=row_num,column=4,columnspan=2)
	self.th6_label = Label(self.heading2, text='Thickness : ').grid(row=row_num+1,column=4,sticky=E)
	self.th6_var = StringVar()	
	self.th6_val = Entry(self.heading2,textvariable=self.th6_var)
	self.th6_val.grid(row=row_num+1,column=5)

	self.sp6_label = Label(self.heading2, text='Speed : ').grid(row=row_num+2,column=4,sticky=E)
	self.sp6_var = StringVar()
	self.sp6_val = Entry(self.heading2,textvariable=self.sp6_var)
	self.sp6_val.grid(row=row_num+2,column=5)

	self.color6_label = Label(self.heading2, text='Color : ').grid(row=row_num+3,column=4,sticky=E)
	self.color6_val = StringVar(self.heading2)
	self.color6_val.set(self.COLOR_OPTIONS[0])
	self.color6_menu = apply(OptionMenu, (self.heading2, self.color6_val) + tuple(self.COLOR_OPTIONS))
	self.color6_menu.grid(row=row_num+3,column=5,sticky="ew")

	self.color6wh_label = Label(self.heading2, text='Color(Wheel) : ').grid(row=row_num+4,column=4,sticky=E)
	self.color6wh_val = StringVar(self.heading2)
	self.color6wh_val.set(self.COLOR_OPTIONS[0])
	self.color6wh_menu = apply(OptionMenu, (self.heading2, self.color6wh_val) + tuple(self.COLOR_OPTIONS))
	self.color6wh_menu.grid(row=row_num+4,column=5,sticky="ew")

	self.dr6_label = Label(self.heading2, text='Direction : ').grid(row=row_num+5,column=4,sticky=E)
	self.dr6_val = StringVar(self.heading2)
	self.dr6_val.set(self.DIR_OPTIONS[0])
	self.dr6_menu = apply(OptionMenu, (self.heading2, self.dr6_val) + tuple(self.DIR_OPTIONS))
	self.dr6_menu.grid(row=row_num+5,column=5,sticky="ew")
	####################
	row_num=row_num+6	

	# no stimuli
	self.heading4 = Label(master,fg='red')
	self.heading4.grid(row=row_num+1,column=0,columnspan=9,sticky='ew')
	self.nostimVar = IntVar() 
	self.nsButton = Checkbutton(self.heading4,text='No Stimuli (Arena exploration tasks) for ',variable=self.nostimVar,command=self.selectNoStim)
	self.nsButton.grid(row=row_num+1,column=0,columnspan=9,sticky='ew')
	self.nsDur = Entry(self.heading4)
	self.nsDur.grid(row=row_num+1,column=10,columnspan=2,sticky='w')
	self.nsDummy = Label(self.heading4,text='frames').grid(row=row_num+1,column=12,sticky='w')

	####################
	self.qlabel = Label(master,fg='red',bd=10)
	self.qlabel.grid(row=row_num+2,column=5,columnspan=4,sticky='ew')
        self.quit = Button(self.qlabel,text='Exit the program!',command=self.quit)
	self.quit.grid(row=row_num+2,column=5,sticky=E)

	####################

	self.startlabel = Label(master,fg='red',bd=10)
	self.startlabel.grid(row=row_num+2,column=0,columnspan=4,sticky='ew')
        self.start = Button(self.startlabel,text='Start the experiment!',command=self.runExp)
	self.start.grid(row=row_num+2,column=0,sticky=E)

    def toggleGroup(self,group,value):
	if value == 1:
		objstate = 'disabled'
	elif value == 0:
		objstate = 'normal'

	for w in group.winfo_children():
           w.configure(state=objstate)

    def selectHGratings(self):
	self.toggleGroup(self.heading3,self.hgvar.get())
	self.toggleGroup(self.heading2,self.hgvar.get())
	self.toggleGroup(self.heading4,self.hgvar.get())
	
    def selectVGratings(self):
	self.toggleGroup(self.heading1,self.vgvar.get())
	self.toggleGroup(self.heading2,self.vgvar.get())
	self.toggleGroup(self.heading4,self.vgvar.get())

    def selectRad(self):
	self.toggleGroup(self.heading1,self.radVar.get())
	self.toggleGroup(self.heading3,self.radVar.get())
	self.toggleGroup(self.heading4,self.radVar.get())

    def selectNoStim(self):
	self.toggleGroup(self.heading1,self.nostimVar.get())
	self.toggleGroup(self.heading3,self.nostimVar.get())
	self.toggleGroup(self.heading2,self.nostimVar.get())

    # copy settings of well 1 into all the other wells
    def apply_all(self):
	if self.radVar.get() == 0 or self.appall.get() == 0:
		# radial stimulus is not selected or the apply all option is not selected
		return
	print 'Copying settings of well 1 into all the other wells'
	self.th2_var.set(self.th1_val.get())
  	self.sp2_var.set(self.sp1_val.get())
	self.color2_val.set(self.color1_val.get())
	self.color2wh_val.set(self.color1wh_val.get())
	self.dr2_val.set(self.dr1_val.get())

	self.th3_var.set(self.th1_val.get())
  	self.sp3_var.set(self.sp1_val.get())
	self.color3_val.set(self.color1_val.get())
	self.color3wh_val.set(self.color1wh_val.get())
	self.dr3_val.set(self.dr1_val.get())

	self.th4_var.set(self.th1_val.get())
  	self.sp4_var.set(self.sp1_val.get())
	self.color4_val.set(self.color1_val.get())
	self.color4wh_val.set(self.color1wh_val.get())
	self.dr4_val.set(self.dr1_val.get())

	self.th5_var.set(self.th1_val.get())
  	self.sp5_var.set(self.sp1_val.get())
	self.color5_val.set(self.color1_val.get())
	self.color5wh_val.set(self.color1wh_val.get())
	self.dr5_val.set(self.dr1_val.get())

	self.th6_var.set(self.th1_val.get())
  	self.sp6_var.set(self.sp1_val.get())
	self.color6_val.set(self.color1_val.get())
	self.color6wh_val.set(self.color1wh_val.get())
	self.dr6_val.set(self.dr1_val.get())

    def runExp(self):
    	'''
	get all the variables on the panel and call the function to display the stimuli
	'''
	# first check what kind of stimulus is wanted
	if self.hgvar.get() == 1:
	    # HORIZONTAL GRATING
	    dir1 = ''
	    dir2 = ''
	    if (self._dir1PlusSet.get() == 1):
		    dir1=dir1+'+'
	    else:
		    dir1=dir1+'-'

	    if (self._dir2PlusSet.get() == 1):
		    dir2=dir2+'+'
	    else:
		    dir2=dir2+'-'
	    displayHorizontalGrating(float(self.duration1_val.get()),float(self.speed1_val.get()),dir1,float(self.duration2_val.get()),float(self.speed2_val.get()),dir2,float(self.hthick_val.get()))

	elif self.vgvar.get() == 1:
	    # VERTICAL GRATING
	    dir1 = ''
	    dir2 = ''
	    if (self._dir1bPlusSet.get() == 1):
		    dir1=dir1+'+'
	    else:
		    dir1=dir1+'-'

	    if (self._dir2bPlusSet.get() == 1):
		    dir2=dir2+'+'
	    else:
		    dir2=dir2+'-'
	    displayVerticalGrating(float(self.duration1b_val.get()),float(self.speed1b_val.get()),dir1,float(self.duration2b_val.get()),float(self.speed2b_val.get()),dir2,float(self.vthick_val.get()))
	elif self.radVar.get() == 1:
	    # RADIAL STIMULI
	    directions = [self.dr1_val.get(),self.dr2_val.get(),self.dr3_val.get(),self.dr4_val.get(),self.dr5_val.get(),self.dr6_val.get()]
	    colors = [self.color1_val.get(), self.color2_val.get(),self.color3_val.get(),self.color4_val.get(),self.color5_val.get(),self.color6_val.get()]
	    colors_wheel = [self.color1wh_val.get(), self.color2wh_val.get(),self.color3wh_val.get(),self.color4wh_val.get(),self.color5wh_val.get(),self.color6wh_val.get()]
	    thicknesses = [float(self.th1_val.get()),float(self.th2_val.get()),float(self.th3_val.get()),float(self.th4_val.get()),float(self.th5_val.get()),float(self.th6_val.get())]
	    speeds = [float(self.sp1_val.get()),float(self.sp2_val.get()),float(self.sp3_val.get()),float(self.sp4_val.get()),float(self.sp5_val.get()),float(self.sp6_val.get())]
	    displayCircularStimuli(directions,colors,colors_wheel,thicknesses,speeds,int(self.radDuration_val.get()))
	elif self.nostimVar.get() == 1:
	    displayNoStimuli(float(self.nsDur.get()))	    
	else:
	    print('Please select at least one option!')

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets(master)

root = Tk()
app = Application(master=root)
app.master.title("STIM Display")
app.mainloop()
root.destroy()
