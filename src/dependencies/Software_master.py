from src.dependencies.imports import *

class Software_master(LabelFrame):

    def __init__(self,master,db):
        super(Software_master,self).__init__(master)
        labelfont=('times',16,'bold')
        self.config(bd=2,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.db=db

        self.canvas = Canvas(self,bg="#bdc3c7")
        self.frame = LabelFrame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(anchor=CENTER, expand=1)
        self.canvas.create_window((0,0), window=self.frame, anchor="n",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.frame.config(bd=2,bg="#bdc3c7",font=labelfont)

        self.vendors=[]
        self.populate()
        self.create_widgets()

    def create_widgets(self):
        row=0;

        self.frame.config(text="New Software Details",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)

        errorfont=('verdana',8)

        Label(self.frame,text="Software ID: ",
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

        Label(self.frame,text="Software Name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.name=Entry(self.frame);
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

        Label(self.frame,text="Software Type: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.app_types=["Application","System"]
        self.app_type=StringVar()
        self.app_type.set(None)
        cnt=0
        for item in self.app_types:
            Radiobutton(self.frame,text=item,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.app_type,
                        value=item).grid(row=row,column=1+cnt,
                                         sticky=W)
            cnt+=1
        row+=1

        self.app_type_err=StringVar()
        self.app_type_err.set("")
        Label(self.frame,textvariable=self.app_type_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Licensed: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.yes=BooleanVar()
        self.yes.set(False)
        Radiobutton(self.frame,text="Yes",
                    variable=self.yes,
                    font=textfont,
                    bg="#bdc3c7",
                    command=self.licensed,
                    value=True).grid(row=row,column=1,
                                     sticky=W)
        self.no=BooleanVar()
        self.no.set(False)
        Radiobutton(self.frame,text="No",
                    variable=self.no,
                    font=textfont,
                    bg="#bdc3c7",
                    command=self.unlicensed,
                    value=True).grid(row=row,column=2,
                                     sticky=W)
        row+=1

        self.lic_err=StringVar()
        self.lic_err.set("")
        Label(self.frame,textvariable=self.lic_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="License No: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.license_no=Entry(self.frame,state=DISABLED)
        self.license_no.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.license_no_err=StringVar()
        self.license_no_err.set("")
        Label(self.frame,textvariable=self.license_no_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Expiry Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.expire=Entry(self.frame,
                          state=DISABLED)
        self.expire.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.cal_open=BooleanVar()
        self.cal_open.set(False)
        self.expire_select=Button(self.frame,text="Calendar",fg="white",
                                  bg="#34495e",font=textfont,
                                  #command=lambda row_no=row:self.selectdate(row_no),
                                  state=DISABLED)
        self.expire_select.grid(row=row,
                                column=2,
                                sticky=E)

        row+=1

        self.expire_err=StringVar()
        self.expire_err.set("")
        Label(self.frame,textvariable=self.expire_err,
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
        self.price=Entry(self.frame)
        self.price.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.price_err=StringVar()
        self.price_err.set("")
        Label(self.frame,textvariable=self.price_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Vendor - Id: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                        column=0,
                                        sticky=N+S+W+E)
        self.vendor=StringVar()
        self.vendor.set(None)
        self.ven_menu=combo(self.frame,self.vendors,self.vendor,True)
        self.ven_menu.grid(row=row,
                           column=1,
                           columnspan=2,
                           sticky=W+E)
        for chl in self.ven_menu.children.values():
            chl.bind('<Control-space>',self.new_vendor)
        row+=1

        self.vendor_err=StringVar()
        self.vendor_err.set("")
        Label(self.frame,textvariable=self.vendor_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Open Source: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.yn=["Yes","No"]
        self.open_src=BooleanVar();
        self.open_src.set(False)
        cnt=0
        x=True
        for items in self.yn:
            Radiobutton(self.frame,text=items,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.open_src,
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

        Label(self.frame,text="Details/Remarks: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                  column=0,
                                                  pady=20,
                                                  sticky=N+S+W+E)
        self.det=Text(self.frame,width=40,height=5,wrap=WORD)
        self.det.grid(row=row,column=1,columnspan=2,sticky=W+E)
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

        self.pack(anchor=CENTER,expand=1)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(width=event.width,height=event.height)

    def new_vendor(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Vendor_details",fromlist=('Vendor_details'))
        self.z=X.Vendor_details(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.start()

    def call_pack(self):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
            self.populate()
            self.ven_menu.value_config(self.vendors)
        except:
            pass

    def populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vendor_id,vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[1]+" - "+items[0])
        self.db.close()

    def selectdate(self,row_no):
        if not self.cal_open.get():
            X=__import__('ttkcalendar')
            self.expiry_date=X.Calendar(self)
            self.expiry_date.grid(row=row_no,column=3)
            self.expire_select.config(text="Confirm")
            self.cal_open.set(True)
        else:
            self.expiry_date.grid_forget()
            self.expire_select.config(text="Calendar")
            self.cal_open.set(False)
            try:
                self.updatedate()
            finally:
                pass

    def updatedate(self):
        self.expire.delete(0,END)
        if self.expiry_date.selection is not None:
            self.expire.insert(0,str(self.expiry_date.selection.date()))
        self.expiry_date.grid_forget()

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Software ID cannot be empty")
        check_ent(self.id,comp,msg,self.id_err)
        msg.set("Software name cannot be empty")
        check_ent(self.name,comp,msg,self.name_err)
        msg.set("Invalid Price")
        check_int(self.price,comp,msg,self.price_err)
        msg.set("Software type not selected")
        check_stvar(self.app_type,self.app_types,comp,msg,self.app_type_err)
        msg.set("Select Vendor")
        check_stvar(self.vendor,self.vendors,comp,msg,self.vendor_err)
        if not self.yes.get() and not self.no.get():
            self.lic_err.set("License option not selected")
            comp.set(False)
        else:
            self.lic_err.set("")
        if self.yes.get():
            msg.set("License No. cannot be empty")
            check_ent(self.license_no,comp,msg,self.license_no_err)
            msg.set("Invalid Expiry Date")
            check_date(self.expire,comp,msg,self.expire_err)
        try:
            self.db.connect()
            if comp.get():
                ven=list(self.vendor.get().split(" - "))
                self.db.execute_sql("""insert into software_master
                                    values('%s','%s','%s',%d,'%s',%d,'%s','%s',%d,'%s');"""
                                        %(self.id.get(),
                                          self.name.get(),
                                          self.app_type.get(),
                                          self.yes.get(),
                                          self.license_no.get(),
                                          int(self.price.get()),
                                          ven[1],
                                          self.expire.get(),
                                          self.open_src.get(),
                                          self.det.get("1.0",END)
                                    ))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1062:
                self.id.config(bg="#ffdbdb")
                self.id_err.set("Software with same ID already exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        Software_master(self.master,self.db)

    def licensed(self):
        if self.yes:
            self.no.set(False)
            self.expire.config(state=NORMAL)
            self.expire_select.config(state=NORMAL)
            self.license_no.config(state=NORMAL)

    def unlicensed(self):
        if self.yes:
            self.license_no_err.set("")
            self.expire_err.set("")
            self.license_no.config(bg="white")
            self.expire.config(bg="white")
            self.yes.set(False)
            self.license_no.delete(0,END)
            self.license_no.config(state=DISABLED)
            self.expire.delete(0,END)
            self.expire.config(state=DISABLED)
            self.expire_select.config(state=DISABLED)
