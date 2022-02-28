import tkinter as tk
import json
from PIL import Image, ImageTk
from app import main

class Application(tk.Frame):
    def __init__(self, master=None, window=None):
        super().__init__(master)
        self.master = master
        self.window = window
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                            command=self.window.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

class Configs(tk.Frame):
    def __init__(self, master, config):
        super().__init__(master, bd=2)
        self.master = master
        self.config = config
        self.elements = {}
        self.pack(pady=15)
        self.create_widgets()
        

    def create_widgets(self):

        for counter,config_element in enumerate(self.config.keys()):
            if self.config[config_element]["type"] == "boolean":
                self.elements[config_element] = Switch(self, state=self.config[config_element]["value"], name = config_element).grid(row = counter, column = 1, sticky = "E")
                self.elements["Label_"+config_element] = tk.Label(self, text=self.config[config_element]["text"]).grid(row = counter, column = 0, sticky = "W")


class Switch(tk.Frame):
    def __init__(self,master=None, state=False, witdh=61, height=36, name = "switch"):
        super().__init__(master)
        self.name = name
        self.master = master
        self.state = state

        self.on_image = ImageTk.PhotoImage(Image.open("./vorlagebilder/ui/switch_on.png").resize((witdh,height), Image.ANTIALIAS))
        self.off_image = ImageTk.PhotoImage(Image.open("./vorlagebilder/ui/switch_off.png").resize((witdh,height), Image.ANTIALIAS))
     

        self.button = tk.Button(master = self, command = self.switch, image=self.on_image if self.state else self.off_image, bd = 0, highlightthickness = 1)
            

        self.button.pack()


    def switch(self):
        if self.state == True:
            self.button.config(image = self.off_image)
            self.state = False
            if type(self.master.config) == dict:
                self.master.config[self.name]["value"] = self.state

        else:
            self.button.config(image = self.on_image)
            self.state = True
            if type(self.master.config) == dict:
                self.master.config[self.name]["value"] = self.state


class Button_Switch(tk.Frame):
    def __init__(self,master=None, state=False, command_on = None, command_off = None, witdh=61, height=36, text_on = "On", text_off = "Off"):
        super().__init__(master)
        self.master = master
        self.state = state
        self.text_on = text_on
        self.text_off = text_off
        self.command_off = command_off
        self.command_on = command_on
        self["bg"] = "red"

        self.button = tk.Button(master = self, text = text_on if state == False else text_off, command = self.switch, bd = 0, highlightthickness = 1)

        self.button.pack(pady=(0,4))


    def switch(self):
        if self.state == True:
            self.config(bg="red")
            self.button["text"] = self.text_on
            self.command_off()
            self.state = False

        else:
            self.config(bg="green")
            self.button["text"] = self.text_off
            self.command_on()
            self.state = True



class Task_UI(tk.Frame):
    """
    This class gets displayed when the Browser is started.
    
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Main"
        self.hi_there["command"] = main
        self.hi_there.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                            command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

