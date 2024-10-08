from tkinter import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,columnspan= 8, column = 1)


title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan= 8, column = 1)


Frame_3=Frame(root)
Frame_3.grid(row=5,column=1,columnspan=8)
title=Label(Frame_3,text="Add Bus Route Details ",fg="khaki4",font="Arial 18 bold")
title.grid(row=1,columnspan= 8, column = 1)


Label(root,text=" ").grid(row=6,column=0)
Label(root,text=" ").grid(row=7,column=0)


route_id=Label(root,text="Route Id",font="Ariel 14")
route_id.grid(row=8,column=0,sticky=E, padx=(330,0))
route_id_entry=Entry(root)
route_id_entry.grid(row=8,column=1,sticky=W)


st_name=Label(root,text="Station Name",font="Ariel 14")
st_name.grid(row=8,column=2,sticky=E, padx=(20,0))
st_name_entry=Entry(root)
st_name_entry.grid(row=8,column=3,sticky=W)


st_id=Label(root,text="Station Id",font="Arial 14")
st_id.grid(row=8,column=4,sticky=E, padx=(20,0))
st_id_entry=Entry(root)
st_id_entry.grid(row=8,column=5,sticky=W)


Button(root,text="Add Route",bg="slategray1",width=10,font="Ariel 12 bold").grid(row=8,column=6, padx=(20,0))
Button(root,text="Delete Route",bg="slategray1",width=10,font="Ariel 12 bold",fg="red2").grid(row=8,column=7, padx=(20,0))


Label(root,text=" ").grid(row=9,column=0)
Label(root,text=" ").grid(row=10,column=0)


HOME=PhotoImage(file=".\\home.png")
def onClick2(e=1):
    root.destroy()
    import page2
Button(root,image=HOME, command=onClick2).grid(row=11,columnspan= 8, column = 1)
