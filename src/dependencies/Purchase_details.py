from src.dependencies.imports import *

class Purchase_details(LabelFrame):

    def __init__(self,master,db,flag):
        super(Purchase_details,self).__init__(master)
        self.grid()
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

        self.flag=flag
        self.item=[]
        self.vendors=[]
        self.selct=[]
        self.db=db
        self.ven_populate()
        self.create_widgets()
        self.populate()
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

        self.frame.config(text="Purchase Details",
                    relief=FLAT,
                    labelanchor=N,
                    padx=30,
                    pady=10)
        textfont=('verdana',10)
        errorfont=('verdana',8)

        Label(self.frame,text="ID: ",
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

        Label(self.frame,text="Purchase Order No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                                     column=0,
                                                     sticky=N+S+W+E)
        self.po_num=Entry(self.frame);
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

        Label(self.frame,text="Vendor ID: ",
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

        Label(self.frame,text="Amount(Total): ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.amt=Entry(self.frame)
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

        Label(self.frame,text="Amount(Paid): ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=N+S+W+E)
        self.paid=Entry(self.frame);
        self.paid.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.paid_err=StringVar()
        self.paid_err.set("")
        Label(self.frame,textvariable=self.paid_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Feedback: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.fb=Text(self.frame,width=40,height=5,wrap=WORD)
        self.fb.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        Label(self.frame,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Bill No.: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                           column=0,
                                           sticky=N+S+W+E)
        self.bill=Entry(self.frame);
        self.bill.grid(row=row,column=1,columnspan=2,sticky=W+E)
        row+=1

        self.bill_err=StringVar()
        self.bill_err.set("")
        Label(self.frame,textvariable=self.bill_err,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=1,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Label(self.frame,text="Items purchased: ",
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

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(width=event.width,height=event.height)

    def new_vendor(self,event):
        self.pack_forget()
        X=__import__("src.dependencies.Vendor_details",fromlist=('Vendor_details'))
        self.z=X.Vendor_details(self.master,self.db,False)
        t=Thread(target=self.call_pack,args=())
        t.setDaemon(True)
        t.start()

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

    def ven_populate(self):
        self.db.connect()
        self.vendors=[]
        x=self.db.execute_sql("select vendor_id,vnd_name from vendor")
        z=list(x.fetchall())
        for items in z:
            self.vendors.append(items[1]+" - "+items[0])
        self.db.close()

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

    def submit(self):
        comp=BooleanVar()
        comp.set(True)
        msg=StringVar()
        msg.set("ID cannot be empty")
        check_ent(self.id,comp,msg,self.id_err)
        msg.set("Invalid Purchase date")
        check_date(self.pur,comp,msg,self.pur_err)
        msg.set("Vendor ID cannot be empty")
        check_stvar(self.ven_id,self.vendors,comp,msg,self.ven_id_err)
        msg.set("Invalid Amount")
        check_int(self.amt,comp,msg,self.amt_err)
        msg.set("Bill cannot be empty")
        check_ent(self.bill,comp,msg,self.bill_err)
        msg.set("Invalid Amount")
        check_int(self.paid,comp,msg,self.paid_err)
        msg.set("Purchase Order Number cannot be empty")
        check_ent(self.po_num,comp,msg,self.po_num_err)
        msg.set("Paid amount is greater than total amount")
        comp_amt(self.paid,self.amt,comp,msg,self.amt_err)
        try:
            self.db.connect()
            if comp.get():
                ven=list(self.ven_id.get().split(" - "))
                self.db.execute_sql("""insert into purchase_order
                                    values('%s','%s','%s','%s',%d,%d,'%s');"""
                                        %(self.id.get(),
                                          self.po_num.get(),
                                          self.pur.get(),
                                          ven[1],
                                          int(self.amt.get()),
                                          int(self.paid.get()),
                                          self.fb.get("1.0",END)
                                    ))
                self.reset()
        except pw.IntegrityError as e:
            print(e)
        except:
            self.db.close()
            print("connection error")

    def reset(self):
        self.destroy()
        if self.flag:
            Purchase_details(self.master,self.db,True)

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
