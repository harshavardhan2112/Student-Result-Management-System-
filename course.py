from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System") 
        self.root.geometry("1000x600+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white").place(x=10,y=15,width=1000,height=35)

        lbl_branch=Label(self.root,text="Branch-Section",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        
        self.var_branch=StringVar()
        self.txt_branch=Entry(self.root,textvariable=self.var_branch,font=(15),bg="lightyellow").place(x=180,y=100,width=250,height=30)

        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=60,y=400,width=220,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=300,y=400,width=220,height=40)


        lbl_search=Label(self.root,text="Branch-Section",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=100)
        self.var_search=StringVar()
        self.txt_search=Entry(self.root,textvariable=self.var_search,font=(15),bg="lightyellow").place(x=670,y=100,width=150,height=30)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="lightblue",command=self.search).place(x=830,y=100,width=150,height=30)
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=600,y=200,width=350,height=380)
        

        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("sno","branchsection"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("sno",text="SNo")
        self.CourseTable.heading("branchsection",text="Branch-Section")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("sno",width=50)
        self.CourseTable.column("branchsection",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1) 
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,ev):
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_branch.set(row[1])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_branch.get()=="":
                messagebox.showerror("Error","Branch Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where branchsection=?",(self.var_branch.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Branch Name already exist",parent=self.root)
                else:
                    cur.execute("insert into course(branchsection) values(?)",[self.var_branch.get()])
                    con.commit()
                    messagebox.showinfo("Success","Branch Name added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_branch.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_branch.get()=="":
                messagebox.showerror("Error","Branch Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where branchsection=?",(self.var_branch.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select branch from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where branchsection=?",(self.var_branch.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course delete Successfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

            
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where branchsection LIKE '%{self.var_search.get()}%'",(self.var_branch.get()))
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop() 
