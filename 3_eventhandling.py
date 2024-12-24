from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):

        ttk.Label(master, text="Greetings in Alolan and Normal language!").grid(row=0, column=0)

        self.label=ttk.Label(master,text="Hello, Tkinter!")
        self.label.grid(row=1,column=0, columnspan=2)

        ttk.Button(master,text="Alola",command=self.alola_hello).grid(row=2,column=0)
        ttk.Button(master,text="Normal",command=self.normal_hello).grid(row=2,column=1)

    def alola_hello(self):
        self.label.config(text="Alola, Tkinter!")
    def normal_hello(self):
        self.label.config(text="Hello, Tkinter!")
     
def main():
    root=Tk()
    app=HelloApp(root)
    root.mainloop()

if __name__=="__main__": main()