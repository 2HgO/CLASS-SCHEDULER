import pymysql
from tkinter import *
from tkinter import messagebox
import sys
import datetime

u=sys.argv[1]
p=sys.argv[2]

class dropdown:
    def __init__(self,appen,lis):
        self.m = StringVar()
        self.m.set("choose")
        self.opt=OptionMenu(appen,self.m,*lis)
        self.opt.grid(row=len(lis),column=1)

    def place(self,p,q):
        self.opt.place(x=p,y=q)

db = pymysql.connect("localhost",u,p,"DBMS")
cursor = db.cursor()
LEC=[]
STU=[]
courses=[]
venues=[]
t=['0{}:00:00'.format(x) for x in range(7,10)]
t+=['{}:00:00'.format(x) for x in range(10,19)]
Day=['Monday','Tuesday','Wednesday','Thursday','Friday']
def up():
    global LEC
    global STU
    global courses
    global venues
    cursor.execute("Select * from Lecturer;")
    LEC = cursor.fetchall()
    cursor.execute("Select * from Student;")
    STU = cursor.fetchall()
    cursor.execute("Select CourseID from Courses order by CourseID ASC;")
    courses = cursor.fetchall()
    cursor.execute("Select Venue from Venues order by Venue ASC")
    venues = list(map(lambda x: str(x).strip(",')("),cursor.fetchall()))

up()

cl={'CT':"blue",'CS-A':"yellow",'CS-B':"green",'CIS':"orange"}
def table():
    ind = 0
    top=Toplevel()
    top.geometry("480x540")
    top.resizable(height=False,width=False)
    top.title("Schedule")
    w=Canvas(top,bg="white",height=480,width=480)
    w.pack()
    for i in range(1,9):
        w.create_line(i*60,0,i*60,480,fill="black")
    for i in range(1,12):
        w.create_line(0,i*40,480,i*40,fill="black")
    for i in range(7,18):
        Label(top,text=(str(i)+":00")).place(x=5,y=(i-7)*40+53)
    for i,l in zip(range(7,15),venues):
        Label(top,text=l).place(x=(i-7)*60+68,y=12)
    def tbl():
        nonlocal ind
        cursor.execute("select Schedule.CourseID, Schedule.Program, Schedule.Venue, Schedule.StartTime, Schedule.StopTime, Courses.LecturerID from Schedule inner join Courses on Courses.CourseID = Schedule.CourseID where Day = '{}';".format(Day[ind]))
        a=cursor.fetchall()
        for i in range(len(a)):
            st=str((datetime.datetime.min + a[i][3]).time())
            sp=str((datetime.datetime.min + a[i][4]).time())
            w.create_rectangle((venues.index(a[i][2])+1)*60,(t.index(st)+1)*40,(venues.index(a[i][2])+2)*60,(t.index(sp)+1)*40,fill=cl[a[i][1]])
            y=((t.index(st)+1)*40 + (t.index(sp)+1)*40)/2 - 18
            Label(w,text="{}\n{}\n{}".format(a[i][0],a[i][1],a[i][5])).place(x=(venues.index(a[i][2]))*60+64,y=y) #(t.index(st))*40+47)
    tbl()
    def prev_():
        nonlocal ind
        if ind >0:
            ind-=1
            for wid in w.winfo_children():
                wid.destroy()
            for i in w.find_all()[19:]:
                w.delete(i)
            tbl()
            lab.config(text=Day[ind])
    def nex_():
        nonlocal ind
        if ind <4:
            ind+=1
            for wid in w.winfo_children():
                wid.destroy()
            for i in w.find_all()[19:]:
                w.delete(i)
            tbl()
            lab.config(text=Day[ind])
    lab=Label(top,text=Day[ind])
    lab.place(x=220,y=505)
    prev=Button(top,text="prev",command = prev_)
    nex = Button(top,text="next",command=nex_)
    prev.place(x=130,y=500)
    nex.place(x=302,y=500)

