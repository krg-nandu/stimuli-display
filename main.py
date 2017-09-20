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
	self.duration1_val = Entry(master, text='0 ').grid(row=2,column=1)

	self.speed1_label = Label(master, text='Speed : ').grid(row=3,column=0)
	self.speed1_val = Entry(master, text='0 ').grid(row=3,column=1)

	'''
	Layout for the second stimulus: Direction, duration, speed
	'''
	self.direction2_label = Label(master, text='Direction shift: ').grid(row=5,column=0)

	_dir2PlusSet = IntVar()
	_dir2MinusSet = IntVar()
	self.dir2_plus = Checkbutton(master,text='+',variable=_dir2PlusSet).grid(row=5,column=1)
	self.dir2_minus = Checkbutton(master,text='-',variable=_dir2MinusSet).grid(row=5,column=2)
	
	self.duration2_label = Label(master, text='Duration (in frames) : ').grid(row=6,column=0)
	self.duration2_val = Entry(master, text='0 ').grid(row=6,column=1)

	self.speed2_label = Label(master, text='Speed : ').grid(row=7,column=0)
	self.speed2_val = Entry(master, text='0 ').grid(row=7,column=1)


	'''
	**************
	Radial Stimuli
	**************
	'''
	row_num = 9
	# set the radial stimuli label
	self.heading2 = Label(master, text='Radial Stimuli',fg='red',bg='black').grid(row=8,column=0,columnspan=3)

	self.well1_label = Label(master, text='Well 1',fg='white',bg='gray').grid(row=row_num,column=0)
	self.well2_label = Label(master, text='Well 2',fg='white',bg='gray').grid(row=row_num,column=1)
	self.well3_label = Label(master, text='Well 3',fg='white',bg='gray').grid(row=row_num,column=2)


	self.well4_label = Label(master, text='Well 4',fg='white',bg='gray').grid(row=row_num+1,column=0)
	self.well5_label = Label(master, text='Well 5',fg='white',bg='gray').grid(row=row_num+1,column=1)
	self.well6_label = Label(master, text='Well 6',fg='white',bg='gray').grid(row=row_num+1,column=2)

        self.QUIT = Button(self)
        self.QUIT1 = Button(self)
        self.QUIT2 = Button(self)
        self.QUIT3 = Button(self)

        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        #self.QUIT.pack({"side": "left"})

        #self.QUIT1.pack({"side": "left"})

        #self.QUIT2.pack({"side": "left"})

        #self.QUIT3.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

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
