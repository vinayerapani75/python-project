
from tkinter import *
from tkinter import messagebox
from PIL import Image   #importing PIL for image formats like jpg,gif etc.
import mysql.connector  #connecting to mysql
mb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="siddarth@369",
    database="world"       #database where the data of user is stored.
    )
mycursor=mb.cursor()        #instance of database.

#=============CREATION OF TABLE======================
#mycursor.execute("create table user_det(name varchar(255),ph_nu varchar(255),email varchar(255),u_name varchar(255) unique,u_pass varchar(255),gend int)")
#print('done')

#==============NEW USER INFORMATION WINDOW=====================#
def show():                 
    user_layer=Toplevel()       #toplayer      
    user_layer.title("BILLING SYSTEM\Login")    #title of toplevel
    user_layer.geometry("1250x700+50+5")        # windowsize with the coodrinates where to start on screen
    user_layer.resizable(False,False)       #don't allow maxisimize option

    img_us=PhotoImage(file="userbg.png")    #creating background image for window
    imgus_bg=Label(user_layer,image=img_us).place(x=0,y=0)  

    #==========creation of Frame========
    
    us_fr=Frame(user_layer,bg="gainsboro",highlightbackground="black",highlightthickness=5,cursor="hand1")
    us_fr.place(x=20,y=30,height=650,width=550)

    

    name=StringVar()   
    ph=IntVar()
    email=StringVar()
    u_n=StringVar()
    u_p=StringVar()
    gen=IntVar()
    
    
     
    l0=Label(us_fr, text="SIGNIN DETAILS", bg="gainsboro",fg="black",font=("Oswald",30,"bold","underline")).place(x=110,y=25)   #title of frame
    l1=Label(us_fr, text="NAME",font=("Oswald",15,"bold"), bg="gainsboro").place(x=80,y=125)                                    #name label
    e1=Entry(us_fr,textvariable=name,font=("Oswald",14,"bold"),width=25,bg="grey",bd=5,fg="white")                  #entry box for name
    e1.place(x=240,y=125)                                                                                           #placement of box
         
    l2=Label(us_fr, text="PHONE NUMBER",font=("Oswald",15,"bold"), bg="gainsboro").place(x=30,y=175)         #ph.no label
    e2=Entry(us_fr,textvariable=ph,font=("Oswald",14,"bold"),width=25,bg="grey",bd=5,fg="white")             #entry box for ph.no
    e2.place(x=240,y=175)                                                                                   #placement of box

    l3=Label(us_fr, text="EMAIL ID",font=("Oswald",15,"bold"), bg="gainsboro").place(x=60,y=225)            #email label
    e3=Entry(us_fr,textvariable=email,font=("Oswald",14,"bold"),width=25,bg="grey",bd=5,fg="white")         #entry box for email
    e3.place(x=240,y=225)                                                                                   #placement of box

    l4=Label(us_fr, text="SET USERNAME",font=("Oswald",15,"bold"), bg="gainsboro").place(x=30,y=275)        #username label 
    e4=Entry(us_fr,textvariable=u_n,font=("Oswald",14,"bold"),width=25,bg="grey",bd=5,fg="white")           #entry box for set username
    e4.place(x=240,y=275)                                                                                   #placement of box

    l5=Label(us_fr, text="SET PASSWORD",font=("Oswald",15,"bold"), bg="gainsboro").place(x=30,y=325)        #set password label
    e5=Entry(us_fr,textvariable=u_p,font=("Oswald",14,"bold"),width=25,bg="grey",bd=5,fg="white")           #entry box for set password
    e5.place(x=240,y=325)                                                                                   #placement of box

    l6=Label(us_fr, text="GENDER",font=("Oswald",15,"bold"), bg="gainsboro").place(x=60,y=375)              #RadioButton for gender
    r1=Radiobutton(us_fr,variable=gen,text="MALE",font=("Oswald",15,"bold"), bg="gainsboro",value=1)        #male option
    r1.place(x=330,y=375)                                                                                   #placement of entrybutton
    r2=Radiobutton(us_fr,variable=gen,text="FEMALE",font=("Oswald",15,"bold"), bg="gainsboro",value=2)      #female option
    r2.place(x=330,y=405)                                                                                   #placement of entrybutton
    r3=Radiobutton(us_fr,variable=gen,text="OTHERS",font=("Oswald",15,"bold"), bg="gainsboro",value=3)      #others option
    r3.place(x=330,y=435)                                                                                   #placement of entrybutton
    #==================THE FUNCTION up_show TO CHECK WEATHER USER HAS ENTERED DETAILS OR NOT==================================
    def up_show():
       if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()==""):     #for empty or not
              messagebox.showerror("Error","All Fields Are Required",parent=user_layer)     #tkinter messagebox to show error if any of the fields are not entered by user.
       f=e4.get()                                                   #fetching username
       que="select u_name from user_det where u_name='"+f+"' "      #checking the username in database. 
       mycursor.execute(que)                                     
       rcount=len(mycursor.fetchall())
       if(rcount==1):                                               #if we get the rowcount==1 then there is already a username created with the name entered by user.
           messagebox.showerror("Error","username is already taken",parent=user_layer)   #and displaying error 'username is already taken'.plz enter new name.

       f1=e2.get()                  #fetching the ph.no entered by user and checking weather 10 number are there or not.                                                  
       cnt=0
       for i in f1:
           cnt=cnt+1
       if(cnt!=10):
           messagebox.showerror("Error","please enter a valid 10 digit number",parent=user_layer)     #if not 10 number entered then display error
       else:                      #if no errors there in information then take the information into database
           mycursor.execute("insert into user_det values (%s, %s, %s, %s, %s, %s)",(name.get(),ph.get(),email.get(),u_n.get(),u_p.get(),gen.get() ) )
           mb.commit()                    #committing the details of user into database 
           messagebox.showinfo("New User","New User Account Created",parent=user_layer)  # when clicked on create then message appears that the newuseraccount created.
           name.set("")
           ph.set("")
           email.set("")
           u_n.set("")
           u_p.set("")
           gen.set("")
           mycursor.execute("select * from user_det where u_name='"+f+"'")
           y=mycursor.fetchall() #only new user info
           for i in y:                  
               print(i)
       '''                    
       def display():       #for displaying the users details. 
          mycursor.execute("select * from user_det")
          x=mycursor.fetchall()
          for i in x:
             print(i)
       '''
   #=======buttons when onclick CREATE the up_show command is shown... when onclick BACK the toplevel is destroyed and back to login window...==============            
    b_1=Button(us_fr,text="CREATE",command=up_show,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED,width=17).place(x=170,y=510)
    #b_2=Button(us_fr,text="show",command=display,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED,width=17).place(x=170,y=570)
    b_3=Button(us_fr,text="BACK",command=user_layer.destroy,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED).place(x=440,y=570)
    user_layer.mainloop()       #ending the toplevel

