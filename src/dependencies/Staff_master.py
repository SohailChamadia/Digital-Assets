from src.dependencies.imports import *

class Staff_master(LabelFrame):

    def __init__(self,master,db,flag):
        super(Staff_master,self).__init__(master)
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.grid()
        self.db=db
        self.flag=flag

        self.depts=self.master.depts
        self.create_widgets()
        if not self.flag:
            self.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Label) ,self.children.values()):
                lab.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Button) ,self.children.values()):
                lab.config(bg="#9b9039")

    def create_widgets(self):
        row=0;

        self.config(text="Staff Master",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self,text="Staff ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.id=Entry(self);
        self.id.grid(row=row,column=1,columnspan=2,sticky=W+E)
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

        Label(self,text="Name: ",
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

        Label(self,text="Designation: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.desg=Entry(self);
        self.desg.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.desg_err=StringVar()
        self.desg_err.set("")
        Label(self,textvariable=self.desg_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Contact No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.con=Entry(self);
        self.con.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.con_err=StringVar()
        self.con_err.set("")
        Label(self,textvariable=self.con_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Email ID 1: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.email1=Entry(self);
        self.email1.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.email1_err=StringVar()
        self.email1_err.set("")
        Label(self,textvariable=self.email1_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Email ID 2: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                             column=0,
                                             sticky=N+S+W+E)
        self.email2=Entry(self);
        self.email2.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.email2_err=StringVar()
        self.email2_err.set("")
        Label(self,textvariable=self.email2_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Address: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                          column=0,
                                          sticky=N+S+W+E)
        self.adr=Text(self,width=40,height=5,wrap=WORD)
        self.adr.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.adr_err=StringVar()
        self.adr_err.set("")
        Label(self,textvariable=self.adr_err,
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

        Label(self,text="Joining Date: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)

        self.join_date=Entry(self)
        self.join_date.grid(row=row,
                         column=1,
                         sticky=W+E)
        self.join_date_select=Button(self,text="Calendar",fg="white",
                              bg="#34495e",font=textfont,
                              command=self.selectdate)
        self.join_date_select.grid(row=row,
                             column=2,
                             sticky=E)
        row+=1

        self.join_date_err=StringVar()
        self.join_date_err.set("")
        Label(self,textvariable=self.join_date_err,
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

    def selectdate(self):
        X=__import__('calendar_ui')
        self.expiry_date=X.CalendarWidget(self.master)
        #self.expire.insert(0,self.expiry_date.selection())

    def dept_populate(self):
        self.db.connect()
        x=self.db.execute_sql("select * from department_master")
        z=list(x.fetchall())
        self.depts=[]
        for items in z:
            self.depts.append(items[0]+" - "+items[1])
        self.db.close()
        self.dept_opt.config(values=self.depts)

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
        msg.set("Invalid contact number")
        check_cont(self.con,comp,msg,self.con_err)
        msg.set("Designation cannot be empty")
        check_ent(self.desg,comp,msg,self.desg_err)
        msg.set("Email ID cannot be empty")
        check_ent(self.email1,comp,msg,self.email1_err)
        msg.set("Email ID cannot be empty")
        check_ent(self.email2,comp,msg,self.email2_err)
        msg.set("ID cannot be empty")
        check_ent(self.id,comp,msg,self.id_err)
        msg.set("Select department")
        check_stvar(self.dept,self.depts,comp,msg,self.dept_err)
        msg.set("Name cannot be empty")
        check_ent(self.name,comp,msg,self.name_err)
        msg.set("Invalid Joining Date")
        check_date(self.join_date,comp,msg,self.join_date_err)
        if self.email1.get()!="" and self.email2.get()!="":
            if self.email1.get()==self.email2.get():
                self.email1.config(bg="#ffdbdb")
                self.email2.config(bg="#ffdbdb")
                self.email1_err.set("Email ID cannot be same")
                self.email2_err.set("Email ID cannot be same")
            else:
                self.email1.config(bg="white")
                self.email2.config(bg="white")
        try:
            self.db.connect()
            if comp.get():
                dpt=list(self.dept.get().split(" - "))
                self.db.execute_sql("""insert into staff_master
                                        values('%s','%s','%s','%s','%s','%s','%s','%s','%s');"""
                                        %(self.id.get(),
                                          self.name.get(),
                                          self.desg.get(),
                                          self.con.get(),
                                          self.email1.get(),
                                          self.email2.get(),
                                          self.adr.get("1.0",END),
                                          dpt[0],
                                          self.join_date.get()
                                    ))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1062:
                self.id.config(bg="#ffdbdb")
                self.id_err.set("Staff ID already exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        if self.flag:
            Staff_master(self.master,self.db,True)
