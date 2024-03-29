from tkinter import*
import tkinter as tk 
from tkinter import ttk
from tkmacosx import Button
from tkinter import messagebox
import datetime
import menu
import sqlite3

def reg_staffpg():
   
    def menupg():
        win.destroy()
        menu.dashboard()

    win=tk.Tk()
    win.title("STAFF REGISTRATION")
    win.resizable(0,0)

    window_width = 400
    window_height = 400

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
            try:
                conn=sqlite3.connect("hostel.db")
                c=conn.cursor()

                c.execute('''CREATE TABLE IF NOT EXISTS Staff(
                          
                          First_Name TEXT,
                          Middle_Name TEXT,
                          Last_Name TEXT,
                          Phone_Number INTEGER PRIMARY KEY,
                          Address TEXT,
                          Date_of_join TEXT,
                          Post TEXT,
                          Salary INTEGER

                    )''')
                
                phone_number = phone_entry.get()
                c.execute("SELECT * FROM Staff WHERE Phone_Number = ?", (phone_number,))
                existing_staff = c.fetchone()
                if existing_staff:
                    messagebox.showerror("Error", "Staff with this phone number already exists.")
                    return
                
                First_Name=firstname_entry.get().capitalize()
                Middle_Name=middlename_entry.get().capitalize()
                Last_Name=lastname_entry.get().capitalize()
                Phone_Num=phone_entry.get()
                Address=address_entry.get().capitalize()
                Date_of_join=doj_entry.get()
                Post=post_entry.get().capitalize()
                Salary=int(salary_entry.get())


                c.execute('''INSERT INTO Staff( First_Name,Middle_Name,Last_Name,Phone_Number,Address,Date_of_join,
                          Post,Salary)

                          VALUES( ?, ?, ?, ?, ?, ?, ?,?)''',
                          (First_Name,Middle_Name,Last_Name,Phone_Num,Address,Date_of_join,Post,Salary))
                              
                conn.commit()
                conn.close()
                
                result=messagebox.showinfo("","Staff successfully registered!")
                if result:
                    menupg()

            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

    def validate_entries():
        # Validate each entry before submitting the form
        validations = [
            (firstname_entry.get(), "First name", validate_non_empty),
            (lastname_entry.get(), "Last name", validate_non_empty),
            (phone_entry.get(), "Phone", validate_phone_number),
            (address_entry.get(), "Address", validate_non_empty),
            (doj_entry.get(), "Date of join", validate_non_empty),
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

    def validate_phone_number(value):
        # Validate phone number to have 10 digits and be a positive number
        return value.isdigit() and len(value) == 10 and int(value) > 0

    def validate_price(value):
        return value.isdigit() and int(value) >=0

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

    save_btn = Button(win, text="Save", bg="#FF7F24",font="verdana 15 bold",borderless=1,command=onclick)
    save_btn.grid(row=8, column=0,  sticky="w",padx=10,pady=10)

    back_btn = Button(win, text="Back", bg="red",borderless=1,font="verdana 15 bold",command=menupg)
    back_btn.grid(row=8, column=1, sticky="w",padx=10,pady=10)


    win.mainloop()


if  __name__ == "__main__":
    reg_staffpg()
                          
                          
                          
                          
                        
                          
                          
                          

            

        



