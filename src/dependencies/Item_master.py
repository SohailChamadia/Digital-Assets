from src.dependencies.imports import *

class Item_master(LabelFrame):

    def __init__(self,master,db,flag):
        super(Item_master,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.db=db
        self.flag=flag
        self.db.connect()
        x=self.db.execute_sql("select items from item_master")
        z=list(x.fetchall())
        self.item=[]
        for items in z:
            self.item.append(items[0])
        self.db.close()
        self.create_widgets()
        if not self.flag:
            self.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Label)
                              or isinstance(w,Radiobutton)
                              or isinstance(w,Checkbutton),self.children.values()):
                lab.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Button) ,self.children.values()):
                lab.config(bg="#9b9039")

    def create_widgets(self):
        row=0;

        self.config(text="Item Master",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self,text="Items: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.items=Listbox(self,height=15)
        self.items.grid(row=row,column=1,columnspan=2,pady=10,sticky=N+S+W+E)
        scr=Scrollbar(self.items)
        scr.pack(side=RIGHT,fill=Y)
        self.items.config(yscrollcommand=scr.set)
        self.items.pack_propagate(False)
        scr.config(command=self.items.yview)

        self.items.bind('<ButtonRelease-1>',self.update_entry)

        for itm in self.item:
            self.items.insert(END,itm)
        row+=1

        Label(self,text="Command: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.yn=["Insert","Delete"]
        self.cmd=StringVar();
        self.cmd.set(False)
        cnt=0
        for items in self.yn:
            Radiobutton(self,text=items,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.cmd,
                        value=items).grid(row=row,column=1+cnt,
                                          sticky=W)
            cnt+=1
        row+=1

        self.cmd_err=StringVar()
        self.cmd_err.set("")
        Label(self,textvariable=self.cmd_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Item name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.name=Entry(self);
        self.name.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.name_err=StringVar()
        self.name_err.set("")
        Label(self,textvariable=self.name_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Button(self,text="SUBMIT",bg="#34495e",font=textfont,
               command=self.submit,fg="white",
               width=12).grid(row=row,
                              column=1,
                              pady=15)
        Button(self,text="RESET",bg="#34495e",font=textfont,
               command=self.reset,fg="white",
               width=12).grid(row=row,
                              column=2,
                              pady=15)

        if not self.flag:
            Button(self,text="BACK",bg="#34495e",font=textfont,
                   command=self.destroy,fg="white",
                   width=12).grid(row=row,
                                  column=0,
                                  pady=15)

        self.pack(anchor=CENTER,expand=1)

    def update_entry(self,event):
        self.name.delete(0,END)
        self.name.insert(0,self.items.get(self.items.curselection()))

    def db_check(self):
        uniq=BooleanVar()
        uniq.set(False)
        if self.cmd.get() == "Delete":
            if self.name.get() in self.item:
                uniq.set(True)
                self.name.config(bg="white")
                self.name_err.set("")
            else:
                self.name_err.set("Item doesn't exists")
                self.name.config(bg="#ffdbdb")
        elif self.cmd.get()!="Insert":
            self.cmd_err.set("Select Command")
        else:
            self.cmd_err.set("")
            uniq.set(True)
        return(uniq.get())

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Name cannot be empty")
        check_ent(self.name,comp,msg,self.name_err)
        try:
            self.db.connect()
            if self.db_check() and comp.get():
                if self.cmd.get()=="Insert":
                    self.db.execute_sql("""insert into item_master
                                            values('%s');"""
                                            %(self.name.get()))
                elif self.cmd.get()=="Delete":
                    self.db.execute_sql("""delete from item_master where
                                            items='%s';"""
                                            %(self.name.get()))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1062:
                self.name_err.set("Item already exists")
                self.name.config(bg="#ffdbdb")
            else:
                self.name.config(bg="white")
                self.name_err.set("")
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        if self.flag:
            Item_master(self.master,self.db,True)
