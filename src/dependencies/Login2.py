from tkinter import *
import peewee as pw

class Login2(LabelFrame):

    def __init__(self,master):
        super(Login2,self).__init__(master)
        self.master=master
        self.grid()
        labelfont=('times',16,'bold')
        self.config(bd=0,bg="#bdc3c7",font=labelfont)
        self.create_widgets()

    def create_widgets(self):

        row=0

        textfont=('verdana',10)
        errorfont=('verdana',10)

        self.config(text="LOGIN DETAILS",
                    labelanchor=N,
                    padx=50,
                    pady=30)

        Label(self,text="Username: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               sticky=W)
        self.user=Entry(self,justify=LEFT)
        self.user.grid(row=row,column=1,sticky=W)
        self.user.focus_set()
        row+=1

        Label(self,text="Password: ",
              font=textfont,bg="#bdc3c7").grid(row=row,
                                               column=0,
                                               pady=10,
                                               sticky=W)
        self.pwd=Entry(self,show='*',justify=LEFT)
        self.pwd.grid(row=row,column=1,sticky=W)
        row+=1

        self.error_msg=StringVar()
        Label(self,textvariable=self.error_msg,
              font=errorfont,
              fg="red",bg="#bdc3c7").grid(row=row,
                                          column=0,
                                          columnspan=2,
                                          sticky=W+E)
        row+=1

        Button(self,text="Login",bg="#34495e",font=textfont,fg="white",
               command=self.authentication).grid(row=row,
                                                 column=0,
                                                 columnspan=2,
                                                 ipady=10,
                                                 sticky=E+W)
        self.pack(anchor=CENTER,expand=1)

    def authentication(self):
        try:
            self.db=pw.MySQLDatabase("assets",
                        host="localhost",
                        port=3306,
                        user=self.user.get(),
                        passwd=self.pwd.get())
        except:
            print("Connection error")
        try:
            self.db.connect()
            x=self.db.execute_sql("""select * from authentication
                                    where user_name="%s"
                                    and pwd="%s";""" %(self.user.get(),
                                                       self.pwd.get()))
            access=self.user.get()
            z=list(x.fetchall())
            self.master.depts=list(z[0][2].split('\n'))
            self.master.depts.remove("")
            self.db.close()
            self.destroy()
            X=__import__('src.dependencies.Main_menu',fromlist=['Main_menu'])
            if access=='admin':
                X.Main_menu(self.master,self.db,True)
            else:
                X.Main_menu(self.master,self.db,False)
        except:
            self.error_msg.set("Invalid username or password")
