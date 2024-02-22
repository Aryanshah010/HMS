from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
import datetime 
import menu
import sqlite3

def std_regpg():
    
    def menupg():
        window.destroy()
        menu.dashboard()

    window=tk.Tk()
    window.title("STUDENT REGISTRATION")
    window.resizable(0,0)

    window_width = 450
    window_height = 680

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    def onclick():
        
        if validate_entries():
            try:
          
                conn = sqlite3.connect('hostel.db')
                cursor = conn.cursor()

                Room_type=v.get()


                # Create Students table if it doesn't exist
                cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                                    std_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Date_of_Admission TEXT,
                                    First_Name TEXT,
                                    Middle_Name TEXT,
                                    Last_Name TEXT,
                                    Phone_Number TEXT,
                                    Address TEXT,
                                    Building TEXT,
                                    Room_No INTEGER,
                                    Room_type TEXT,
                                    Total_Fees REAL,
                                    Guardian_First_Name TEXT,
                                    Guardian_Middle_Name TEXT,
                                    Guardian_Last_Name TEXT,
                                    Guardian_Phone_Number TEXT,
                                    Guardian_Address TEXT
                                )''')

                # Extract values from Tkinter widgets
                
                date = date_value.get()
                first_name = std_first_entry.get().capitalize()
                middle_name = std_middle_entry.get().capitalize()
                last_name = std_last_entry.get().capitalize()
                phone_number = std_phone_entry.get()
                address = std_address_entry.get().capitalize()
                building_val = building.get()
                room_no = room_entry.get()
                total_fees = room_price_entry.get()
                guardian_first_name = guardian_first_entry.get().capitalize()
                guardian_middle_name = guardian_middle_entry.get().capitalize()
                guardian_last_name = guardian_last_entry.get().capitalize()
                guardian_phone_number = guardian_phone_entry.get()
                guardian_address = guardian_address_entry.get().capitalize()

                # Insert values into the Students table
                cursor.execute('''INSERT INTO Students (Date_of_Admission, First_Name, Middle_Name, Last_Name, 
                                                        Phone_Number, Address, Building, Room_No,Room_type, Total_Fees, 
                                                        Guardian_First_Name, Guardian_Middle_Name, Guardian_Last_Name, 
                                                        Guardian_Phone_Number, Guardian_Address) 
                                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''',
                            ( date, first_name, middle_name, last_name, phone_number, address,
                                building_val, room_no,Room_type, total_fees, guardian_first_name, guardian_middle_name,
                                guardian_last_name, guardian_phone_number, guardian_address))
                
                conn.commit()
                conn.close()

                r=tk.messagebox.showinfo("", "Student successfully registered!")
                if r:
                    menupg()

            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

    def fetch_max_std_id():
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()

            # Check if the Students table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Students'")
            table_exists = cursor.fetchone()

            if table_exists:
                # Students table exists, fetch the maximum std_id
                cursor.execute("SELECT MAX(std_id) FROM Students")
                max_id = cursor.fetchone()[0]  # Fetch the maximum std_id
                conn.close()
                return max_id if max_id else 0  # Return the maximum std_id or 0 if no records exist
            else:
                # Students table does not exist, return 0
                conn.close()
                return 0

        except Exception as e:
            tk.messagebox.showerror("Error", str(e))
            return 0
        
    default_std_id = fetch_max_std_id() + 1

    def validate_entries():
        # Validate each entry before submitting the form
        validations = [
            (std_id_entry.get(), "Registration ID", validate_non_empty),
            (date_value.get(), "Date", validate_non_empty),
            (std_first_entry.get(), "First Name", validate_non_empty),
            (std_last_entry.get(), "Last Name", validate_non_empty),
            (std_phone_entry.get(), "Phone Number", validate_phone_number),
            (std_address_entry.get(), "Address", validate_non_empty),
            (building.get(), "Building", validate_non_empty),
            (room_entry.get(), "Room No", validate_non_empty),
            (room_price_entry.get(), "Total Fees", validate_price),
            (guardian_first_entry.get(), "Guardian First Name", validate_non_empty),
            (guardian_last_entry.get(), "Guardian Last Name", validate_non_empty),
            (guardian_phone_entry.get(), "Guardian Phone Number", validate_phone_number),
            (guardian_address_entry.get(), "Guardian Address", validate_non_empty)
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
        return value.isdigit() and int(value) >=0

    # Registration Frame
    std_registration_frame=LabelFrame(window,text="REGISTRATION ID")
    std_registration_frame.grid(row=0,column=0,padx=10,pady=10,sticky='w')

    std_id=Label(std_registration_frame,text="S-ID:")
    std_id.grid(row=0,column=0)

    std_id_entry=Entry(std_registration_frame)
    std_id_entry.grid(row=0,column=1)
    std_id_entry.insert(0, default_std_id)
    
    def on_id_change(event):
        # Display an error message if user tries to change the std_id
        tk.messagebox.showerror("Error", "Cannot modify S-ID field.")
        std_id_entry.delete(0, 'end')
        std_id_entry.insert(0, default_std_id)


    std_id_entry.bind("<FocusIn>", on_id_change)
    
    
    date_label=Label(std_registration_frame,text="Date:")
    date_label.grid(row=1,column=0,pady=3)

    date_value = Entry(std_registration_frame)
    date_value.grid(row=1, column=1)

    # Automatically fill current date when the entry box is clicked or tapped
    def fill_current_date(event):
        current_date = datetime.datetime.now().strftime("%Y/%m/%d")
        date_value.delete(0, END)
        date_value.insert(0, current_date)

    date_value.bind("<Button-1>", fill_current_date)
    date_value.bind("<ButtonRelease-1>", fill_current_date)

    # Room Type Frame
    room_frame=LabelFrame(window,text="Room Type")
    room_frame.grid(row=0,column=1,sticky="w",padx=10,pady=10)

    v = StringVar(room_frame, "1") 

    values = {"1 bed" : "1", 
            "2 beds " : "2", 
            "3 beds" : "3", 
            "4 beds" : "4"} 
            
    for (text, value) in values.items(): 
        Radiobutton(room_frame, text = text, variable = v, 
            value = value).grid(sticky="w") 
        

    # student Frame
        
    std_info=LabelFrame(window,text="STUDENT INFO")
    std_info.grid(row=1,column=0,padx=10,pady=10,sticky='w')

    std_first=Label(std_info,text="First Name:")
    std_first.grid(row=0,column=0,sticky="w")

    std_first_entry=Entry(std_info)
    std_first_entry.grid(row=0,column=1)

    std_middle=Label(std_info,text="Middle Name:")
    std_middle.grid(row=1,column=0,sticky="w")

    std_middle_entry=Entry(std_info)
    std_middle_entry.grid(row=1,column=1)

    std_last=Label(std_info,text="Last Name:")
    std_last.grid(row=2,column=0,sticky="w")

    std_last_entry=Entry(std_info)
    std_last_entry.grid(row=2,column=1)

    std_phone=Label(std_info,text="Phone Number:")
    std_phone.grid(row=3,column=0,sticky="w")

    std_phone_entry=Entry(std_info)
    std_phone_entry.grid(row=3,column=1)

    std_address=Label(std_info,text="Address:")
    std_address.grid(row=4,column=0,sticky="w")

    std_address_entry=Entry(std_info)
    std_address_entry.grid(row=4,column=1)

    # Guardian info

    guardian_info=LabelFrame(window,text="GUARDIAN INFO")
    guardian_info.grid(row=2,column=0,padx=10,pady=10,sticky='w')

    guardian_first=Label(guardian_info,text="First Name:")
    guardian_first.grid(row=0,column=0,sticky="w")

    guardian_first_entry=Entry(guardian_info)
    guardian_first_entry.grid(row=0,column=1)

    guardian_middle=Label(guardian_info,text="Middle Name:")
    guardian_middle.grid(row=1,column=0,sticky="w")

    guardian_middle_entry=Entry(guardian_info)
    guardian_middle_entry.grid(row=1,column=1)

    guardian_last=Label(guardian_info,text="Last Name:")
    guardian_last.grid(row=2,column=0,sticky="w")

    guardian_last_entry=Entry(guardian_info)
    guardian_last_entry.grid(row=2,column=1)

    guardian_phone=Label(guardian_info,text="Phone Number:")
    guardian_phone.grid(row=3,column=0,sticky="w")

    guardian_phone_entry=Entry(guardian_info)
    guardian_phone_entry.grid(row=3,column=1)

    guardian_address=Label(guardian_info,text="Address:")
    guardian_address.grid(row=4,column=0,sticky="w")

    guardian_address_entry=Entry(guardian_info)
    guardian_address_entry.grid(row=4,column=1)

    # Room allocation

    room_all=LabelFrame(window,text="ROOM ALLOCATION")
    room_all.grid(row=3,column=0,sticky="w",padx=10,pady=10)

    building_label=Label(room_all,text="Building:")
    building_label.grid(row=0,column=0,sticky="w")

    building=ttk.Combobox(room_all,values=["A","B","C","D","E","F"])
    building.grid(row=0,column=1)

    room_num=Label(room_all,text="Room No:")
    room_num.grid(row=1,column=0,sticky="w")

    room_entry=Spinbox(room_all,from_=1,to=150)
    room_entry.grid(row=1,column=1)


    room_price=Label(room_all,text="Total Fees:")
    room_price.grid(row=2,column=0,sticky="w")

    room_price_entry=Entry(room_all,width=22)
    room_price_entry.grid(row=2,column=1)

    create_btn = Button(window, text="Create", bg="#00FFFF",font=("verdana 15 bold"),borderless=1,command=onclick)
    create_btn.place(x=16,y=640)

    close_btn = Button(window, text="Back", bg="#FF7F24",font=("verdana 15 bold"),borderless=1,command=menupg)
    close_btn.place(x=150,y=640)


    window.mainloop() 


if  __name__ == "__main__":
    std_regpg()





















































    

