from src.dependencies.imports import *

class Department_master(LabelFrame):

    def __init__(self,master,db,flag):
        super(Department_master,self).__init__(master)

        labelfont=('times',16,'bold')
        self.canvas = Canvas(self,bg="#bdc3c7")
        self.frame = LabelFrame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(anchor=CENTER, expand=1)
        self.canvas.create_window((0,0), window=self.frame, anchor="n",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.frame.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.db=db
        self.flag=flag
        self.dept=self.master.depts
        self.create_widgets()
        if not self.flag:
            self.frame.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Label)
                              or isinstance(w,Radiobutton)
                              or isinstance(w,Checkbutton),self.frame.children.values()):
                lab.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Button) ,self.frame.children.values()):
                lab.config(bg="#9b9039")

    def create_widgets(self):

        row=0;
        self.frame.config(text="Department/Laboratory Master",
                          relief=FLAT,
                          labelanchor=N,
                          padx=30,
                          pady=10)

        textfont=('verdana',10)
        errorfont=('verdana',8)
        titlefont=('verdana',12,'bold')

        Label(self.frame,text="Form type: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.modes=["Department","Laboratory"]
        self.mode=[IntVar(),IntVar()]
        cnt=0
        for item in self.modes:
            Checkbutton(self.frame,text=item,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.mode[cnt],
                        command= lambda x=item:self.open(x),
                        ).grid(row=row,column=1+cnt,
                               ipady=10,sticky=W)
            cnt+=1
        row+=1

        self.type_err=StringVar()
        self.type_err.set("")
        Label(self.frame,textvariable=self.type_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Command: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.yn=["Insert","Delete"]
        self.cmd=StringVar();
        self.cmd.set(None)
        cnt=0
        for items in self.yn:
            Radiobutton(self.frame,text=items,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.cmd,
                        command=self.cmd_call,
                        value=items).grid(row=row,
                                          column=1+cnt,
                                          sticky=W)
            cnt+=1
        row+=1

        self.cmd_err=StringVar()
        self.cmd_err.set("")
        Label(self.frame,textvariable=self.cmd_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Department Details",
              font=titlefont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                columnspan=3,
                                                sticky=N+S+W+E)
        row+=1

        Label(self.frame,text="Departments: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)

        self.depts=Listbox(self.frame,height=5,state=DISABLED)
        self.depts.grid(row=row,column=1,columnspan=2,pady=10,sticky=N+S+W+E)
        scr=Scrollbar(self.depts)
        scr.pack(side=RIGHT,fill=Y)
        self.depts.config(yscrollcommand=scr.set)
        self.depts.pack_propagate(False)
        scr.config(command=self.depts.yview)

        row+=1

        self.depts.bind('<ButtonRelease-1>',self.update_entry)

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Department ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.id=Entry(self.frame,state=DISABLED);
        self.id.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.id_err=StringVar()
        self.id_err.set("")
        Label(self.frame,textvariable=self.id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Department name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.name=Entry(self.frame,state=DISABLED);
        self.name.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.name_err=StringVar()
        self.name_err.set("")
        Label(self.frame,textvariable=self.name_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Laboratory Details",
              font=titlefont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                columnspan=3,
                                                sticky=N+S+W+E)
        row+=1

        Label(self.frame,bg="#bdc3c7").grid(row=row,
                                            column=1,
                                            columnspan=2,
                                            sticky=W+E)
        row+=1

        Label(self.frame,text="Department: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.dept_sel=StringVar()
        self.dept_sel.set(None)
        self.dept_opt=ttk.Combobox(self.frame,textvariable=self.dept_sel,
                                   values=self.dept,state=DISABLED)
        self.dept_opt.grid(row=row,
                           column=1,
                           columnspan=2,
                           sticky=W+E)
        row+=1

        self.dept_err=StringVar()
        self.dept_err.set("")
        Label(self.frame,textvariable=self.dept_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Laboratory ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.lab_id=Entry(self.frame,state=DISABLED);
        self.lab_id.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.lab_id_err=StringVar()
        self.lab_id_err.set("")
        Label(self.frame,textvariable=self.lab_id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Laboratory name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.lab_name=Entry(self.frame,state=DISABLED);
        self.lab_name.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.lab_name_err=StringVar()
        self.lab_name_err.set("")
        Label(self.frame,textvariable=self.lab_name_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Laboratory Incharge: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.inc=Entry(self.frame,state=DISABLED);
        self.inc.grid(row=row,column=1,columnspan=2,sticky=W+E)
        self.inc.bind('<Control-space>',self.new_staff)
        row+=1

        self.inc_err=StringVar()
        self.inc_err.set("")
        Label(self.frame,textvariable=self.inc_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Button(self.frame,text="SUBMIT",bg="#34495e",font=textfont,
               command=self.submit,fg="white",
               width=12).grid(row=row,
                              column=1,
                              pady=15)
        Button(self.frame,text="RESET",bg="#34495e",font=textfont,
               command=self.reset,fg="white",
               width=12).grid(row=row,
                              column=2,
                              pady=15)

        if not self.flag:
            Button(self.frame,text="BACK",bg="#34495e",font=textfont,
                   command=self.destroy,fg="white",
                   width=12).grid(row=row,
                                  column=0,
                                  pady=15)

        self.pack(anchor=CENTER,expand=1)

    def update_entry(self,event):
        self.id.delete(0,END)
        self.name.delete(0,END)
        dept=self.depts.get(self.depts.curselection()).split(' - ')
        self.id.insert(0,dept[0])
        self.name.insert(0,dept[1])

    def cmd_call(self):
        if self.mode[1].get():
            if self.cmd.get()=="Insert":
                self.lab_name.config(state=NORMAL)
                self.dept_opt.config(state=NORMAL)
                self.inc.config(state=NORMAL)
            else:
                self.inc.delete(0,END)
                self.dept_err.set("")
                self.lab_name_err.set("")
                self.inc_err.set("")
                self.dept_sel.set(None)
                self.lab_name.delete(0,END)
                self.lab_name.config(bg="white")
                self.lab_name.config(state=DISABLED)
                self.inc.config(bg="white")
                self.inc.config(state=DISABLED)
                self.dept_opt.config(state=DISABLED)

    def open(self,x):
        if x=="Department":
            if self.mode[0].get():
                self.depts.config(state=NORMAL)
                self.populate()
                self.id.config(state=NORMAL)
                self.name.config(state=NORMAL)
            else:
                self.unpopulate()
                self.name_err.set("")
                self.id_err.set("")
                self.cmd_err.set("")
                self.name.config(bg="white")
                self.id.config(bg="white")
                self.depts.config(state=DISABLED)
                self.name.delete(0,END)
                self.name.config(state=DISABLED)
                self.id.delete(0,END)
                self.id.config(state=DISABLED)
        if x=="Laboratory":
            if self.mode[1].get():
                self.lab_id.config(state=NORMAL)
            else:
                self.lab_id_err.set("")
                self.lab_id.delete(0,END)
                self.lab_id.config(bg="white")
                self.lab_id.config(state=DISABLED)
                self.inc.delete(0,END)
                self.dept_err.set("")
                self.lab_name_err.set("")
                self.inc_err.set("")
                self.dept_sel.set(None)
                self.lab_name.delete(0,END)
                self.lab_name.config(bg="white")
                self.lab_name.config(state=DISABLED)
                self.inc.config(bg="white")
                self.inc.config(state=DISABLED)
                self.dept_opt.config(state=DISABLED)
            self.cmd_call()

    def populate(self):
        for itm in self.dept:
            self.depts.insert(END,itm)

    def unpopulate(self):
        self.depts.delete(0,END)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(width=event.width,height=event.height)

    def new_staff(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Staff_master",fromlist=('Staff_master'))
        self.z=X.Staff_master(self.master,self.db,False)
        arg=""
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def call_pack(self,arg):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
        except:
            pass

    def db_check(self):
        uniq=BooleanVar()
        uniq.set(True)
        if self.cmd.get() == "Insert":
            if self.mode[0].get():
                if not any(item.startswith(self.id.get()) for item in self.dept):
                    self.id.config(bg="white")
                    self.id_err.set("")
                else:
                    uniq.set(False)
                    self.id.config(bg="#ffdbdb")
                    self.id_err.set("Department with same Id already exists")
                if not any(item.endswith(self.name.get()) for item in self.dept):
                    self.name.config(bg="white")
                    self.name_err.set("")
                else:
                    uniq.set(False)
                    self.name_err.set("Department already exists")
                    self.name.config(bg="#ffdbdb")
            if self.mode[1].get():
                x=self.db.execute_sql("""select department_id from laboratory_master
                                        where lab_id='%s';"""
                                        %(self.lab_id.get()))
                z=list(x.fetchall())
                dep_id=(self.dept_sel.get().split(" - "))
                if len(z)!=0:
                    self.lab_id.config(bg="#ffdbdb")
                    self.lab_id_err.set("Lab with same id exists")
                    uniq.set(False)
                    if any(item==dep_id[0] for item in z):
                        self.lab_name_err.set("Lab with same id exists in other department")
                        self.lab_id.config(bg="#ffdbdb")
                        uniq.set(False)
                    else:
                        self.lab_name_err.set("")
                        self.lab_name.config(bg="white")
                x=self.db.execute_sql("""select dept from staff_master
                                        where staff_id='%s';"""
                                        %(self.inc.get()))
                z=x.fetchall()
                if len(z)==0:
                    self.inc_err.set("Staff ID doesnt exists")
                    self.inc.config(bg="#ffdbdb")
                else:
                    dep_id=(self.dept_sel.get().split(" - "))
                    if z[0][0]!=dep_id[0]:
                        self.inc_err.set("Staff doesnt belong to this department")
                        self.inc.config(bg="#ffdbdb")
                        uniq.set(False)
                    else:
                        self.inc_err.set("")
                        self.inc.config(bg="white")
        elif self.cmd.get() == "Delete":
            if self.mode[0].get():
                if (self.id.get()+" - "+self.name.get()) in self.dept:
                    self.name.config(bg="white")
                    self.id.config(bg="white")
                    self.name_err.set("")
                else:
                    uniq.set(False)
                    self.id.config(bg="#ffdbdb")
                    self.name_err.set("Department doesn't exists")
                    self.name.config(bg="#ffdbdb")
            if self.mode[1].get():
                x=self.db.execute_sql("""select department_id from laboratory_master
                                        where lab_id='%s';"""
                                        %(self.lab_id.get()))
                z=list(x.fetchall())
                if len(z)==0:
                    self.lab_id.config(bg="#ffdbdb")
                    self.lab_id_err.set("Lab doesnt exists")
                    uniq.set(False)
                else:
                    dep_id=(self.dept_sel.get().split(" - "))
                    if any(item==dep_id[0] for item in z):
                        self.lab_name_err.set("Lab exists in other department")
                        self.lab_id.config(bg="#ffdbdb")
                    else:
                        self.lab_name_err.set("")
                        self.lab_name.config(bg="white")
        return(uniq.get())

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        if not self.mode[0].get() and not self.mode[1].get():
            comp.set(False)
            self.type_err.set("Select entry type")
        else:
            self.type_err.set("")
        msg.set("Select command")
        check_stvar(self.cmd,self.yn,comp,msg,self.cmd_err)
        if self.mode[0].get():
            msg.set("Department name cannot be empty")
            check_ent(self.name,comp,msg,self.name_err)
            msg.set("Department id cannot be empty")
            check_ent(self.id,comp,msg,self.id_err)
        if self.mode[1].get():
            msg.set("Laboratory id cannot be empty")
            check_ent(self.lab_id,comp,msg,self.lab_id_err)
            if self.cmd.get()=="Insert":
                msg.set("Laboratory name cannot be empty")
                check_ent(self.lab_name,comp,msg,self.lab_name_err)
                msg.set("Laboratory Incharge cannot be empty")
                check_ent(self.inc,comp,msg,self.inc_err)
                msg.set("Department not selected")
                check_stvar(self.dept_sel,self.dept,comp,msg,self.dept_err)
        try:
            self.db.connect()
            if self.db_check() and comp.get():
                if self.mode[0].get():
                    if self.cmd.get()=="Insert":
                        self.db.execute_sql("""insert into department_master
                                                values('%s','%s');"""
                                                %(self.id.get(),
                                                self.name.get()))
                        self.master.depts.append(self.id.get()+" - "+self.name.get())
                        self.master.depts.sort()
                        access=""
                        for items in self.dept:
                            access+=(items+"\n")
                        self.db.execute_sql("""update authentication set acs='%s' where
                                                user_name='admin';"""
                                                %(access))
                    elif self.cmd.get()=="Delete":
                        self.db.execute_sql("""delete from department_master where
                                                department_id='%s';"""
                                                %(self.id.get()))
                        self.master.depts.remove(self.id.get()+" - "+self.name.get())
                        access=""
                        for items in self.dept:
                            access+=(items+"\n")
                        self.db.execute_sql("""update authentication set acs='%s' where
                                                user_name='root';"""
                                                %(access))
                    if not self.mode[1].get():
                        self.reset()
                if self.mode[1].get():
                    dep_id=(self.dept_sel.get().split(" - "))
                    if self.cmd.get()=="Insert":
                        self.db.execute_sql("""insert into laboratory_master
                                                values('%s','%s','%s','%s');"""
                                                %(self.lab_id.get(),
                                                dep_id[0],
                                                self.lab_name.get(),
                                                self.inc.get()))
                    elif self.cmd.get()=="Delete":
                        self.db.execute_sql("""delete from laboratory_master where
                                                lab_id='%s';"""
                                                %(self.lab_id.get()))
                self.reset()
        except pw.IntegrityError as e:
            print(e)
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        if self.flag:
            Department_master(self.master,self.db,True)
