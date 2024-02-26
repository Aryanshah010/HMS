from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL  import Image , ImageTk
from tkmacosx import Button
import datetime
import menu
import sqlite3

def initialize_database():
    try:
        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Staff_Payments (
                        staff_payment_id INTEGER PRIMARY KEY,
                        Phone_Number INTEGER,
                        salary_date TEXT,
                        payment_amount INTEGER,
                        FOREIGN KEY (Phone_Number) REFERENCES Staff (Phone_Number)
                    )''')

        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def salarypg():
    initialize_database()

    def on_scroll(*args):
        date_amt_box.yview(*args)


    def search_staff():
        phoneNum=phone_entry.get()
        if not phoneNum:
            messagebox.showerror("Error", "Please enter a valid phone number.")
            return
        
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Staff WHERE Phone_Number=?", (phoneNum,))
            staff_data = cursor.fetchone()
            conn.close()

            if staff_data:
                Firstnameentry.delete(0, 'end')
                Firstnameentry.insert(0, staff_data[0])
                Middlenameentry.delete(0, 'end')
                Middlenameentry.insert(0, staff_data[1])
                Lastnameentry.delete(0, 'end')
                Lastnameentry.insert(0, staff_data[2])
                post_entry.delete(0,'end')
                post_entry.insert(0,staff_data[6])

                
                # Clear existing records in the treeview
                clear_treeview()

                # Load and display fee records for this student
                load_fee_records(phoneNum)
            else:
                messagebox.showerror("Error", "Staff not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    
    def clear_treeview():
        date_amt_box.delete(*date_amt_box.get_children())


    def load_fee_records(phoneNum):
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("SELECT salary_date, payment_amount FROM Staff_Payments  WHERE Phone_Number=?", (phoneNum,))
            fee_records = cursor.fetchall()
            conn.close()

            for record in fee_records:
                # Explicitly convert amount to integer and then to string
                amount_paid = str(int(record[1]))
                date_amt_box.insert("", "end", values=(record[0], amount_paid))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def menupg():
        win.destroy()
        menu.dashboard()

    def fill_current_date(event):
        current_date = datetime.datetime.now().strftime("%Y/%m/%d")
        Monthentry.delete(0, END)
        Monthentry.insert(0, current_date)


    def save():

        try:
            phoneNum=phone_entry.get()
            salary_date=Monthentry.get()
            amount=int(AmountPaidentry.get())

            if not phoneNum or not salary_date or not amount:
                    messagebox.showerror("", "Please fill in all fields.")
                    return
            if amount<=0:
                 messagebox.showerror("","Please enter valid amount")
                 return
            
            
            try:
                amount_paid = int(amount)
            except ValueError:
                    messagebox.showerror("Error", "Amount must be a valid integer.")
                    return
            
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Staff_Payments(phone_number, salary_date,payment_amount ) VALUES (?, ?, ?)", (phoneNum, salary_date, amount_paid))
            conn.commit()
            conn.close()
            
            date_amt_box.insert("", "end", values=(salary_date, amount_paid))

            y = messagebox.askyesno("", "Do you want to save the fee of this staff?")
            if y:
                    r = messagebox.showinfo("", "Staff fee saved successfully!")
                    if r:
                        menupg()
        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")


    win=tk.Tk()
    win.resizable(0,0)
    win.title("STAFF SALARY")

    window_width = 483
    window_height = 630

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    phone =Label(win,text="Phone Number:")
    phone.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    phone_entry=Entry(win)
    phone_entry.grid(row=0,column=1,padx=10,pady=10)


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

    post = Label(win,text="Post:")
    post.grid(row=4,column=0 ,sticky="w",padx=10,pady=10)


    post_entry =Entry(win)
    post_entry.grid(row=4,column=1,padx=10,pady=10)

    Month =Label(win,text="Date of payment:")
    Month.grid(row=5,column=0 ,sticky="w",padx=10,pady=10)

    Monthentry =Entry(win)
    Monthentry.grid(row=5,column=1,padx=10,pady=10)

    Monthentry.bind("<Button-1>", fill_current_date)
    Monthentry.bind("<ButtonRelease-1>", fill_current_date)


    AmountPaid =Label(win,text="Payment Amount:")
    AmountPaid.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    AmountPaidentry =Entry(win)
    AmountPaidentry.grid(row=6,column=1,padx=10,pady=10)

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))  
    search_icon = ImageTk.PhotoImage(icon_image)


    search_button = Button(win, text="Search", bg="#00C8D8",fg="white",font="verdana 14",image=search_icon, borderless=1,compound="left",command=search_staff)

    search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')

    save_btn = Button(win, text="Save", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=save)
    save_btn.place(x=20,y=350)

    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 14 bold",borderless=1,command=menupg)
    back_btn.place(x=143,y=350)


   # salary paid record
    date_amt_box = ttk.Treeview(win)
    # defining columns
    date_amt_box['columns'] = ("Date", "Amount")
    date_amt_box.column("#0", width=0, minwidth=0)  # Set width to 0 and stretch to NO
    date_amt_box.column("Date", anchor=CENTER, width=200, minwidth=250)
    date_amt_box.column("Amount", anchor=CENTER, width=200, minwidth=250)
    
    date_amt_box.heading("#0", text="", anchor=CENTER)
    date_amt_box.heading("Date", text="Date", anchor=CENTER)
    date_amt_box.heading("Amount", text="Amount", anchor=CENTER)
    
    # Place the salary paid record at the bottom
    date_amt_box.grid(row=7, column=0, columnspan=4, pady=60, sticky="nsew")
    
    # make_data()  # Insert sample data

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=on_scroll)
    scrollbar.grid(row=7,column=3,sticky="nse",pady=85,padx=0,rowspan=1000)
    # Link the scrollbar to the Treeview widget
    date_amt_box.configure(yscrollcommand=scrollbar.set)

    win.mainloop()


if  __name__ == "__main__":
    salarypg()