from tkinter import *
root=Tk()
import sqlite3

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan=12, column= 1)

title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan=12, column= 1)

Frame_3=Frame(root)
Frame_3.grid(row=5,columnspan=12, column= 1)
title=Label(Frame_3,text="Add Bus Details ",fg="khaki4",font="Arial 20 bold")
title.grid(row=1,columnspan=12, column= 1)

Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

connect = sqlite3.Connection("Bus_Booking.db")

conn = connect.cursor()
def Add1(e=1):
    conn = connect.cursor()
    conn.execute("INSERT INTO BUS(Bus_ID,Type, Capacity, Fare, Route_ID , Operator_ID) Values (?,?,?,?,?,?)",(Bus_ID.get(),Type.get(),Capacity.get(),Fare.get(),Route_ID.get(),Operator_ID.get()))
    connect.commit()
    connect.close()
    lab1 = Label(root, text= Bus_ID.get()+" "+Type.get()+" "+Capacity.get()+" "+Fare.get()+" "+Route_ID.get(), font = 'Arian 12')
    lab1.grid(row= 11, column =3, columnspan = 5)
    messagebox.showinfo("success","Record added successfully")

def Edit1(e=1):
    conn = connect.cursor()
    conn.execute("update BUS set Bus_ID=?,Type=?, Capacity =?, Fare=?,Route_ID=? where Bus_ID= ? ",(Bus_ID.get(),Type.get(),Capacity.get(),Fare.get(),Route_ID.get(),Operator_ID.get()))
    connect.commit()
    connect.close()


bus_id=Label(root,text="Bus ID",font="Arial 15")
bus_id.grid(row=8,column=0,sticky=E, padx=(115,0))
bus_id_entry=Entry(root)
bus_id_entry.grid(row=8,column=1,sticky=W)


bus_type=Label(root,text="Bus Type",font="Arial 15")
bus_type.grid(row=8,column=2,sticky=E, padx=(15,0))
bus_type=StringVar()
bus_type.set("Bus Type")
option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non-AC sleeper 2x1"]
d_menu=OptionMenu(root,bus_type,*option)
d_menu.grid(row=8,column=3,sticky=W)



capacity=Label(root,text="Capacity",font="Arial 15")
capacity.grid(row=8,column=4,sticky=E, padx=(15,0))
capacity_entry=Entry(root)
capacity_entry.grid(row=8,column=5,sticky=W)



fare=Label(root,text="Fare Rs",font="Arial 15")
fare.grid(row=8,column=6,sticky=E, padx=(15,0))

fare_entry=Entry(root)
fare_entry.grid(row=8,column=7,sticky=W)



op_id=Label(root,text="Operator id",font="Arial 15")
op_id.grid(row=8,column=8,sticky=E, padx=(15,0))

op_id_entry=Entry(root)
op_id_entry.grid(row=8,column=9,sticky=W)



route_id=Label(root,text="Route id",font="Arial 15")
route_id.grid(row=8,column=10,sticky=E, padx=(15,0))

route_id_entry=Entry(root)
route_id_entry.grid(row=8,column=11,sticky=W)



Label(root,text=" ").grid(row=9,column=0)
Label(root,text=" ").grid(row=10,column=0)



Button(root,text="Add Bus",bg="slategray1",width=10,font="Arial 10 bold", command=Add1).grid(row=11, column= 8)

Button(root,text="Edit Bus",bg="slategray1",width=10,font="Arial 10 bold", command=Edit1).grid(row=11, column= 9)

HOME=PhotoImage(file=".\\home.png")
def onClick2(e=1):
    root.destroy()
    import Mypage2
Button(root,image=HOME, command=onClick2).grid(row=11,columnspan=12, column= 1)