#======================LOGIN WINDOW=========    
root=Tk()                     #creation of window
root.title("BILLING SYSTEM\Login")          #title of rootwindow
root.geometry("1250x700+50+5")              # windowsize with the coodrinates where to start on screen
root.resizable(False,False)       #don't allow maxisimize option

img_lg=PhotoImage(file="loginbg.png")           #creating background image for window
imglg_bg=Label(root,image=img_lg).place(x=0,y=0)
#==========creation of Frame========
log_fr=Frame(root,bg="gainsboro",highlightbackground="black",highlightthickness=5,cursor="hand1")
log_fr.place(x=100,y=230,height=400,width=550)            #placing frame

        
head=Label(log_fr,text="LOGIN",font=("Oswald",25,"bold","underline"),bg="gainsboro").place(x=225,y=10)      #title of frame
lb_u=Label(log_fr,text="USERNAME",font=("Oswald",15,"bold"),bg="gainsboro").place(x=75,y=150)               #LOGIN username label
en_u=Entry(log_fr,font=("Oswald",15,"bold"),bg="grey",bd=5,fg="white")                                      #entrybox for username
en_u.place(x=250,y=150,height=35,width=230)                                                                 #placement of entrybox

lb_p=Label(log_fr,text="PASSWORD",font=("Oswald",15,"bold"),bg="gainsboro").place(x=75,y=200)               #password label
en_p=Entry(log_fr,font=("Oswald",15,"bold"),show="•",bg="grey",bd=5,fg="white")                             #entrybox for password
en_p.place(x=250,y=200,height=35,width=230)                                                                 #placement of entrybox
#=========================CREATING A FUNCTION to change the password for USER if he FORGET HIS password============
def fgpass(): 
    fg=Toplevel()     #ccreating window on login window
    fg.title("change password")   #title of window
    fg.geometry("500x500")        #window size
    fg.resizable(False,False)     #don't allow maximization of window
