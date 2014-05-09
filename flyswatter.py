#!/usr/bin/python

FIFOLOC = 'fifo'
OUTPLOC = '/home/ian/.config/pianobarfly/current.txt'


import Tkinter

class Pianobar(object):
    def __init__(self, parent):
        self.parent = parent

        
    def playpause(self):
        with open(FIFOLOC, 'a') as out:             
            out.write('p')          
    
    def skip(self):
        with open(FIFOLOC, 'a') as out:             
            out.write('n')
	
    def love(self):
        with open(FIFOLOC, 'a') as out:             
            out.write('+')
	
    def ban(self):
        with open(FIFOLOC, 'a') as out:             
            out.write('-')
   
    def quitP(self):
        with open(FIFOLOC, 'a') as out:             
            out.write('q') 
        quit()

    def changeStation(parent):
        pass

    def updateLabel(self):
        with open(OUTPLOC, 'r') as inp:
             self.parent.labelVariable.set( inp.read())

        self.parent.after(1000, self.updateLabel) 


class Controller(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.labelVariable = Tkinter.StringVar() 
        self.pianobar = Pianobar(self)
        self.initialize()

    def initialize(self):
        self.grid()

        # Buttons
        playpause = Tkinter.Button(self, text=u"Play/Pause",
                                        command=self.pianobar.playpause)
        skip  = Tkinter.Button(self, text=u"Next", command=self.pianobar.skip)
        love = Tkinter.Button(self, text=u"Love", command=self.pianobar.love)
        ban = Tkinter.Button(self, text=u"Ban", command=self.pianobar.ban)
        playpause.grid(column=1,row=1)
        skip.grid(column=2,row=1)
        love.grid(column=1,row=0)
        ban.grid(column=1,row=2)


        # Menu
        options = Tkinter.Menubutton(self, text=u"Options") #, 
                                        #command=self.pianobar.newStation)
        options.menu = Tkinter.Menu(options)
        options['menu'] = options.menu 
        options.menu.add('command', label=u"change Station...", 
                               command=self.pianobar.changeStation)
        options.menu.add('command', label=u"Quit", 
                               command=self.pianobar.quitP)
        options.grid(column=0,row=1)

        # Info
        self.labelVariable = Tkinter.StringVar()
        info = Tkinter.Message(self, textvariable=self.labelVariable,
                             anchor='w', width=500)
        info.grid(column=0,row=3,columnspan=3,sticky='EW')
        self.pianobar.updateLabel()



if __name__ == "__main__":
    app = Controller(None) 
    app.mainloop()

