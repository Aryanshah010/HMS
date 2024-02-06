from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
from PIL import Image, ImageTk
import re

# popup message for delete and update button
def delete_confirmation():
    result = tk.messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this student?")
    if result:
        confirm_popup()

def confirm_popup():
    confirm_result = tk.messagebox.askyesno("Confirmation", "Do you really want to delete this student?")
    if confirm_result:
        tk.messagebox.showinfo("Delete Successful", "Student deleted successfully.")
    else:
        tk.messagebox.showinfo("Deletion Canceled", "Student deletion canceled.")

def click():
    
    tk.messagebox.showinfo("Update", "Student info is updated successfully!")


window=tk.Tk()
window.title("Update/Delete Student")
window.geometry("475x420")
window.resizable(0,0)

std_id=Label(window,text="S-ID:")
std_id.grid(row=0,column=0,sticky="w",padx=10,pady=10)

std_id_entry=Entry(window,width=22)
std_id_entry.grid(row=0,column=1)

# search Button with icon

icon_image = Image.open("searchicon.png")
icon_image = icon_image.resize((16, 16))  
search_icon = ImageTk.PhotoImage(icon_image)

search_button = Button(window, text="Search", bg="#00C8D8",fg="white",image=search_icon, compound="left")
search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')


phone_label=Label(window,text="Phone:")
phone_label.grid(row=1,column=0,sticky="w",padx=10,pady=10)

phone_label_entry=Entry(window,width=22)
phone_label_entry.grid(row=1,column=1)

std_first=Label(window,text="First Name:")
std_first.grid(row=2,column=0,sticky="w",padx=10,pady=10)

std_first_entry=Entry(window,width=22)
std_first_entry.grid(row=2,column=1)

std_middle=Label(window,text="Middle Name:")
std_middle.grid(row=3,column=0,sticky="w",padx=10,pady=10)

std_middle_entry=Entry(window,width=22)
std_middle_entry.grid(row=3,column=1)

std_last=Label(window,text="Last Name:")
std_last.grid(row=4,column=0,sticky="w",padx=10,pady=10)

std_last_entry=Entry(window,width=22)
std_last_entry.grid(row=4,column=1)

building_label=Label(window,text="Building:")
building_label.grid(row=5,column=0,sticky="w",padx=10,pady=10)

building=ttk.Combobox(window,width=21,values=["A","B","C","D","E","F"])
building.grid(row=5,column=1)

room_num=Label(window,text="Room No:")
room_num.grid(row=6,column=0,sticky="w",padx=10,pady=10)

room_num_entry=Entry(window,width=22)
room_num_entry.grid(row=6,column=1)

room_price=Label(window,text="Total Fees:")
room_price.grid(row=7,column=0,sticky="w",padx=10,pady=10)

room_price_entry=Entry(window,width=22)
room_price_entry.grid(row=7,column=1)

update_btn = Button(window, text="Update", bg="#FF7F24",font="vardana 15 bold",borderless=1,command=click)
update_btn.grid(row=8, column=0,  sticky="w",padx=10,pady=10)

delete_btn = Button(window, text="delete", bg="red",font="vardana 15 bold",command=delete_confirmation)
delete_btn.grid(row=8, column=1, sticky="w",padx=10,pady=10)

close_btn = Button(window, text="Back", bg="pink",fg="black",font="vardana 13 bold",borderless=1)
close_btn.grid(row=8, column=3,  sticky="e",padx=10)

window.mainloop()


