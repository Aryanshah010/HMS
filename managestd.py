from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
from PIL import Image, ImageTk
import menu
import sqlite3


def manage_stdpg():
   

    def menupg():
        window.destroy()
        menu.dashboard()

    def validate_entries():
        validations = [
            (std_id_entry.get(), "S-ID", validate_std),
            (phone_label_entry.get(), "Phone", validate_phone_number),
            (std_first_entry.get(), "First name", validate_non_empty),
            (std_last_entry.get(), "Last name", validate_non_empty),
            (std_address_entry.get(),"Address",validate_non_empty),
            (building.get(), "Building", validate_non_empty),
            (room_num_entry.get(), "Room number", validate_room),
            (room_price_entry.get(), "Total fees", validate_price),
            
        ]

        for value, entry_name, validation_func in validations:
            if not validation_func(value):
                messagebox.showerror("Validation Error", f"{entry_name} is not valid or its empty.")
                return False

        return True

    def validate_non_empty(value):
        return bool(value.strip())

    def validate_room(value):
        return value.isdigit() and int(value)>=0

    def validate_std(value):
        return value.isdigit() and int(value)>=0

    def validate_phone_number(value):
        # Validate phone number to have 10 digits and be a positive number
        return value.isdigit() and len(value) == 10 and int(value) > 0

    def validate_price(value):
        return value.isdigit() and int(value) >=0

    # popup message for delete and update button
    def delete_confirmation():

        s_id=std_id_entry.get()

        if not s_id:
            messagebox.showerror(" ", "Please enter s-id to search.")
            return
        std_details = get_std_details_from_db(s_id)
        
        # Check if staff details are fetched successfully
        if not std_details:
            messagebox.showerror(" ", "Student not found with the provided s-id!")
            return

        result = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this student?")
        if result:
            try:
                conn = sqlite3.connect("hostel.db")
                c = conn.cursor()

                # Delete the record from the database
                c.execute("DELETE FROM Students WHERE std_id = ?", (s_id,))
                conn.commit()
                conn.close()

                ok=messagebox.showinfo(" ","Student record deleted successfully.")
                if ok:
                    menupg()

            except Exception as e:
                 messagebox.showerror("Error", str(e))

    def click_update():

        if validate_entries():

            try:
                conn = sqlite3.connect("hostel.db")
                c = conn.cursor()

                current_student_id=std_id_entry.get()

                c.execute("SELECT * FROM Students WHERE std_id = ?", (current_student_id,))
                existing_std= c.fetchone()

                if existing_std:

                    s_id=std_id_entry.get()
                    phone=phone_label_entry.get()
                    first_name=std_first_entry.get().capitalize()
                    middle_name=std_middle_entry.get().capitalize()
                    last_name=std_last_entry.get().capitalize()
                    address=std_address_entry.get().capitalize()
                    Building=building.get()
                    room=room_num_entry.get()
                    roomprice=int(room_price_entry.get())


                    c.execute('''UPDATE Students SET Phone_Number=?, First_Name=?, Middle_Name=?, Last_Name=?,Address=?,Building=?,Room_No=?,
                                Total_Fees=? WHERE std_id=?''',
                                (phone,first_name,middle_name,last_name,address,Building,room,roomprice,s_id))

                    conn.commit()
                    conn.close()

                    o=messagebox.askyesno(" ", "Do you want to update the data of this student?")
                    if o:
                        r=messagebox.showinfo("","Student updated successfully!")
                        if r:
                            menupg()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    
    def search_std():

        s_id=std_id_entry.get()

        if s_id:
            std_details = get_std_details_from_db(s_id)
            if std_details:
                fill_entry_fields(std_details)
            else:
                messagebox.showerror(" ","Student not found with the provided s-id!")
        else:
            messagebox.showerror(" ","Please enter S-ID to search!")

    def get_std_details_from_db(s_id):

        try:
            connection = sqlite3.connect('hostel.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students WHERE std_id = ?", (s_id,))
            std_details = cursor.fetchone()
            return std_details
        
        except sqlite3.Error as error:
            print("Error fetching student details:", error)
            return None
        
        finally:
            if connection:
                connection.close()

    def fill_entry_fields(details):

        std_first_entry.delete(0, END)
        std_middle_entry.delete(0, END)
        std_last_entry.delete(0, END)
        std_address_entry.delete(0, END)
        phone_label_entry.delete(0,END)
        building.delete(0,END)
        room_num_entry.delete(0,END)
        room_price_entry.delete(0,END)


        phone_label_entry.insert(0, details[5])  
        std_first_entry.insert(0, details[2])  
        std_middle_entry.insert(0, details[3])    
        std_last_entry.insert(0, details[4])  
        std_address_entry.insert(0,details[6])  
        building.insert(0,details[7])              
        room_num_entry.insert(0, details[8])       
        room_price_entry.insert(0, int(details[10]))       

  
    window=tk.Tk()
    window.title("Update/Delete Student")
    window.resizable(0,0)
    window_width = 480
    window_height = 440

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    std_id=Label(window,text="S-ID:")
    std_id.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    std_id_entry=Entry(window,width=22)
    std_id_entry.grid(row=0,column=1)

    # search Button with icon

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))  
    search_icon = ImageTk.PhotoImage(icon_image)

    search_button = Button(window, text="Search", bg="#00C8D8",fg="white",font="verdana 14",image=search_icon, borderless=1, compound="left",command=search_std)
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

    std_address=Label(window,text="Address:")
    std_address.grid(row=5,column=0,sticky="w",padx=10,pady=10)

    std_address_entry=Entry(window,width=22)
    std_address_entry.grid(row=5,column=1)

    building_label=Label(window,text="Building:")
    building_label.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    building=ttk.Combobox(window,width=21,values=["A","B","C","D","E","F"])
    building.grid(row=6,column=1)

    room_num=Label(window,text="Room No:")
    room_num.grid(row=7,column=0,sticky="w",padx=10,pady=10)

    room_num_entry=Entry(window,width=22)
    room_num_entry.grid(row=7,column=1)

    room_price=Label(window,text="Total Fees:")
    room_price.grid(row=8,column=0,sticky="w",padx=10,pady=10)

    room_price_entry=Entry(window,width=22)
    room_price_entry.grid(row=8,column=1)

    update_btn = Button(window, text="Update", bg="#FF7F24",font="verdana 15 bold",borderless=1,command=click_update)
    update_btn.grid(row=9, column=0,  sticky="w",padx=10,pady=10)

    delete_btn = Button(window, text="Delete", bg="red",font="verdana 15 bold",borderless=1,command=delete_confirmation)
    delete_btn.grid(row=9, column=1, sticky="w",padx=10,pady=10)

    close_btn = Button(window, text="Back", bg="pink",fg="black",borderless=1,font="verdana 13 bold",command=menupg)
    close_btn.grid(row=9, column=3,  sticky="e",padx=10)

    window.mainloop()


if  __name__ == "__main__":
    manage_stdpg()
