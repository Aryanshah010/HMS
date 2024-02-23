from tkinter import*
import tkinter as tk 
from tkinter import ttk
from tkmacosx import Button
from tkinter import messagebox
from PIL import Image, ImageTk
import menu
import sqlite3

def manage_staffpg():

    def onclick_update():

        if validate_entries():
            try:
                conn = sqlite3.connect("hostel.db")
                c = conn.cursor()

                # Get the current phone number from the entry field
                current_phone_number = phone_entry.get()

                # Check if the staff with the provided phone number exists
                c.execute("SELECT * FROM Staff WHERE Phone_Number = ?", (current_phone_number,))
                existing_staff = c.fetchone()

                if existing_staff:

                    new_phone_number = phone_entry.get()
                    First_Name = firstname_entry.get().capitalize()
                    Middle_Name = middlename_entry.get().capitalize()
                    Last_Name = lastname_entry.get().capitalize()
                    Address = address_entry.get().capitalize()
                    Post = post_entry.get()
                    Salary = int(salary_entry.get())

                    # Update the record in the database
                    c.execute('''UPDATE Staff SET First_Name=?, Middle_Name=?, Last_Name=?, Address=?, 
                                Post=?, Salary=?, Phone_Number=? WHERE Phone_Number=?''',
                                (First_Name, Middle_Name, Last_Name, Address, Post, Salary,
                                new_phone_number, current_phone_number))

                    conn.commit()
                    conn.close()

                    o=messagebox.showinfo("", "Staff record updated successfully!")
                    if o:
                        menupg()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def onclick_delete():

        phone_number = phone_entry.get()
        
        # Check if the phone number field is empty
        if not phone_number:
            messagebox.showerror("Error", "Please enter a phone number to search.")
            return
        
        staff_details = get_staff_details_from_db(phone_number)
        
        # Check if staff details are fetched successfully
        if not staff_details:
            messagebox.showerror("Error", "Staff not found with the provided phone number!")
            return
        
        result = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this staff?")
        if result:
            try:
                conn = sqlite3.connect("hostel.db")
                c = conn.cursor()

                # Delete the record from the database
                c.execute("DELETE FROM Staff WHERE Phone_Number = ?", (phone_number,))
                conn.commit()
                conn.close()

                ok=messagebox.showinfo("Delete Successful", "Staff record deleted successfully.")
                if ok:
                    menupg()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def search_staff():

        phone_number = phone_entry.get()

        if phone_number:
            staff_details = get_staff_details_from_db(phone_number)
            if staff_details:
                fill_entry_fields(staff_details)
            else:
                messagebox.showerror("Error", "Staff not found with the provided phone number!")
        else:
            messagebox.showerror("Error", "Please enter a phone number to search!")

    def get_staff_details_from_db(phone_number):
        try:
            connection = sqlite3.connect('hostel.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Staff WHERE Phone_Number = ?", (phone_number,))
            staff_details = cursor.fetchone()
            return staff_details
        except sqlite3.Error as error:
            print("Error fetching staff details:", error)
            return None
        finally:
            if connection:
                connection.close()

    def fill_entry_fields(details):

        firstname_entry.delete(0, END)
        middlename_entry.delete(0, END)
        lastname_entry.delete(0, END)
        address_entry.delete(0, END)
        post_entry.set('')
        salary_entry.delete(0, END)

        firstname_entry.insert(0, details[0])  
        middlename_entry.insert(0, details[1])  
        lastname_entry.insert(0, details[2])    
        address_entry.insert(0, details[4])    
        post_entry.set(details[6])              
        salary_entry.insert(0, details[7])       


    
    def menupg():
        win.destroy()
        menu.dashboard()

    win=tk.Tk()
    win.title("UPDATE/DELETE STAFF")
    win.resizable(0,0)

    window_width = 475
    window_height = 370

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def validate_entries():
        validations = [
            (phone_entry.get(), "Phone number", validate_phone_number),
            (firstname_entry.get(), "First name", validate_non_empty),
            (lastname_entry.get(), "Last name", validate_non_empty),
            (address_entry.get(), "Address", validate_non_empty),
            (post_entry.get(), "Post", validate_non_empty),
            (salary_entry.get(), "Salary", validate_price),        
        ]
        for value, entry_name, validation_func in validations:
            if not validation_func(value):
                messagebox.showerror("Validation Error", f"{entry_name} is not valid or its empty.")
                return False
        return True

    def validate_non_empty(value):
        return bool(value.strip())

    def validate_str(value):
        return str(value)

    def validate_phone_number(value):
        return value.isdigit() and len(value) == 10 and int(value) > 0

    def validate_price(value):
        return value.isdigit() and float(value) >=0

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))  
    search_icon = ImageTk.PhotoImage(icon_image)


    search_button = Button(win, text="Search", bg="#00C8D8",fg="white",font="verdana 14",image=search_icon, compound="left", command=search_staff)
    search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')


    firstname=Label(win, text="First name:")
    firstname.grid(row=1,column=0,sticky="w",padx=10,pady=10)

    firstname_entry=Entry(win,width=22)
    firstname_entry.grid(row=1,column=1)

    middlename=Label(win, text="Middle Name:")
    middlename.grid(row=2,column=0,sticky="w",padx=10,pady=10)

    middlename_entry= Entry(win,width=22)
    middlename_entry.grid(row=2,column=1)

    lastname= Label(win, text="Last Name:")
    lastname.grid(row=3,column=0,sticky="w",padx=10,pady=10)

    lastname_entry= Entry(win,width=22)
    lastname_entry.grid(row=3,column=1)


    phone= Label(win, text="Phone:")
    phone.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    phone_entry= Entry(win,width=22)
    phone_entry.grid(row=0,column=1)

    address= Label(win, text="Address:")
    address.grid(row=4,column=0,sticky="w",padx=10,pady=10)

    address_entry= Entry(win,width=22)
    address_entry.grid(row=4,column=1)

    post= Label(win, text="Post:")
    post.grid(row=5,column=0,sticky="w",padx=10,pady=10)
                
    post_entry=  ttk.Combobox(win,values=["Cleaner","Cook","warden","security guard"] )
    post_entry.grid(row=5,column=1)

    salary= Label(win, text="Salary:")
    salary.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    salary_entry=Entry(win,width=22)
    salary_entry.grid(row=6,column=1)

    update_btn = Button(win, text="Update", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=onclick_update)
    update_btn.grid(row=7, column=0,  sticky="w",padx=10,pady=10)

    delete_btn = Button(win, text="Delete", bg="red",font="verdana 14 bold",borderless=1,command=onclick_delete)
    delete_btn.grid(row=7, column=1, sticky="w",padx=10,pady=10)

    close_btn = Button(win, text="Back", bg="pink",fg="black",font="verdana 13 bold",borderless=1,command=menupg)
    close_btn.grid(row=7, column=3,  sticky="e",padx=10)

    win.mainloop()


if  __name__ == "__main__":
    manage_staffpg()

