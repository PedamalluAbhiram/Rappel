#ENGINEERING EXPLORATION PROJECT BATCH 5 TKINTER APPLICATION_ RAPPEL(LIBRARY BOOK REMINDER)_____Backend
#Import the required modules
import sqlite3
import cv2
#from pyzbar.pyzbar import decode
import time
import smtplib
#Declaration of global variables
id_3 = 1
bc=0
bn=''
an=''
sn=''
rn=0
em=''
adn=0
br=''
pn=0
s_y=2021
s_m=7
s_d=3
b=''
a=0
#********************************************************************************Scan Function**********************************************
def scan():
    cap= cv2.VideoCapture(0)
    cap.set(3, 600)        #To set the size of the video capture window
    cap.set(4, 600)
    camera = True
    while camera == True:
        success, frame=cap.read()
        key=cv2.waitKey(1)
        flag=0
        if key%256 == 27:
           break
        for code in decode(frame):
           global a
           a = code.data.decode('utf-8')         #To decode the barcode and store the information in the variable
           flag=1
           time.sleep(3)

        if flag == 1:
           camera=False
           break
      
        cv2.imshow('Testing-code-scan',frame)
        cv2.waitKey(10)
    
    cap.release()    
    cv2.destroyAllWindows
    return a

#**************************************To display the information on the info box****************************************s
def call_func(ar):
        global b,s_d,s_m,s_y
        if ar=='update':
            b="UPDATED  BOOK  DETAILS  SUCCESSFULLY!"
        if ar=='add':
            b="ADDED BOOK  DETAILS  SUCCESSFULLY!"
        if ar=='delete':
            b="DELETED BOOK  DETAILS  SUCCESSFULLY!"
        if ar=='saved':
            b="DETAILS  RECORDED  SUCCESSFULLY!"
        if ar=='updated':
            b="UPDATED  STUDENT  DETAILS  SUCCESSFULLY!"
        if ar=='added':
            b="ADDED STUDENT  DETAILS  SUCCESSFULLY!"
        if ar=='deleted':
            b="DELETED  STUDENT  DETAILS  SUCCESSFULLY!"
        if ar=='sent':
            b="EMAIL  SENT  SUCCESSFULLY!"
        if ar=='date':
            b="TODAY's DATE  :  " + str(s_d)+"/"+str(s_m) +"/"+str(s_y)
        if ar=='delete_e':
            b="DETAILS  DELETED  SUCCESSFULLY!"


def Info_func():
    global b
    return b
#****************************************This is for the issued details database**********************************************
#Fuction to establish a connection between code and the database and create a table if not exists
def connect_3():                          
    conn = sqlite3.connect("send_emails.db") 
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS send_email (id_3 INTEGER PRIMARY KEY, studentname text , rollnumber integer , email text ,admnum integer , branch text , phonenum integer, bookcode integer, bookname text, author text , s_date integer , s_month integer , s_year integer)")
    conn.commit()
    conn.close()

#Function to view the details present in the database
def view_3():
    conn = sqlite3.connect("send_emails.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM send_email")
    rows=cur.fetchall()
    conn.close()
    return rows

#Funtion to insert new details in the database
def insert_3(studentname,rollnumber,email,admnum,branch,phonenum,bookcode, bookname, author,s_d,s_m,s_y):
    conn = sqlite3.connect("send_emails.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO send_email VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(studentname, rollnumber ,email,admnum,branch,phonenum,bookcode, bookname, author,s_d,s_m,s_y))
    #view_3()
    #call_func('add_e')
    conn.commit()
    conn.close()   

#Function to delete the details in the datbase
def delete_3(id_a):
    conn = sqlite3.connect("send_emails.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM send_email WHERE id_3=?",(id_a,))
    conn.commit()
    conn.close()
    view_3()
    print("Details deleted !!")
    call_func('delete_e')

#This is to search for a particular member in the data baseS
def search_3(s_d='',s_m='',s_y=''):
    conn = sqlite3.connect("send_emails.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM send_email WHERE s_date=? AND s_month=? AND s_year=? ",(s_d,s_m,s_y))
    rows=cur.fetchall()
    conn.close()
    return rows
#************************************This is for the books database***************************************************
#Fuction to establish a connection between code and the database and create a table if not exists
def connect():                          
    conn = sqlite3.connect("books.db") 
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, bookcode integer, bookname text, author text)")
    conn.commit()
    conn.close()

