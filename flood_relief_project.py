from tkinter import *
import DB_connect
def Affected_Area():
    root1 = Toplevel(root)
    root1.geometry('1300x700+0+0')
    col1 = '#ff3434'  # darkblue
    col2 = '#ff9393'  # lightblue
    c1 = Canvas(root1, width=1300, height=700, bg=col2)
    c1.pack()
    #Add
    c1.create_rectangle(450, 10, 850, 80, fill='black', outline='yellow', width=3)
    lbl_Area = Label(root1, text='Affected Area', font=('ariel', 30), bg='black', fg='white')
    lbl_Area.place(x=500, y=20)
    c1.create_rectangle(100, 150, 600, 600, fill='white', width=0,)

    c1.create_rectangle(130, 280, 550, 450, fill=col1, width=0)
    def addrec():
        insertsql = "INSERT INTO affected_areas VALUES (%s,%s,%s)"
        if pincode1.get()==0:
            L=Label(root1,text="pincode can't be 0")
            L.place(x=150,y=290)
        record = (pincode1.get(), location.get(), population.get())
        DB_connect.insert_into_table(insertsql, record)
        button_add1.config(text="Added")


    xpos = 150
    ypos = 300
    pincode1 = IntVar()
    lbl_pincode = Label(root1, text="Pincode:", font=('ariel', 15), bg=col1, fg='white')
    lbl_pincode.place(x=xpos, y=ypos)
    E_pincode = Entry(root1, font=('ariel', 15),textvariable=pincode1)
    E_pincode.place(x=xpos + 150, y=ypos)

    location = StringVar()
    lbl_Location = Label(root1, text="Location:", font=('ariel', 15), bg=col1, fg='white')
    lbl_Location.place(x=xpos, y=ypos + 50)
    E_Location = Entry(root1, font=('ariel', 15),textvariable=location)
    E_Location.place(x=xpos + 150, y=ypos + 50)

    population = IntVar()
    lbl_population = Label(root1, text="Population:", font=('ariel', 15), bg=col1, fg='white')
    lbl_population.place(x=xpos, y=ypos + 100)
    E_population = Entry(root1, font=('ariel', 15),textvariable=population)
    E_population.place(x=xpos + 150, y=ypos + 100)

    button_add1 = Button(root1, text="ADD", font=('ariel', 15), bg=col1, fg='white', activebackground='blue',command=addrec)
    button_add1.place(x=300, y=550)





    # display
    c1.create_rectangle(700, 150, 1200, 600, fill='white', width=0, )
    def displayrec():
        disp_sql=f"SELECT * FROM affected_areas where pincode={pincode.get()}"
        row=DB_connect.search_in_table(disp_sql)
        if row==False:
            lbl = Label(root1, text='no data found!', font=('Arial', 14))
            lbl.place(x=900, y=330)
        else:
            lbl1 = Label(root1,text=f"pincode: {row[0]}", font=('Arial', 14))
            lbl1.place(x=900, y=330)
            lbl2 = Label(root1,text=f"location: {row[1]}", font=('Arial', 14))
            lbl2.place(x=900, y=380)
            lbl3 = Label(root1,text=f"population: {row[2]}", font=('Arial', 14))
            lbl3.place(x=900, y=430)

    c1.create_rectangle(730, 230, 1150, 300, fill=col1, width=0)
    label_disp = Label(root1, text='View details of an affected area', font=('ariel', 15), bg='white')
    label_disp.place(x=750, y=200)
    lbl_pincode = Label(root1, text="Pincode:", font=('ariel', 15), bg=col1, fg='white')
    lbl_pincode.place(x=750, y=250)
    pincode=IntVar()
    E1_pincode = Entry(root1, font=('ariel', 15),textvariable=pincode)
    E1_pincode.place(x=900, y=250)
    button2 = Button(root1, text="Submit", font=('ariel', 15), bg=col1, fg='white',activebackground='blue',command=displayrec)
    button2.place(x=900, y=550)
    root1.mainloop()


