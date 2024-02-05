from tkinter import*
import tkinter as tk 
from tkinter import ttk
from tkmacosx import Button
from tkinter import messagebox
import datetime


win=tk.Tk()
win.geometry("400x400")
win.title("Staff Registration")
win.resizable(0,0)

def onclick():
    if validate_entries():
        tk.messagebox.showinfo("", "Staff successfully registered!")

def validate_entries():
    # Validate each entry before submitting the form
    validations = [
        (firstname_entry.get(), "firstname", validate_non_empty),
        (lastname_entry.get(), "lastname", validate_non_empty),
        (phone_entry.get(), "phone", validate_phone_number),
        (address_entry.get(), "address", validate_non_empty),
        (doj_entry.get(), "Date of join", validate_non_empty),
        (post_entry.get(), "post", validate_non_empty),
        (salary_entry.get(), "Salary", validate_price),
        
    ]

    for value, entry_name, validation_func in validations:
        if not validation_func(value):
            messagebox.showerror("Validation Error", f"{entry_name} is not valid or its empty.")
            return False

    return True

def validate_non_empty(value):
    return bool(value.strip())

def validate_phone_number(value):
    # Validate phone number to have 10 digits and be a positive number
    return value.isdigit() and len(value) == 10 and int(value) > 0

def validate_price(value):
    return value.isdigit() and float(value) >=0

def fill_current_date(event):
    current_date = datetime.datetime.now().strftime("%Y/%m/%d")
    doj_entry.delete(0, END)
    doj_entry.insert(0, current_date)

firstname=Label(win, text="First name:")
firstname.grid(row=0,column=0,sticky="w",padx=10,pady=10)

firstname_entry=Entry(win,width=22)
firstname_entry.grid(row=0,column=1)

middlename=Label(win, text="Middle Name:")
middlename.grid(row=1,column=0,sticky="w",padx=10,pady=10)

middlename_entry= Entry(win,width=22)
middlename_entry.grid(row=1,column=1)

lastname= Label(win, text="Last Name:")
lastname.grid(row=2,column=0,sticky="w",padx=10,pady=10)

lastname_entry= Entry(win,width=22)
lastname_entry.grid(row=2,column=1)


phone= Label(win, text="Phone:")
phone.grid(row=3,column=0,sticky="w",padx=10,pady=10)

phone_entry= Entry(win,width=22)
phone_entry.grid(row=3,column=1)

address= Label(win, text="Address:")
address.grid(row=4,column=0,sticky="w",padx=10,pady=10)

address_entry= Entry(win,width=22)
address_entry.grid(row=4,column=1)

doj= Label(win, text="Date Of Join:")
doj.grid(row=5,column=0,sticky="w",padx=10,pady=10)

doj_entry = Entry(win,width=22)

doj_entry.grid(row=5,column=1)

doj_entry.bind("<Button-1>", fill_current_date)
doj_entry.bind("<ButtonRelease-1>", fill_current_date)

post= Label(win, text="Post:")
post.grid(row=6,column=0,sticky="w",padx=10,pady=10)
            
post_entry=  ttk.Combobox(win,values=["Cleaner","Cook","warden","security guard"] )
post_entry.grid(row=6,column=1)

salary= Label(win, text="Salary:")
salary.grid(row=7,column=0,sticky="w",padx=10,pady=10)

salary_entry=Entry(win,width=22)
salary_entry.grid(row=7,column=1)

save_btn = Button(win, text="Save", bg="#FF7F24",font="vardana 15 bold",borderless=1,command=onclick)
save_btn.grid(row=8, column=0,  sticky="w",padx=10,pady=10)

back_btn = Button(win, text="back", bg="red",font="vardana 15 bold")
back_btn.grid(row=8, column=1, sticky="w",padx=10,pady=10)


win.mainloop()