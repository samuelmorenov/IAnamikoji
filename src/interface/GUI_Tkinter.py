# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import *

class GUI_Tkinter:
    def __init__(self):
        self.window = Tk();
        return
    
    def start(self):
        self.window.mainloop()
        