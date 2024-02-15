from tkinter import*
import tkinter as tk 
from tkinter import ttk
from tkmacosx import Button
from tkinter import messagebox
from PIL import Image, ImageTk
import menu

def manage_staffpg():
    
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


    def onclick():
        if validate_entries():
            tk.messagebox.showinfo("", "Staff successfully registered!")

    def validate_entries():
        # Validate each entry before submitting the form
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
        # Validate phone number to have 10 digits and be a positive number
        return value.isdigit() and len(value) == 10 and int(value) > 0

    def validate_price(value):
        return value.isdigit() and float(value) >=0

    # popup message for delete and update button
    def delete_confirmation():
        result = tk.messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this staff?")
        if result:
            confirm_popup()

    def confirm_popup():
        confirm_result = tk.messagebox.askyesno("Confirmation", "Do you really want to delete this staff?")
        if confirm_result:
            tk.messagebox.showinfo("Delete Successful", "Staff deleted successfully.")
        else:
            tk.messagebox.showinfo("Deletion Canceled", "Staff deletion canceled.")

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))  
    search_icon = ImageTk.PhotoImage(icon_image)


    search_button = Button(win, text="Search", bg="#00C8D8",fg="white",font="verdana 14",image=search_icon, compound="left")
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
    post.grid(row=6,column=0,sticky="w",padx=10,pady=10)
                
    post_entry=  ttk.Combobox(win,values=["Cleaner","Cook","warden","security guard"] )
    post_entry.grid(row=6,column=1)

    salary= Label(win, text="Salary:")
    salary.grid(row=7,column=0,sticky="w",padx=10,pady=10)

    salary_entry=Entry(win,width=22)
    salary_entry.grid(row=7,column=1)

    update_btn = Button(win, text="Update", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=onclick)
    update_btn.grid(row=8, column=0,  sticky="w",padx=10,pady=10)

    delete_btn = Button(win, text="Delete", bg="red",font="verdana 14 bold",borderless=1,command=delete_confirmation)
    delete_btn.grid(row=8, column=1, sticky="w",padx=10,pady=10)

    close_btn = Button(win, text="Back", bg="pink",fg="black",font="verdana 13 bold",borderless=1,command=menupg)
    close_btn.grid(row=8, column=3,  sticky="e",padx=10)

    win.mainloop()


if  __name__ == "__main__":
    manage_staffpg()