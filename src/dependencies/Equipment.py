from src.dependencies.imports import *

class Equipment(Frame):

    def __init__(self,master,db,flag):

        super(Equipment,self).__init__(master)
        self.master=master
        self.db=db
        self.flag=flag
        self.config(bg="#bdc3c7")
        self.depts=self.master.depts
        self.focus_set()

        self.canvas = Canvas(self,bg="#bdc3c7")
        self.frame = LabelFrame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(anchor=CENTER, expand=1)
        self.canvas.create_window((0,0), window=self.frame, anchor="n",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        labelfont=('times',16,'bold')
        self.frame.config(bg="#bdc3c7",font=labelfont)
        self.item=[]
        self.vendors=[]
        self.locs=[]
        self.staff=[]
        self.item_populate()
        self.ven_populate()
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
        self.frame.config(text="New Equipment Details",
                          relief=FLAT,
                          labelanchor=N,
                          padx=30,
                          pady=10)

        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self.frame,text="Machine Id: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.id=Entry(self.frame);
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

        Label(self.frame,text="Serial No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.sn=Entry(self.frame);
        self.sn.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.sn_err=StringVar()
        self.sn_err.set("")
        Label(self.frame,textvariable=self.sn_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Configuration: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.conf=Text(self.frame,width=40,height=5,wrap=WORD)
        self.conf.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Type of machine: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.type=StringVar()
        self.type.set(None)
        self.type_option=combo(self.frame,self.item,self.type,True)
        self.type_option.grid(row=row,
                              column=1,
                              columnspan=2,
                              sticky=W+E)
        if self.master.admin_access:
            for chl in self.type_option.children.values():
                chl.bind('<Control-space>',self.new_item)
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

        Label(self.frame,text="Software support: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.yn=["Yes","No"]
        self.soft=BooleanVar();
        self.soft.set(False)
        cnt=0
        x=True
        for items in self.yn:
            Radiobutton(self.frame,text=items,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.soft,
                        value=x).grid(row=row,column=1+cnt,
                                      sticky=W+S)
            cnt+=1
            x=not x
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Purchase Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.pur=Entry(self.frame)
        self.pur.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.pur_select=Button(self.frame,text="Calendar",fg="white",
                              bg="#34495e",font=textfont,
                              command=self.selectdate)
        self.pur_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.pur_err=StringVar()
        self.pur_err.set("")
        Label(self.frame,textvariable=self.pur_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Vendor Id: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.ven_id=StringVar();
        self.ven_id.set(None)
        self.ven_opt=combo(self.frame,self.vendors,self.ven_id,True)
        self.ven_opt.grid(row=row,column=1,columnspan=2,sticky=W+E)

        for chl in self.ven_opt.children.values():
            chl.bind('<Control-space>',self.new_vendor)

        row+=1

        self.ven_id_err=StringVar()
        self.ven_id_err.set("")
        Label(self.frame,textvariable=self.ven_id_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Price: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.amt=Entry(self.frame);
        self.amt.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.amt_err=StringVar()
        self.amt_err.set("")
        Label(self.frame,textvariable=self.amt_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Model: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.model=Entry(self.frame);
        self.model.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Department: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.dept=StringVar()
        self.dept.set("")
        self.dept_option=ttk.Combobox(self.frame,textvariable=self.dept,
                                      validate="focusout",
                                      validatecommand=self.staff_populate,
                                      values=self.depts)
        self.dept_option.grid(row=row,
                              column=1,
                              columnspan=2,
                              sticky=W+E)
        if self.master.admin_access:
            self.dept_option.bind('<Control-space>',self.new_department)
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

        Label(self.frame,text="Installation place: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.loc=StringVar()
        self.loc.set("")
        self.loc_opt=ttk.Combobox(self.frame,textvariable=self.loc,
                                  postcommand=self.lab_populate,
                                  values=self.locs);
        self.loc_opt.grid(row=row,column=1,columnspan=2,sticky=W+E)

        if self.master.admin_access:
            self.loc_opt.bind('<Control-space>',self.new_department)
        row+=1

        self.loc_err=StringVar()
        self.loc_err.set("")
        Label(self.frame,textvariable=self.loc_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Warranty Due Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.end=Entry(self.frame)
        self.end.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.end_select=Button(self.frame,text="Calendar",fg="white",
                                  bg="#34495e",font=textfont,
                               command=self.selectdate)
        self.end_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.end_err=StringVar()
        self.end_err.set("")
        Label(self.frame,textvariable=self.end_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Incharge (Staff ID): ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.inc=StringVar();
        self.inc.set("")
        self.inc_opt=combo(self.frame,self.staff,self.inc,True)
        self.inc_opt.grid(row=row,column=1,columnspan=2,sticky=W+E)

        if self.master.admin_access:
            for chl in self.inc_opt.children.values():
                chl.bind('<Control-space>',self.new_staff)
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

        Label(self.frame,text="Used by: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.users=["Students","Staff","Admin","Lab asst."]
        self.user=[IntVar(),IntVar(),IntVar(),IntVar()]
        cnt=0
        ind=0
        for item in self.users:
            Checkbutton(self.frame,text=item,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.user[ind]
                        ).grid(row=row,column=1+cnt,
                               ipady=10,sticky=W)
            cnt+=1
            ind+=1
            row+=(cnt//2)
            cnt%=2
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Issuable: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.yn=["Yes","No"]
        self.iss=BooleanVar();
        self.iss.set(False)
        cnt=0
        x=True
        for items in self.yn:
            Radiobutton(self.frame,text=items,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.iss,
                        value=x).grid(row=row,column=1+cnt,
                                          sticky=W)
            cnt+=1
            x=not x
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Purchase Order No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.po_num=Entry(self.frame);
        self.po_num.bind('<Control-space>',self.new_purchase)
        self.po_num.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.po_num_err=StringVar()
        self.po_num_err.set("")
        Label(self.frame,textvariable=self.po_num_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Machine Type: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.net=["LAN","WAN"]
        self.net_type=StringVar()
        self.net_type.set(None)
        cnt=0
        for item in self.net:
            Radiobutton(self.frame,text=item,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.net_type,
                        value=item).grid(row=row,column=1+cnt,
                                         sticky=W)
            cnt+=1
        row+=1

        self.net_type_err=StringVar()
        self.net_type_err.set("")
        Label(self.frame,textvariable=self.net_type_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Remarks: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.rem=Text(self.frame,width=40,height=5,wrap=WORD)
        self.rem.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.sub=Button(self.frame,text="SUBMIT",bg="#34495e",font=textfont,
                        command=self.submit,fg="white",
                        width=12)
        self.sub.grid(row=row,
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

    def selectdate(self):
        X=__import__('date')
        self.expiry_date=X.Calendar(self.master)
        #self.expire.insert(0,self.expiry_date.selection())

    def lab_populate(self):
        self.db.connect()
        self.locs=[]
        dpt=list(self.dept.get().split(" - "))
        x=self.db.execute_sql("select lab_id,lab_name from laboratory_master where department_id='%s';"%(dpt[0]))
        z=list(x.fetchall())
        for items in z:
            self.locs.append(items[1]+" - "+items[0])
        self.db.close()
        self.loc_opt.config(values=self.locs)

    def ven_populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vendor_id,vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[1]+" - "+items[0])
        self.db.close()

    def staff_populate(self):
        self.db.connect()
        self.staff=[]
        dpt=list(self.dept.get().split(" - "))
        x=self.db.execute_sql("select staff_id,staff_name from staff_master where dept='%s'"%(dpt[0]))
        z=list(x.fetchall())
        for items in z:
            self.staff.append(items[1]+" - "+items[0])
        self.db.close()
        self.inc_opt.value_config(self.staff)
        return True

    def item_populate(self):
        self.db.connect()
        x=self.db.execute_sql("select items from item_master")
        z=list(x.fetchall())
        self.item=[]
        for items in z:
            self.item.append(items[0])
        self.db.close()

    def dept_populate(self):
        self.db.connect()
        x=self.db.execute_sql("select * from department_master")
        z=list(x.fetchall())
        self.depts=[]
        for items in z:
            self.depts.append(items[0]+" - "+items[1])
        self.db.close()
        self.dept_option.config(values=self.depts)

    def new_staff(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Staff_master",fromlist=('Staff_master'))
        self.z=X.Staff_master(self.master,self.db,False)
        arg="Staff"
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
        arg="Vendor"
        t=Thread(target=self.call_pack,args=(arg,))
        t.setDaemon(True)
        t.start()

    def new_item(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Item_master",fromlist=('Item_master'))
        self.z=X.Item_master(self.master,self.db,False)
        arg="Item"
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
            elif arg=="Item":
                self.item_populate()
                self.type_option.value_config(self.item)
            elif arg=="Vendor":
                self.ven_populate()
                self.ven_opt.value_config(self.vendors)
            elif arg=="Staff":
                self.staff_populate()
        except:
            pass

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(width=event.width,height=event.height)

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("ID cannot be empty")
        check_ent(self.id,comp,msg,self.id_err)
        msg.set("Serial No. cannot be empty")
        check_ent(self.sn,comp,msg,self.sn_err)
        msg.set("Type of machine not selected")
        check_stvar(self.type,self.item,comp,msg,self.type_err)
        msg.set("Invalid Purchase Date")
        check_date(self.pur,comp,msg,self.pur_err)
        msg.set("Vendor ID not selected")
        check_stvar(self.ven_id,self.vendors,comp,msg,self.ven_id_err)
        msg.set("Invalid Price")
        check_int(self.amt,comp,msg,self.amt_err)
        msg.set("Select Department")
        check_stvar(self.dept,self.depts,comp,msg,self.dept_err)
        msg.set("Select Installation place")
        check_stvar(self.loc,self.locs,comp,msg,self.loc_err)
        msg.set("Invalid Warranty Due Date")
        check_date(self.end,comp,msg,self.end_err)
        msg.set("Incharge (Staff Id) not selected")
        check_stvar(self.inc,self.staff,comp,msg,self.inc_err)
        msg.set("Purchase order number cannot be empty")
        check_ent(self.po_num,comp,msg,self.po_num_err)
        msg.set("Machine type not selected")
        check_stvar(self.net_type,self.net,comp,msg,self.net_type_err)
        msg.set("Warranty date should not be before Purchase date")
        comp_date(self.pur,self.end,comp,msg,self.end_err)
        access=""
        cnt=0
        for items in self.user:
            if items.get()==1:
                access+=(self.users[cnt]+"\n")
            cnt+=1
        try:
            self.db.connect()
            if comp.get():
                dpt=list(self.dept.get().split(" - "))
                lab=list(self.loc.get().split(" - "))
                ven=list(self.ven_id.get().split(" - "))
                staff=list(self.inc.get().split(" - "))
                self.db.execute_sql("""insert into equipment
                                    values('%s','%s','%s','%s',%d,
                                           '%s','%s',%d,
                                           '%s','%s','%s','%s','%s','%s',%d,
                                           '%s','%s','%s');"""
                                        %(self.id.get(),
                                          self.sn.get(),
                                          self.conf.get("1.0",END),
                                          self.type.get(),
                                          self.soft.get(),
                                          self.pur.get(),
                                          ven[1],
                                          int(self.amt.get()),
                                          self.model.get(),
                                          dpt[0],
                                          lab[1],
                                          self.end.get(),
                                          staff[1],
                                          access,
                                          self.iss.get(),
                                          self.po_num.get(),
                                          self.net_type.get(),
                                          self.rem.get("1.0",END)
                                    ))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1062:
                self.id.config(bg="#ffdbdb")
                self.id_err.set("Machine with same ID already exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
            if x==1452:
                self.po_num.config(bg="#ffdbdb")
                self.po_num_err.set("Purchase Order doesn't exists")
            else:
                self.po_num_err.set("")
                self.po_num.config(bg='white')
        except:
            self.db.close()
            print("connection error")

    def reset(self):
        self.destroy()
        if self.flag:
            Equipment(self.master,self.db,True)
