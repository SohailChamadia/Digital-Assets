from src.dependencies.imports import *

class Update_details(LabelFrame):

    def __init__(self,master,db):
        super(Update_details,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.db=db
        self.master=master

        self.depts=self.master.depts
        self.machines=[]
        self.vendors=[]
        self.ven_populate()
        self.create_widgets()
        self.mach_populate()

    def create_widgets(self):
        row=0;

        self.config(text="Update Details",
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

        Label(self,text="Repair Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                             sticky=N+S+W+E)
        self.st=Entry(self)
        self.st.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.st_select=Button(self,text="Calendar",fg="white",
                                  bg="#34495e",font=textfont,
                              command=self.selectdate)
        self.st_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.st_err=StringVar()
        self.st_err.set("")
        Label(self,textvariable=self.st_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Problem (Details): ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                    column=0,
                                                    sticky=N+S+W+E)
        self.det_prob=Text(self,width=40,height=5,wrap=WORD)
        self.det_prob.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.det_prob_err=StringVar()
        self.det_prob_err.set("")
        Label(self,textvariable=self.det_prob_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Vendor ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                            column=0,
                                            sticky=N+S+W+E)
        self.ven_id=StringVar();
        self.ven_id.set(None)
        self.ven_opt=combo(self,self.vendors,self.ven_id)
        self.ven_opt.grid(row=row,column=1,columnspan=2,sticky=W+E)

        for chl in self.ven_opt.children.values():
            chl.bind('<Control-space>',self.new_vendor)

        row+=1

        self.ven_id_err=StringVar()
        self.ven_id_err.set("")
        Label(self,textvariable=self.ven_id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Cost: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                       column=0,
                                       sticky=N+S+W+E)
        self.cost=Entry(self);
        self.cost.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.cost_err=StringVar()
        self.cost_err.set("")
        Label(self,textvariable=self.cost_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Solution (Details): ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                     column=0,
                                                     sticky=N+S+W+E)
        self.det_sol=Text(self,width=40,height=4,wrap=WORD)
        self.det_sol.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.det_sol_err=StringVar()
        self.det_sol_err.set("")
        Label(self,textvariable=self.det_sol_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Call_id No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.call_id=Entry(self);
        self.call_id.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.call_id_err=StringVar()
        self.call_id_err.set("")
        Label(self,textvariable=self.call_id_err,
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

    def new_equipment(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Equipment",fromlist=('Equipment'))
        self.z=X.Equipment(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.setDaemon(True)
        t.start()

    def new_vendor(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Vendor_details",fromlist=('Vendor_details'))
        self.z=X.Vendor_details(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.setDaemon(True)
        t.start()

    def ven_populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[0])
        self.db.close()

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

    def call_pack(self):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
        except:
            pass

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Solution Details cannot be empty")
        check_txt(self.det_sol,comp,msg,self.det_sol_err)
        msg.set("Problem Details cannot be empty")
        check_txt(self.det_prob,comp,msg,self.det_prob_err)
        msg.set("Invalid Caller ID")
        check_cont(self.call_id,comp,msg,self.call_id_err)
        msg.set("Invalid Cost")
        check_int(self.cost,comp,msg,self.cost_err)
        msg.set("Machine ID cannot be empty")
        check_stvar(self.m_id,self.machines,comp,msg,self.m_id_err)
        msg.set("Invalid Start date")
        check_date(self.st,comp,msg,self.st_err)
        msg.set("Vendor ID cannot be empty")
        check_stvar(self.ven_id,self.vendors,comp,msg,self.ven_id_err)
        try:
            self.db.connect()
            if comp.get():
                ven=list(self.ven_id.get().split(" - "))
                self.db.execute_sql("""insert into update_details
                                        values('%s','%s','%s','%s',%d,'%s','%s');"""
                                            %(self.m_id.get(),
                                              self.st.get(),
                                              self.det_prob.get("1.0",END),
                                              ven[1],
                                              int(self.cost.get()),
                                              self.det_sol.get("1.0",END),
                                              self.call_id.get()
                                        ))
                self.reset()
        except pw.IntegrityError as e:
            print(e)
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        Update_details(self.master,self.db)
