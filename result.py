from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System") 
        self.root.geometry("1000x600+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1000,height=50)

        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_branchsection=StringVar()
        self.var_cgpa=StringVar()
        self.var_name=StringVar()
        self.rollno_list=["Select"]
        self.fetch_roll()

        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160)
        lbl_branchsection=Label(self.root,text="Branch-Section",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=220)
        lbl_cgpa=Label(self.root,text="CGPA",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=280)
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_rollno,values=self.rollno_list,font=(15),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200,height=30)
        self.txt_student.current(0)

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="lightblue",cursor="hand2",command=self.search).place(x=500,y=100,width=150,height=30)

        self.txt_name=Entry(self.root,textvariable=self.var_name,font=(20),bg="lightyellow",state='readonly').place(x=280,y=160,width=320,height=30)
        self.txt_branchsection=Entry(self.root,textvariable=self.var_branchsection,font=(20),bg="lightyellow",state='readonly').place(x=280,y=220,width=320,height=30)
        self.txt_cgpa=Entry(self.root,textvariable=self.var_cgpa,font=(20),bg="lightyellow").place(x=280,y=280,width=320,height=30)


        self.btn_add=Button(self.root,text="Submit",font=("times new roman",15,"bold"),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=170,y=420,width=120,height=35)
        self.btn_add=Button(self.root,text="Update",font=("times new roman",15,"bold"),bg="lightblue",activebackground="lightblue",cursor="hand2",command=self.update).place(x=300,y=420,width=120,height=35)
        self.btn_update=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",activebackground="lightgrey",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)



    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select rollno from students")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.rollno_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error **due to {str(ex)}")

            
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,branchsection from students where rollno=?",(self.var_rollno.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_branchsection.set(row[1])
                
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_branchsection.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from res where rollno=? and branchsection=?",(self.var_rollno.get(),self.var_branchsection.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exist",parent=self.root)
                else:
                    cur.execute("insert into res(rollno,name,branchsection,cgpa) values(?,?,?,?)",(self.var_rollno.get(),self.var_name.get(),self.var_branchsection.get(),self.var_cgpa.get()))
                    con.commit()
                    messagebox.showinfo("Success","Result added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_branchsection.set("")
        self.var_cgpa.set("")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from students where rollno=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update res set cgpa=? where rollno=?",(self.var_cgpa.get(),self.var_rollno.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Student updated Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



            

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop() 
