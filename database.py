import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(sno INTEGER PRIMARY KEY AUTOINCREMENT,branchsection text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS students(rollno INTEGER PRIMARY KEY,name text,branchsection text,email text,gender text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS res(rid INTEGER PRIMARY KEY AUTOINCREMENT,rollno text,name text,branchsection text,cgpa text)")
    con.commit()
    
create_db()
