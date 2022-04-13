from tkinter import *
import tkinter as tk
from tkinter import ttk
window_3=tk.Tk()
font=("Elephant",12)

l13=Label(window_3,text="DD",font=font,bg="wheat1")
l13.place(x=495,y=505)
t_date_text=StringVar()
t_date=ttk.Combobox(window_3,textvariable=t_date_text,font=("Elephant",12),width=3)
t_date["values"]=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
t_date.current(24)
t_date.place(x=490,y=475)
#t_date.bind("<<ComboboxSelected>>",enter_command)


l14=Label(window_3,text="MM",font=font,bg="wheat1")
l14.place(x=565,y=505)
t_month_text=StringVar()
t_month=ttk.Combobox(window_3,textvariable=t_month_text,font=("Elephant",12),width=3)
t_month["values"]=(1,2,3,4,5,6,7,8,9,10,11,12)
t_month.current(6)
t_month.place(x=560,y=475)

l15=Label(window_3,text="YYYY",font=font,bg="wheat1")
l15.place(x=635,y=505)
t_year_text=StringVar()
t_year=ttk.Combobox(window_3,textvariable=t_year_text,font=("Elephant",12),width=5)
t_year["values"]=(2021,2022,2023,2024,2025,2026,2027,2028,2029,2030)
t_year.current(0)
t_year.place(x=630,y=475)

window_3.state('zoomed')
window_3.mainloop()