from tkinter import *
import tkinter.messagebox
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=5)



title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,column=0)



Label(root,text="").grid(row=2,column=0)
Enter_Journey_Details=Label(root,text="Check Your Booking",bg="khaki1",fg="red2")
Enter_Journey_Details.grid(row=3,column=0,columnspan=1)
enter_mobile=Label(root,text="Enter Your Mobile No :")
enter_mobile.grid(row=5,column=0,padx=650, sticky=W)


mobile_entry=Entry(root)
mobile_entry.grid(row=5,column=0, padx=812, sticky=W)

def onClick():
    tkinter.messagebox.showinfo("Welcome",  "This is just a placeholder")
Button(root,text="Check Booking", command= onClick).grid(row=5,column=0, padx=(300,0))

