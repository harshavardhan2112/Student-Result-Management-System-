from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System") 
        self.root.geometry("1000x600+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white").place(x=10,y=15,width=1000,height=35)

        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_branchsection=StringVar()

        lbl_rollno=Label(self.root,text="Rollno",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=150)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=200)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=250)
        
        
        
        self.txt_rollno=Entry(self.root,textvariable=self.var_rollno,font=(15),bg="lightyellow").place(x=180,y=100,width=250,height=30)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=(15),bg="lightyellow").place(x=180,y=150,width=250,height=30)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=(15),bg="lightyellow").place(x=180,y=200,width=250,height=30)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=(156),state='readonly',justify=CENTER)
        self.txt_gender.place(x=180,y=250,width=250,height=30)
        self.txt_gender.current(0)
        
        self.branchsection=Label(self.root,text="Branch-Section",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=300)
        self.branchsection_list=["Select"]
        self.fetch_course()
        self.txt_branchsection=ttk.Combobox(self.root,textvariable=self.var_branchsection,values=self.branchsection_list,font=(15),state='readonly',justify=CENTER)
        self.txt_branchsection.place(x=180,y=300,width=250,height=30)
        self.txt_branchsection.current(0)
        
        
        
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=60,y=450,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#008543",fg="white",cursor="hand2",command=self.update).place(x=180,y=450,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=300,y=450,width=110,height=40)


        lbl_search_rollno=Label(self.root,text="Rollno",font=("goudy old style",15,"bold"),bg="white").place(x=570,y=100)
        self.var_search=StringVar()
        self.txt_search=Entry(self.root,textvariable=self.var_search,font=(15),bg="lightyellow").place(x=650,y=100,width=170,height=30)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="lightblue",command=self.search).place(x=830,y=100,width=150,height=30)
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=480,y=200,width=500,height=380)
        

        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("rollno","name","branchsection","email","gender"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("rollno",text="Rollno")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("branchsection",text="BranchSection")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("rollno",width=80)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("branchsection",width=65)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=40)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,ev):
        
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_branchsection.set(row[2])
        self.var_email.set(row[3])
        self.var_gender.set(row[4])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="" or self.var_name.get()=="" or self.var_branchsection=="Select":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            elif(len(self.var_rollno.get())!=12):
                messagebox.showerror("Error","Roll Number should be of 12 digits",parent=self.root)
            else:
                cur.execute("select * from students where rollno=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No already present",parent=self.root)
                else:
                    cur.execute("insert into students(rollno,name,branchsection,email,gender) values(?,?,?,?,?)",(self.var_rollno.get(),self.var_name.get(),self.var_branchsection.get(),self.var_email.get(),self.var_gender.get()))
                    con.commit()
                    messagebox.showinfo("Success","Student added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

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
                    cur.execute("update students set name=?,branchsection=?,email=?,gender=? where rollno=?",(self.var_name.get(),self.var_branchsection.get(),self.var_email.get(),self.var_gender.get(),self.var_rollno.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Student updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_branchsection.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Rollno should be required",parent=self.root)
            else:
                cur.execute("select * from students where rollno=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from students where rollno=?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student delete Successfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

            
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from students")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select branchsection from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.branchsection_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error **due to {str(ex)}")

            
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from students where rollno=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        
if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop() 
