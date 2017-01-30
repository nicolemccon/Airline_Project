import sqlite3
import pandas as pd
import csv

def booking_seats(req_seat,seat_a,name):
    
    if req_seat <= seat_a:
        #print("Booking feasible")
        new_list=[]
        count=0
        for i in range(req_seat): #to iterate the number of times the no of seats required to book
                        
            new_list.append(name)    
            print(new_list)
            count=count+1
            print("new_list",new_list)
            #entries = ()
            seat_a = seat_a-len(new_list)
            print("Now the number of seats available are", seat_a)
            
            
    else:
        print("The booking cannot happen")
        not_booked=[]
        passengers_refused=0
        #count1=0
        #for t in range(req_seat):
          #  not_booked.append(name)
            #print("The number of unbooked passengers is", len(not_booked))
            #passengers_refused= passengers_refused + len(not_booked)
           
        
    #print("No of bookings done by", name,"is",count)        
                
                
conn = sqlite3.connect('airline_seating.db')
print("Opened database successfully")
db=conn.cursor()

db.execute("select * from seating")
for obj in db:
    print(obj[0:3])

db.execute("select COUNT(seat) from seating")
 
for obj in db:
    no_of_seats= obj[0]
    print(no_of_seats)
    
db.execute("SELECT COUNT(name) FROM seating WHERE name LIKE '' ;")
for obj in db:
    seat_a= obj[0]
    print("Number of available seats:", seat_a)  
    
db.execute("SELECT COUNT(name) FROM seating WHERE name NOT LIKE '' ;")
for obj in db:
    no_of_seats_taken=obj[0]
    print("The number of seats taken",no_of_seats_taken)
    
    
db.execute("SELECT seat,count(*) from seating group by seat")
i=0
for obj in db:
    no_seats=obj[0]
    print(obj[0])
    i=i+1
print(i)
no_seats_in_row=i;


tb = pd.read_sql_query("SELECT * FROM seating;", conn)  # give the table name and the connection
print(tb.head()) #reading a table using pandas and sqlite


with open('bookings.csv', 'r', newline='') as bookingfile:
    reader=csv.reader(bookingfile)
    for row in reader:
        #print(row)#just to check if the csv file is getting read properly
        name_pass=(row[0])
        req_seat=int((row[1]))
        k=booking_seats(req_seat,seat_a,name_pass)
        print(k)
    























    