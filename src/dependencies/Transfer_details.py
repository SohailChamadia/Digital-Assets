from src.dependencies.imports import *

class Transfer_details(LabelFrame):

    def __init__(self,master,db):
        super(Transfer_details,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.db=db
        self.machines=[]
        self.depts=self.master.depts
        self.create_widgets()
        self.mach_populate()

    def create_widgets(self):
        row=0;

        self.config(text="Transfer Details",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self,text="Machine ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.m_id=StringVar();
        self.m_id.set("")
        self.m_id_opt=combo(self,self.machines,self.m_id,True)
        self.m_id_opt.grid(row=row,column=1,columnspan=2,sticky=W+E)
        for chl in self.m_id_opt.children.values():
            chl.bind('<Control-space>',self.new_equipment)

        row+=1

        self.m_id_err=StringVar()
        self.m_id_err.set("")
        Label(self,textvariable=self.m_id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Transfer Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.tr=Entry(self)
        self.tr.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.tr_select=Button(self,text="Calendar",fg="white",
                              bg="#34495e",font=textfont,
                              command=self.selectdate)
        self.tr_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.tr_err=StringVar()
        self.tr_err.set("")
        Label(self,textvariable=self.tr_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Department: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.dept=StringVar()
        self.dept.set(None)
        self.dept_opt=ttk.Combobox(self,textvariable=self.dept,
                            values=self.depts)
        self.dept_opt.grid(row=row,
                           column=1,
                           columnspan=2,
                           sticky=W+E)
        if self.master.admin_access:
            self.dept_opt.bind('<Control-space>',self.new_department)
        row+=1

        self.dept_err=StringVar()
        self.dept_err.set("")
        Label(self,textvariable=self.dept_err,
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

        self.pack(anchor=CENTER,expand=1)

    def selectdate(self):
        X=__import__('calendar_ui')
        self.expiry_date=X.CalendarWidget(self.master)
        #self.expire.insert(0,self.expiry_date.selection())

    def dept_populate(self):
        self.db.connect()
        x=self.db.execute_sql("select dept from department_master")
        z=list(x.fetchall())
        self.depts=[]
        for items in z:
            self.depts.append(items[0])
        self.db.close()
        self.dept_opt.config(values=self.depts)

    def mach_populate(self):
        self.db.connect()
        self.machines=[]
        dpt=[]
        for items in self.depts:
            tmp=(items.split(" - "))
            dpt.append(tmp[0])
        if len(dpt)==1:
            s="("+dpt[0]+")"
        else:
            s=str(tuple(dpt))
        if len(dpt)>0:
            x=self.db.execute_sql("select machine from equipment where department in %s;"%(s))
            z=list(x.fetchall())
            for items in z:
                self.machines.append(items[0])
        self.db.close()
        self.m_id_opt.value_config(self.machines)

    def new_equipment(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Equipment",fromlist=('Equipment'))
        self.z=X.Equipment(self.master,self.db,False)
        arg=""
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def new_department(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Department_master",fromlist=('Department_master'))
        self.z=X.Department_master(self.master,self.db,False)
        arg="Department"
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def call_pack(self,arg):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
            if arg=="Department":
                self.dept_populate()
        except:
            pass

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Machine ID cannot be empty")
        check_stvar(self.m_id,self.machines,comp,msg,self.m_id_err)
        msg.set("Invalid Transfer Date")
        check_date(self.tr,comp,msg,self.tr_err)
        msg.set("Select Department")
        check_stvar(self.dept,self.depts,comp,msg,self.dept_err)
        try:
            self.db.connect()
            if comp.get():
                dpt=list(self.dept.get().split(" - "))
                self.db.execute_sql("""insert into transfer_details
                                        values('%s','%s','%s');"""
                                            %(self.m_id.get(),
                                              self.tr.get(),
                                              dpt[0]
                                        ))
                self.reset()
        except pw.IntegrityError as e:
            print(e)
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        Transfer_details(self.master,self.db)