#==============Label frame with name CHANGEPASSWORD===================
    fg_la=LabelFrame(fg,text="CHANGE PASWORD",bg="gainsboro",highlightbackground="black",highlightthickness=5,cursor="hand1",font=("Oswald",15,"bold","underline"))
    fg_la.place(x=0,y=0,height=500,width=500)

    

    lb_u=Label(fg_la,text="USERNAME",font=("Oswald",15,"bold"),bg="gainsboro").place(x=45,y=150)    #username label
    en_u=Entry(fg_la,font=("Oswald",15,"bold"),bg="grey",bd=5,fg="white")                           #entrybox for username
    en_u.place(x=230,y=150,height=35,width=230)                                                     #placement of entrybox

    lb_p=Label(fg_la,text="SET NEW PASSWORD",font=("Oswald",15,"bold"),bg="gainsboro").place(x=5,y=200)    #Set new password  label 
    en_p=Entry(fg_la,font=("Oswald",15,"bold"),show="•",bg="grey",bd=5,fg="white")                         #entrybox for set new password
    en_p.place(x=230,y=200,height=35,width=230)                                                            #placement of entrybox
    #===========FUNCTION FOR SAVING THE NEW PASSWORD SET BY THE USER===========
    def savedet():
        un=en_u.get()       #FETCHING USER NAME
        fgp=en_p.get()      #fetching new password

        que1="select u_name from user_det where u_name='"+un+"'"         #selecting username from table in database and saving the new password of user 
        mycursor.execute(que1)
        user=len(mycursor.fetchall())
        if(un=="" or fgp==""): 
            messagebox.showerror("Error","All Fields Are Required",parent=fg) #if not entered the showerror message
        if(user!=1):
            messagebox.showerror("Error","Username is  invalid",parent=fg)   #if username is not found in database show error message
        else:
            quefg = "UPDATE user_det SET u_pass = '"+fgp+"' WHERE u_name = '"+un+"'"         #else take the new password of that user and update it in database.
            #print(quefg)
            mycursor.execute(quefg)
            mb.commit()                          #saving changes
            messagebox.showinfo("change successful","New Password updated Successfully",parent=fg)    #message is shown after the password is updated              
            fg.destroy()            #destroying the topwindow and back to login window
       

    #==============button SAVE to call the function savedet() to update new password and back to login window=================    
    bu_1=Button(fg_la,text="SAVE",command=savedet,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED,width=14).place(x=170,y=330)
    
    

    fg.mainloop() #closing of window

       
#=======================FUNCTION to check the cerdentials of user if matched the go to next window if not then no===================
def check_in():
    z=en_u.get()
    k=en_p.get()
    if(z=="" or k==""): 
         messagebox.showerror("Error","All Fields Are Required",parent=root)       #if not entered the showerror message

    que="select * from user_det where u_name='"+z+"' and u_pass='"+k+"' "          
    mycursor.execute(que)
    check=len(mycursor.fetchall())
    #===========checking weather entered username exisits or not========
    que1="select u_name from user_det where u_name='"+z+"'"
    mycursor.execute(que1)
    user=len(mycursor.fetchall())
    #===========checking weather entered password exisits or not==========
    que2="select u_pass from user_det where u_name='"+z+"'"
    mycursor.execute(que2)
    ch=mycursor.fetchall()
    tup=str(ch)
    #print(tup)
    #print(type(tup))
    afg="[('"+k+"',)]"
    #print(afg)
    #print(type(afg))
    
    if(user!=1):
        messagebox.showerror("Error","Username is  invalid",parent=root)      #if username is not present in database show error
    elif(tup!=afg):
         messagebox.showerror("Error","worng password",parent=root)           #if password doesn't match with username show error 
    elif(check==1):
        messagebox.showinfo("LOGIN","You Are Successfully Loggedin",parent=root)   #if everthing is correct then showinfo message
        win2=Toplevel()
        win2.title("User bills information") 
        win2.geometry('400x500')
        us_fr1=Frame(win2,bg="black",highlightbackground="white",highlightthickness=5,cursor="hand1")
        us_fr1.place(x=0,y=0,height=500,width=400)
        #========================Buttons for the below functions to retrieve and to save data===================================
        Total_amnt=Button(us_fr1,text="New Bill",command=new_bill,bg='white',width=15).place(x=150,y=150)
        see_bill=Button(us_fr1,text="Previous Bills",command=bills,bg='white',width=15).place(x=150,y=200)
        invoice=Button(us_fr1,text="Generate Invoice",command=records,bg='white',width=15).place(x=150,y=250)

