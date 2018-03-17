from src.dependencies.imports import *

class User_master(LabelFrame):

    def __init__(self,master,db):
        super(User_master,self).__init__(master)
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.master=master
        self.db=db

        self.depts=self.master.depts
        self.create_widgets()

    def create_widgets(self):
        row=0;

        self.config(text="User Master",
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
        self.id.bind('<Control-space>',self.new_staff)
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

        Label(self,text="User ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.user=Entry(self);
        self.user.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.user_err=StringVar()
        self.user_err.set("")
        Label(self,textvariable=self.user_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Password: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.pwd=Entry(self);
        self.pwd.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.pwd_err=StringVar()
        self.pwd_err.set("")
        Label(self,textvariable=self.pwd_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self,text="Access to: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        ind=0
        cnt=0
        self.user_access=[]
        for item in self.depts:
            self.user_access.append(IntVar())
            Checkbutton(self,text=item,
                        font=textfont,
                        bg="#bdc3c7",
                        variable=self.user_access[ind]
                        ).grid(row=row,column=1+cnt,
                               ipady=10,sticky=W)
            cnt+=1
            ind+=1
            row+=(cnt//2)
            cnt%=2
        row+=1

        self.user_access_err=StringVar()
        self.user_access_err.set("")
        Label(self,textvariable=self.user_access_err,
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

    def check_db(self):
        uniq=BooleanVar()
        uniq.set(True)
        if self.id.get()!="":
            x=self.db.execute_sql("select * from user_master where staff_id='%s';"%(self.id.get()))
            if len(x.fetchall()) > 0:
                uniq.set(False)
                self.id.config(bg="#ffdbdb")
                self.id_err.set("User with same Staff ID already exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
        return(uniq.get())

    def new_staff(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Staff_master",fromlist=('Staff_master'))
        self.z=X.Staff_master(self.master,self.db,False)
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

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Staff ID cannot be empty")
        check_ent(self.id,comp,msg,self.id_err)
        msg.set("Username cannot be empty")
        check_ent(self.user,comp,msg,self.user_err)
        msg.set("Password cannot be empty")
        check_ent(self.pwd,comp,msg,self.pwd_err)
        access=""
        cnt=0
        for items in self.user_access:
            if items.get()==1:
                access+=(self.depts[cnt]+"\n")
            cnt+=1
        try:
            self.db.connect()
            if self.check_db() and comp.get():
                self.db.execute_sql("""create user '%s' identified by '%s';"""
                                    %(self.user.get(),
                                    self.pwd.get()
                                    ))
                self.db.execute_sql("""grant all privileges on assets.* to
                                    '%s' identified by '%s';"""
                                    %(self.user.get(),
                                    self.pwd.get()
                                    ))
                self.db.execute_sql("""flush privileges;""")
                self.db.execute_sql("""insert into user_master
                                        values('%s','%s','%s','%s');"""
                                        %(self.user.get(),
                                          self.id.get(),
                                          self.pwd.get(),
                                          access
                                    ))
                self.db.execute_sql("""insert into authentication
                                        values('%s','%s','%s');"""
                                        %(self.user.get(),
                                          self.pwd.get(),
                                          access
                                    ))
                self.reset()
        except pw.InternalError as e:
            x,y=e.args
            print(e)
            if x==1396:
                self.user.config(bg="#ffdbdb")
                self.user_err.set("Username already exists")
            else:
                self.user_err.set("")
                self.user.config(bg='white')
        except pw.IntegrityError as e:
            try:
                self.db.execute_sql("drop user '%s';"%self.user.get())
            except:
                pass
            x,y=e.args
            print(e)
            if x==1062:
                self.user.config(bg="#ffdbdb")
                self.user_err.set("Username already exists")
            else:
                self.user_err.set("")
                self.user.config(bg='white')
            if x==1452:
                self.id.config(bg="#ffdbdb")
                self.id_err.set("Staff ID doesn't exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
        except:
            self.db.close()
            print("Connection error")

    def reset(self):
        self.destroy()
        User_master(self.master,self.db)
