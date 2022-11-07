from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
import os
class viewresultClass2:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System") 
        self.root.geometry("1000x600+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="View Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1000,height=50)

        self.var_search=StringVar()
        self.var_id=""

        lbl_search=Label(self.root,text="Search by Roll No",font=("goudy old style",15,"bold"),bg="white").place(x=200,y=100,height=35)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=380,y=100,width=200,height=35)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="lightblue",cursor="hand2",command=self.search).place(x=600,y=100,width=150,height=35)



        lbl_rollno=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=200,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=340,y=230,width=200,height=50)
        lbl_branchsection=Label(self.root,text="Branch-Section",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=530,y=230,width=200,height=50)
        lbl_cgpa=Label(self.root,text="CGPA",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=720,y=230,width=200,height=50)


        self.rollno=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.rollno.place(x=150,y=280,width=200,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=340,y=280,width=200,height=50)
        self.branchsection=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.branchsection.place(x=530,y=280,width=200,height=50)
        self.cgpa=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.cgpa.place(x=720,y=280,width=200,height=50)

        btn_exit=Button(self.root,text="Exit",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.exit).place(x=500,y=350,width=100,height=35)


    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. is required",parent=self.root)
            else:
                cur.execute("select * from res where rollno=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.rollno.config(text=row[1]) 
                    self.name.config(text=row[2])
                    self.branchsection.config(text=row[3])
                    self.cgpa.config(text=row[4])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def exit(self):
        self.root.destroy()
        os.system("python login.py")


            
if __name__=="__main__":
    root=Tk()
    obj=viewresultClass2(root)
    root.mainloop() 
