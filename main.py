from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self,master):

	# set the linear stimuli label
	self.heading1 = Label(master, text='Linear Stimuli').grid(row=0,column=1)
	#self.heading1.pack()

	self.direction1_label = Label(master, text='Initial Direction : ').grid(row=1,column=0)
	#self.direction1_label.pack()

	_dir1PlusSet = IntVar()
	_dir1MinusSet = IntVar()
	self.dir1_plus = Checkbutton(master,text='+',variable=_dir1PlusSet).grid(row=1,column=1)
	self.dir1_minus = Checkbutton(master,text='-',variable=_dir1MinusSet).grid(row=1,column=2)
	
	self.duration_label = Label(master, text='Duration (in frames) : ').grid(row=2,column=0)
	self.duration_val = Entry(master, text='0 ').grid(row=2,column=1)

	# set the radial stimuli label
	self.heading2 = Label(self, text='Radial Stimuli')

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
