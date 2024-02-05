from tkinter import*
import tkinter as tk 
from tkinter import ttk
import datetime
win=tk.Tk()
win.geometry("400x300")
win.title("Staff Registration")
win.resizable(0,0)

def fill_current_date(event):
    current_date = datetime.datetime.now().strftime("%Y/%m/%d")
    doj_entry.delete(0, END)
    doj_entry.insert(0, current_date)

firstname=Label(win, text="First name: ").place(x=40, y=10)
firstname_entry=Entry(win,width=23).place(x=125, y=10)

middlename=Label(win, text="Middle Name: ").place(x=40, y=35)
middlename_entry= Entry(win,width=23).place(x=125, y=35)

lastname= Label(win, text="Last Name: ").place(x=40, y=60)
lastname_entry= Entry(win,width=23).place(x=125, y=60)

phone= Label(win, text="Phone: ").place(x=40, y=85)
phone_entry= Entry(win,width=23).place(x=125, y=85)

address= Label(win, text="Address: ").place(x=40, y=110)
address_entry= Entry(win,width=23).place(x=125, y=110)

doj= Label(win, text="Date Of Join: ").place(x=40, y=135)
doj_entry = Entry(win,width=23)
doj_entry.place(x=125,y=135)

doj_entry.bind("<Button-1>", fill_current_date)
doj_entry.bind("<ButtonRelease-1>", fill_current_date)

post= Label(win, text="Post: ").place(x=40, y=160)
post_entry=  ttk.Combobox(win,values=["Cleaner","Cook"] ).place(x=125, y=160)

salary= Label(win, text="Salary: ").place(x=40, y=185)
salary_entry=Entry(win,width=23).place(x=125, y=185)

save_btn = Button(win, text="Save", bg="#00FFFF",font="vardana 15 bold").place(x=70,y=250)
back_btn = Button(win, text="Back", bg="#FF7F24",font="vardana 15 bold").place(x=140,y=250)

win.mainloop()