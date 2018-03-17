from tkinter import *
from src.dependencies.Login2 import *
from tkinter import messagebox
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root=Tk()
root.title("Digital Asset Management")
root.attributes("-fullscreen",True)

def end_fullscreen(self):
    x=messagebox.askyesno("EXIT","Are you sure?")
    if x:
        root.destroy()

def focus_next(event):
    event.widget.tk_focusNext().focus()
    return("break")

root.bind("<Escape>",end_fullscreen)
root.bind_class('Entry',"<Return>",focus_next)
root.bind_class('Radiobutton',"<Return>",focus_next)
root.bind_class('Button',"<Return>",focus_next)
root.bind_class('Frame',"<Return>",focus_next)

mainframe = Frame(root,bg="#5ee5cc")
mainframe.grid(sticky=N+S+W+E)

titleframe=Frame(mainframe,bd=4,bg="#e3e5e3",relief=RIDGE)
titleframe.grid(row=0,column=0,sticky=N+W+E)
titleframe.columnconfigure(1,weight=1)
titleframe.rowconfigure(0,weight=2)
titleframe.rowconfigure(1,weight=1)
titleframe.rowconfigure(2,weight=1)

img=PhotoImage(file=resource_path('src\img\logo.png'))
head=Label(titleframe,image=img,bg="#e3e5e3").grid(row=0,rowspan=3,column=0)
titlefont=('times',30,'bold')
Label(titleframe,text="DIGITAL ASSETS",bg="#e3e5e3",
           font=titlefont).grid(row=0,column=1)
titlefont=('times',14,'italic')
Label(titleframe,text="Developed by: Sohail Chamadia",bg="#e3e5e3",
           font=titlefont).grid(row=1,column=1)
titlefont=('times',14,'italic')
Label(titleframe,text="For further details contact: +91-8460766696",bg="#e3e5e3",
           font=titlefont).grid(row=2,column=1)

img2=PhotoImage(file=resource_path('src\img\logo2.png'))
comp=Label(titleframe,image=img2,bg="#e3e5e3").grid(row=0,rowspan=3,column=2)

bodyframe=Frame(mainframe,bg="#34495e")#"#16a085"
bodyframe.grid(row=1,column=0,sticky=N+S+W+E)
Login2(bodyframe)

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)

root.mainloop()