def Student():
    i = 0
    top=Toplevel()
    top.title("Student")
    top.geometry("300x280")
    top.resizable(height=False,width=False)
    l1 = Label(top,text="Matric:")
    l2 = Label(top,text="FName:")
    l3 = Label(top,text="Lname:")
    l4 = Label(top,text="Program:")
    l1.place(x=98,y=30)
    l2.place(x=105,y=70)
    l3.place(x=105,y=110)
    l4.place(x=91,y=150)
    d1 = Label(top,text=STU[i][1])
    d2 = Label(top,text=STU[i][2])
    d3 = Label(top,text=STU[i][3])
    d4 = Label(top,text=STU[i][4])
    d1.place(x=170,y=30)
    d2.place(x=170,y=70)
    d3.place(x=170,y=110)
    d4.place(x=170,y=150)
    def pr():
        nonlocal i
        if i > 0: 
            i -= 1
        d1.configure(text=STU[i][1])
        d2.configure(text=STU[i][2])
        d3.configure(text=STU[i][3])
        d4.configure(text=STU[i][4])
    def ne():
        nonlocal i
        if i < len(STU)-1: 
            i += 1
        d1.configure(text=STU[i][1])
        d2.configure(text=STU[i][2])
        d3.configure(text=STU[i][3])
        d4.configure(text=STU[i][4])
    def new():
        nonlocal i
        def upd(a,b,c,ap):
            a=a.strip()
            b=b.strip()
            sql="insert into Student value (NULL,NULL,'{}','{}','{}');".format(a,b,c)
            try:
                cursor.execute(sql)
                cursor.execute("call GenMatric();")
                db.commit()
                messagebox.showinfo("Confirmation","Student Added Successfully.")
                up()
                ap.destroy()
            except:
                db.rollback()
                messagebox.showerror("Value Error","Could not add Student")
        appen = Toplevel()
        appen.title("New Student")
        appen.geometry("300x230")
        appen.resizable(height=False,width=False)
        l1 = Label(appen,text="id:")
        l1.place(x=50,y=20)
        l2 = Label(appen,text ="FName:")
        l2.place(x=29,y=60)
        l3 = Label(appen,text ="LName:")
        l3.place(x=29,y=100)
        l4 = Label(appen,text ="Program:")
        l4.place(x=15,y=140)
        id_ = Label(appen,text=str(len(STU)+1))
        id_.place(x=100,y=20)
        fname = Entry(appen,bd=5)
        fname.place(x=100,y=60)
        lname = Entry(appen,bd=5)
        lname.place(x=100,y=100)
        prog=dropdown(appen,['CT','CIS','CS-A','CS-B'])
        prog.place(100,135)
        comit=Button(appen,text="register",command=lambda: upd(fname.get(),lname.get(),prog.m.get(),appen))
        comit.place(x=100,y=180)

    prev = Button(top,text="Prev",command = pr)
    prev.place(x=50,y=190)
    next_ = Button(top,text="Next",command = ne)
    next_.place(x =190,y=190)
    new = Button(top,text="+",command= new)
    new.place(x=130,y=230)

def Lecturer():
    i = 0
    top=Toplevel()
    top.title("Lecturer")
    top.geometry("300x230")
    top.resizable(height=False,width=False)
    l1 = Label(top,text="LecturerID:")
    l2 = Label(top,text="FName:")
    l3 = Label(top,text="Lname:")
    l1.place(x=70,y=30)
    l2.place(x=105,y=70)
    l3.place(x=105,y=110)
    d1 = Label(top,text=LEC[i][1])
    d2 = Label(top,text=LEC[i][2])
    d3 = Label(top,text=LEC[i][3])
    d1.place(x=170,y=30)
    d2.place(x=170,y=70)
    d3.place(x=170,y=110)
    def pr():
        nonlocal i
        if i > 0: 
            i -= 1
        d1.configure(text=LEC[i][1])
        d2.configure(text=LEC[i][2])
        d3.configure(text=LEC[i][3])
    def ne():
        nonlocal i
        if i < len(LEC)-1: 
            i += 1
        d1.configure(text=LEC[i][1])
        d2.configure(text=LEC[i][2])
        d3.configure(text=LEC[i][3])
    def new():
        nonlocal i
        def upd(a,b,ap):
            a=a.strip()
            b=b.strip()
            sql="insert into Lecturer value (NULL,NULL,'{}','{}');".format(a,b)
            try:
                cursor.execute(sql)
                cursor.execute("call GenLecID();")
                db.commit()
                messagebox.showinfo("Confirmation","Lecturer Added Successfully.")
                up()
                ap.destroy()
            except:
                db.rollback()
                messagebox.showerror("Value Error","Could not add Lecturer")
        appen = Toplevel()
        appen.title("New Lecturer")
        appen.geometry("300x210")
        appen.resizable(height=False,width=False)
        l1 = Label(appen,text="id:")
        l1.place(x=50,y=20)
        l2 = Label(appen,text ="FName:")
        l2.place(x=29,y=60)
        l3 = Label(appen,text ="LName:")
        l3.place(x=29,y=100)
        id_ = Label(appen,text=str(len(LEC)+1))
        id_.place(x=100,y=20)
        fname = Entry(appen,bd=5)
        fname.place(x=100,y=60)
        lname = Entry(appen,bd=5)
        lname.place(x=100,y=100)
        comit=Button(appen,text="register",command=lambda: upd(fname.get(),lname.get(),appen))
        comit.place(x=100,y=140)
    prev = Button(top,text="Prev",command = pr)
    prev.place(x =50,y=150 )
    next_ = Button(top,text="Next",command = ne)
    next_.place(x =180,y=150)
    new = Button(top,text="+",command= new)
    new.place(x=130,y=190)