#================Function to create new bill===================
def new_bill():
    


     
    main=Toplevel() #creating new bill window
    main.title("New Bill")
    main.geometry('1000x800')
    fr0=LabelFrame(main,text="Customer Details",bd=10,relief="groove",font=("times new roman",20),fg="blue",bg="black")#frame containing customer bill details
    fr0.place(x=0,y=20,relwidth=1)
    cust_title=Label(fr0,text="Bill Name",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=0,padx=20,pady=5)#
    ct=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold'))#To enter bill name
    ct.grid(row=0,column=1)

    cust_bill=Label(fr0,text="Bill No.",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=2,padx=20,pady=5)
    cn_txt=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold'))#to enter unique bill number
    cn_txt.grid(row=0,column=3)
    item_name=StringVar()#To hold the user entered item names
    price=IntVar()#To hold the user entered item price
    quantity=IntVar()#To hold the user entered item quantity
    total=IntVar()#To hold the toltal amount of particular item

    #============Function to store the bill name and bill number of the user================
    def save():
        #tn=cn_txt.get()
        db=ct.get()
        bn=cn_txt.get()
        li_db=[]
        li_tb=[]
        
        mycursor.execute('show databases')
        x=mycursor.fetchall()
        for i in x:
            li_db.append(i[0])
        if db in li_db:       #checking whether user entered bill name and bill number exists in the database or not
            mycursor.execute('show tables from {}'.format(db))
            y=mycursor.fetchall()
            for j in y:
                li_tb.append(j[0])
            if bn in li_tb:
                messagebox.showerror("Error","Bill No. already exists",parent=main)#pop up box to show error message
            else:
                mycursor.execute('create table {}.{}(item_name varchar(20),price float,quantity int,total float,gst varchar(20),checkout float)'.format(db,bn))
                
                
                          
            
        else:
            mycursor.execute('create database {}'.format(db))
            mycursor.execute('create table {}.{}(item_name varchar(20),price float,quantity int,total float,gst varchar(20),checkout float)'.format(db,bn))
                
        
        
        
    #===================Fuction to store the user entered items and its particulars into the database================================
    def add_item():
        #tn=cn_txt.get()
        db=ct.get()#To store the user entered bill name
        bn=cn_txt.get()#To store the user entered bill number
        mycursor.execute('insert into {}.{}(item_name,price,quantity,total,gst,checkout) values(%s,%s,%s,%s,%s,%s)'.format(db,bn),(item_name.get(),price.get(),quantity.get(),price.get()*quantity.get(),'0%',0.0))#Inserting items into the database
        mb.commit()
        mycursor.execute('select * from {}.{}'.format(db,bn))
        x=mycursor.fetchall()
        r=2
        for i in x:  #To print the list of items and its details 
            Label(fr3,bg='black',fg='white', text=i[0]).grid(row=r ,column=0)
            Label(fr3,bg='black',fg='white', text=i[1]).grid(row=r ,column=1)
            Label(fr3, bg='black',fg='white',text=i[2]).grid(row=r ,column=2)
            Label(fr3,bg='black',fg='white', text=i[3]).grid(row=r ,column=3)
            r=r+1
        item_name.set("")
        price.set("")
        quantity.set("")
        total.set("")

    #=========Function to sum up the costs of items==========
    def TOTAL():
        #tn=cn_txt.get()
        db=ct.get()
        bn=cn_txt.get()
        mycursor.execute('select sum(total) from {}.{}'.format(db,bn))
        x=mycursor.fetchall()
        Label(fr2,width=15,text=x).place(x=390,y=150)

    #========Function to include the GST and displaying total amount to be paid=================-==
    def checkout():
        db=ct.get()
        bn=cn_txt.get()
        tax=tkvar.get()#To hold the % of GST and to add this to the total amount
        if tax=='3%':
            tax=3
        if tax=='5%':
            tax=5
        if tax=='7%':
            tax=7
        if tax=='9%':
            tax=9
        if tax=='10%':
            tax=10
        
        mycursor.execute('select sum(total) from {}.{}'.format(db,bn))
        x=mycursor.fetchall()
        tot=float(x[0][0])
        y=float(x[0][0])
        check=tot+(x[0][0]*tax/100)#Adding total with GST
        mycursor.execute("update {}.{} set gst={} where gst='0%'".format(db,bn,tax))
        mb.commit()
        mycursor.execute("update {}.{} set checkout={} where checkout=0.0".format(db,bn,check))
        mb.commit()
        Label(main,text=check,bg='black',width=10,bd=5,relief="groove",fg='white',font=("times new roman",17)).place(x=230,y=590)
        Label(main,text='(Incl. of  all taxes)',bg='black',fg='white',font=("times new roman",7)).place(x=250,y=630) 
    
    




    inovice_no=Label(fr0,text="Invoice No.",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=4,padx=20,pady=5)
    inv_entry=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold')).grid(row=0,column=5)

    #========Button to save the user entered bill details by calling save() function===============================
    srch_butn=Button(fr0,text="SAVE",command=save,width=10).grid(row=0,column=6,padx=20,pady=5)#Save button to store the bill name and bill number

    fr1=LabelFrame(main,bd=5,relief="groove",font=("times new roman",20),fg="blue",bg="black")# Frame to hold the item details
    fr1.place(x=10,y=110,relwidth=1,height=700)

    fr2=LabelFrame(fr1,text="Item Names",bd=10,relief="groove",font=("times new roman",20),fg="blue",bg="black")
    fr2.place(x=5,y=10,width=550,height=300)
    l21=Label(fr2,text="Item name",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=0,padx=5,pady=5)#Label to show ITem name text
    e21=Entry(fr2,width=10,bg='white',bd=5,textvariable=item_name,relief="sunken",font=("Arial",12,'bold')).grid(row=0,column=1,padx=20,pady=10)#entry box to enter item names

    l22=Label(fr2,text="Price",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=2,padx=5,pady=5)
    e22=Entry(fr2,width=10,bg='white',bd=5,textvariable=price,relief="sunken",font=("Arial",12,'bold')).grid(row=0,column=3,padx=20,pady=10)#entry box to enter price

    l23=Label(fr2,text="Quantity",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=1,column=1)
    e23=Entry(fr2,width=10,bg='white',bd=5,textvariable=quantity,relief="sunken",font=("Arial",12,'bold')).grid(row=1,column=2,padx=20,pady=10)#entry box to enter quantity

    #==========Button to save the item details into the database by calling add_item() function==================
    add_itm=Button(fr2,text="ADD ITEM",command=add_item,bg='white',width=10).place(x=140,y=150)

    #==========Button to sum up the cost of individuals by calling TOTAl() function================
    Total_amnt=Button(fr2,text="TOTAL",command=TOTAL,bg='white',width=10).place(x=250,y=150)


    #===========Frame to display user entered item details on the GUI========================
    fr3=LabelFrame(fr1,bd=10,relief="groove",font=("times new roman",20),fg="blue",bg="black")
    fr3.place(x=580,y=15,width=375,height=500)
    Label(fr3, text="Item name",width=15,bd=5,relief="sunken", bg='black',fg="white").grid(row=1, column=0)
    Label(fr3, text="Price",bg='black',width=10,bd=5,relief="sunken", fg="white").grid(row=1, column=1)
    Label(fr3, text="Quantity",bg='black',width=10,bd=5,relief="sunken", fg="white").grid(row=1, column=2)
    Label(fr3, text="Total", bg='black',width=10,bd=5,relief="sunken",fg="white").grid(row=1, column=3)
    #====================================================================================================

    tkvar=StringVar(main)# variable to store the GST
    choices={'3%','5%','7%','10%'}
    tkvar.set('3%')
    popmenu=OptionMenu(main,tkvar,*choices)#GST option menu
    Label(main,text="GST",width=10,bd=5,relief="sunken", font=("times new roman",17),bg='black',fg="white").place(x=30,y=500)
    popmenu.place(x=55,y=540)
    #=====================Button to show the total amount including GST=========================
    gst=Button(main,text="CHECKOUT",font=("times new roman",17),command=checkout,width=10).place(x=430,y=500)


