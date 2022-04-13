from platform import win32_edition
import tkinter as tk
from tkinter import Entry, Frame, Label, Listbox, PhotoImage, Scale, Scrollbar, StringVar, Text, ttk
from tkinter import messagebox
from tkinter.constants import BOTH, END, RIDGE
from PIL import Image,ImageTk
import final_backend_done

window_4=tk.Tk()
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

'''def info_box():
    message=final_backend_done.Info_func()
    Info.delete(1.0,END)
    Info.insert(tk.END,message)

def view_details_command():
    list3.delete(0,END)
    for row in final_backend_done.view_3():
        list3.insert(END,row)
    info_box()'''


l_1=Label(window_4,bg="gray99",text="Details of the Books Issued",font=("Elephant",20))
l_1.place(x=200,y=50)

frame_det=Frame(window_4,bg="SkyBlue1",height=600,width=1000,bd=10,relief=RIDGE)
frame_det.place(x=150,y=100)
list3=Listbox(window_4,height=31,width=150)
list3.place(x=180,y=130)
sb3=Scrollbar(window_4)
sb3.place(x=1090,y=130,height=500,width=30)
list3.configure(yscrollcommand=sb3.set)
sb3.configure(command=list3.yview)

b13=tk.Button(window_4,bd=10,text="View",width=14,font=("Elephant",13),bg="dodger blue")
b13.place(x=180,y=631)

b13=tk.Button(window_4,bd=10,text="Preview",width=14,font=("Elephant",13),bg="dodger blue")
b13.place(x=400,y=631)

b13=tk.Button(window_4,bd=10,text="Send Emails",width=15,font=("Elephant",13),bg="dodger blue")
b13.place(x=925,y=631)


window_4.state('zoomed')
window_4.mainloop()