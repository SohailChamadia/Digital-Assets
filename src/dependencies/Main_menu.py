from tkinter import *
import math

class Main_menu(Frame):

    def __init__(self,master,db,admin_access):
        super(Main_menu,self).__init__(master)
        self.grid(sticky=N+S+W+E)
        self.master=master
        self.admin_access=admin_access
        self.db=db
        self.create_widgets()

    def create_widgets(self):

        self.frames=["Equipment Entry","Software details","AMC Details"
                    ,"Update/Repair Details", "Vendor Details","Transfer Details",
                     "Item Issue/ Return Details","Purchase Order Details"]
        self.admin_frames=["Staff Master","User Master","Item Master","Department Master"]
        self.user_cnt=8;
        if self.admin_access:
            self.user_cnt=0;
            self.frames.extend(self.admin_frames)
        self.count=1;

        textfont=('verdana',10)

        width=(self.master.winfo_screenwidth())//(14*len(self.frames))

        mainframe = Frame(self,bg="#34495e")
        mainframe.grid(row=0,column=0,columnspan=3,sticky=N+W+E)

        self.opt=[]
        for items in self.frames:
            self.opt.append(Button(mainframe,
                                   text=items,
                                   relief=GROOVE,
                                   font=textfont,
                                   bg="#bdc3c7",
                                   activebackground="#bdc3c7",
                                   height=2,
                                   wraplength=110,
                                   width=width,
                                   command=lambda name=items,ref=self.count-1:self.selection(ref,name)
                                   ))
            self.opt[-1].grid(row=0,
                              column=self.count,
                              ipadx=16+self.user_cnt,
                              sticky=N+S+W+E)
            self.count+=1
        self.dashboard=Frame(self,bg="#34495e")
        self.dashboard.grid(row=1,column=0,sticky=N+S+W+E)
        #X=__import__('dashboard')
        #X.Dashboard(self.dashboard,self.db)

        self.content=Frame(self,bg="#34495e")
        self.content.grid(row=1,column=1,sticky=N+S+W+E)
        self.opt[0].config(bg="black",fg="white")
        self.content.depts=self.master.depts
        self.content.admin_access=self.admin_access
        X=__import__('src.dependencies.Equipment',fromlist=('Equipment'))
        X.Equipment(self.content,self.db,True)

        self.error=Frame(self,bg="#34495e")
        self.error.grid(row=1,column=2,sticky=N+S+W+E)
        #X=__import__('dashboard')
        #X.Dashboard(self.error,self.db)

        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)

        self.columnconfigure(0,weight=1)
        #self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(1,weight=1)

    def selection(self,ref,item):
        for cnt in range(self.count-1):
            self.opt[cnt].config(bg="#bdc3c7",fg="black")
        self.opt[ref].config(bg="black",fg="white")
        self.content.destroy()
        self.content = Frame(self,bg="#34495e",relief=GROOVE)
        self.content.grid(row=1,column=1,sticky=N+S+W+E)
        self.content.admin_access=self.admin_access
        self.content.focus_set()
        self.content.depts=self.master.depts
        if item == "Equipment Entry":
            X = __import__('src.dependencies.Equipment',fromlist=('Equipment'))
            X.Equipment(self.content,self.db,True)
        elif item=="Software details":
            X=__import__('src.dependencies.Software_master',fromlist=('Software_master'))
            X.Software_master(self.content,self.db)
        elif item=="AMC Details":
            X=__import__('src.dependencies.Amc_details',fromlist=('Amc_details'))
            X.Amc_details(self.content,self.db)
        elif item=="Update/Repair Details":
            X=__import__('src.dependencies.Update_details',fromlist=('Update_details'))
            X.Update_details(self.content,self.db)
        elif item=="Vendor Details":
            X=__import__('src.dependencies.Vendor_details',fromlist=('Vendor_details'))
            X.Vendor_details(self.content,self.db,True)
        elif item=="Transfer Details":
            X=__import__('src.dependencies.Transfer_details',fromlist=('Transfer_details'))
            X.Transfer_details(self.content,self.db)
        elif item=="Item Issue/ Return Details":
            X=__import__('src.dependencies.Item_issue',fromlist=('Item_issue'))
            X.Item_issue(self.content,self.db)
        elif item=="Purchase Order Details":
            X=__import__('src.dependencies.Purchase_details',fromlist=('Purchase_details'))
            X.Purchase_details(self.content,self.db,True)
        elif item=="Staff Master":
            X=__import__('src.dependencies.Staff_master',fromlist=('Staff_master'))
            X.Staff_master(self.content,self.db,True)
        elif item=="User Master":
            X=__import__('src.dependencies.User_master',fromlist=('User_master'))
            X.User_master(self.content,self.db)
        elif item=="Item Master":
            X=__import__('src.dependencies.Item_master',fromlist=('Item_master'))
            X.Item_master(self.content,self.db,True)
        elif item=="Department Master":
            X=__import__('src.dependencies.Department_master',fromlist=('Department_master'))
            X.Department_master(self.content,self.db,True)
