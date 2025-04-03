from tkinter import *

class BaseGUI:
    def __init__(self, dimensions="250x240", title="Base GUI"):
        self.create_window(dimensions=dimensions, title=title)
        self.create_widgets()
    
    def create_window(self, dimensions, title):
        self.window = Tk()
        self.window.geometry(dimensions)
        self.window.title(title)
    
    def create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()