#=================Function to generate invoice with bil name and bill number================================
def records():
    rec=Toplevel()
    rec.title("Generate Invoice")
    rec.geometry('750x700')


    #===================Function to fetch item details of previous bills==================================        
    def fetch():
        db=ct.get()
        bn=cn_txt.get()
        mycursor.execute('select * from {}.{}'.format(db,bn))#Retrieving item details of previous bills
        x=mycursor.fetchall()
        r=2
        for i in x:          #To print the item details on the gui
            Label(fr1,bg='black',fg='white', text=i[0]).grid(row=r ,column=0)
            Label(fr1,bg='black',fg='white', text=i[1]).grid(row=r ,column=1)
            Label(fr1, bg='black',fg='white',text=i[2]).grid(row=r ,column=2)
            Label(fr1,bg='black',fg='white', text=i[3]).grid(row=r ,column=3)
            r=r+1
        mycursor.execute('select checkout from {}.{}'.format(db,bn))
        y=mycursor.fetchall()
        mycursor.execute('select gst from {}.{}'.format(db,bn))
        z=mycursor.fetchall()
        for i in y:
            text_tot=i[0]
        for j in z:
            text_gst=j[0]
        print(text_tot,text_gst)
        st='(including GST '+str(text_gst)+' %)'
        print(text_tot,text_gst)
        Label(fr1,width=8,text=text_tot).grid(row=r+1,column=3)
        Label(fr1,text=st,width=16,bg='black',fg='white',font=("times new roman",7)).grid(row=r+2,column=3)
        

        
    fr0=LabelFrame(rec,text="Bill Details",bd=10,relief="groove",fg='grey',font=("times new roman",20),bg="black")
    fr0.place(x=0,y=20,relwidth=1)#Frame to enter bill details
    cust_title=Label(fr0,text="Bill Name",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=0,padx=20,pady=5)
    ct=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold'))
    ct.grid(row=0,column=1)
    cust_bill=Label(fr0,text="Bill No.",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=2,padx=20,pady=5)
    cn_txt=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold'))
    cn_txt.grid(row=0,column=3)
    #=========================Button to fetch item details by calling fetch() function===========================================
    srch_btn=Button(fr0,text="FETCH",command=fetch,bg='white',bd=3,relief="sunken",width=10).grid(row=0,column=4,padx=20,pady=5)

    fr1=LabelFrame(rec,bd=10,relief="groove",font=("times new roman",20),fg="blue",bg="black")
    fr1.place(x=110,y=120,width=395,height=500)#Frame to display item details
    Label(fr1, text="Item name",width=15,bd=5,relief="sunken", bg='black',fg="white").grid(row=1, column=0)
    Label(fr1, text="Price",bg='black',width=10,bd=5,relief="sunken", fg="white").grid(row=1, column=1)
    Label(fr1, text="Quantity",bg='black',width=10,bd=5,relief="sunken", fg="white").grid(row=1, column=2)
    Label(fr1, text="Total", bg='black',width=11,bd=5,relief="sunken",fg="white").grid(row=1, column=3)

