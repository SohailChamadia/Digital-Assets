from src.dependencies.imports import *

class Vendor_details(Frame):

    def __init__(self,master,db,flag):
        super(Vendor_details,self).__init__(master)
        self.grid()
        self.db=db
        self.config(bg="#bdc3c7")
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
        self.frame.config(bd=10,bg="#bdc3c7",font=labelfont)
        self.selct=[]
        self.item=[]
        self.master=master
        self.flag=flag
        self.vendors=[]
        self.ven_populate()
        self.create_widgets()
        self.populate()
        if not self.flag:
            self.frame.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Label) ,self.frame.children.values()):
                lab.config(bg="#e8e0a9")
            for lab in filter(lambda w:isinstance(w,Button) ,self.frame.children.values()):
                lab.config(bg="#9b9039")


    def create_widgets(self):
        row=0;
        self.frame.config(text="New Vendor Details",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)#e8e0a9

        Label(self.frame,text="Vendor ID: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                            column=0,
                                            sticky=N+S+W+E)
        self.id=StringVar()
        self.id.set(len(self.vendors)+1)
        Label(self.frame,textvariable=self.id,
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=1,
                                               columnspan=2,
                                               sticky=N+S+W+E)
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

        Label(self.frame,text="Name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                       column=0,
                                       sticky=N+S+W+E)
#        self.ven_name=StringVar();
#        self.ven_name.set("")
#        self.name=combo(self.frame,self.vendors,self.ven_name,False)
        self.ven_name=Entry(self.frame)
        self.ven_name.grid(row=row,column=1,columnspan=2,sticky=W+E)
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

        Label(self.frame,text="Company name: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.cmp=Entry(self.frame);
        self.cmp.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.cmp_err=StringVar()
        self.cmp_err.set("")
        Label(self.frame,textvariable=self.cmp_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Address: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                          column=0,
                                          sticky=N+S+W+E)
        self.add=Text(self.frame,width=40,height=4,wrap=WORD)
        self.add.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.add_err=StringVar()
        self.add_err.set("")
        Label(self.frame,textvariable=self.add_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Preffered for items: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.sel=Listbox(self.frame,height=5,selectmode=MULTIPLE)
        self.sel.grid(row=row,column=2,pady=10,sticky=N+S+W+E)
        scr1=Scrollbar(self.sel)
        scr1.pack(side=RIGHT,fill=Y)
        self.sel.config(yscrollcommand=scr1.set)
        self.sel.pack_propagate(False)
        scr1.config(command=self.sel.yview)

        self.items=Listbox(self.frame,height=5,selectmode=MULTIPLE)
        self.items.grid(row=row,column=1,pady=10,sticky=N+S+W+E)
        if self.master.admin_access:
            self.items.bind('<Control-space>',self.new_item)
        scr2=Scrollbar(self.items)
        scr2.pack(side=RIGHT,fill=Y)
        self.items.config(yscrollcommand=scr2.set)
        self.items.pack_propagate(False)
        scr2.config(command=self.items.yview)

        for itm in self.item:
            self.items.insert(END,itm)
        row+=1

        Button(self.frame,text="<<",command=self.unclick,width=15,fg="white",
               font=textfont,bg="#34495e").grid(row=row,
                                                column=2,
                                                sticky=N+S)
        Button(self.frame,text=">>",command=self.click,width=15,fg="white",
               font=textfont,bg="#34495e").grid(row=row,
                                                column=1,
                                                sticky=N+S)

        row+=1

        Label(self.frame,text="Company Contact No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.num=Entry(self.frame);
        self.num.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.num_err=StringVar()
        self.num_err.set("")
        Label(self.frame,textvariable=self.num_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Company URL: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                              column=0,
                                              sticky=N+S+W+E)
        self.url=Entry(self.frame);
        self.url.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.url_err=StringVar()
        self.url_err.set("")
        Label(self.frame,textvariable=self.url_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Other details: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                column=0,
                                                sticky=N+S+W+E)
        self.det=Text(self.frame,width=40,height=4,wrap=WORD)
        self.det.grid(row=row,column=1,columnspan=2,sticky=W+E)
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

    def new_item(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Item_master",fromlist=('Item_master'))
        self.z=X.Item_master(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.setDaemon(True)
        t.start()

    def call_pack(self):
        try:
            while self.z.winfo_exists():
                sleep(0.1)
                pass
            self.pack(anchor=CENTER,expand=1)
            self.populate()
        except:
            pass

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(width=event.width,height=event.height)

    def populate(self):
        self.db.connect()
        x=self.db.execute_sql("select items from item_master")
        z=list(x.fetchall())
        self.item=[]
        self.items.delete(0,END)
        for itm in z:
            self.item.append(itm[0])
            self.items.insert(END,itm[0])
        self.db.close()

    def ven_populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[0])
        self.db.close()

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("Company Name cannot be empty")
        check_ent(self.cmp,comp,msg,self.cmp_err)
        msg.set("Name already exists"+self.ven_name.get())
        check_comp_stvar(self.ven_name,self.vendors,comp,msg,self.name_err)
        msg.set("Address cannot be empty")
        check_txt(self.add,comp,msg,self.add_err)
        msg.set("URL cannot be empty")
        check_ent(self.url,comp,msg,self.url_err)
        msg.set("Invalid Contact Number")
        check_cont(self.num,comp,msg,self.num_err)
        prefer=""
        for items in self.selct:
            prefer+=(items+"\n")
        try:
            self.db.connect()
            if comp.get():
                self.db.execute_sql("""insert into vendor
                                    values('%s','%s','%s','%s','%s','%s','%s','%s');"""
                                        %(self.id.get(),
                                          self.ven_name.get(),
                                          self.cmp.get(),
                                          self.add.get("1.0",END),
                                          prefer,
                                          self.url.get(),
                                          self.num.get(),
                                          self.det.get("1.0",END)
                                    ))
                self.reset()
        except pw.IntegrityError as e:
            x,y=e.args
            print(e)
            if x==1062:
                self.id.config(bg="#ffdbdb")
                self.id_err.set("Vendor ID already exists")
            else:
                self.id_err.set("")
                self.id.config(bg='white')
        except:
            self.db.close()
            print(e)

    def reset(self):
        self.destroy()
        if self.flag:
            Vendor_details(self.master,self.db,True)

    def click(self):
        for items in reversed(self.items.curselection()):
            cnt=0;
            while(self.sel.get(cnt)<self.items.get(items) and self.sel.size()>cnt):
                cnt+=1
            self.sel.insert(cnt,self.items.get(items))
            self.selct.append(self.items.get(items))
            self.item.remove(self.items.get(items))
            self.items.delete(items)
        self.selct.sort()

    def unclick(self):
        for items in reversed(self.sel.curselection()):
            cnt=0;
            while(self.items.get(cnt)<self.sel.get(items) and self.items.size()>cnt):
                cnt+=1
            self.items.insert(cnt,self.sel.get(items))
            self.item.append(self.sel.get(items))
            self.selct.remove(self.sel.get(items))
            self.sel.delete(items)
        self.item.sort()
