from tkinter import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan=4, column=1)



title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan=4, column=1)

Frame_3=Frame(root)
Frame_3.grid(row=5,columnspan=4, column=1)

title=Label(Frame_3,text="Add New Details to DataBase ",fg="khaki4",font="Arial 14 bold")
title.grid(row=1,columnspan=4, column=1)
Label(root,text="").grid(row=5,columnspan=4, column=1)



def onClick6(e=1):
    root.destroy()
    import page6
Button(root,text="New Operator",bg="navajowhite2", command=onClick6).grid(row=8,column=0, padx=(600,0))



def onClick7(e=1):
    root.destroy()
    import page7
Button(root,text="New Bus",bg="navajowhite2", command=onClick7).grid(row=8,column=1, padx=(120,0))



def onClick8(e=1):
    root.destroy()
    import page8
Button(root,text="New Route",bg="navajowhite2", command=onClick8).grid(row=8,column=2, padx=(120,0))



def onClick9(e=1):
    root.destroy()
    import page9
Button(root,text="New Run",bg="navajowhite2", command=onClick9).grid(row=8,column=3, padx=(120,0))



HOME=PhotoImage(file=".\\home.png")
def onClick2(e=1):
    root.destroy()
    import page2
Button(root,image=HOME, command=onClick2).grid(row=9,columnspan = 4, column= 1)
