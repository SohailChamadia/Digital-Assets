from src.dependencies.imports import *

class Amc_details(LabelFrame):

    def __init__(self,master,db):
        super(Amc_details,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.db=db

        self.master=master
        self.depts=self.master.depts
        self.machines=[]
        self.vendors=[]
        self.ven_populate()
        self.mach_populate()
        self.create_widgets()

    def create_widgets(self):
        row=0;

        self.config(text="AMC details",
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
        self.m_id_opt=combo(self,self.machines,self.m_id)
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

        Label(self,text="Purchase Order No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                     column=0,
                                                     sticky=N+S+W+E)
        self.po_num=Entry(self);
        self.po_num.bind('<Control-space>',self.new_purchase)
        self.po_num.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.po_num_err=StringVar()
        self.po_num_err.set("")
        Label(self,textvariable=self.po_num_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Start Date: ",
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

        Label(self,text="End Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.end=Entry(self)
        self.end.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.end_select=Button(self,text="Calendar",fg="white",
                                  bg="#34495e",font=textfont,
                               command=self.selectdate)
        self.end_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.end_err=StringVar()
        self.end_err.set("")
        Label(self,textvariable=self.end_err,
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
        self.expire.insert(0,self.expiry_date.selection())

    def ven_populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vendor_id,vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[1]+" - "+items[0])
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

    def new_equipment(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Equipment",fromlist=('Equipment'))
        self.z=X.Equipment(self.master,self.db,False)
        arg="Equipment"
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def new_purchase(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Purchase_details",fromlist=('Purchase_details'))
        self.z=X.Purchase_details(self.master,self.db,False)
        arg=""
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def new_vendor(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Vendor_details",fromlist=('Vendor_details'))
        self.z=X.Vendor_details(self.master,self.db,False)
        arg=""
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def call_pack(self,arg):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            if arg=="Equipment":
                self.mach_populate()
            self.pack(anchor=CENTER,expand=1)
        except:
            pass

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Invalid Expiry date")
        check_date(self.end,comp,msg,self.end_err)
        msg.set("Machine ID cannot be empty")
        check_stvar(self.m_id,self.machines,comp,msg,self.m_id_err)
        msg.set("Purchase Order cannot be empty")
        check_ent(self.po_num,comp,msg,self.po_num_err)
        msg.set("Invalid Start Date")
        check_date(self.st,comp,msg,self.st_err)
        msg.set("Vendor ID cannot be empty")
        check_stvar(self.ven_id,self.vendors,comp,msg,self.ven_id_err)
        msg.set("Expiry date should be before Start Date")
        comp_date(self.st,self.end,comp,msg,self.end_err)
        try:
            self.db.connect()
            if comp.get():
                ven=list(self.ven_id.get().split(" - "))
                self.db.execute_sql("""insert into amc
                                        values('%s','%s','%s','%s','%s');"""
                                            %(self.m_id.get(),
                                              self.po_num.get(),
                                              self.st.get(),
                                              self.end.get(),
                                              ven[1]
                                        ))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1452:
                self.po_num.config(bg="#ffdbdb")
                self.po_num_err.set("Purchase Order doesn't exists")
            else:
                self.po_num_err.set("")
                self.po_num.config(bg='white')
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        Amc_details(self.master,self.db)
