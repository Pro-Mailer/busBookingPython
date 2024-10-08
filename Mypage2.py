from tkinter import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan = 3, column=0, padx =(500,0))

Label(root,text=" ").grid(row=1,column=0)

title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=2,columnspan = 3, column=0, padx =(450,0))

Label(root,text=" ").grid(row=3,column=0)



def onClick3(e=1):
    root.destroy()
    import Mypage3
Button(root,text ="Seat Booking" , font="20", bg='palegreen2', command=onClick3).grid(row=4,column=0, padx =(450,0))


def onClick4(e=1):
    root.destroy()
    import Mypage4
Button(root,text ="Check booked Seat", font="20", bg='palegreen2', command=onClick4).grid(row=4,column=1, padx =(40,0))


def onClick5(e=1):
    root.destroy()
    import Mypage5
Button(root,text ="Add Bus Details", font="20", bg='palegreen2', command=onClick5).grid(row=4,column=2, padx =(40,0))






title=Label(root,text="Only for Admins",fg='red2',font="Ariel 15")
title.grid(row=5,column=2, padx =(40,0))
