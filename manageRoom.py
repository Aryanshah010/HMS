from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button
from tkinter import ttk
import menu
import sqlite3

def manage_roompg():

    def menupg():
        window.destroy()
        menu.dashboard()

    def validate_entries():
        # Check if any of the fields are empty
        if not room_num_entry.get() or not building.get() or not total_fees_entry.get():
            messagebox.showerror("Validation Error", "Please fill in all the fields.")
            return False

        # Check if room number is a positive integer
        try:
            room_number = int(room_num_entry.get())
            if room_number <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("", "Room number must be a positive integer.")
            return False

        # Check if total fees is a positive integer
        try:
            total_fees = int(total_fees_entry.get())
            if total_fees < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("", "Please enter a valid fee amount.")
            return False

        return True

    
    def create_rooms_table():

        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            room_number INTEGER,
                            building TEXT,
                            beds TEXT,
                            room_status TEXT,
                            total_fees INTEGER
                        )''')
        conn.commit()
        conn.close()

    create_rooms_table()

    def fetch_last_room_number():

        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(room_number) FROM Rooms")
        last_room_number = cursor.fetchone()[0]
        conn.close()
        return last_room_number + 1 if last_room_number else 1
    
    def insert_room_details(room_number, building, beds, room_status, total_fees):

        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Rooms (room_number, building, beds, room_status, total_fees)
                        VALUES (?, ?, ?, ?, ?)''', (room_number, building, beds, room_status, total_fees))
        conn.commit()
        conn.close()
        
    def create():

        if validate_entries():
            room_number = int(room_num_entry.get())
            building_val = building.get()
            room_type_val = v.get()
            room_status_val = val.get()
            total_fees_val = int(total_fees_entry.get())

            insert_room_details(room_number, building_val, room_type_val, room_status_val, total_fees_val)

            o=messagebox.askyesno("", "Do you want to create this room?")
            if o:
               k=messagebox.showinfo("","Room created successfully!")
               if k:
                   menupg()

    def update_room_status(room_number, room_status):

        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Rooms SET room_status = ? WHERE room_number = ?''', (room_status, room_number))
        conn.commit()
        conn.close()

    def delete_room(room_number):
        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Rooms WHERE room_number = ?''', (room_number,))
        conn.commit()
        conn.close()

    def update():
        room_number_str = update_room_num_entry.get()
        if not room_number_str:
            messagebox.showerror("Error", "Please enter a room number.")
            return

        try:
            room_number = int(room_number_str)
            if room_number <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Room number must be a positive integer.")
            return

        if is_room_registered(room_number):
            room_status_val = val.get()
            update_room_status(room_number, room_status_val)
            z = messagebox.askyesno("", "Do you want to update room status of this room?")
            if z:
                v = messagebox.showinfo("", "Room status updated successfully!")
                if v:
                    menupg()
        else:
            messagebox.showerror("Error", f"Room number {room_number} does not exist.")
    
    def is_room_registered(room_number):
        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Rooms WHERE room_number = ?", (room_number,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
    
    def delete():
            room_number_str = update_room_num_entry.get()
            if not room_number_str:
                messagebox.showerror("Error", "Please enter a room number.")
                return

            try:
                room_number = int(room_number_str)
                if room_number <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Room number must be a positive integer.")
                return

            if is_room_registered(room_number):
                result = messagebox.askyesno("", f"Are you sure you want to delete room {room_number}?")
                if result:
                    delete_room(room_number)
                    l = messagebox.showinfo("", f"Room {room_number} deleted successfully.")
                    if l:
                        menupg()
            else:
                messagebox.showerror("Error", f"Room number {room_number} does not exist.")
            


    window=tk.Tk()
    window.title("Manage Room")
    window.resizable(0,0)
    window_width = 400
    window_height = 650

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


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

    create_btn = Button(new_room_frame, text="Create", bg="#00FFFF",font="verdana 13 bold",borderless=1,command=create)
    create_btn.grid(row=5, column=0, sticky="w",padx=10,pady=10)

    Update_delete_frame=LabelFrame(window,text="Update/Delete Room")
    Update_delete_frame.grid(row=1,column=0,sticky="w",padx=10,pady=10)

    room_num_label=Label(Update_delete_frame,text="Room No:")
    room_num_label.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    update_room_num_entry=Entry(Update_delete_frame,width=21)
    update_room_num_entry.grid(row=0,column=1)

    room_status=LabelFrame(Update_delete_frame,text="Room Status")
    room_status.grid(row=1,column=0,sticky="w",padx=10,pady=10)

    val=StringVar(room_status,"Unbooked")

    values={"Booked":"Booked",
            "Unbooked":"Unbooked",
            "Semi-Booked":"Semi-Booked"}

    for (text,value) in values.items():
        Radiobutton(room_status,text=text,variable=val,value=value).grid(sticky="w")
        

    update_btn = Button(Update_delete_frame, text="Update", bg="#FF7F24",font="verdana 13 bold",borderless=1,command=update)
    update_btn.grid(row=2, column=0,  sticky="w",padx=10,pady=10)

    delete_btn = Button(Update_delete_frame, text="Delete", bg="red",font="verdana 13 bold",borderless=1,command=delete)
    delete_btn.grid(row=2, column=1, sticky="w",padx=10,pady=10)


    back_btn=Button(window,text="Back",bg="#DA00D6",font="verdana 15 bold",command=menupg)
    back_btn.place(x=10,y=600)

    last_room_number = fetch_last_room_number()
    room_num_entry.insert(0, last_room_number)

    window.mainloop()


if  __name__ == "__main__":
    manage_roompg()