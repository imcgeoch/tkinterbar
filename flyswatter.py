#!/usr/bin/python

import Tkinter

class Pianobar(object):
    def playpause(parent):
        pass
    def skip(parent):
        pass
    def love(parent):
        pass
    def ban(parent):
        pass
    def changeStation(parent):
        pass



class Controller(Tkinter.Tk):
    def __init__(self,parent,pianobar):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.pianobar = pianobar
        
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

        options.grid(column=0,row=1)

        # Info
        self.labelVariable = Tkinter.StringVar()
        info = Tkinter.Label(self, textvariable=self.labelVariable,
                             anchor='w')
        info.grid(column=0,row=3,columnspan=3,sticky='EW')



if __name__ == "__main__":
    pianobar = Pianobar()
    app = Controller(None,pianobar) 
    app.mainloop()