#==================Function to show user previous bills=====================================================
def bills():
    bill=Toplevel()
    bill.title("Bill Numbers")
    bill.geometry('750x700')

    #==============Function to fetch previous bill by entering user bill name====================================== 
    def fetch():
        db=ct.get()
        
        mycursor.execute('show tables from {}'.format(db))
        x=mycursor.fetchall()
        
        r=1
        c=2
        for i in x:      # To show the bills 
            Label(fr1,bg='black',fg='white', text=i[0]).grid(row=r ,column=3,padx=70,pady=5)
            r=r+1

    fr0=LabelFrame(bill,text="Bills",bd=10,relief="groove",fg='grey',font=("times new roman",20),bg="black")
    fr0.place(x=0,y=20,relwidth=1)#Frame to enter bil name and fetch
    cust_title=Label(fr0,text="Bill Name",bg='black',bd=5,relief="sunken",fg='white',font=("times new roman",15)).grid(row=0,column=0,padx=20,pady=5)
    ct=Entry(fr0,width=20,bg='white',font=("Arial",10,'bold'))
    ct.grid(row=0,column=1)
    #=====Button to fetch the previous bills by calling fetch() function===========
    srch_btn=Button(fr0,text="FETCH",command=fetch,bg='white',bd=3,relief="sunken",width=10).grid(row=0,column=2,padx=20,pady=5)
    fr1=LabelFrame(bill,bd=10,relief="groove",font=("times new roman",20),fg="blue",bg="black")
    fr1.place(x=110,y=120,width=300,height=500)#Frame to show previous bills
    
    

    
        
#=====================button used to do the above function===========================================
b_2=Button(log_fr,text="New User",command=show,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED).place(x=365,y=70)
b_1=Button(log_fr,text="LOG IN",command=check_in,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED,width=15).place(x=180,y=300)
b_3=Button(root,text="EXIT",command=root.destroy,bg="black",fg="white",activebackground="white",activeforeground="red",font=("Oswald",15,"bold"),bd=5,relief=RAISED,).place(x=520,y=640)
b_4=Button(log_fr,text="Forgot Password",command=fgpass,font=("Oswald",15,"bold"),bg="gainsboro",relief=FLAT).place(x=65,y=255)
root.mainloop()
