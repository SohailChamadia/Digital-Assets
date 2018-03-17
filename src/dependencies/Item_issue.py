from src.dependencies.imports import *

class Item_issue(LabelFrame):

    def __init__(self,master,db):
        super(Item_issue,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.depts=self.master.depts
        self.machines=[]
        self.db=db
        self.create_widgets()

    def create_widgets(self):

        row=0;
        self.config(text="Item Issue/Return Details",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self,text="Type: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.iss_type=BooleanVar()
        self.iss_type.set(False)
        Radiobutton(self,text="Issue",
                    font=textfont,bg="#bdc3c7",
                    variable=self.iss_type,
                    command=self.issue_form,
                    value=True).grid(row=row,column=1,
                                     sticky=W)
        self.ret_type=BooleanVar()
        self.ret_type.set(False)
        Radiobutton(self,text="Return",
                    font=textfont,bg="#bdc3c7",
                    variable=self.ret_type,
                    command=self.return_form,
                    value=True).grid(row=row,column=2,
                                     sticky=W)
        row+=1

        self.type_err=StringVar()
        self.type_err.set("")
        Label(self,textvariable=self.type_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Machine ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.id=StringVar();
        self.id.set("")
        self.id_opt=combo(self,self.machines,self.id,True)
        self.id_opt.grid(row=row,column=1,sticky=W+E)
        for chl in self.id_opt.children.values():
            chl.bind('<Control-space>',self.new_equipment)
        self.fetch=Button(self,text="Fetch",fg="white",
                           bg="#34495e",font=textfont,
                           command=self.item_return,width=8,
                           state=DISABLED)
        self.fetch.grid(row=row,
                        column=2,
                        sticky=E)

        row+=1

        self.id_err=StringVar()
        self.id_err.set("")
        Label(self,textvariable=self.id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Issue Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.issue=Entry(self,
                         state=DISABLED)
        self.issue.grid(row=row,
                        column=1,
                        sticky=W+E)
        self.issue_select=Button(self,text="Calendar",fg="white",
                                 bg="#34495e",font=textfont,
                                 command=self.selectdate,width=8,
                                 state=DISABLED)
        self.issue_select.grid(row=row,
                               column=2,
                               sticky=E)

        row+=1

        self.issue_err=StringVar()
        self.issue_err.set("")
        Label(self,textvariable=self.issue_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Issued by: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.issby=Entry(self,
                         state=DISABLED);
        self.issby.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.issby_err=StringVar()
        self.issby_err.set("")
        Label(self,textvariable=self.issby_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Issued to: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.issto=Entry(self,
                         state=DISABLED);
        self.issto.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.issto_err=StringVar()
        self.issto_err.set("")
        Label(self,textvariable=self.issto_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Return Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.ret=Entry(self,
                       state=DISABLED)
        self.ret.grid(row=row,
                      column=1,
                      sticky=W+E)
        self.ret_select=Button(self,text="Calendar",fg="white",
                               bg="#34495e",font=textfont,
                               command=self.selectdate,width=8,
                               state=DISABLED)
        self.ret_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.ret_err=StringVar()
        self.ret_err.set("")
        Label(self,textvariable=self.ret_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Returned to: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.retto=Entry(self,
                         state=DISABLED);
        self.retto.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.retto_err=StringVar()
        self.retto_err.set("")
        Label(self,textvariable=self.retto_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Returned on: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.reton=Entry(self,
                         state=DISABLED)
        self.reton.grid(row=row,
                        column=1,
                        sticky=W+E)
        self.reton_select=Button(self,text="Calendar",fg="white",
                                 bg="#34495e",font=textfont,
                                 command=self.selectdate,width=8,
                                 state=DISABLED)
        self.reton_select.grid(row=row,
                               column=2,
                               sticky=E)
        row+=1

        self.reton_err=StringVar()
        self.reton_err.set("")
        Label(self,textvariable=self.reton_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Remarks: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.rem=Text(self,width=40,height=5,wrap=WORD)
        self.rem.grid(row=row,column=1,columnspan=2,sticky=W+E)
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

        self.pack(anchor=CENTER,expand=1)

    def selectdate(self):
        X=__import__('calendar_ui')
        self.expiry_date=X.CalendarWidget(self.master)
        #self.expire.insert(0,self.expiry_date.selection())

    def new_equipment(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Equipment",fromlist=('Equipment'))
        self.z=X.Equipment(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.setDaemon(True)
        t.start()

    def call_pack(self):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
        except:
            pass

    def item_return(self):
        self.db.connect()
        cur=self.db.execute_sql("""select * from item_issue
                                where machine_id='%s' and issue='1';"""
                                %(self.id.get()))
        data=list(cur.fetchall())
        self.issue.config(state=NORMAL)
        self.issby.config(state=NORMAL)
        self.issto.config(state=NORMAL)
        self.ret.config(state=NORMAL)
        self.issue.insert(0,data[0][2])
        self.issby.insert(0,data[0][3])
        self.issto.insert(0,data[0][4])
        self.ret.insert(0,data[0][5])
        self.rem.insert("1.0",data[0][8])
        self.issue.config(state=DISABLED)
        self.issby.config(state=DISABLED)
        self.issto.config(state=DISABLED)
        self.ret.config(state=DISABLED)
        self.db.close()

    def issue_form(self):
        self.machines=[]
        dpt=[]
        for items in self.depts:
            tmp=(items.split(" - "))
            dpt.append(tmp[0])
        if len(dpt)==1:
            dpt="("+dpt[0]+")"
        else:
            dpt=str(tuple(dpt))
        x=self.db.execute_sql("""select machine from equipment
                                where issuable='1'
                                and department in %s;"""%(dpt))
        z=list(x.fetchall())
        for mach in z:
            self.machines.append(mach[0])
        x=self.db.execute_sql("""select machine_id from item_issue
                                where issue='1';""")
        z=list(x.fetchall())
        for mach in z:
            self.machines.remove(mach[0])
        self.id_opt.value_config(self.machines)
        self.id.set("")
        self.ret_type.set(False)
        self.issue.config(state=NORMAL)
        self.issto.config(state=NORMAL)
        self.issby.config(state=NORMAL)
        self.ret.config(state=NORMAL)
        self.issue_select.config(state=NORMAL)
        self.ret_select.config(state=NORMAL)
        self.issue.delete(0,END)
        self.issby.delete(0,END)
        self.issto.delete(0,END)
        self.ret.delete(0,END)
        self.rem.delete("1.0",END)
        self.retto.delete(0,END)
        self.retto.config(bg="white",state=DISABLED)
        self.retto_err.set("")
        self.reton.delete(0,END)
        self.reton.config(bg="white",state=DISABLED)
        self.reton_err.set("")
        self.reton_select.config(state=DISABLED)
        self.fetch.config(state=DISABLED)

    def return_form(self):
        self.machines=[]
        cur=self.db.execute_sql("""select machine_id from item_issue
                                where issue='1';""")
        z=list(cur.fetchall())
        for mach in z:
            self.machines.append(mach[0])
        self.id_opt.value_config(self.machines)
        self.id.set("")
        self.iss_type.set(False)
        self.issue.delete(0,END)
        self.issue.config(bg="white",state=DISABLED)
        self.issue_err.set("")
        self.issto.delete(0,END)
        self.issto.config(bg="white",state=DISABLED)
        self.issto_err.set("")
        self.issby.delete(0,END)
        self.issby.config(bg="white",state=DISABLED)
        self.issby_err.set("")
        self.issue_select.config(state=DISABLED)
        self.ret_select.config(state=DISABLED)
        self.ret.delete(0,END)
        self.ret.config(bg="white",state=DISABLED)
        self.ret_err.set("")
        self.retto.config(state=NORMAL)
        self.reton.config(state=NORMAL)
        self.reton_select.config(state=NORMAL)
        self.fetch.config(state=NORMAL)

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        if not self.iss_type.get() and not self.ret_type.get():
            self.type_err.set("Select Type")
            comp.set("False")
        else:
            self.type_err.set("")
            comp.set("True")
        if self.iss_type.get():
            msg.set("This field cannot be empty")
            check_ent(self.issby,comp,msg,self.issby_err)
            msg.set("This field cannot be empty")
            check_ent(self.issto,comp,msg,self.issto_err)
            msg.set("Invalid Issue Date")
            check_date(self.issue,comp,msg,self.issue_err)
            msg.set("Invalid Return Date")
            check_date(self.ret,comp,msg,self.ret_err)
            msg.set("Return date should be after Issue date")
            comp_date(self.issue,self.ret,comp,msg,self.ret_err)
        if self.ret_type.get():
            msg.set("This field cannot be empty")
            check_date(self.reton,comp,msg,self.reton_err)
            msg.set("This field cannot be empty")
            check_ent(self.retto,comp,msg,self.retto_err)
        msg.set("Machine ID cannot be empty")
        check_stvar(self.id,self.machines,comp,msg,self.id_err)
        try:
            self.db.connect()
            if comp.get():
                if self.iss_type.get():
                    self.db.execute_sql("""insert into item_issue
                                        values(%d,'%s','%s','%s','%s','%s',NULL,NULL,'%s');"""
                                            %(self.iss_type.get(),
                                              self.id.get(),
                                              self.issue.get(),
                                              self.issby.get(),
                                              self.issto.get(),
                                              self.ret.get(),
                                              self.rem.get("1.0",END)
                                        ))
                else:
                    self.db.execute_sql("""update item_issue
                                        set issue=%d,return_on='%s',ret_accepted_by='%s',remark='%s'
                                        where machine_id='%s' and issue='%s';"""
                                            %(self.iss_type.get(),
                                              self.reton.get(),
                                              self.retto.get(),
                                              self.rem.get("1.0",END),
                                              self.id.get(),
                                              self.ret_type.get()
                                        ))
                self.reset()
        except pw.IntegrityError as e:
            print(e)
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        Item_issue(self.master,self.db)
