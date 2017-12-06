from Tkinter import *
from bounceballs import *


class Application(Frame):
    def createWidgets(self, master):

        row_num = 0
        self.heading1 = Label(master)
        self.heading1.grid(row=row_num, column=0, columnspan=2, sticky='ew')
        self.COLOR_OPTIONS = ["White", "Gray", "Red", "Green", "Blue", "Yellow"]

        '''
        Layout for the startle experiment: Durations of the different phases, speed, color
        '''
        self.title = Label(self.heading1, text='Startle stimulus', fg='red', bd=10, highlightbackground='red').grid(row=row_num, column=0, columnspan=2, sticky='ew')
        self.duration1_label = Label(self.heading1, text='Acclimatization Duration (t1): ')
        self.duration1_label.grid(row=(row_num + 3), column=0, sticky=E)
        self.duration1_val = Entry(self.heading1)
        self.duration1_val.grid(row=(row_num + 3), column=1)

        self.duration2_label = Label(self.heading1, text='Startle Duration (t2): ')
        self.duration2_label.grid(row=(row_num + 4), column=0, sticky=E)
        self.duration2_val = Entry(self.heading1)
        self.duration2_val.grid(row=(row_num + 4), column=1)

        self.duration3_label = Label(self.heading1, text='Recovery Duration (t3): ')
        self.duration3_label.grid(row=(row_num + 5), column=0, sticky=E)
        self.duration3_val = Entry(self.heading1)
        self.duration3_val.grid(row=(row_num + 5), column=1)

        self.speed1_label = Label(self.heading1, text='Speed : ')
        self.speed1_label.grid(row=(row_num + 6), column=0, sticky=E)
        self.speed1_val = Entry(self.heading1)
        self.speed1_val.grid(row=(row_num + 6), column=1)

        self.color_label = Label(self.heading1, text='Color : ').grid(row=row_num + 7, column=0, sticky=E)
        self.color_val = StringVar(self.heading1)
        self.color_val.set(self.COLOR_OPTIONS[0])
        self.color_menu = apply(OptionMenu, (self.heading1, self.color_val) + tuple(self.COLOR_OPTIONS))
        self.color_menu.grid(row=row_num + 7, column=1, sticky="ew")


        ####################
        self.qlabel = Label(master, fg='red', bd=10)
        self.qlabel.grid(row=row_num + 8, column=1, sticky='ew')
        self.quit = Button(self.qlabel, text='Exit the program!', command=self.quit)
        self.quit.grid(row=row_num + 8, column=1, sticky=E)

        ####################

        self.startlabel = Label(master, fg='red', bd=10)
        self.startlabel.grid(row=row_num + 8, column=0, sticky='ew')
        self.start = Button(self.startlabel, text='Start the experiment!', command=self.runExp)
        self.start.grid(row=row_num + 8, column=0, sticky=E)

    def runExp(self):
        '''
        get all the variables on the panel and call the function to display the stimuli
        '''
        t1 = int(self.duration1_val.get())
        t2 = int(self.duration2_val.get())
        t3 = int(self.duration3_val.get())
        sp = float(self.speed1_val.get())
        color = self.color_val.get()
        startleDisplayProtocol(t1,t2,t3,sp,color)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets(master)


root = Tk()
app = Application(master=root)
app.master.title("STIM Display")
app.mainloop()
root.destroy()
