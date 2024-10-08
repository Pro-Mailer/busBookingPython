from tkinter import*
root=Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 0,sticky=W,padx=(630,0))
Label(root,text = "Online Bus Booking System", font = "arial 18 bold", bg = 'sky blue', fg ='Red').grid(row = 1, column = 0, padx = 600)
Label(root,text="Name:Devansh Gupta", font = "arial 14 bold" , fg = 'blue').grid(row = 2 , column = 0, pady = 30)
Label(root,text="Er : 211B104", font = "arial 14 bold" , fg = 'blue').grid(row = 3 , column = 0, pady = 30)
Label(root,text="Mobile:9981797008", font = "arial 14 bold" , fg = 'blue').grid(row = 4 , column = 0, pady = 30)
def mypage2():
    root.destroy()
    import Mypage2
Label(root,text="Submitted to :Dr. Mahesh Kumar", font = "arial 18 bold" , bg = 'sky blue' ,fg = 'red').grid(row = 5 , column = 0, pady = 30)
Label(root,text="Project Based Learning", font = "arial 16 bold" , fg = 'red').grid(row = 6 , column = 0)
Button(root,text="Press any key to Proceed", font = "arial 16 bold" , fg = 'red',command=mypage2).grid(row= 7,pady=30)








root.mainloop()
                             


