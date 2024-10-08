from tkinter import *
from tkinter.messagebox import *
root=Tk()
import sqlite3


w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan = 14, column= 1, padx=(0, 150))

title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan = 14, column= 1, padx=(0, 150))

connect = sqlite3.connect("Bus_Booking_System.db")
conn = connect.cursor()


Frame_3=Frame(root)
Frame_3.grid(row=5,column=1,columnspan = 14, padx=(0, 115))
title=Label(Frame_3,text="Add Bus Operator Details ",fg="red2",font="Arial 18 bold")
title.grid(row=1,columnspan = 14, column= 1, padx=80)
Label(root,text=" ").grid(row=6,column=0)
Label(root,text=" ").grid(row=7,column=0)

def Add1(e=1):
    connect = sqlite3.connect("Bus_Booking_System.db")
    conn = connect.cursor()
    conn.execute("INSERT INTO OPERATOR(Operator_ID,Opt_Name, Address,Phone_no) Values (?,?,?,?)",(op_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get()))
    lab1 = Label(root, text= op_id_entry.get()+" "+name_entry.get()+" "+address_entry.get()+" "+phone_entry.get(), font = 'Arian 12')
    lab1.grid(row= 11, column =3, columnspan = 5)
    showinfo("success",  "Record added successfully")
    connect.commit()
    connect.close()
def Edit1(e=1):
    connect = sqlite3.connect("Bus_Booking_System.db")
    conn = connect.cursor()
    conn.execute("update OPERATOR set Operator_ID=?,Opt_Name=?, Address =?,Phone_no=? where Operator_ID= ? ",(op_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),op_id_entry.get()))
    lab2 = Label(root, text= op_id_entry.get()+" "+name_entry.get()+" "+address_entry.get()+" "+phone_entry.get(), font = 'Arian 12')
    lab2.grid(row= 11, column =3, columnspan = 5)
    showinfo("operator entry update", "operator record updated succesully")
    connect.commit()
    connect.close()
op_id=Label(root,text="Operator id",font="Ariel 15")
op_id.grid(row=9,column=0,sticky=E, padx=(180,0))

op_id_entry=Entry(root)
op_id_entry.grid(row=9,column=1,sticky=W)

name=Label(root,text="Name",font="Ariel 15 ")
name.grid(row=9,column=2,sticky=E, padx=(25,0))

name_entry=Entry(root)
name_entry.grid(row=9,column=3,sticky=W)

address=Label(root,text="Address",font="Ariel 15")
address.grid(row=9,column=4,sticky=E, padx=(25,0))

address_entry=Entry(root)
address_entry.grid(row=9,column=5,sticky=W)

phone=Label(root,text="Phone",font="Ariel 15")
phone.grid(row=9,column=6,sticky=E, padx=(25,0))

phone_entry=Entry(root)
phone_entry.grid(row=9,column=7,sticky=W)



Button(root,text="Add",bg="slategray1",font="Ariel 15", command=Add1).grid(row=9,column=10, padx=(25,0))
Button(root,text="Edit",bg="slategray1",font="Ariel 15", command=Edit1).grid(row=9,column=11, padx=(25,0))

Label(root,text=" ").grid(row=10,column=12)
Label(root,text=" ").grid(row=11,column=13)

HOME=PhotoImage(file=".\\home.png")
def onClick2(e=1):
    root.destroy()
    import Mypage2
Button(root,image=HOME, command=onClick2).grid(row=12,columnspan = 14, column= 1, padx=(0, 115))
