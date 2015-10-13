import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.hi_there = tk.Button(self, activebackground='blue', bg='magenta')
        self.hi_there["text"] = "You know you want to \n click me."
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.butt = tk.Button(self, activebackground='white', bg='blue')
        self.butt["text"] = "I'm not dead yet!"
        self.butt["command"] = self.the_grail
        self.butt.pack()#00ffff

        self.QUIT = tk.Button(self, text="Go away. These aren't your coconuts.", fg="black",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

        self.putThings = tk.Entry(self, bd='4', width='18')
        self.putThings.pack(side="bottom")


    def say_hi(self):
        print("These are a lovely bunch of coconuts and they're ALL MINE.")

    def the_grail(self):
        print("I SWEAR I\'M NOT DEAD YET!")





root = tk.Tk()
app = Application(master=root)
app.mainloop()
