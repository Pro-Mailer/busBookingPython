import sqlite3

connect = sqlite3.Connection("Bus_Booking_System.db")

conn = connect.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS BUS(Bus_ID int,Type text, Capacity int, Fare int, Route_ID int, Operator_ID int, PRIMARY KEY(BUS_ID),
FOREIGN KEY(Operator_ID) references OPERATOR(Operator_ID), FOREIGN KEY(Route_ID) references Route(Route_ID))""")

conn.execute("""CREATE TABLE IF NOT EXISTS OPERATOR(Operator_ID int ,Bus_ID int, Opt_Name text, Address text, Email_ID text,Phone_no int, PRIMARY KEY(OPERATOR_ID),
FOREIGN KEY(Bus_ID) references BUS(Bus_Id))""")

conn.execute("""CREATE TABLE IF NOT EXISTS ROUTE(Route_ID int , Station_ID int , Station_Name text,Bus_ID int, PRIMARY KEY(Route_ID, Station_ID),
FOREIGN KEY(Bus_ID) references BUS(Bus_ID))""")
#########################################################
conn.execute("""CREATE TABLE IF NOT EXISTS RUN(Bus_ID int, Date date, Seat_Availavle int, PRIMARY KEY(BUS_ID, Date),
FOREIGN KEY(BUS_ID) references BUS(Bus_ID))""")

conn.execute("""CREATE TABLE IF NOT EXISTS BOOKING_HISTORY(Booking_ID int AUTO INCREMENT, Passengers_Name text, Gender text, No_of_seats int, Mobile_no int,
Fare int, Bus_ID int, PRIMARY KEY(Booking_ID), FOREIGN KEY(BUS_ID) references BUS(BUS_ID))""")

#conn.execute("Insert or Replace INTO route Values( 1001, 1002, 'Guna', 69)")
#conn.execute("Insert or Replace INTO route Values( 1001, 1003, 'JJN', 69)")
#conn.execute("Insert or Replace INTO OPERATOR Values(4021,69, 'BABURAO', 'JUET', 'BBRJUET@GMAIL.COM',7746034917)")
#conn.execute("Insert or Replace INTO BUS Values(69, 'AC', 42, 1500, 1001, 4021)")
#conn.execute("Insert or Replace INTO run Values(69 , '10/12/2002', 42)")
             
conn.execute("select * from bus")

records = conn. fetchall()
print(records)
conn.execute("select * from operator")

records = conn. fetchall()
print(records)
conn.execute("select * from ROUTE")

records = conn. fetchall()
print(records)
conn.execute("select * from RUN")

records = conn. fetchall()
print(records)

connect.commit()



connect.close()
