from tkinter import *
root=Tk()
import sqlite3


w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan=8, column=1)

title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan=8, column=1)

connect = sqlite3.Connection("Bus_Booking_System.db")

conn = connect.cursor()


connect = sqlite3.Connection("Bus_Booking_System.db")
conn = connect.cursor()
conn.execute("INSERT INTO RUN(Bus_ID, Date, Seat_Availavle) values(?,?,?)", (bus_id_entry.get(), r_date_entry.get(), seat_a_entry.get()))
connect.commit()
connect.close()
lab1 = Label(root, text= bus_id_entry.get()+" "+r_date_entry.get()+" "+seat_a_entry.get(), font = 'Arian 12')
lab1.grid(row=11, column=2, columnspan = 4)
messagebox.showinfo("run entry", "run record added")


Frame_3=Frame(root)
Frame_3.grid(row=5,columnspan=8, column=1)
title=Label(Frame_3,text="Add Bus Running Details ",fg="red3",font="Ariel 18 bold")
title.grid(row=1,columnspan=8)

Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

bus_id=Label(root,text="Bus ID",font="Ariel 14")
bus_id.grid(row=8,column=0,sticky=E, padx=(330,0))
bus_id_entry=Entry(root)
bus_id_entry.grid(row=8,column=1,sticky=W)

r_date=Label(root,text="Running Date",font="Ariel 14")
r_date.grid(row=8,column=2,sticky=E, padx=(25,5))
r_date_entry=Entry(root)
r_date_entry.grid(row=8,column=3,sticky=W)

seat_a=Label(root,text="Seat Available",font="Ariel 14")
seat_a.grid(row=8,column=4,sticky=E, padx=(25,5))
seat_a_entry=Entry(root)
seat_a_entry.grid(row=8,column=5,sticky=W)

Button(root,text="Add run",bg="slategray1",width=10,font="Ariel 12 bold").grid(row=8,column=6, padx=(20,0))

Button(root,text="Edit Bus",bg="slategray1",width=10,font="Ariel 12 bold").grid(row=8,column=7, padx=(20,0))

Label(root,text="").grid(row=9,column=0)
Label(root,text="").grid(row=10,column=0)

HOME=PhotoImage(file=".\\home.png")
def onClick2(e=1):
    root.destroy()
    import Mypage2
Button(root,image=HOME, command=onClick2).grid(row=11,columnspan=8, column=1)
