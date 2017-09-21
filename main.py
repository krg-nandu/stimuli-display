from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self,master):

	'''
	**************
	Linear Stimuli
	**************
	'''
	# set the linear stimuli label
	self.heading1 = Label(master, text='Linear Stimuli',fg='red',bg='black').grid(row=0,column=0,columnspan=3)
	#self.heading1.pack()

	'''
	Layout for the first stimulus: Direction, duration, speed
	'''
	self.direction1_label = Label(master, text='Initial Direction : ').grid(row=1,column=0)

	_dir1PlusSet = IntVar()
	_dir1MinusSet = IntVar()
	self.dir1_plus = Checkbutton(master,text='+',variable=_dir1PlusSet).grid(row=1,column=1)
	self.dir1_minus = Checkbutton(master,text='-',variable=_dir1MinusSet).grid(row=1,column=2)
	
	self.duration1_label = Label(master, text='Duration (in frames) : ').grid(row=2,column=0)
	self.duration1_val = Entry(master).grid(row=2,column=1)

	self.speed1_label = Label(master, text='Speed : ').grid(row=3,column=0)
	self.speed1_val = Entry(master).grid(row=3,column=1)

	'''
	Layout for the second stimulus: Direction, duration, speed
	'''
	self.direction2_label = Label(master, text='Direction shift: ').grid(row=5,column=0)

	_dir2PlusSet = IntVar()
	_dir2MinusSet = IntVar()
	self.dir2_plus = Checkbutton(master,text='+',variable=_dir2PlusSet).grid(row=5,column=1)
	self.dir2_minus = Checkbutton(master,text='-',variable=_dir2MinusSet).grid(row=5,column=2)
	
	self.duration2_label = Label(master, text='Duration (in frames) : ').grid(row=6,column=0)
	self.duration2_val = Entry(master).grid(row=6,column=1)

	self.speed2_label = Label(master, text='Speed : ').grid(row=7,column=0)
	self.speed2_val = Entry(master).grid(row=7,column=1)


	'''
	**************
	Radial Stimuli
	**************
	'''
	self.COLOR_OPTIONS = ["White","Gray","Red","Green","Blue","Yellow"]
	self.DIR_OPTIONS = ["Clockwise","Anti-Clockwise"]

	row_num = 9
	# set the radial stimuli label
	self.heading2 = Label(master, text='Radial Stimuli',fg='red',bg='black').grid(row=8,column=0,columnspan=3)
	
	####################
	self.well1_label = Label(master, text='Well 1',fg='white',bg='gray').grid(row=row_num,column=0,columnspan=2)
	self.th1_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=0)
	self.th1_val = Entry(master).grid(row=row_num+1,column=1)
	self.color1_label = Label(master, text='Color : ').grid(row=row_num+2,column=0)

	self.color1_val = StringVar(master)
	self.color1_val.set(self.COLOR_OPTIONS[0])
	self.color1_menu = apply(OptionMenu, (master, self.color1_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=1,sticky="ew")

	self.dr1_label = Label(master, text='Direction : ').grid(row=row_num+3,column=0)
	self.dr1_val = StringVar(master)
	self.dr1_val.set(self.DIR_OPTIONS[0])
	self.dr1_menu = apply(OptionMenu, (master, self.dr1_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=1,sticky="ew")
	
	####################
	self.well2_label = Label(master, text='Well 2',fg='white',bg='gray').grid(row=row_num,column=2,columnspan=2)
	self.th2_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=2,sticky=E)
	self.th2_val = Entry(master).grid(row=row_num+1,column=3)
	self.color2_label = Label(master, text='Color : ').grid(row=row_num+2,column=2,sticky=E)

	self.color2_val = StringVar(master)
	self.color2_val.set(self.COLOR_OPTIONS[0])
	self.color2_menu = apply(OptionMenu, (master, self.color2_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=3,sticky="ew")

	self.dr2_label = Label(master, text='Direction : ').grid(row=row_num+3,column=2,sticky=E)
	self.dr2_val = StringVar(master)
	self.dr2_val.set(self.DIR_OPTIONS[0])
	self.dr2_menu = apply(OptionMenu, (master, self.dr2_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=3,sticky="ew")
	####################

	self.well3_label = Label(master, text='Well 3',fg='white',bg='gray').grid(row=row_num,column=4,columnspan=2)

	self.th3_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=4,sticky=E)
	self.th3_val = Entry(master).grid(row=row_num+1,column=5)
	self.color3_label = Label(master, text='Color : ').grid(row=row_num+2,column=4,sticky=E)

	self.color3_val = StringVar(master)
	self.color3_val.set(self.COLOR_OPTIONS[0])
	self.color3_menu = apply(OptionMenu, (master, self.color3_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=5,sticky="ew")

	self.dr3_label = Label(master, text='Direction : ').grid(row=row_num+3,column=4,sticky=E)
	self.dr3_val = StringVar(master)
	self.dr3_val.set(self.DIR_OPTIONS[0])
	self.dr3_menu = apply(OptionMenu, (master, self.dr3_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=5,sticky="ew")
	####################

	row_num=row_num+4
	self.well4_label = Label(master, text='Well 4',fg='white',bg='gray').grid(row=row_num,column=0,columnspan=2)

	self.th4_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=0)
	self.th4_val = Entry(master).grid(row=row_num+1,column=1)
	self.color4_label = Label(master, text='Color : ').grid(row=row_num+2,column=0)

	self.color4_val = StringVar(master)
	self.color4_val.set(self.COLOR_OPTIONS[0])

	self.color4_menu = apply(OptionMenu, (master, self.color4_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=1,sticky="ew")

	self.dr4_label = Label(master, text='Direction : ').grid(row=row_num+3,column=0)
	self.dr4_val = StringVar(master)
	self.dr4_val.set(self.DIR_OPTIONS[0])
	self.dr4_menu = apply(OptionMenu, (master, self.dr4_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=1,sticky="ew")
	####################

	self.well5_label = Label(master, text='Well 5',fg='white',bg='gray').grid(row=row_num,column=2,columnspan=2)
	self.th5_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=2,sticky=E)
	self.th5_val = Entry(master).grid(row=row_num+1,column=3)
	self.color5_label = Label(master, text='Color : ').grid(row=row_num+2,column=2,sticky=E)

	self.color5_val = StringVar(master)
	self.color5_val.set(self.COLOR_OPTIONS[0])
	self.color5_menu = apply(OptionMenu, (master, self.color5_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=3,sticky="ew")

	self.dr5_label = Label(master, text='Direction : ').grid(row=row_num+3,column=2,sticky=E)
	self.dr5_val = StringVar(master)
	self.dr5_val.set(self.DIR_OPTIONS[0])
	self.dr5_menu = apply(OptionMenu, (master, self.dr5_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=3,sticky="ew")
	####################

	self.well6_label = Label(master, text='Well 6',fg='white',bg='gray').grid(row=row_num,column=4,columnspan=2)
	self.th6_label = Label(master, text='Thickness : ').grid(row=row_num+1,column=4,sticky=E)
	self.th6_val = Entry(master).grid(row=row_num+1,column=5)
	self.color6_label = Label(master, text='Color : ').grid(row=row_num+2,column=4,sticky=E)

	self.color6_val = StringVar(master)
	self.color6_val.set(self.COLOR_OPTIONS[0])
	self.color6_menu = apply(OptionMenu, (master, self.color6_val) + tuple(self.COLOR_OPTIONS)).grid(row=row_num+2,column=5,sticky="ew")

	self.dr6_label = Label(master, text='Direction : ').grid(row=row_num+3,column=4,sticky=E)
	self.dr6_val = StringVar(master)
	self.dr6_val.set(self.DIR_OPTIONS[0])
	self.dr6_menu = apply(OptionMenu, (master, self.dr6_val) + tuple(self.DIR_OPTIONS)).grid(row=row_num+3,column=5,sticky="ew")
	####################

        self.QUIT = Button(self)
        self.QUIT1 = Button(self)
        self.QUIT2 = Button(self)
        self.QUIT3 = Button(self)

        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit


        #self.hi_there.pack({"side": "left"})

	self.trigger = Button(self)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.pack()
        self.createWidgets(master)

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
