from tkinter import *

class Dashboard(Frame):

    def __init__(self,master,db):
        super(Dashboard,self).__init__(master)
        self.grid(sticky=N+S+W+E)
        self.master=master
        self.db=db
        self.create_widgets()

    def create_widgets(self):

        row=0
        textfont=('verdana',10)

        self.opt=["Profile Details","Change Password","Logout"]
        for item in self.opt:
            Button(self,text=item,bg="#34495e",font=textfont,
                   relief=FLAT,
                   fg="white").grid(row=row,
                                    column=0,
                                    sticky=N+W+E)
            row+=1
        self.pack(side=TOP)
