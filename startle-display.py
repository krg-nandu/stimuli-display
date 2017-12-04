from Tkinter import *
from bounceballs import *


class Application(Frame):
    def createWidgets(self, master):

        '''
        **************
        Linear Stimuli
        **************
        '''
        row_num = 0
        # set the linear stimuli label
        self.heading1 = Label(master, text='Startle stimulus', fg='red', bd=10, highlightbackground='red')
        self.heading1.grid(row=row_num, column=0, columnspan=3, sticky='ew')

        '''
        Layout for the startle experiment: Durations of the different phases, speed, color
        '''
        self.duration1_label = Label(self.heading1, text='Acclimatization Duration : ')
        self.duration1_label.grid(row=(row_num + 3), column=0)
        self.duration1_val = Entry(self.heading1)
        self.duration1_val.grid(row=(row_num + 3), column=1)

        self.duration2_label = Label(self.heading1, text='Startle Duration : ')
        self.duration2_label.grid(row=(row_num + 4), column=0)
        self.duration2_val = Entry(self.heading1)
        self.duration2_val.grid(row=(row_num + 4), column=1)

        self.duration3_label = Label(self.heading1, text='Recovery Duration : ')
        self.duration3_label.grid(row=(row_num + 5), column=0)
        self.duration3_val = Entry(self.heading1)
        self.duration3_val.grid(row=(row_num + 5), column=1)

        self.speed1_label = Label(self.heading1, text='Speed : ')
        self.speed1_label.grid(row=(row_num + 6), column=0)
        self.speed1_val = Entry(self.heading1)
        self.speed1_val.grid(row=(row_num + 6), column=1)

        ####################
        self.qlabel = Label(master, fg='red', bd=10)
        self.qlabel.grid(row=row_num + 2, column=5, columnspan=4, sticky='ew')
        self.quit = Button(self.qlabel, text='Exit the program!', command=self.quit)
        self.quit.grid(row=row_num + 2, column=5, sticky=E)

        ####################

        self.startlabel = Label(master, fg='red', bd=10)
        self.startlabel.grid(row=row_num + 2, column=0, columnspan=4, sticky='ew')
        self.start = Button(self.startlabel, text='Start the experiment!', command=self.runExp)
        self.start.grid(row=row_num + 2, column=0, sticky=E)

    def toggleGroup(self, group, value):
        if value == 1:
            objstate = 'disabled'
        elif value == 0:
            objstate = 'normal'

        for w in group.winfo_children():
            w.configure(state=objstate)

    def selectHGratings(self):
        self.toggleGroup(self.heading3, self.hgvar.get())
        self.toggleGroup(self.heading2, self.hgvar.get())
        self.toggleGroup(self.heading4, self.hgvar.get())

    def selectVGratings(self):
        self.toggleGroup(self.heading1, self.vgvar.get())
        self.toggleGroup(self.heading2, self.vgvar.get())
        self.toggleGroup(self.heading4, self.vgvar.get())

    def selectRad(self):
        self.toggleGroup(self.heading1, self.radVar.get())
        self.toggleGroup(self.heading3, self.radVar.get())
        self.toggleGroup(self.heading4, self.radVar.get())

    def selectNoStim(self):
        self.toggleGroup(self.heading1, self.nostimVar.get())
        self.toggleGroup(self.heading3, self.nostimVar.get())
        self.toggleGroup(self.heading2, self.nostimVar.get())

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
                dir1 = dir1 + '+'
            else:
                dir1 = dir1 + '-'

            if (self._dir2PlusSet.get() == 1):
                dir2 = dir2 + '+'
            else:
                dir2 = dir2 + '-'
            displayHorizontalGrating(float(self.duration1_val.get()), float(self.speed1_val.get()), dir1,
                                     float(self.duration2_val.get()), float(self.speed2_val.get()), dir2,
                                     float(self.hthick_val.get()))

        elif self.vgvar.get() == 1:
            # VERTICAL GRATING
            dir1 = ''
            dir2 = ''
            if (self._dir1bPlusSet.get() == 1):
                dir1 = dir1 + '+'
            else:
                dir1 = dir1 + '-'

            if (self._dir2bPlusSet.get() == 1):
                dir2 = dir2 + '+'
            else:
                dir2 = dir2 + '-'
            displayVerticalGrating(float(self.duration1b_val.get()), float(self.speed1b_val.get()), dir1,
                                   float(self.duration2b_val.get()), float(self.speed2b_val.get()), dir2,
                                   float(self.vthick_val.get()))
        elif self.radVar.get() == 1:
            # RADIAL STIMULI
            directions = [self.dr1_val.get(), self.dr2_val.get(), self.dr3_val.get(), self.dr4_val.get(),
                          self.dr5_val.get(), self.dr6_val.get()]
            colors = [self.color1_val.get(), self.color2_val.get(), self.color3_val.get(), self.color4_val.get(),
                      self.color5_val.get(), self.color6_val.get()]
            colors_wheel = [self.color1wh_val.get(), self.color2wh_val.get(), self.color3wh_val.get(),
                            self.color4wh_val.get(), self.color5wh_val.get(), self.color6wh_val.get()]
            thicknesses = [float(self.th1_val.get()), float(self.th2_val.get()), float(self.th3_val.get()),
                           float(self.th4_val.get()), float(self.th5_val.get()), float(self.th6_val.get())]
            speeds = [float(self.sp1_val.get()), float(self.sp2_val.get()), float(self.sp3_val.get()),
                      float(self.sp4_val.get()), float(self.sp5_val.get()), float(self.sp6_val.get())]
            displayCircularStimuli(directions, colors, colors_wheel, thicknesses, speeds,
                                   int(self.radDuration_val.get()))
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
