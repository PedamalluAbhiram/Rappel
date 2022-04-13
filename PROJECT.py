#PROJECT TKINTER APPLICATION_ RAPPEL(LIBRARY BOOK REMINDER)_____Frontend
#importing the required modules
from platform import win32_edition
import tkinter as tk
from tkinter import Entry, Frame, Label, Listbox,  Scrollbar, StringVar, Text, ttk
from tkinter import messagebox
from tkinter.constants import END, RIDGE
from PIL import Image,ImageTk
import final_backend_done       #To import the functions in the backend_done

#declaring the required global variables
details=[]
button_std=''
std=''
std_img_address="std_img.jpg"
window_1=''
window_2=''
window_3=''
window_wel=''
addmission_number=0
g_t_date_text=1
g_t_month_text=7
g_t_year_text=2021
#***************************************************Loginpage*************************************************
def LoginPage(event):
    global window_1
    window_1=tk.Toplevel()
    window_1.title("Login Page_RAPPEL_ver1.0")
    window_1.iconbitmap("icon.ico")
    window_1.geometry("1550x785")
    
    load=Image.open("pic_16.jpg")
    load=load.resize((1550,790))
    photo=ImageTk.PhotoImage(load)
    label=tk.Label(window_1,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    E1=tk.Entry(window_1,width=40,bd=5,font=("Arial Bold",12))
    E1.place(x=608,y=486,height=35)
    E2=tk.Entry(window_1,width=33,show='*',bd=5,font=("Arial Bold",15))
    E2.place(x=608,y=560,height=35)

    def verify():            #To verify whether the username and password matched with the details in the database 
        try:
            with open("credential.txt","r") as f:
                info=f.readlines()
                i=0
            
                for e in info:
                    u, p = e.split(",")
                    if u.strip()==E1.get() and p.strip()==E2.get():
                        MainPage()             #Opens the main page if the login is successful
                        window_1.destroy
                        i=1
                        break
                if i==0:
                    messagebox.showinfo("Error","Please provide correct username and password!!")
                    window_1.destroy()
        except:
                print("In except block")
                messagebox.showinfo("Error","Please provide correct username and password!!")


    
    button=tk.Button(window_1,text="Submit",bd=0,width=9,font=("Arial Bold",11),bg="DarkGoldenrod1",command=verify) 
    button.place(x=712,y=618)

    
    window_1.state('zoomed')
    window_1.mainloop()
#******************************************************ScanPage*****************************************************************************
#To scan the student id card and get the student details
def ScanPage():
    global window_2,window_3
    window_2=tk.Toplevel()  #Tk() is a class and window is the object
    window_2.wm_title("Scan_Page_ver_0.5")
    window_2.iconbitmap('icon.ico')
    window_2.geometry("1550x785")
    window_2.configure(bg="DodgerBlue4")

    def scan_command():
        global addmission_number,window_2,window_3
        window_3.destroy()
        addmission_number=final_backend_done.scan()
        window_2.destroy()
        MainPage()

    load=Image.open("scan_img.jpg")
    load=load.resize((600,500))
    photo=ImageTk.PhotoImage(load)
    label=tk.Label(window_2,image=photo)
    label.image=photo
    label.place(x=200,y=150)
    def skip():
        global window_3,window_2
        window_3.destroy()
        window_2.destroy()
        MainPage()
   

    b11=tk.Button(window_2,text="Scan",bd=10,bg="orange",font=("Arial Bold",15),width=20,command=scan_command)
    b11.place(x=900,y=340)
    b11=tk.Button(window_2,text="Skip",bd=10,bg="orange",font=("Arial Bold",15),width=20,command=skip)
    b11.place(x=900,y=440)
    la=tk.Label(window_2,fg="snow",text="STUDENT ID CARD SCAN WINDOW ",bd=5,bg="DodgerBlue4",font=("Elephant",30))
    la.place(x=300,y=10)
    window_2.state('zoomed')
    window_2.mainloop()    
#********************************MainPage*******************************************************************************
#HOME PAGE OF THE APPLICATION
def MainPage():
    global window_1,window_3,window_wel
    window_1.destroy()
    window_3=tk.Toplevel()
    window_3.wm_title("RAPPEL_Main Page_ver_1.0")  #To set the title for the window
    window_3.iconbitmap("icon.ico")        #To set an icon to the window
    window_3.geometry("1550x785")              #To give the dimensions of the window
    window_3.configure(bg="wheat1")        #To provide background colout
    font=('Arial Bold',12)
    font_la=("Elephant",14)

    def get_selected_row(event):          #Function to print the deatils of selected book in corresponding feilds
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e7.delete(0,END)
        e7.insert(END,selected_tuple[1])
        e8.delete(0,END)
        e8.insert(END,selected_tuple[2])
        e9.delete(0,END)
        e9.insert(END,selected_tuple[3])

    def get_selected_row_1(event):         #Function to print the deatils of selected student in corresponding feilds
        global selected_tuple_1
        index_1=list2.curselection()[0]
        selected_tuple_1=list2.get(index_1)
        e1.delete(0,END)
        e1.insert(END,selected_tuple_1[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple_1[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple_1[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple_1[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple_1[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple_1[6])
        find_command(rollno_text.get())

        
    def selected_1():                      #Function to store the deatils of student , book issued and date of issue 
        id_no=list3.get(0)
        s_name=studentname_text.get()
        r_no=rollno_text.get()
        e_mail=email_text.get()
        add_no=addmissionno_text.get()
        branch=branch_text.get()
        ph_no=phonenumber_text.get()
        b_code=bookcode_text.get()
        b_name=bookname_text.get()
        a_name=author_text.get()
        s_date=t_date_text.get()
        s_month=t_month_text.get()
        s_year=t_year_text.get()
        if s_name=='' or r_no=='' or e_mail=='' or add_no=='' or branch=='' or ph_no=='' or b_code=='' or b_name=='' or a_name=='' or s_date=='' or s_month=='' or s_year=='':
            response=messagebox.askyesno("Empty Field!!","Please fill all the required details\n Do you want to return to main page?")
            if response==1:
                window_3.destroy()
                MainPage()
            print(response)
        else:
            final_backend_done.save_details(id_no,s_name,r_no,e_mail,add_no,branch,ph_no,b_code,b_name,a_name,s_date,s_month,s_year)
            info_box()

    def view_command():                         #Function to call view function from backend and display all books details in list1
        list1.delete(0,END)
        for rows in final_backend_done.view():
            list1.insert(END,rows)

    def search_command():                          #Function to call search function from backend and search for the required book and display all book details in list1
        list1.delete(0,END)
        for rows in final_backend_done.search(bookcode_text.get(),bookname_text.get(),author_text.get()):
            list1.insert(END,rows)

    def insert_command():                 #function to call insert function in backend and add new book details in list 1
        final_backend_done.insert(bookcode_text.get(),bookname_text.get(),author_text.get())
        list1.delete(0,END)
        list1.insert(END,(bookcode_text.get(),bookname_text.get(),author_text.get()))
        view_command()
        info_box()

    def enter_command(event):                 #Function to save present day date, month, year
        final_backend_done.save_date(t_date_text.get(),t_month_text.get(),t_year_text.get())
        global g_t_date_text,g_t_month_text,g_t_year_text
        g_t_date_text=t_date.get()
        g_t_month_text=t_month.get()
        g_t_year_text=t_year_text.get()
        info_box()

    def delete_command():                #Function to call delete function in backend and delete selected book details from list 1
        final_backend_done.delete(selected_tuple[0])
        view_command()
        info_box()

    def update_command():                #Function to call update function in backend and update the changes made in book details in list 1
        final_backend_done.update(selected_tuple[0],bookcode_text.get(),bookname_text.get(),author_text.get())
        info_box()

    def look_command():               #Function to call find command in backend and search for the student based on the addmission number
        global addmission_number
        list2.delete(0,END)
        print(addmission_number)
        for row in final_backend_done.find(studentname_text.get(),rollno_text.get(),email_text.get(),addmission_number,branch_text.get(),phonenumber_text.get()):
            list2.insert(END,row)
    
    def find_student_command():               #Function to call find command in backend and search for the student based on the addmission number
        list2.delete(0,END)
        for row in final_backend_done.find(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get()):
            list2.insert(END,row)

    def add_command():                 #Function to call add function in backend and add new student details in list 2
        final_backend_done.add(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get())
        list2.delete(0,END)
        list2.insert(END,(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get()))
        info_box()

    def view_command_1():               #Function to call view_1 function in backend and display all the students details in list2
        list2.delete(0,END)
        for row in final_backend_done.view_1():
            list2.insert(END,row)

    def erase_command():        #function to call erase function in backend to delete selected student details from list 2
        final_backend_done.erase(selected_tuple_1[0])
        view_command_1()
        info_box()

    def update_s_command():      #function to call the update in backend and update the student details in list2 
        final_backend_done.update_s(selected_tuple_1[0],studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get())
        info_box()


    def info_command():        #New window to display information of the application
        window_7=tk.Toplevel()
        window_7.title("Developer Information Box_RAPPLE_ver_1.0")
        window_7.geometry("1550x785")
        window_7.configure(bg='seashell3')
        Info=Text(window_7,height=80,width=90,font=("Elephant",12),bg="SkyBlue1",bd=10,relief=RIDGE)
        Info.place(x=0,y=0)
        
        message='''*RAPPEL is a  software that is designed & developed to manage all the in-house functions of a library. 
        >> A librarian requires maintaining a database of new books and the books that are borrowed by users along with their due dates.
        >>The best way to maintain, organize,and handle countless books systematically is to implement a library management system software. 
        >>This system completely automates all your library’s activities. You can find books in an instant, issue/reissue books quickly, and
           manageall the data efficiently and orderly using this system. The purpose of a library management system is to provide instant and
           accurate dataregarding any type of book, thereby saving a lot of time and effort.
        >>RAPPEL is a highly integrated, user-friendly, and compatible library automation system for complete computerization of all the
           in-house operations of any size or type of library. The library management software is intuitive, efficient, and compliant.
           RAPPLE is embedded with Barcode scanner. 
        >>The circulation module enables the librarian to create and manage borrower types along with keeping a tab on their book issue date,
           return date,dues, and fines. It enables a smooth circulation of books in the library.
        \n\n>>>KEY FEATURES OF RAPPLE SOFTWARE
        >>can be integrated with the school management system
        >>100% assurance for import of other library software data into RAPPEL
        >>Mark standard data import/export
        >>Fully secured & maintenance-free library software
        >>Best onsite training & service support for all types of libraries
        >>Fine and Dues Calculation
        \n\n>>>ADVANTAGES OF LIBRARY MANAGEMENT SYSTEM 
        >>The library software is user-friendly, intuitive, and easy-to-use
        >>It offers 24*7 access to the library resources
        >>Highly secure and efficient library database management
        >>Provides greater efficiency of work processes & saves time of librarian
        >>Cost-effective software for library and can be configured as per requirements
        >>Right from managing the acquisition of issued/borrowed books, returned books & due date calculation,
           it helps in managing the daily work process in the library.
        >>The library management system is  software for managing library, track all the books borrowed with due dates, fees, etc. 
        \n\n                  This system completely automates all your library’s activities.'''
        Info.insert(tk.END,message)
        load=Image.open("info_img_1.jpg")
        load=load.resize((430,400))
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(window_7,image=photo)
        label.image=photo
        label.place(x=1105,y=0)

        load_1=Image.open("info_img.jpg")
        load_1=load_1.resize((430,400))
        photo_1=ImageTk.PhotoImage(load_1)
        label_1=tk.Label(window_7,image=photo_1)
        label_1.image=photo_1
        label_1.place(x=1105,y=400)

        window_7.state('zoomed')
        window_7.mainloop()

    def about_command():       #New window to display information about the developers
        window_8=tk.Toplevel()
        window_8.title("About_RAPPLE_ver_1.0")
        window_8.geometry("400x250")
        window_8.configure(bg='SteelBlue1')

        labe=Label(window_8,bg="SteelBlue1",font=("Elephant",11),text="Developers of RAPPEL ver_1.0\n\nP.Abhiram(160120737025,IT-1)")
        labe.pack()
        window_8.mainloop()

    def help_command():              #To open the help window
        window_9=tk.Toplevel()
        window_9.title("Help Desk_RAPPLE_ver_1.0")
        window_9.geometry("500x260")
        window_9.configure(bg='floral white')

        img=Image.open("help_img.jpg")
        img=img.resize((500,260))
        my= ImageTk.PhotoImage(img)
        label=Label(window_9,image=my)
        label.place(x=0,y=0)

        window_9.mainloop()

    def IssuedDetailsPage():             #To open the window that contails the details of the student and the books issued
        window_4=tk.Toplevel()
        window_4.title("Issued Book Details_RAPPEL_ver_1.0")
        window_4.geometry("1550x785")
        window_4.iconbitmap("icon.ico")
        window_4.configure(bg="NavajoWhite2")   

        load=Image.open("pic_3.jpg")
        load=load.resize((1550,785))
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(window_4,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        def view_command_3():             #To view the details
            list3.delete(0,END)
            for row in final_backend_done.view_3():
                list3.insert(END,row)
                
        def send_email():              #To send the email to the required student
            global g_t_date_text,g_t_month_text,g_t_year_text
            final_backend_done.send_mail(g_t_date_text,g_t_month_text,g_t_year_text)
            view_command_3()
            information_box()

        def view_details_command():
            list3.delete(0,END)
            for row in final_backend_done.view_3():
                list3.insert(END,row)

        l_1=Label(window_4,bg="gray99",text="Details of the Books Issued",font=("Elephant",20))
        l_1.place(x=100,y=25)

        frame_det=Frame(window_4,bg="SkyBlue1",height=600,width=1000,bd=10,relief=RIDGE)
        frame_det.place(x=50,y=75)
        list3=Listbox(window_4,height=31,width=150)
        list3.place(x=80,y=105)
        sb3=Scrollbar(window_4)
        sb3.place(x=990,y=105,height=500,width=30)
        list3.configure(yscrollcommand=sb3.set)
        sb3.configure(command=list3.yview)

        def information_box():
            message=final_backend_done.Info_func()
            Info.delete(1.0,END)
            Info.insert(tk.END,message)

        l16=Label(window_4,text="Information box",font=("Elephant",13),bg='gray99')
        l16.place(x=650,y=15)
        Info=Text(window_4,height=1,width=31,font=("Elephant",12),bd=10,relief=RIDGE)
        Info.place(x=650,y=35)

        b13=tk.Button(window_4,bd=10,text="View",width=14,font=("Elephant",13),bg="dodger blue",command=view_details_command)
        b13.place(x=80,y=606)

        b13=tk.Button(window_4,bd=10,text="Send Emails",width=15,font=("Elephant",13),bg="dodger blue",command=send_email)
        b13.place(x=820,y=606)


        window_4.state('zoomed')
        window_4.mainloop()
    
    def register():       #To register new user
        window_10=tk.Tk()
        window_10.resizable(0,0)
        window_10.configure(bg="deep sky blue")
        window_10.iconbitmap("icon.ico")
        window_10.title("Register")

        l1=tk.Label(window_10,text="Username             :",font=('Arial bold',15),bg="deep sky blue")
        l1.place(x=10,y=10)
        t1=tk.Entry(window_10,width=30,bd=5,font=('Arial bold',11))
        t1.place(x=200,y=10)
        l2=tk.Label(window_10,text="Create Password  :",font=('Arial bold',15),bg="deep sky blue")
        l2.place(x=10,y=60)
        t2=tk.Entry(window_10,width=30,bd=5,font=('Arial bold',11))
        t2.place(x=200,y=60)
        l3=tk.Label(window_10,text="Confirm Password :",font=('Arial bold',15),bg="deep sky blue")
        l3.place(x=10,y=110)
        t3=tk.Entry(window_10,width=30,bd=5,font=('Arial bold',11))
        t3.place(x=200,y=110)

        def  check():         #To check whether the password in both the fields is same or not
            if t1.get()!="" or t2.get()!="" or t3.get()!="":
                if t2.get()==t3.get():
                    with open("credential.txt","a") as f:
                        f.write(t1.get()+","+t2.get()+"\n")
                        messagebox.showinfo("Welcome","You are registered successfully!!")
                else:
                    messagebox.showinfo("Error","Your password didn't get matched!!")
            else:
                messagebox.showinfo("Error","Please fill the complete fields")
   
    
        b1=tk.Button(window_10,text="Sign in",font=("arial",15),bd=5,bg='#ffc22a',command=check)
        b1.place(x=170,y=150)

   
        window_10.geometry("470x220")
        window_10.mainloop()


    book_frame=Frame(window_3,bg="DodgerBlue4",bd=10,relief=RIDGE)
    book_frame.place(x=1250,y=340,width=200,height=180)

    img=Image.open("logo.png")                    #To add an image in the window
    img=img.resize((900,136))
    my= ImageTk.PhotoImage(img)
    label=Label(window_3,image=my)
    label.place(x=10,y=0)

    img_1=Image.open("owl.png")                  #To add an image in the window
    img_1=img_1.resize((270,230))
    my_1= ImageTk.PhotoImage(img_1)
    label_1=Label(window_3,image=my_1)
    label_1.place(x=460,y=560)

    img_3=Image.open("library_image.png")        #To add an image in the window
    img_3=img_3.resize((595,136))
    my_3= ImageTk.PhotoImage(img_3)
    label_3=Label(window_3,image=my_3)
    label_3.place(x=915,y=0)

    img_2=Image.open("pic.png")           #To add an image in the window
    img_2=img_2.resize((250,220))
    my_2= ImageTk.PhotoImage(img_2)
    label_2=Label(window_3,image=my_2)
    label_2.place(x=750,y=560)

    img_7=Image.open("book_img.jpg")        #To add an image in the window
    img_7=img_7.resize((175,155))
    my_7= ImageTk.PhotoImage(img_7)
    label_7=Label(book_frame,image=my_7)
    label_7.place(x=0,y=0)

    Dataframe=Frame(window_3,bd=15,relief=RIDGE,bg="orange")
    Dataframe.place(x=10,y=170,width=1500,height=160)

    #*************************************To create labels and entry boxes to take input from user****************************************

    l1=Label(window_3,bg="orange",text="Student Name",font=font_la)
    l1.place(x=50,y=205)
    studentname_text=StringVar()
    e1=Entry(window_3,textvariable=studentname_text,font=("Arial Bold",13))
    e1.place(x=250,y=200,width=250,height=30)

    l2=Label(window_3,bg="orange",text="Roll Number",font=font_la)
    l2.place(x=530,y=205)
    rollno_text=StringVar()
    e2=Entry(window_3,textvariable=rollno_text,font=("Arial Bold",13))
    e2.place(x=670,y=200,width=300,height=30)

    l3=Label(window_3,text="Email",bg="orange",font=font_la)
    l3.place(x=1010,y=205)
    email_text=StringVar()
    e3=Entry(window_3,textvariable=email_text,font=("Arial Bold",13))
    e3.place(x=1200,y=200,width=250,height=30)

    l4=Label(window_3,text="Admission Number",bg="orange",font=font_la)
    l4.place(x=35,y=240)
    addmissionno_text=StringVar()
    e4=Entry(window_3,textvariable=addmissionno_text,font=("Arial Bold",13))
    e4.place(x=250,y=235,width=250,height=30)

    l5=Label(window_3,text="Branch",bg="orange",font=font_la)
    l5.place(x=530,y=240)
    branch_text=StringVar()
    e5=Entry(window_3,textvariable=branch_text,font=("Arial Bold",13))
    e5.place(x=670,y=235,width=300,height=30)

    l6=Label(window_3,text="Phone number",bg="orange",font=font_la)
    l6.place(x=1010,y=240)
    phonenumber_text=StringVar()
    e6=Entry(window_3,textvariable=phonenumber_text,font=("Arial Bold",13))
    e6.place(x=1200,y=235,width=250,height=30)

    l7=Label(window_3,text="Book code",bg="orange",font=font_la)
    l7.place(x=50,y=275)
    bookcode_text=StringVar()
    e7=Entry(window_3,textvariable=bookcode_text,font=("Arial Bold",13))
    e7.place(x=250,y=270,width=250,height=30)


    l8=Label(window_3,text="Book name",bg="orange",font=font_la)
    l8.place(x=530,y=275)
    bookname_text=StringVar()
    e8=Entry(window_3,textvariable=bookname_text,font=("Arial Bold",13))
    e8.place(x=650,y=270,width=320,height=30)

    l9=Label(window_3,text="Author",bg="orange",font=font_la)
    l9.place(x=1010,y=275)
    author_text=StringVar()
    e9=Entry(window_3,textvariable=author_text,font=("Arial Bold",13))
    e9.place(x=1200,y=270,width=250,height=30)


    l12=Label(window_3,text="Date of Issue of the Book ",font=("Elephant",13),bg="wheat1")
    l12.place(x=480,y=445)

    #To create dropdown list for the date,month,year
    l13=Label(window_3,text="DD",font=font,bg="wheat1")
    l13.place(x=495,y=505)
    t_date_text=StringVar()
    t_date=ttk.Combobox(window_3,textvariable=t_date_text,state="readonly",font=("Elephant",12),width=3)
    t_date["values"]=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    t_date.current(0)
    t_date.place(x=490,y=475)
    t_date.bind("<<ComboboxSelected>>",enter_command)


    l14=Label(window_3,text="MM",font=font,bg="wheat1")
    l14.place(x=565,y=505)
    t_month_text=StringVar()
    t_month=ttk.Combobox(window_3,textvariable=t_month_text,state="readonly",font=("Elephant",12),width=3)
    t_month["values"]=(1,2,3,4,5,6,7,8,9,10,11,12)
    t_month.current(0)
    t_month.place(x=560,y=475)

    l15=Label(window_3,text="YYYY",font=font,bg="wheat1")
    l15.place(x=635,y=505)
    t_year_text=StringVar()
    t_year=ttk.Combobox(window_3,textvariable=t_year_text,state="readonly",font=("Elephant",12),width=5)
    t_year["values"]=(2021,2022,2023,2024,2025,2026,2027,2028,2029,2030)
    t_year.current(0)
    t_year.place(x=630,y=475)

    l16=Label(window_3,text="Information box",font=("Elephant",12),bg="wheat1")
    l16.place(x=480,y=340)
    Info=Text(window_3,height=2,width=38,font=("Elephant",13),bd=10,relief=RIDGE)
    Info.place(x=480,y=370)


    def info_box():
        message=final_backend_done.Info_func()
        Info.delete(1.0,END)
        Info.insert(tk.END,message)

    #To create a list Box which can display info about the students, books
    list1_frame=Frame(window_3,bd=10,relief=RIDGE,width=100,bg="wheat1")
    list1_frame.place(x=1010,y=560,width=500,height=230)
    l10=Label(window_3,text="BOOKS   DETAILS",font=font_la,bg="wheat1")
    l10.place(x=1250,y=530)
    list1=Listbox(window_3,height=11,width=73)
    list1.place(x=1030,y=580)
    sb1=Scrollbar(window_3)
    sb1.place(x=1477,y=642)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>',get_selected_row)

    list2_frame=Frame(window_3,bd=10,relief=RIDGE,width=100,bg="wheat1")
    list2_frame.place(x=10,y=560,width=430,height=230)
    l11=Label(window_3,text="STUDENTS DETAILS",font=font_la,bg="wheat1")
    l11.place(x=17,y=530)
    list2=Listbox(window_3,height=11,width=63)
    list2.place(x=25,y=580)
    sb2=Scrollbar(window_3)
    sb2.place(x=410,y=642)
    list2.configure(yscrollcommand=sb2.set)
    sb2.configure(command=list2.yview)
    list2.bind('<<ListboxSelect>>',get_selected_row_1)

    list3=Listbox(window_3,height=11,width=125)
    list3.pack
    sb3=Scrollbar(window_3)
    sb3.pack
    list3.configure(yscrollcommand=sb3.set)
    sb3.configure(command=list3.yview)
                
    details=[]
    photo_frame=Frame(window_3,bg="DodgerBlue4",bd=10,relief=RIDGE)
    photo_frame.place(x=40,y=340,width=180,height=180)
    std=Image.open(std_img_address)
    std=std.resize((155,155))
    my_std= ImageTk.PhotoImage(std)

    global my_label

    my_label=Label(photo_frame,image=my_std)
    my_label.grid(row=0,column=0)    

    #To display the image of the selected  student 
    def find_command(roll_num):
        global details
        global button_std
        global std_img_address,std,my_std
        global my_label

        for row in final_backend_done.find(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get()):
            details.append(row[2])
        std_img_address=str(roll_num)+".jpg"
        my_label.grid_forget()
        std=Image.open(std_img_address)
        std=std.resize((155,155))
        my_std= ImageTk.PhotoImage(std)
        my_label=Label(photo_frame,image=my_std)
        my_label.grid(row=10,column=0)

   

    books_frame=Frame(window_3,bd=12,relief=RIDGE,bg="SkyBlue1")
    books_frame.place(x=1040,y=330,width=190,height=225)

    Dataframe_stud=Frame(window_3,bd=12,relief=RIDGE,bg="SkyBlue1")
    Dataframe_stud.place(x=255,y=330,width=190,height=225)

    look_command()
    #********************************************To create buttons to perform various tasks************************************
    
    b2=tk.Button(window_3,text="View all Books", width=15,command=view_command,font=font,bg="dodger blue")
    b2.place(x=1054,y=345)

    b3=tk.Button(window_3,text="Search  Book", width=15,command=search_command,font=font,bg="dodger blue")
    b3.place(x=1054,y=385)

    b4=tk.Button(window_3,text="Add Book", width=15,command=insert_command,font=font,bg="dodger blue")
    b4.place(x=1054,y=425)

    b5=tk.Button(window_3,text="Update  Book", width=15,command=update_command,font=font,bg="dodger blue")
    b5.place(x=1054,y=465)

    b6=tk.Button(window_3,text="Delete  Book", width=15,command=delete_command,font=font,bg="dodger blue")
    b6.place(x=1054,y=505)

    b11=tk.Button(window_3,text="All students",bg="dodger blue",width=15,command=view_command_1,font=font)
    b11.place(x=270,y=345)

    b9=tk.Button(window_3,text="Find Student",bg="dodger blue",width=15,command=find_student_command,font=font)
    b9.place(x=270,y=385)

    b10=tk.Button(window_3,text="Add Student",bg="dodger blue",width=15,command=add_command,font=font)
    b10.place(x=270,y=425)

    b9=tk.Button(window_3,text="Delete Student",bg="dodger blue",width=15,command=erase_command,font=font)
    b9.place(x=270,y=505)

    b8=tk.Button(window_3,text="Issue the Book",bg="orange",width=15,font=("Elephant",15),bd=10,command=selected_1)
    b8.place(x=770,y=470)

    b10=tk.Button(window_3,text="Update Student",bg="dodger blue",width=15,command=update_s_command,font=font)
    b10.place(x=270,y=465)


    b_1=tk.Button(window_3,text="New Scan",width=15,font=("Arial Bold",13),bg="ivory3",command=ScanPage)
    b_1.place(x=10,y=140)

    b_2=tk.Button(window_3,text="Issued Book Details",width=21,font=("Arial Bold",13),bg="ivory3",command=IssuedDetailsPage)
    b_2.place(x=170,y=140)

    b_3=tk.Button(window_3,text="Info",width=15,font=("Arial Bold",13),bg="ivory3",command=info_command)
    b_3.place(x=390,y=140)

    b_4=tk.Button(window_3,text="About  !",width=15,font=("Arial Bold",13),bg="ivory3",command=about_command)
    b_4.place(x=550,y=140)

    b_5=tk.Button(window_3,text="Help  ?",width=15,font=("Arial Bold",13),bg="ivory3",command=help_command)
    b_5.place(x=710,y=140)

    B2=tk.Button(window_3,text="Register New User",width=17,command=register,font=("Arial Bold",13),bg="ivory3")
    B2.place(x=870,y=140)

    b_7=tk.Button(window_3,text="Exit",width=15,font=("Arial Bold",13),bg="ivory3",command=window_wel.destroy)
    b_7.place(x=1050,y=140)

    b_6=tk.Button(window_3,text="",bg="ivory3",width=41)
    b_6.place(x=1210,y=140,height=33)

    window_3.state("zoomed")
    tk.mainloop()
    window_3.mainloop()
#***************************************WelcomePage*************************************************
def welcomepage():
        global window_wel
        window_wel=tk.Tk()
        window_wel.title("Welcome Page_RAPPEL_ver_1.0")
        window_wel.iconbitmap("icon.ico")
        window_wel.geometry("1550x785")

        load=Image.open("welcome.jpg")
        load=load.resize((1550,790))
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(window_1,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        label.bind("<Button-1>",LoginPage)

        window_wel.state('zoomed')
        window_wel.mainloop()
welcomepage()

