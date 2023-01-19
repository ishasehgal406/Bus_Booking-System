from tkinter import *
import sqlite3
from tkinter.messagebox import *
#root=Tk()
from datetime import date
con=sqlite3.Connection("busdatabase211b141")
cur=con.cursor()
class project:
    def s1_isha(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//4,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Name :  Isha Sehgal ",fg="blue",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5)
        Label(root,text="").grid(row=6,column=0,pady=30)

        Frame_4=Frame(root)
        Frame_4.grid(row=7,column=0,columnspan=10)
        title=Label(Frame_4,text="Er : 211B141 ",fg="blue",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5)
        Label(root,text="").grid(row=8,column=0,pady=30)

        Frame_5=Frame(root)
        Frame_5.grid(row=9,column=0,columnspan=10)
        title=Label(Frame_5,text="Mobile : 9810406406",fg="blue",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//3,columnspan=7)
        Label(root,text="").grid(row=10,column=0,pady=30)

        Frame_6=Frame(root)
        Frame_6.grid(row=11,column=0,columnspan=10)
        title=Label(Frame_6,text="Submitted to : Dr. Mahesh Kumar ",fg="red",bg="light blue",font="Arial 14 bold")
        title.grid(row=1,column=0,padx=w//3,columnspan=7)

        Frame_7=Frame(root)
        Frame_7.grid(row=12,column=0,columnspan=10)
        title=Label(Frame_7,text="Project Based Learning",fg="red",font="Arial 10 bold")
        title.grid(row=1,column=0,padx=w//3,columnspan=7)
        
        def funtion1(fun=0):
            root.destroy()
            self.s2_home()
        root.bind('<KeyPress>',funtion1)
        root.mainloop()
    def s2_home(self):
        
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)
        Label(root,text="").grid(row=5,column=0)
        def for_book_seat(fun1=0):
            root.destroy()
            self.s3_seatbooking()
        
        Button(root,text="Seat Booking",bg="forest green",command=for_book_seat).grid(row=6,column=0,columnspan=7)
        def check_your_seat(fun2=0):
            root.destroy()
            self.s4_checkbooking()
        Button(root,text="Check Booked Seat",bg="forest green",command=check_your_seat).grid(row=6,column=2,columnspan=6)
        def adding_details(gopal=0):
            root.destroy()
            self.s5_detailadmin()
        Button(root,text="Add Bus Details",bg="forest green",command=adding_details).grid(row=6,column=4,columnspan=5)
        Label(root,text="").grid(row=7,column=0)

        admin=Label(root,text="For Admin Only",fg="red").grid(row=8,column=4,columnspan=5)
        root.mainloop()
    def s3_seatbooking(self):
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        frame_4=Frame(root)
        frame5=Frame(root)
        check=0
        def clicked(value):
            global check
            check=value
            


        def show_bus_details():
            con=sqlite3.Connection("busdatabase211b141")
            cur=con.cursor()
            r=IntVar()
            frame_4.grid(row=8,column=0,columnspan=10)
            cur.execute('select * from route where station_name=:to',
                        {
                            "to":to_entry.get()
                        }
                        )
            to_records=cur.fetchall()
            #print(to_records)
            cur.execute('select * from route where station_name=:from',
                        {
                            "from":from_entry.get()
                        }
                        )
            from_records=cur.fetchall()
            #print(from_records)
            if(to_records==[]):
                showinfo("sorry"," we have no bus on this route")
                return
            if(from_records==[]):
                showinfo("sorry"," we have no bus on this route")
                return
            i=0
            j=0
            tempid=0
            for record in to_records:
                for rec in from_records:
                    if(to_records[i][0]==from_records[j][0]):
                        if(to_records[i][1]>from_records[j][1]):
                            tempid=to_records[i][0]
                    j=j+1
                i=i+1
                j=0
            if(tempid==0):
                showinfo('no bus found','sorry,no buses are available')
                return
            cur.execute('select * from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0',
                        {
                            'tempid':tempid,
                            'jdate':journey_date_entry.get()
                        }
                        )
            run_info=cur.fetchall()
            if(run_info==[]):
                showinfo("sorry","no bus found")
                return
            for widget in frame_4.winfo_children():
                widget.destroy()
            Label(frame_4,text='select bus',fg="green3",font="Arial 13 bold").grid(row=0,column=0,padx=20)
            Label(frame_4,text="operator",fg="green3",font="Arial 12 bold").grid(row=0,column=2,padx=20)
            Label(frame_4,text="bus type",fg="green3",font="Arial 12 bold").grid(row=0,column=4,padx=20)
            Label(frame_4,text="Available/capacity",fg="green3",font="Arial 12 bold").grid(row=0,column=6,padx=20)
            Label(frame_4,text="fare",fg="green3",font="Arial 12 bold").grid(row=0,column=8,padx=20)
            Button(frame_4,text='Proceed To Book',fg="black", bg='green2',command=book).grid(row=2,column=10,padx=20)
            cur.execute('select count(*) from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0',
                        {
                            'tempid':tempid,
                            'jdate':journey_date_entry.get()
                        }
                        )
            no_of_labels=cur.fetchall()
            enteries=no_of_labels[0][0]
            counter=0
            while(enteries!=0):
                cur.execute('select * from bus where bus_id=:busid',
                            {
                                "busid":run_info[counter][0]
                            }
                            )
                bus_info=cur.fetchall()

                cur.execute("select name from operator where op_id=:oid",
                            {
                                'oid':bus_info[0][5]
                            }
                            )
                op_name=cur.fetchall()
                Radiobutton(frame_4,text='bus'+str(counter+1),font="Helvetica 11",variable=r,value=counter+1,command=lambda : clicked(r.get())).grid(row=counter+1,column=0,padx=20,pady=5)
                Label(frame_4,text=op_name[0][0],fg='blue',font='helvetica 12 italic').grid(row=counter+1,column=2,padx=20,pady=5)
                Label(frame_4,text=bus_info[0][1],fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=4,padx=20,pady=5)
                Label(frame_4,text=str(run_info[counter][2])+'/'+str(bus_info[0][2]),fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=6,padx=20,pady=5)
                Label(frame_4,text=bus_info[0][3],fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=8,padx=20,pady=5)
                counter=counter+1
                enteries=enteries-1
        def book():
            global check
            if(check==0):
                showerror("field missing","please select a bus")
                frame5.grid_forget()
                return
            def confirm():
                con=sqlite3.Connection("busdatabase211b141")
                cur=con.cursor()
            

                if(cname.get()==""):
                    showerror("field missing ","please enter name")
                elif(gender.get()=="select"):
                    showerror("field missing","please enter gender")
                elif(mno.get()==""):
                    showerror("field missing","please enter mobile number")
                elif(cage.get()==""):
                    showerror("field missing","please enter age")
                elif(cseat.get()==""):
                    showerror("field missing","please enter No of seats")
                else:
                    try:
                        global check
                        int(mno.get())

                        int(cage.get())

                        int(cseat.get())

                        if(len(mno.get())!=10):
                            showerror("Wrong input","please enter a valid mobile number")
                            mno.delete(0,END)
                            return
                        if(int(cage.get())>130):
                            showerror("wrong error","please enter a valid age")
                            cage.delete(0,END)
                            return
                        cur.execute("select * from route where station_name=:to",
                                    {
                                        'to':to_entry.get()
                                    }
                                    )
                        to_records=cur.fetchall()

                        cur.execute("select * from route where station_name=:from",
                                    {
                                        'from':from_entry.get()
                                    }
                                    )
                        from_records=cur.fetchall()
                        i=0
                        j=0
                        tempid=0
                        for record in to_records:
                            for rec in from_records:
                                if(to_records[i][0]==from_records[j][0]):
                                    if(to_records[i][1]>from_records[j][1]):
                                        tempid=to_records[i][0]
                                j=j+1
                            i=i+1
                            j=0
                        cur.execute("select * from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0",
                                    {
                                        'tempid':tempid,
                                        'jdate':journey_date_entry.get()
                                    }
                                    )
                        run_info=cur.fetchall()

                        if(int(cseat.get())>run_info[check-1][2] or int(cseat.get())<1):
                            showerror('invalid input',"please enter a valid number of seats")
                            cseat.delete(0,END)
                            return
                        cur.execute('select * from bus where bus_id=:busid',
                                    {
                                        "busid":run_info[check-1][0]
                                    }
                                    )
                        bus_info=cur.fetchall()
                        cur.execute("select booking_id,phone from booking_history")
                        ref=cur.fetchall()
                        h=0
                        cur.execute("select count(*) from booking_history")
                        lastid=cur.fetchall()
                        reference=lastid[0][0]+1
                        for ph in ref:
                            if(ref[h][1]==int(mno.get())):
                                showinfo("record exist","booking from this number already exit..")
                                return
                            h=h+1
                        choice=askyesno("confimation","your fare is "+str(int(cseat.get())*bus_info[0][3])+'\nConfirm booking?')
                        cur.execute("INSERT INTO Booking_history(booking_id,p_name,phone,travel_on,booked_on,gender,age,source,destination,fare,seats) VALUES(:ref, :pname, :phone,:travelon, :bookedon, :gender,:age,:source,:destination,:fare,:seat)",

                                        {

                                            'pname': cname.get(),

                                            'ref': reference,

                                            'phone': mno.get(),

                                            'travelon': journey_date_entry.get(),

                                            'bookedon': date.today(),

                                            'gender': gender.get(),

                                            'age' : cage.get(),

                                            'source': from_entry.get(),

                                            'destination': to_entry.get(),

                                            'fare': (int(cseat.get())*bus_info[0][3]),

                                            'seat': cseat.get()

                                        }

                                        )
                        new=run_info[check-1][2]-int(cseat.get())
                        cur.execute("update run set seat_available=:seat where b_id=:busid",
                                    {
                                        'seat': new,
                                        'busid': bus_info[0][0]
                                        
                                    }
                                    )
                        if(choice==1):

                            showinfo('Success','Seat booked!')

                            cname.delete(0,END)

                            cage.delete(0,END)

                            cseat.delete(0,END)

                            mno.delete(0,END)

                            gender.set("Select")

                            frame5.grid_forget()

                            frame_4.grid_forget()

                            to_entry.delete(0,END)

                            from_entry.delete(0,END)

                            journey_date_entry.delete(0,END)

                            con.commit()
                            def funtion_ticket(fun4=0):
                                root.destroy()
                                self.ticketdisplay()
                            funtion_ticket()
                            #root.destroy()

                            #import Bus_Ticket

                    except:

                        showerror('Invalid Entry','Booking already exist or you may have entered wrong values\nPlease enter valid values...')

                        cname.delete(0,END)

                        cage.delete(0,END)

                        cseat.delete(0,END)

                        mno.delete(0,END)

                        gender.set("Select")

                    

                    

                con.commit()

                con.close()

                


            Label(frame5,text='Fill Passenger Details',fg='Red',bg='LightBlue1',font="Arial 21 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)

            frame5.grid(row=9,column=0,columnspan=10)

            Label(frame5,text="Name",font='Arial 11 bold').grid(row=1,column=0)

            cname=Entry(frame5)

            cname.grid(row=1,column=1)



            Label(frame5,text="Gender",font='Arial 11 bold').grid(row=1,column=2)

            gender=StringVar()

            gender.set("Select")

            option=["Male","Female","Other"]

            menu=OptionMenu(frame5,gender,*option)

            menu.grid(row=1,column=3)



            Label(frame5,text="Mobile No",font='Arial 11 bold').grid(row=1,column=4)

            mno=Entry(frame5)

            mno.grid(row=1,column=5)



            Label(frame5,text="Age",font='Arial 11 bold').grid(row=1,column=6)

            cage=Entry(frame5,width=10)

            cage.grid(row=1,column=7)



            Label(frame5,text="No Of Seats",font='Arial 11 bold').grid(row=1,column=8)

            cseat=Entry(frame5,width=10)

            cseat.grid(row=1,column=9)



            Button(frame5,text='Book Seat',fg="black",bg='white',font='Arial 15',command=confirm).grid(row=1,column=10,padx=10)




        def fun1_check_error():
            if len(to_entry.get())==0:
                showerror('Value Missing','Please Enter Destination')
            elif len(from_entry.get())==0:
                showerror('Value Missing','Please Enter From')
            elif len(journey_date_entry.get())==0:
                showerror('Value Missing','Please Enter Date')
            else:
                show_bus_details()

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 17 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Enter Journey Details",fg="green",font="Arial 13 bold",bg="light green")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)

        to=Label(root,text="To")
        to.grid(row=7,column=0,sticky=E)
        to_entry=Entry(root)
        to_entry.grid(row=7,column=1,sticky=W,padx=20)

        from_=Label(root,text="From")
        from_.grid(row=7,column=1,sticky=E)
        from_entry=Entry(root)
        from_entry.grid(row=7,column=2,sticky=W,padx=20)

        journey_date=Label(root,text="Journey Date")
        journey_date.grid(row=7,column=3,sticky=E)
        journey_date_entry=Entry(root)
        journey_date_entry.grid(row=7,column=4,sticky=W,padx=20)

        Button(root,text="Show Bus",bg="light green",command=fun1_check_error).grid(row=7,column=5)
        def home(fun5=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=7,column=6)
        root.mainloop()

    def ticketdisplay(self):
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file='Bus_for_project.png')

        Frame1=Frame(root)

        Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.5)

        Label(Frame1,image=img).pack()

        Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()

            
        Label(Frame1,text='Bus Ticket',fg='black',font="Arial 15 bold",pady=5).pack()

        Frame2=Frame(root,relief='groove',bd=5)

        Frame2.grid(row=1,column=0,columnspan=10,padx=w/2.5,pady=10)

        #con.commit()

        cur.execute("SELECT count(*) FROM booking_history")

        lastid = cur.fetchall()

        cur.execute("SELECT * FROM booking_history where booking_id=:lastid",
                        {
                            'lastid': lastid[0][0]
                        }
                        )
        info = cur.fetchall()
        ac=(info[0][9])/info[0][10]
        for widget in Frame2.winfo_children():
            widget.destroy()
        Label(Frame2,text='Passenger Name : '+str(info[0][1]),font='Arial 13 bold').grid(row=0,column=0,sticky='w')

        Label(Frame2,text='No of seats : '+str(info[0][10]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

        Label(Frame2,text='age : '+str(info[0][6]),font='Arial 13 bold').grid(row=2,column=0,sticky='w')

        Label(Frame2,text='booking ref : '+str(info[0][0]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

        Label(Frame2,text='travel On : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

        Label(Frame2,text='gender : '+str(info[0][5]),font='Arial 13 bold').grid(row=0,column=1,sticky='w')

        Label(Frame2,text='phone number : '+str(info[0][2]),font='Arial 13 bold').grid(row=1,column=1,sticky='w')

        Label(Frame2,text='fare : '+str(ac),font='Arial 13 bold').grid(row=2,column=1,sticky='w')

        Label(Frame2,text='booked on '+str(info[0][4]),font='Arial 13 bold').grid(row=3,column=1,sticky='w')

        Label(Frame2,text='boarding point '+str(info[0][7]),font='Arial 13 bold').grid(row=4,column=1,sticky='w')

        #Label(Frame2,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

        Label(Frame2,text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=5,column=0,columnspan=10)
        def exitt():
            root.destroy()
        """def home():
            root.destroy()
            import Main_Menu"""
        Button(root,text='Exit',font='Times_new_roman 10',command=exitt).grid(row=7,column=1,columnspan=10)
        def home(fun=0):
            con.close()
            root.destroy()
            self.s2_home()
        photu=PhotoImage(file="home.png")
        Button(root,image=photu,font='Times_new_roman 10',command=home).grid(row=7,column=0,columnspan=10)
        root.mainloop()
    def s4_checkbooking(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        import sqlite3
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        def check_error():
            if len(Enter_your_mobile_no_entry.get())==0:
                showerror('Value Missing','Please Enter mobile number')
            else :
                
                Frame2=Frame(root,relief="groove",bd=5)
                Frame2.grid(row=11,column=0,columnspan=10)
                Label(root,text="").grid(row=10,column=0)
                cur.execute("select * from booking_history where phone={}".format(int(Enter_your_mobile_no_entry.get())))
                info=cur.fetchall()
                ac=(info[0][9])/info[0][10]
                Label(Frame2,text='Passenger Name : '+str(info[0][1]),font='Arial 13 bold').grid(row=0,column=0,sticky='w')

                Label(Frame2,text='No of seats : '+str(info[0][10]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

                Label(Frame2,text='age : '+str(info[0][6]),font='Arial 13 bold').grid(row=2,column=0,sticky='w')

                Label(Frame2,text='booking ref : '+str(info[0][0]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

                Label(Frame2,text='travel On : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

                Label(Frame2,text='gender : '+str(info[0][5]),font='Arial 13 bold').grid(row=0,column=1,sticky='w')

                Label(Frame2,text='phone number : '+str(info[0][2]),font='Arial 13 bold').grid(row=1,column=1,sticky='w')

                Label(Frame2,text='fare : '+str(ac),font='Arial 13 bold').grid(row=2,column=1,sticky='w')

                Label(Frame2,text='booked on '+str(info[0][4]),font='Arial 13 bold').grid(row=3,column=1,sticky='w')

                Label(Frame2,text='boarding point '+str(info[0][7]),font='Arial 13 bold').grid(row=4,column=1,sticky='w')

                Label(Frame2,text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=5,column=0,columnspan=10)

                

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Check Your Booking",fg="green",font="Arial 13 bold",bg="light green")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)

        Enter_your_mobile_no=Label(root,text="Enter Your Mobile No")
        Enter_your_mobile_no.grid(row=7,column=0,sticky=E,columnspan=5)
        Enter_your_mobile_no_entry=Entry(root)
        Enter_your_mobile_no_entry.grid(row=7,column=5,sticky=W,padx=20,columnspan=3)
        

        Button(root,text="Check Booking",command=check_error).grid(row=7,column=6)
        def home(fun7=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=7,column=7)
        root.mainloop()

    def s5_detailadmin(self):
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Add New Details to DataBase ",fg="green",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        def add_operator_deatils():
            root.destroy()
            self.s6_operator()
        Button(root,text="New Operator",bg="light green",command=add_operator_deatils).grid(row=7,column=0,columnspan=7)
        def add_new_bus():
            root.destroy()
            self.s7_addbus()
        Button(root,text="New Bus",bg="orange red",command=add_new_bus).grid(row=7,column=1,columnspan=7)
        def add_new_route():
            root.destroy()
            self.s8_addbusroute()
        Button(root,text="New Route",bg="royal blue",command=add_new_route).grid(row=7,column=2,columnspan=7)
        def add_new_run():
            root.destroy()
            self.s9_addrun()
        Button(root,text="New Run",bg="rosy brown",command=add_new_run).grid(row=7,column=3,columnspan=7)
        root.mainloop()

    def s6_operator(self):
        import sqlite3
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Add Bus Operator Details ",fg="green",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        operator_id=Label(root,text="Operator id")
        operator_id.grid(row=8,column=0,sticky=E)
        operator_id_entry=Entry(root)
        operator_id_entry.grid(row=8,column=1,sticky=W)

        name=Label(root,text="Name")
        name.grid(row=8,column=1,sticky=E)
        name_entry=Entry(root)
        name_entry.grid(row=8,column=2,sticky=W)

        address=Label(root,text="Address")
        address.grid(row=8,column=2,sticky=E)
        address_entry=Entry(root)
        address_entry.grid(row=8,column=3,sticky=W)

        phone=Label(root,text="Phone")
        phone.grid(row=8,column=3,sticky=E)
        phone_entry=Entry(root)
        phone_entry.grid(row=8,column=4,sticky=W)

        email=Label(root,text="Email")
        email.grid(row=8,column=4,sticky=E)
        email_entry=Entry(root)
        email_entry.grid(row=8,column=5,sticky=W)


        def check_error():
            def insert():
                cur.execute('insert into operator(op_id,name,address,phone,email) values(?,?,?,?,?)',(operator_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get()))
                '''cur.execute('select * from operator')
                data=cur.fetchall()
                a=len(data)'''
                a=str(operator_id_entry.get())+' '+str(name_entry.get())+' '+str(address_entry.get())+' '+str(phone_entry.get())+' '+str(email_entry.get())
                Label(root,text=a).grid(row=9,column=3)
                showinfo('Operator Entry Added','Operator Record Added successfully')
                con.commit()
            if len(operator_id_entry.get())==0:
                showerror('Value Missing','Please Enter operator id')
            elif len(name_entry.get())==0:
                showerror('Value Missing','Please Enter name of the operator')
            elif len(address_entry.get())==0:
                showerror('Value Missing','Please Enter address')
            elif len(phone_entry.get())==0:
                showerror('Value Missing','Please Enter phone number')
            elif len(email_entry.get())==0:
                showerror('Value Missing','Please Enter email id')
            else :
                insert()
        def check_error_edit():
            def edit():
                cur.execute('select op_id from operator where op_id={}'.format(operator_id_entry.get()))
                opid=cur.fetchall()
                if len(opid)==0:
                    showerror('Operator Invalid','Operator entered does not exist in database !')
                else:   
                    cur.execute('''delete from operator where op_id={}'''.format(operator_id_entry.get()))
                    cur.execute('insert into operator(op_id,name,address,phone,email) values(?,?,?,?,?)',(operator_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get()))
                    a=str(operator_id_entry.get())+' '+str(name_entry.get())+' '+str(address_entry.get())+' '+str(phone_entry.get())+' '+str(email_entry.get())
                    Label(root,text=a).grid(row=9,column=3)
                    showinfo('Operator Entry Edited','Operator Record Edited successfully')
                    con.commit()
            if len(operator_id_entry.get())==0:
                showerror('Value Missing','Please Enter operator id')
            elif len(name_entry.get())==0:
                showerror('Value Missing','Please Enter name of the operator')
            elif len(address_entry.get())==0:
                showerror('Value Missing','Please Enter address')
            elif len(phone_entry.get())==0:
                showerror('Value Missing','Please Enter phone number')
            elif len(email_entry.get())==0:
                showerror('Value Missing','Please Enter email id')
            else :
                edit()


        Button(root,text="Add",bg="light green",command=check_error).grid(row=8,column=6)

        Button(root,text="Edit",bg="light green",command=check_error_edit).grid(row=8,column=7)

        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        def home(fun8=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=11,column=4)
        #con.close()
        root.mainloop()

    def s7_addbus(self):
        import sqlite3
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        def check_error():
            def insert():
                cur.execute('insert into bus(bus_id,bus_type,capacity,fare,r_id,operator_id) values(?,?,?,?,?,?)',(bus_id_entry.get(),bus_type.get(),capacity_entry.get(),fare_entry.get(),route_id_entry.get(),operator_id_entry.get()))    
                a=str(bus_id_entry.get())+' '+str(bus_type.get())+' '+str(capacity_entry.get())+'   '+str(fare_entry.get())+'   '+str(route_id_entry.get())+'   '+str(operator_id_entry.get())
                Label(root,text=a).grid(row=9,column=3)
                con.commit()
                showinfo('Bus Entry','Bus Record added')
            if len(bus_id_entry.get())==0:
                showerror('Value Missing','Please Enter Bus ID')
            elif len(capacity_entry.get())==0:
                showerror('Value Missing','Please Enter capacity of the bus')
            elif len(fare_entry.get())==0:
                showerror('Value Missing','Please Enter fare of the bus')
            elif len(route_id_entry.get())==0:
                showerror('Value Missing','Please Enter route id of the bus')
            elif len(operator_id_entry.get())==0:
                showerror('Value Missing','Please Enter operator id of the bus')
            else :
                insert()
        def check_error_edit():
                def edit():
                    cur.execute('select op_id from operator where op_id={}'.format(operator_id_entry.get()))
                    opid=cur.fetchall()
                    if len(opid)==0:
                        showerror('Operator Invalid','Operator entered does not exist in database !')
                    else:    
                        cur.execute('select bus_id from bus where bus_id={}'.format(bus_id_entry.get()))
                        busid=cur.fetchall()
                        if len(busid)==0:
                            showerror('Bus Invalid','Bus entered does not exist in database ! ')
                        else:    
                            #import sqlite
                            cur.execute('''delete from bus where bus_id={}'''.format(bus_id_entry.get()))
                            cur.execute('insert into bus(bus_id,bus_type,capacity,fare,r_id,operator_id) values(?,?,?,?,?,?)',(bus_id_entry.get(),bus_type.get(),capacity_entry.get(),fare_entry.get(),route_id_entry.get(),operator_id_entry.get()))
                            a=str(bus_id_entry.get())+' '+str(bus_type.get())+' '+str(capacity_entry.get())+'   '+str(fare_entry.get())+'   '+str(route_id_entry.get())+'   '+str(operator_id_entry.get())
                            Label(root,text=a).grid(row=9,column=3)
                            con.commit()
                if len(bus_id_entry.get())==0:
                    showerror('Value Missing','Please Enter Bus ID')
                elif len(capacity_entry.get())==0:
                    showerror('Value Missing','Please Enter capacity of the bus')
                elif len(fare_entry.get())==0:
                    showerror('Value Missing','Please Enter fare of the bus')
                elif len(route_id_entry.get())==0:
                    showerror('Value Missing','Please Enter route id of the bus')
                elif len(operator_id_entry.get())==0:
                    showerror('Value Missing','Please Enter operator id of the bus')
                else :
                    edit()
                

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Add Bus Details ",fg="green",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        bus_id=Label(root,text="Bus ID")
        bus_id.grid(row=8,column=1,sticky=E)
        bus_id_entry=Entry(root)
        bus_id_entry.grid(row=8,column=2,sticky=W)

        bus_type=Label(root,text="Bus Type")
        bus_type.grid(row=8,column=2,sticky=E)
        bus_type=StringVar()
        bus_type.set("Bus Type")
        option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non-AC sleeper 2x1"]
        d_menu=OptionMenu(root,bus_type,*option)
        d_menu.grid(row=8,column=3,sticky=W)

        capacity=Label(root,text="Capacity")
        capacity.grid(row=8,column=3,sticky=E)
        capacity_entry=Entry(root)
        capacity_entry.grid(row=8,column=4,sticky=W)

        fare=Label(root,text="Fare Rs")
        fare.grid(row=8,column=4,sticky=E)
        fare_entry=Entry(root)
        fare_entry.grid(row=8,column=5,sticky=W)

        route_id=Label(root,text="Route id")
        route_id.grid(row=8,column=5,sticky=E)
        route_id_entry=Entry(root)
        route_id_entry.grid(row=8,column=6,sticky=W)

        operator_id=Label(root,text="operator id")
        operator_id.grid(row=8,column=6,sticky=E)
        operator_id_entry=Entry(root)
        operator_id_entry.grid(row=8,column=7,sticky=W)

        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)

        Button(root,text="Add Bus",bg="light green",command=check_error).grid(row=11,column=4,sticky=E,padx=20)

        Button(root,text="Edit Bus",bg="light green",command=check_error_edit).grid(row=11,column=5,sticky=W)
        def home(fun9=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=11,column=6,sticky=W)
        root.mainloop()
    def s8_addbusroute(self):
        import sqlite3
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        def check_error():
            def insert():
                cur.execute('insert into route(route_id,station_name,station_id) values(?,?,?)',(route_id_entry.get(),station_name_entry.get(),station_id_entry.get()))
                a=str(route_id_entry.get())+'   '+str(station_name_entry.get())+'   '+str(station_id_entry.get())
                Label(root,text=a).grid(row=9,column=3)
                showinfo('Route Entry','Bus Route Record Added successfully')
                con.commit()
                #con.close()
            if len(route_id_entry.get())==0:
                showerror('Value Missing','Please Enter route id')
            elif len(station_name_entry.get())==0:
                showerror('Value Missing','Please Enter name of the station')
            elif len(station_id_entry.get())==0:
                showerror('Value Missing','Please Enter station id')
            else :
                insert()
            
        def check_error_delete():
            cur.execute('select route_id from route where route_id={}'.format(route_id_entry.get()))
            routeid=cur.fetchall()
            if len(routeid)==0:
                showerror('Route Invalid','Route entered does not exist in database ! ')
            else:
                cur.execute('''delete from route where route_id={} and station_id={};'''.format(route_id_entry.get(),station_id_entry.get()))
                con.commit()
                showinfo('Route Entry','Bus Route Record Deleted successfully')
        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Add Bus Route Details ",fg="green",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        route_id=Label(root,text="Route Id")
        route_id.grid(row=8,column=1,sticky=E)
        route_id_entry=Entry(root)
        route_id_entry.grid(row=8,column=2,sticky=W)

        station_name=Label(root,text="station Name")
        station_name.grid(row=8,column=2,sticky=E)
        station_name_entry=Entry(root)
        station_name_entry.grid(row=8,column=3,sticky=W)

        station_id=Label(root,text="station Id")
        station_id.grid(row=8,column=3,sticky=E)
        station_id_entry=Entry(root)
        station_id_entry.grid(row=8,column=4,sticky=W)

        Button(root,text="Add Route",bg="light green",command=check_error).grid(row=8,column=5)
        Button(root,text="Delete Route",bg="light green",command=check_error_delete).grid(row=8,column=6)

        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        def home(fun9=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=11,column=3,padx=20)
        root.mainloop()
        
    def s9_addrun(self):
        import sqlite3
        con=sqlite3.Connection("busdatabase211b141")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        def check_error():
            def insert():
                cur.execute('insert into run(b_id,running_date,seat_available) values(?,?,?)',(bus_id_entry.get(),running_date_entry.get(),seat_available_entry.get()))    
                a=str(bus_id_entry.get())+' '+str(running_date_entry.get())+' '+str(seat_available_entry.get())
                Label(root,text=a).grid(row=9,column=3)
                con.commit()
                showinfo('Bus Running Added','Bus Running Record Added successfully')
            if len(bus_id_entry.get())==0:
                showerror('Value Missing','Please Enter bus id')
            elif len(running_date_entry.get())==0:
                showerror('Value Missing','Please Enter running date')
            elif len(seat_available_entry.get())==0:
                showerror('Value Missing','Please Enter number of seats available')
            else :
                insert()
            
        def check_error_edit():
            def delete():
                cur.execute('select bus_id from bus where bus_id={}'.format(bus_id_entry.get()))
                busid=cur.fetchall()
                if len(busid)==0:
                    showerror('Bus Invalid','Bus ID entered does not exist in database !')
                else:
                    cur.execute('''delete from run where b_id=(?) and running_date=(?)''',(bus_id_entry.get(),running_date_entry.get()))    
                    con.commit()
                    showinfo('Bus Running Deleted','Bus Running Record Deleted successfully')
            if len(bus_id_entry.get())==0:
                showerror('Value Missing','Please Enter bus id')
            elif len(running_date_entry.get())==0:
                showerror('Value Missing','Please Enter running date')
            elif len(seat_available_entry.get())==0:
                showerror('Value Missing','Please Enter number of seats available')
            else :
                delete()
                
        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Add Bus Running Details ",fg="green",font="Arial 13 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        bus_id=Label(root,text="Bus ID")
        bus_id.grid(row=8,column=1,sticky=E)
        bus_id_entry=Entry(root)
        bus_id_entry.grid(row=8,column=2,sticky=W)

        running_date=Label(root,text="Running Date")
        running_date.grid(row=8,column=2,sticky=E)
        running_date_entry=Entry(root)
        running_date_entry.grid(row=8,column=3,sticky=W)

        seat_available=Label(root,text="Seat Available")
        seat_available.grid(row=8,column=3,sticky=E)
        seat_available_entry=Entry(root)
        seat_available_entry.grid(row=8,column=4,sticky=W)

        Button(root,text="Add run",bg="light green",command=check_error).grid(row=8,column=5,sticky=W)

        Button(root,text="Edit Bus",bg="light green",command=check_error_edit).grid(row=8,column=6,sticky=W)

        Label(root,text="").grid(row=9,column=0)
        Label(root,text="").grid(row=10,column=0)
        def home(fun10=0):
            con.close()
            root.destroy()
            self.s2_home()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=11,column=4)
        root.mainloop()


final=project()
final.s1_isha()