#Function to view the details present in the database
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

#Funtion to insert new details in the database
def insert(bookcode, bookname, author):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",(bookcode, bookname, author))
    view()
    call_func('add')
    conn.commit()
    conn.close()

#This is to search for a particular member in the data baseS
def search(bookcode="",bookname="",author=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE bookcode=? OR bookname=? OR author=?",(bookcode,bookname,author))
    rows=cur.fetchall()
    conn.close()
    return rows

#Function to delete the details in the database   
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    view()
    call_func('delete')
    conn.commit()
    conn.close()

#Function to update the details in the database   
def update(id,bookcode,bookname,author):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET bookcode=?, bookname=?, author=? WHERE id=?",(bookcode,bookname,author,id))
    conn.commit()
    call_func('update')
    conn.close()

#************************************This is for the students database*****************************************************
#Fuction to establish a connection between code and the database and create a table if not exists
def connect_1():   
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id_1 INTEGER PRIMARY KEY, studentname text,rollno integer, email text, addmissionno integer, branch text, phonenumber integer)")
    conn.commit()
    conn.close()

#This is to search for a particular member in the data baseS
def find(studentname, rollno, email, addmissionno, branch, phonenumber):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE studentname=? OR rollno=? OR email=? OR addmissionno=? OR branch=? OR phonenumber=?",( studentname, rollno, email, addmissionno, branch, phonenumber))
    rows=cur.fetchall()
    conn.close()
    print("rows")
    print(rows)
    return rows

#Funtion to insert new details in the database
def add(studentname, rollno, email, addmissionno, branch, phonenumber):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?)",(studentname, rollno, email, addmissionno, branch, phonenumber))
    view()
    call_func('added')
    conn.commit()
    conn.close()

#Function to view the details present in the database
def view_1():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    conn.close()
    return rows

#Function to delete the details in the database     
def erase(id_1):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id_1=?",(id_1,))
    view_1()
    call_func('deleted')
    conn.commit()
    conn.close()
 
#Function to update the details in the database  
def update_s(id_1,studentname, rollno, email, addmissionno, branch, phonenumber):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET studentname=?, rollno=?, email=?, addmissionno=?,branch=?,phonenumber=? WHERE id_1=?",(studentname, rollno, email, addmissionno, branch, phonenumber,id_1))
    conn.commit()
    call_func('updated')
    conn.close()

#Function to save the details in the database 
def save_date(date,month,year):
    global s_d,s_m,s_y
    s_d=date
    s_m=month
    s_y=year
    call_func('date')
    print("DATE:"+s_d +"-"+s_m+"-"+ s_y)
   
#**************************************To save all the student and book details and date of issue of the book****************** 
def save_details(id_s,student_name,roll_no,e_mail,addmission_no,branch,phone_number,book_code,book_name,author_name,d,m,y):
     global bc,bn,an,sn,rn,em,adn,br,pn,s_d,s_m,s_y,id_3
     tuple3=(id_s,student_name,roll_no,e_mail,addmission_no,branch,phone_number,book_code,book_name,author_name,d,m,y)
     id_3 = tuple3[0]
     sn=tuple3[1]
     rn=tuple3[2]
     em=tuple3[3]
     adn=tuple3[4]
     br=tuple3[5]
     pn=tuple3[6]
     bc=tuple3[7]
     bn=tuple3[8]
     an=tuple3[9]
     s_d=tuple3[10]
     s_m=tuple3[11]
     s_y=tuple3[12]
     insert_3(sn,rn,em,adn,br,pn,bc,bn,an,s_d,s_m,s_y)
     call_func('saved')
     view_3()
    
def save_img(roll_no):
     roll = roll_no
     return roll

