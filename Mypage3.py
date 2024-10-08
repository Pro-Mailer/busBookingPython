from tkinter import *
root=Tk()
from tkinter import messagebox
import sqlite3

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0 ,columnspan = 8, column = 1,padx=(0,150))



title=Label(root,text="Online Bus Booking System",bg='slategray1', fg='red2',font="Ariel 25 bold")
title.grid(row=1,columnspan = 8, column = 1,padx=(0,150))

Label(root,text=" ").grid(row=2)

Enter_Journey_Details=Label(root,text="Enter Journey Details", fg="red2",font="Ariel 15 bold" )
Enter_Journey_Details.grid(row=3,columnspan = 8, column = 1,padx=(0,150))

Label(root,text=" ").grid(row=4)


to=Label(root,text="To")
to.grid(row=5, column = 0, sticky = E, padx= (350,10))
to_entry=Entry(root)
to_entry.grid(row=5, column = 1)



fro=Label(root,text="From")
fro.grid(row=5 , column = 2, padx=(75,10),sticky = E)
from_entry=Entry(root)
from_entry.grid(row=5, column = 3, sticky=W)






journey_date=Label(root,text="Journey Date")
journey_date.grid(row=5, column=4, padx=(75,10))
journey_date_entry=Entry(root)
journey_date_entry.grid(row=5, column=5, sticky=W)

def book():
    blank = Label(root, text = "                            " )
    blank.grid(row = 11, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 12, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 13, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 14, column = 0)
    
    fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
    fill_label.grid(row = 15, column = 0, columnspan = 8)

    blank = Label(root, text = "                            " )
    blank.grid(row = 16, column = 0)

    name_text = Label(root, text = "Name")
    name_text.grid(row = 17, column=0)

    name_ent = Entry(root)
    name_ent.grid(row =17, column=1)

    gender_text = Label(root, text = "Gender")
    gender_text.grid(row = 17, column=2)

    gender_drop = OptionMenu(root, 'clicked' , "Male", "Female", "Third Gender")
    gender_drop.grid(row = 17, column = 3)

    seats_text = Label(root, text = "No of Seats")
    seats_text.grid(row = 17, column=4)

    seats_ent = Entry(root)
    seats_ent.grid(row =17, column=5)

    mobile_text = Label(root, text = "Mobile No")
    mobile_text.grid(row = 17, column=6)

    mobile_ent = Entry(root)
    mobile_ent.grid(row =17, column=7)

    age_text = Label(root, text = "Age")
    age_text.grid(row = 17, column=8)

    age_ent = Entry(root)
    age_ent.grid(row =17, column=9)

    book_button = Button(root, text = "Book Seat", bg ="lightgreen", command = sure)
    book_button.grid(row = 17, column=10)

    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()

    c.execute("INSERT INTO BOOKING_HISTORY(Passengers_Name , Gender , No_of_seats , Mobile_no) VALUES(?,?,?,?)", (name_ent.get(),clicked.get(),seats_ent.get(),mobile_ent.get()))
    connect.commit()
    


book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = book)
book_button.grid(row =20 , column= 6, columnspan=2)

frame=Frame(root)
l=[]
b=[]
h=[]
def show():
    select_text = Label(frame, text = "Select Bus", fg = "green")
    select_text.grid(row = 0, column=0,padx=(80,160))

    opt_text = Label(frame, text = "Operator", fg = "green")
    opt_text.grid(row = 0, column=1,padx=(0,160))

    type_text = Label(frame, text = "Bus Type", fg = "green")
    type_text.grid(row = 0, column=2,padx=(0,160))

    available_text = Label(frame, text = "Available", fg = "green")
    available_text.grid(row = 0, column=3,padx=(0,160))
    
    capacity_text = Label(frame, text = "Capacity", fg = "green")
    capacity_text.grid(row = 0, column=4,padx=(0,160))

    fare_text = Label(frame, text = "Fare", fg = "green")
    fare_text.grid(row = 0, column=5,padx=(0,120))
    frame.grid(row=6,columnspan=20,pady=30)
    book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = book)
    book_button.grid(row =20 , column= 7, columnspan=2)

    
    connect = sqlite3.Connection("Bus_Booking_System.db")
    conn = connect.cursor()
    

    conn.execute('''Select o.Opt_name, b.type, r.Seat_Availavle,b.Capacity, b.fare from bus as b, operator as o, run as r, route as re where re.station_name = ? and  b.operator_id = o.operator_id and b.bus_id = r.bus_id''',(from_entry.get(),))
    records = conn. fetchall()
    info=records
    #for i in records:
     #   businfo=i
      #  l.append(businfo[2])
       # b.append(businfo[2])
        #h.append(businfo[2])
    #print(v)
    #print(records)
    count =1
    count2=1
    for i in info:
        count1=1
        l=i
        length=len(l)
        for j in range(length):

                Label(frame,text=l[j]).grid(row=count2,column=count1,sticky=W)
                count1=count1+1
    count2=count2+1
    Radiobutton(root)
    connect.commit()



    
Button(root,text ="Find my Bus!", command = show).grid(row=5, column=6, padx=(75,10))
img_1=PhotoImage(file=".\\home.png")


def onClick2(e=1):
    root.destroy()
    import Mypage2
    
Button(root,image=img_1, command=onClick2).grid(row=5, column=7, padx=(75,0))

