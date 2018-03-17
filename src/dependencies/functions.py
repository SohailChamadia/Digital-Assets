from src.dependencies.imports import *

class combo(Frame):

    def __init__(self,master,lst,var,flag=False):
        super(combo,self).__init__(master)
        self.var=var
        self.grid()
        self.create_widgets()
        self.lst=lst
        self.flag=flag
        self.update(self.lst)

    def create_widgets(self):

        row=0
        self.txt=Entry(self)
        self.txt.grid(row=row,column=0,sticky=W+E)
        cmdedt=self.register(self.edt)

        self.txt.config(validate="key",
                        vcmd=(cmdedt,'%P'))

        row+=1

        self.sugg_con=Frame(self)
        self.sugg_con.grid(row=row,column=0,sticky=W+E)
        self.sugg=Listbox(self.sugg_con,height=0,selectmode=SINGLE)
        scrollbar = Scrollbar(self.sugg_con, orient=VERTICAL)
        self.sugg.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.sugg.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.sugg.pack(side=LEFT, fill=BOTH, expand=1)

        self.sugg.bind('<ButtonRelease-1>',self.update_entry)

        row+=1

        self.columnconfigure(0,weight=1)

    def update_entry(self,event):
        try:
            if(self.flag):
                tmp=self.sugg.get(self.sugg.curselection())
                self.txt.delete(0,END)
                self.txt.insert(0,tmp)
                self.var.set(tmp)
        except:
            pass

    def value_config(self,lst):
        self.lst=lst
        self.update(self.lst)

    def edt(self,strarg):
        predict(self.lst,self.txt,self,strarg)
        if(not self.flag):
            self.var=strarg
        return True

    def update(self,lst):
        self.sugg.delete(0,END)
        if len(lst)>6:
            self.sugg.config(height=6)
        else:
            self.sugg.config(height=len(lst))
        for i in lst:
            self.sugg.insert(END,i)
        if len(lst)==0 and self.flag:
            self.var.set("")

def predict(arr,prefix,opt,text):
    val=[]
    for item in arr:
        if item.lower().startswith(text.lower()):
            val.append(item)
    opt.update(val)

def check_ent(ref,flag,msg,error):
    if len(ref.get()) == 0:
        ref.config(bg="#ffdbdb")
        flag.set(False)
        error.set(msg.get())
    else:
        error.set("")
        ref.config(bg="white")

def check_txt(ref,flag,msg,error):
    if len(ref.get("1.0",END)) == 1:
        ref.config(bg="#ffdbdb")
        flag.set(False)
        error.set(msg.get())
    else:
        error.set("")
        ref.config(bg="white")

def check_int(ref,flag,msg,error):
    if not ref.get().isnumeric():
        flag.set(False)
        ref.config(bg="#ffdbdb")
        error.set(msg.get())
    else:
        error.set("")
        ref.config(bg='white')

def check_stvar(ref,list,flag,msg,error):
    if ref.get() not in list:
        error.set(msg.get())
        flag.set(False)
    else:
        error.set("")

def check_comp_stvar(ref,list,flag,msg,error):
    if ref.get() in list:
        error.set(msg.get())
        flag.set(False)
    else:
        error.set("")

def check_date(ref,flag,msg,error):
    try:
        try:
            x=datetime.datetime.strptime(ref.get(), '%d-%m-%Y')
        except:
            x=datetime.datetime.strptime(ref.get(), '%Y-%m-%d')
        ref.config(bg='white')
        ref.delete(0,END)
        ref.insert(0,x.date())
        error.set("")
    except:
        if error.get()=="":
            error.set(msg.get())
        ref.config(bg="#ffdbdb")
        flag.set(False)

def comp_date(date1,date2,flag,msg,error):
    try:
        try:
            d1=datetime.datetime.strptime(date1.get(), '%d-%m-%Y')
            d2=datetime.datetime.strptime(date2.get(), '%d-%m-%Y')
        except:
            d1=datetime.datetime.strptime(date1.get(), '%Y-%m-%d')
            d2=datetime.datetime.strptime(date2.get(), '%Y-%m-%d')
        if d1>d2:
            flag.set(False)
            date1.config(bg="#ffdbdb")
            date2.config(bg="#ffdbdb")
            if error.get()=="":
                error.set(msg.get())
        else:
            error.set("")
            date1.config(bg="white")
            date2.config(bg="white")
    except:
        flag.set(False)

def check_cont(ref,flag,msg,error):
    if len(ref.get()) == 10:
        error.set("")
        check_int(ref,flag,msg,error)
    else:
        error.set(msg.get())
        flag.set(False)
        ref.config(bg="#ffdbdb")

def comp_amt(amt1,amt2,flag,msg,error):
    try:
        x=int(amt1.get())
        y=int(amt2.get())
        if y<x:
            flag.set(False)
            amt1.config(bg="#ffdbdb")
            amt2.config(bg="#ffdbdb")
            error.set(msg.get())
        else:
            error.set("")
            amt1.config(bg="white")
            amt2.config(bg="white")
    except:
        flag.set(False)
