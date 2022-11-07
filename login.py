from tkinter import*
from PIL import ImageTk
from tkinter import messagebox,ttk
import pymysql
import os



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")



        left_lb1=Label(self.root,bg="#08A3D2",bd=0)
        left_lb1.place(x=0,y=0,relheight=1,relwidth=1)

        right_lb1=Label(self.root,bg="#031F3C",bd=0)
        right_lb1.place(x=600,y=0,relheight=1,relwidth=1)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=50,y=100,width=480,height=500)

        login_frame1=Frame(self.root,bg="white")
        login_frame1.place(x=700,y=100,width=480,height=500)

        

        title=Label(login_frame1,text="ADMIN LOGIN",font=("times new roman",30,"bold"),bg="white")
        title.place(x=-160,y=100,width=700,height=35)
        
        email=Label(login_frame1,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=50,y=150)
        self.txt_email=Entry(login_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=180,width=350,height=35)


        pass_=Label(login_frame1,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=50,y=250)
        self.txt_pass_=Entry(login_frame1,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_pass_.place(x=50,y=280,width=350,height=35)


        btn_reg=Button(login_frame1,cursor="hand2",command=self.register_window,text="Register new account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=50,y=320)
        btn_forget=Button(login_frame1,cursor="hand2",command=self.forget_password_window,text="Forget Password",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)


        btn_login=Button(login_frame1,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=50,y=380,width=180,height=40)

        title=Label(login_frame,text="STUDENT RESULT",font=("times new roman",30,"bold"),bg="white")
        title.place(x=-120,y=200,width=700,height=35)


        enter_btn=Button(login_frame,text="Result",command=self.res,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=120,y=300,width=180,height=40)

        self.bg1=ImageTk.PhotoImage(file="cbit1.jpg")
        bg=Label(self.root,image=self.bg1).place(x=530,y=250,width=170,height=250)


    def reset(self):
            self.txt_pass_.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_new_pass_.delete(0,END)
            self.txt_email.delete(0,END)
            self.cmb_quest.set(0)

    def forget_password(self):
            if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass_.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root2)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="empl2")
                    cur=con.cursor()
                    cur.execute("select * from emp3 where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Please select the correct Sequrity Question/Enter Answer",parent=self.root2)
                    else:
                        cur.execute("update emp3 set password=%s where email=%s",(self.txt_new_pass_.get(),self.txt_email.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Your password has been rest,Please login with new password",parent=self.root2)
                        self.reset()
                        self.root2.destroy()
                except Exception as es:
                    messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root2)



    def forget_password_window(self):
            if self.txt_email.get()=="":
                messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="empl2")
                    cur=con.cursor()
                    cur.execute("select * from emp3 where email=%s",self.txt_email.get(),)
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","User doesn't Exist",parent=self.root)
                    else:
                        con.close()
                        self.root2=Toplevel()
                        self.root2.title("Forget Password")
                        self.root2.geometry("350x400+495+150")
                        self.root2.config(bg="white")
                        self.root2.focus_force()
                        self.root2.grab_set()

                        
                        t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)


                        question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                        self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly",justify=CENTER)
                        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best friend name")
                        self.cmb_quest.place(x=50,y=130,width=250)
                        self.cmb_quest.current(0)


                        answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                        self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                        self.txt_answer.place(x=50,y=210,width=250)

                        new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                        self.txt_new_pass_=Entry(self.root2,font=("times new roman",15),bg="lightgray",show='*')
                        self.txt_new_pass_.place(x=50,y=290,width=250)

                        btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                        
                except Exception as es:
                    messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)
    def register_window(self):
            import register
            self.root.destroy()
            os.system("python register.py")

    def login(self):
            if self.txt_email.get()=="" or self.txt_pass_.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="empl2")
                    cur=con.cursor()
                    cur.execute("select * from emp3 where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                    else:
                        messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                        self.root.destroy()
                        os.system("python prog.py")
                        
                        
                    con.close()
                except Exception as es:
                    messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)
    

    def res(self):
        import viewres2
        self.root.destroy()
        os.system("python viewres2.py")
        

root=Tk()
obj=Login_window(root)
root.mainloop()
                    