def schedule():
    def course_handler(a,b,c,d,e,f,top):
        try:
            cursor.execute("select CourseID from CourseTaken where Program = '{}';".format(b))
            pro_course = list(map(lambda x: str(x).strip(",')("),cursor.fetchall()))
            cursor.execute("select Size from Venues order by Venue ASC;")
            v = list(map(lambda x: str(x).strip(",')("),cursor.fetchall()))
            cursor.execute("select * from Student where Program = '{}';".format(b))
            classSize = len(cursor.fetchall())
            cursor.execute("select Program, Day, CourseID, StartTime, StopTime from Schedule where CourseID = '{}' and Program = '{}';".format(a,b))
            dur = sum(list(map(lambda o:int(str(o[4])[:2].strip(":("))-int(str(o[3])[:2].strip(":(,)")),cursor.fetchall())))
            cursor.execute("select Units from Courses where CourseID = '{}';".format(a))
            cred = int(cursor.fetchall()[0][0])
            cursor.execute("select Venue, Day, StartTime, StopTime from Schedule;")
            sch = cursor.fetchall()
            cursor.execute("select Program, Day, StartTime, StopTime from Schedule;")
            clas = cursor.fetchall()
            cursor.execute("select LecturerID, Day, StartTime, StopTime from Courses inner join Schedule on Courses.CourseID = Schedule.CourseID where Courses.CourseID = '{}';".format(a))
            lect = cursor.fetchall()
        except:
            messagebox.showerror("Connection Error","Could Not connect to database")
            return

        def timer(a):
            return datetime.timedelta(hours=datetime.datetime.strptime(a,'%H:%M:%S').hour)
        if f<=e:
            messagebox.showerror("Schedule Error","Stop Time cannot be earlier than Start Time")
        elif a not in pro_course:
            messagebox.showerror("Schedule Error","{} do not offer {}".format(b,a))
        elif int(v[list(map(lambda x: str(x).strip(",')("),venues)).index(c)])<classSize:
            messagebox.showerror("Schedule Error","Venue is too small")
        elif cred < dur+int(datetime.datetime.strptime(f,'%H:%M:%S').hour-datetime.datetime.strptime(e,'%H:%M:%S').hour):
            messagebox.showerror("Schedule Error", "Course Overload")
        elif (str(c),str(d),timer(e),timer(f)) in sch:
            messagebox.showerror("Schedule Error","class already holding at venue")
        elif (str(b),str(d),timer(e),timer(f)) in clas:
            messagebox.showerror("Schedule Error","{} already have a class then".format(b))
        elif (str(lect[0][0]),str(d),timer(e),timer(f)) in lect:
            messagebox.showerror("Schedule Error","{} is already teaching a class then".format(lect[0][0]))
        else:
            try:
                cursor.execute("INSERT into Schedule value ('{}','{}','{}','{}','{}','{}');".format(a,b,c,d,e,f))
                db.commit()
                top.destroy()
            except:
                db.rollback()
                messagebox.showerror("Connection Error","Could not connect to database")

    top=Toplevel()
    top.title("Scheduler")
    top.geometry("360x320")
    top.resizable(height=False,width=False)
    l1 = Label(top, text = 'Course:')
    l2 = Label(top,text = 'Program:')
    l3 = Label(top, text = 'Venue:')
    l4 = Label(top, text = 'Day:')
    l5 = Label(top, text = 'Start time:')
    l6 = Label(top, text = 'Stop time:')
    l1.place(x=100,y=30)
    l2.place(x=93,y=70)
    l3.place(x=107,y=110)
    l4.place(x=121,y=150)
    l5.place(x=72,y=190)
    l6.place(x=79,y=230)
    e1 = dropdown(top,list(map(lambda x: str(x).strip(",')("),courses)))
    e1.place(170,25)
    e2 = dropdown(top,['CT','CIS','CS-A','CS-B'])
    e2.place(170,65)
    e3 = dropdown(top,list(map(lambda x: str(x).strip(",')("),venues)))
    e3.place(170,105)
    e4 = dropdown(top,['Monday','Tuesday','Wednesday','Thursday','Friday'])
    e4.place(170,145)
    e5 = dropdown(top,t[:len(t)-1])
    e5.place(170,185)
    e6 = dropdown(top,t[1:])
    e6.place(170,225)
    add_course = Button(top,text="ADD COURSE",command=lambda:course_handler(e1.m.get(),e2.m.get(),e3.m.get(),e4.m.get(),e5.m.get(),e6.m.get(),top))
    add_course.place(x=140,y=275)
    
root = Tk()
root.title("DBMS")
root.geometry("500x500")
root.resizable(height=False,width=False)
w=Canvas(root,bg="white",height=500,width=500)
w.pack()
stu = Button(root,text = "Show Students",command = Student)
lec = Button(root,text = "Show Lecturers",command = Lecturer)
sch = Button(root,text = "Time Table",command=table)
form = Button(root, text = "Schedule Class", command = schedule)
stu.place(x=186.5,y=80)
lec.place(x=186,y=180)
sch.place(x=200,y=280)
form.place(x=186,y=380)
root.mainloop()

db.close()