std_email=''
book_code=1
book_name=''
author_name=''
std_name=''
roll_no=0

#****************************To send emails to the selected students****************************
def send_mail(t_d,t_m,t_y):
    global s_d,s_m,s_y,std_email,book_code,book_name,author_name,std_name,roll_no
    t_d=int(t_d)
    t_m=int(t_m)
    t_y=int(t_y)
    #*******************Logic fo get the date 14 days back the present date*********************
    if t_d<15:
        check_month=t_m-1   
        if t_m==1:
            check_month=12
            check_date=31+t_d-14
            check_year=t_y-1
        else:
            #check_month=t_m
            check_month=t_m-1 
            check_year=t_y 
            leap=check_year%4
            print("leap "+str(leap))
            if check_month in (1,3,5,7,8,10,12):
                check_date=31+t_d-14
            elif check_month == 2:
                if check_year%4==0:
                    check_date=29+t_d-14
                else:
                    check_date=28+t_d-14
            else:
                check_date=30+t_d-14 
        print(str(check_date)+"-"+str(check_month)+"-"+str(check_year))
    else:
        check_date=t_d-14
        check_month=t_m
        check_year=t_y
        print(str(check_date)+"-"+str(check_month)+"-"+str(check_year))

    tuple_list=search_3(check_date,check_month,check_year)

    email_tuple_elements = []
    for a_tuple in tuple_list:           #To store required emails
        email_tuple_elements.append(a_tuple[3])
    tuple_length=len(email_tuple_elements)

    stdname_tuple_elements=[]
    for r_tuple in tuple_list:           #To store required student_name
        stdname_tuple_elements.append(r_tuple[1])
    tuple_length=len(stdname_tuple_elements)

    bookcode_tuple_elements=[]
    for b_tuple in tuple_list:           #To store required book_codes
        bookcode_tuple_elements.append(b_tuple[7])
    tuple_length=len(bookcode_tuple_elements)

    bookname_tuple_elements=[]
    for c_tuple in tuple_list:           #To store required book_name
        bookname_tuple_elements.append(c_tuple[8])
    tuple_length=len(bookname_tuple_elements)

    id_tuple_elements=[]
    for d_tuple in tuple_list:           #To store required id
        id_tuple_elements.append(d_tuple[0])
    tuple_length=len(id_tuple_elements)

    authorname_tuple_elements=[]
    for e_tuple in tuple_list:           #To store required author_name
        authorname_tuple_elements.append(e_tuple[9])
    tuple_length=len(authorname_tuple_elements)

    
    rollno_tuple_elements=[]
    for s_tuple in tuple_list:           #To store required roll_no
        rollno_tuple_elements.append(s_tuple[2])
    tuple_length=len(rollno_tuple_elements)

    #To send the email to multiple required students  
    for i in range(0,tuple_length):
        std_email=email_tuple_elements[i]
        book_code=bookcode_tuple_elements[i]
        book_name=bookname_tuple_elements[i]
        id_tobe_deleted=id_tuple_elements[i]
        author_name=authorname_tuple_elements[i]
        std_name=stdname_tuple_elements[i]
        roll_no=rollno_tuple_elements[i]
        def send_email():
            global std_email,book_code,book_name,author_name,std_name,roll_no
            str_book_code=str(book_code)
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)            #To establish a connection to the server
            server.login("rohithgundaram@gmail.com","sonugundaram@gmail.com")
            message= "FROM LIBRARY DEPARTMENT OF CBIT.\n\nHi, "+std_name +"\n\nBOOK DETAILS: \n\nBook name    : "+ str(book_name)  +"\nBook code    : "+ str_book_code +"\nAuthor Name: "+author_name +"\n\nPLEASE RETURN THE BOOK TO THE LIBRARY BY TOMORROW.\nELSE YOU WILL HAVE TO PAY THE FINE!!\nTHANK YOU."
            server.sendmail("rohithgundaram@gmail.com", std_email ,message)
            server.quit()
        send_email()
        delete_3(str(id_tobe_deleted))
    call_func('sent')
    
connect_3()
connect_1()
connect()


