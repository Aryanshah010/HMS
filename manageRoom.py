from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button
from tkinter import ttk

def onclick():
     tk.messagebox.showinfo("","Room created successfully!")
def onclicked():
     tk.messagebox.showinfo("","Room updated successfully!")

def delete_confirmation():
    result = tk.messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this room?")
    if result:
        confirm_popup()

def confirm_popup():
    confirm_result = tk.messagebox.askyesno("Confirmation", "Do you really want to delete this room?")
    if confirm_result:
        tk.messagebox.showinfo("Delete Successful", "Room deleted successfully.")
    else:
        tk.messagebox.showinfo("Deletion Canceled", "Room deletion canceled.")
	

window=tk.Tk()
window.title("Manage Room")
window.geometry("400x600")
window.resizable(0,0)

new_room_frame=LabelFrame(window,text="REGISTER NEW ROOM")
new_room_frame.grid(row=0,column=0,padx=10,pady=10)

room_num_label=Label(new_room_frame,text="Room No:")
room_num_label.grid(row=0,column=0,sticky="w",padx=10,pady=10)

room_num_entry=Entry(new_room_frame,width=21)
room_num_entry.grid(row=0,column=1)

building_label=Label(new_room_frame,text="Building:")
building_label.grid(row=1,column=0,sticky="w",padx=10,pady=10)

building=ttk.Combobox(new_room_frame,values=["A","B","C","D","E","F"])
building.grid(row=1,column=1)

	
total_fees=Label(new_room_frame,text="Total Fees:")
total_fees.grid(row=2,column=0,sticky="w",padx=10,pady=10)

total_fees_entry=Entry(new_room_frame,width=21)
total_fees_entry.grid(row=2,column=1)


room_type=LabelFrame(new_room_frame,text="ROOM TYPE")
room_type.grid(row=3,column=0,sticky="w",padx=10,pady=10)

v= StringVar(room_type, "0") 

values = {"1 Bed" : "1", 
		"2 Beds " : "2", 
		"3 Beds" : "3", 
		"4 Beds" : "4"} 
		 
for (text, value) in values.items(): 
	Radiobutton(room_type, text = text, variable = v, 
		value = value).grid(sticky="w") 

create_btn = Button(new_room_frame, text="Create", bg="#00FFFF",font="verdana 13 bold",borderless=1,command=onclick)
create_btn.grid(row=5, column=0, sticky="w",padx=10,pady=10)

Update_delete_frame=LabelFrame(window,text="Update/Delete Room")
Update_delete_frame.grid(row=1,column=0,sticky="w",padx=10,pady=10)

room_num_label=Label(Update_delete_frame,text="Room No:")
room_num_label.grid(row=0,column=0,sticky="w",padx=10,pady=10)

room_num_entry=Entry(Update_delete_frame,width=21)
room_num_entry.grid(row=0,column=1)

room_status=LabelFrame(Update_delete_frame,text="Room Status")
room_status.grid(row=1,column=0,sticky="w",padx=10,pady=10)

val=StringVar(room_status,"0")

values={"Booked":"1",
		"Unbooked":"2"}

for (text,value) in values.items():
	Radiobutton(room_status,text=text,variable=val,value=value).grid(sticky="w")
	

update_btn = Button(Update_delete_frame, text="Update", bg="#FF7F24",font="verdana 13 bold",borderless=1,command=onclicked)
update_btn.grid(row=2, column=0,  sticky="w",padx=10,pady=10)

delete_btn = Button(Update_delete_frame, text="Delete", bg="red",font="verdana 13 bold",borderless=1,command=delete_confirmation)
delete_btn.grid(row=2, column=1, sticky="w",padx=10,pady=10)


back_btn=Button(window,text="Back",bg="#DA00D6",font="verdana 15 bold")
back_btn.place(x=10,y=565)

window.mainloop()