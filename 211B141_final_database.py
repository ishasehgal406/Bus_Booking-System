import sqlite3
con=sqlite3.Connection("busdatabase211b141")
cur=con.cursor()

cur.execute('''create table operator(op_id numeric,name varchar(25),address varchar(25),phone numeric,
                                     email varchar(100),primary key(op_id))''')
cur.execute('create table route(route_id numeric,station_name varchar(25),station_id numeric)')

cur.execute('''create table bus(bus_id numeric,bus_type varchar(15),capacity numeric,fare numeric,
               r_id numeric,operator_id numeric,foreign key(r_id) references route(route_id) on delete cascade,
               foreign key(operator_id) references operator(op_id) on delete cascade,primary key(bus_id))''')

cur.execute('create table run(b_id numeric,running_date date,seat_available numeric)')

cur.execute('''create table booking_history(booking_id numeric,p_name numeric,phone numeric,travel_on date,
             booked_on date,gender varchar(10),age numeric,source varchar(50),destination varchar(50),
            fare numeric,seats numeric,primary key(booking_id))''')



con.commit()
