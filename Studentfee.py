from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL  import Image , ImageTk
from tkmacosx import Button
import datetime

def fill_current_date(event):
    current_date = datetime.datetime.now().strftime("%Y/%m/%d")
    Monthentry.delete(0, END)
    Monthentry.insert(0, current_date)


def onclick():
    tk.messagebox.showinfo("","Student fees saved!")

win=tk.Tk()
win.geometry("540x400")
win.resizable(0,0)
win.title("STUDENT FEE")

S_Id =Label(win,text="S-ID :")
S_Id.grid(row=0,column=0,sticky="w",padx=10,pady=10)

S_Id_entry=Entry(win)
S_Id_entry.grid(row=0,column=1,padx=10,pady=10)


Firstname =Label(win,text ="First Name :")
Firstname.grid(row=1,column=0,sticky="w",padx=10,pady=10)

Firstnameentry=Entry(win)
Firstnameentry.grid(row=1,column=1,padx=10,pady=10)

Middlename =Label(win,text="Middle Name :")
Middlename.grid(row= 2,column=0 ,sticky="w",padx=10,pady=10)
   
Middlenameentry=Entry(win)
Middlenameentry.grid(row=2,column=1,padx=10,pady=10)

Lastname =Label(win,text="Last Name :")
Lastname.grid(row=3,column=0,sticky="w",padx=10,pady=10)


Lastnameentry = Entry(win)
Lastnameentry.grid(row=3 ,column=1,padx=10,pady=10)

Roomnumber = Label(win,text="Room Number :")
Roomnumber.grid(row=4,column=0 ,sticky="w",padx=10,pady=10)


Roomnumberentry =Entry(win)
Roomnumberentry.grid(row=4,column=1,padx=10,pady=10)

Month =Label(win,text="Date of payment received:")
Month.grid(row=5,column=0 ,sticky="w",padx=10,pady=10)

Monthentry =Entry(win)
Monthentry.grid(row=5,column=1,padx=10,pady=10)

Monthentry.bind("<Button-1>", fill_current_date)
Monthentry.bind("<ButtonRelease-1>", fill_current_date)


AmountPaid =Label(win,text="FEE Received:")
AmountPaid.grid(row=6,column=0,sticky="w",padx=10,pady=10)

AmountPaidentry =Entry(win)
AmountPaidentry.grid(row=6,column=1,padx=10,pady=10)

icon_image = Image.open("searchicon.png")
icon_image = icon_image.resize((16, 16))  
search_icon = ImageTk.PhotoImage(icon_image)

search_button = Button(win, text="Search", bg="#00C8D8",fg="white",image=search_icon, borderless=1,compound="left")
search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')

save_btn = Button(win, text="Save", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=onclick)
save_btn.place(x=20,y=350)

back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 14 bold",borderless=1)
back_btn.place(x=143,y=350)

win.mainloop()