def Manage_inventory():
    root2 = Toplevel(root)
    root2.geometry('1300x700+0+0')
    col1 = '#364f6b' #darkblue
    col2 = '#278ea5' #lightblue 
    c2 = Canvas(root2, width=1300, height=700, bg=col2)
    c2.pack()
    # Add and update
    c2.create_rectangle(450, 10, 850, 80, fill='black', outline='yellow', width=3)
    lbl_Inventory = Label(root2, text='Manage Inventory', font=('ariel', 30), bg='black', fg='white')
    lbl_Inventory.place(x=500, y=20)
    c2.create_rectangle(100, 150, 600, 600, fill='white', width=0, )
    c2.create_rectangle(130, 280, 550, 450, fill=col1, width=0)
    def addrec2():
        insertsql = "INSERT INTO inventory VALUES (%s,%s,%s)"
        record = (Itemid.get(), Item_Name.get(), quantity.get())
        DB_connect.insert_into_table(insertsql, record)
        button_add2.config(text="Added")




   

    xpos = 150
    ypos = 300
    Itemid=IntVar()
    lbl_Itemid = Label(root2, text="Item ID:", font=('ariel', 15), bg=col1, fg='white')
    lbl_Itemid.place(x=xpos, y=ypos)
    E_Itemid = Entry(root2, font=('ariel', 15),textvariable=Itemid)
    E_Itemid.place(x=xpos + 150, y=ypos)

    Item_Name=StringVar()
    lbl_Item_Name = Label(root2, text="Item Name:", font=('ariel', 15), bg=col1, fg='white')
    lbl_Item_Name.place(x=xpos, y=ypos + 50)
    E_Item_Name = Entry(root2, font=('ariel', 15),textvariable=Item_Name)
    E_Item_Name.place(x=xpos + 150, y=ypos + 50)

    quantity=IntVar()
    lbl_quantity = Label(root2, text="Quantity:", font=('ariel', 15), bg=col1, fg='white')
    lbl_quantity.place(x=xpos, y=ypos + 100)
    E_quantity = Entry(root2, font=('ariel', 15),textvariable=quantity)
    E_quantity.place(x=xpos + 150, y=ypos + 100)

    button_add2 = Button(root2, text="ADD", font=('ariel', 15), bg=col1, fg='white', activebackground='blue',
                         command=addrec2)
    button_add2.place(x=300, y=550)


    # display
    c2.create_rectangle(700, 150, 1200, 600, fill='white', width=0, )

    def displayrec2():
        disp_sql = f"SELECT * FROM inventory where Item_ID={Itemid1.get()}"
        row = DB_connect.search_in_table(disp_sql)
        if row == False:
            lbl = Label(root2, text='no data found!', font=('Arial', 14))
            lbl.place(x=900, y=330)
        else:
            lbl1 = Label(root2, text=f"Item ID: {row[0]}", font=('Arial', 14))
            lbl1.place(x=900, y=330)
            lbl2 = Label(root2, text=f"Item Name: {row[1]}", font=('Arial', 14))
            lbl2.place(x=900, y=380)
            lbl3 = Label(root2, text=f"Quantity: {row[2]}", font=('Arial', 14))
            lbl3.place(x=900, y=430)

    c2.create_rectangle(730, 230, 1150, 300, fill=col1, width=0)
    label_disp = Label(root2, text='View Items in the Inventory', font=('ariel', 15), bg='white')
    label_disp.place(x=750, y=200)
    lbl_Rid = Label(root2, text="Item ID:", font=('ariel', 15), bg=col1, fg='white')
    lbl_Rid.place(x=750, y=250)
    Itemid1=IntVar()
    E_Rid = Entry(root2, font=('ariel', 15),textvariable=Itemid1)
    E_Rid.place(x=900, y=250)
    button2 = Button(root2, text="Submit", font=('ariel', 15), bg=col1, fg='white',command=displayrec2)
    button2.place(x=900, y=550)
    root2.mainloop()

def rescued_people():
    root3=Toplevel(root)
    root3.geometry('1300x700+0+0')
    col1 = '#085f63'#'#3d5af1'  # darkblue
    col2 = '#17b978'#'#00d1ff'
    col3 = '#00fff0'
    col4 = '#e2f3f5'  # white
    c3=Canvas(root3,width=1300,height=700,bg=col2)
    c3.pack()
    #Add and update
    c3.create_rectangle(450,10,850,80,fill='black',outline='yellow',width=3)
    lbl_Rescued=Label(root3,text='Rescued People',font=('ariel',30),bg='black',fg='white')
    lbl_Rescued.place(x=500,y=20)
    c3.create_rectangle(100,150,600,600,fill='white',width=0,)
    def addrec3():
        insertsql = "INSERT INTO rescued_people VALUES (%s,%s,%s,%s)"
        record = (Rid.get(), Name.get(), Age.get(), address.get())
        DB_connect.insert_into_table(insertsql, record)
        button_add3.config(text="Added")



    
    c3.create_rectangle(130,280,550,520,fill=col1,width=0)
    xpos=150
    ypos=300
    Rid=IntVar()
    lbl_Id = Label(root3, text="R Id:", font=('ariel', 15), bg=col1, fg='white')
    lbl_Id.place(x=xpos, y=ypos)
    E_Id = Entry(root3, font=('ariel', 15),textvariable=Rid)
    E_Id.place(x=xpos + 150, y=ypos)

    Name=StringVar()
    lbl_Name=Label(root3,text="Name:",font=('ariel',15),bg=col1,fg='white')
    lbl_Name.place(x=xpos,y=ypos+50)
    E_Name=Entry(root3,font=('ariel', 15),textvariable=Name)
    E_Name.place(x=xpos+150,y=ypos+50)

    Age=IntVar()
    lbl_Age = Label(root3, text="Age:", font=('ariel', 15),bg=col1,fg='white')
    lbl_Age.place(x=xpos, y=ypos+100)
    E_Age=Entry(root3,font=('ariel', 15),textvariable=Age)
    E_Age.place(x=xpos+150,y=ypos+100)

    address=StringVar()
    lbl_Address = Label(root3, text="Address:", font=('ariel', 15),bg=col1,fg='white')
    lbl_Address.place(x=xpos, y=ypos+150)
    E_Address=Entry(root3,font=('ariel', 15),textvariable=address)
    E_Address.place(x=xpos+150,y=ypos+150)

    button_add3 = Button(root3, text="ADD", font=('ariel', 15), bg=col1, fg='white', activebackground='blue',
                         command=addrec3)
    button_add3.place(x=300, y=550)



    #display
    c3.create_rectangle(700, 150, 1200, 600, fill='white', width=0, )
    def displayrec3():
        disp_sql = f"SELECT * FROM rescued_people where R_id={Rid1.get()}"
        row = DB_connect.search_in_table(disp_sql)
        if row == False:
            lbl = Label(root3, text='no data found!', font=('Arial', 14))
            lbl.place(x=900, y=330)
        else:
            lbl1 = Label(root3, text=f"R ID: {row[0]}", font=('Arial', 14))
            lbl1.place(x=900, y=330)
            lbl2 = Label(root3, text=f"Name: {row[1]}", font=('Arial', 14))
            lbl2.place(x=900, y=380)
            lbl3 = Label(root3, text=f"Age: {row[2]}", font=('Arial', 14))
            lbl3.place(x=900, y=430)
            lbl4 = Label(root3, text=f"Address: {row[3]}", font=('Arial', 14))
            lbl4.place(x=900, y=480)
    c3.create_rectangle(730,230,1150,300,fill=col1,width=0)
    label_disp=Label(root3,text='View Details of Rescued People',font=('ariel', 15),bg='white')
    label_disp.place(x=750,y=200)
    lbl_Rid = Label(root3, text="R id:", font=('ariel', 15), bg=col1,fg='white')
    lbl_Rid.place(x=750, y=250)
    Rid1=IntVar()
    E_Rid = Entry(root3, font=('ariel', 15),textvariable=Rid1)
    E_Rid.place(x=900, y=250)
    button2 = Button(root3, text="Submit", font=('ariel', 15), bg=col1, fg='white',command=displayrec3)
    button2.place(x=900, y=550)
    root3.mainloop()

#main window
root=Tk()

#this functions creates the database and the tables required
DB_connect.create_tables()

root.geometry('1300x700+0+0')
root.title('Flood management System')
c=Canvas(root,width=1300,height=700,bg="blue")
c.pack()
img=PhotoImage(file="cartoon-flood.png")
c.create_image(650,350,image=img)
c.create_rectangle(280,15,1050,100,fill='black',outline='yellow',width=3)
welcome_label=Label(root,text="Welcome to Flood Relief Management System",bg='black',fg='white',font=("Times new roman",30))
welcome_label.place(x=290,y=30)
button_Affected_areas=Button(root,text='Affected Areas',bg='black',fg='white',font=("Times new roman",20),cursor='hand2',width=20,command=Affected_Area)
button_Affected_areas.place(x=500,y=190)
button_inventory=Button(root,text="Manage Inventory",bg='black',fg='white',font=("Times new roman",20),cursor='hand2',width=20,command=Manage_inventory)
button_inventory.place(x=500,y=250)
button_rescue=Button(root,text='Rescued people',bg='black',fg='white',font=("Times new roman",20),cursor='hand2',width=20,command=rescued_people)
button_rescue.place(x=500,y=310)
root.mainloop()
