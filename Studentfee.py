from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
import datetime
import menu
import sqlite3

def initialize_database():
    try:
        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (
                        payment_id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        date_paid DATE,
                        amount_paid INTEGER,
                        FOREIGN KEY (student_id) REFERENCES Students (std_id)
                    )''')

        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def feespg():
    initialize_database()

    def search_student():
        student_id = S_Id_entry.get()
        if not student_id:
            messagebox.showerror("Error", "Please enter a student ID.")
            return

        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Students WHERE std_id=?", (student_id,))
            student_data = cursor.fetchone()
            conn.close()

            if student_data:
                Firstnameentry.delete(0, 'end')
                Firstnameentry.insert(0, student_data[2])
                Middlenameentry.delete(0, 'end')
                Middlenameentry.insert(0, student_data[3])
                Lastnameentry.delete(0, 'end')
                Lastnameentry.insert(0, student_data[4])
                phoneentry.delete(0, 'end')
                phoneentry.insert(0, student_data[5])
                Roomnumberentry.delete(0, 'end')
                Roomnumberentry.insert(0, student_data[8])
                roomtypeentry.delete(0, 'end')
                roomtypeentry.insert(0, student_data[9])

                # Clear existing records in the treeview
                clear_treeview()

                # Load and display fee records for this student
                load_fee_records(student_id)
            else:
                messagebox.showerror("Error", "Student not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_treeview():
        date_amt_box.delete(*date_amt_box.get_children())

    def load_fee_records(student_id):
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("SELECT date_paid, amount_paid FROM Payments WHERE student_id=?", (student_id,))
            fee_records = cursor.fetchall()
            conn.close()

            for record in fee_records:
                # Explicitly convert amount to integer and then to string
                amount_paid_str = str(int(record[1]))
                date_amt_box.insert("", "end", values=(record[0], amount_paid_str))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_fee_record():
        try:
            # Get student ID and fee details
            student_id = S_Id_entry.get()
            date_paid = Monthentry.get()
            amount_paid_str = AmountPaidentry.get()

            # Check if all fields are filled
            if not student_id or not date_paid or not amount_paid_str:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            # Convert amount to integer
            try:
                amount_paid = int(amount_paid_str)
            except ValueError:
                messagebox.showerror("Error", "Amount must be a valid integer.")
                return

            # Save the fee record in the database
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Payments (student_id, date_paid, amount_paid) VALUES (?, ?, ?)", (student_id, date_paid, amount_paid))
            conn.commit()
            conn.close()

            # Update the treeview to reflect the new fee record
            date_amt_box.insert("", "end", values=(date_paid, amount_paid))

            # Show a success message
            y = messagebox.askyesno("", "Do you want to save the fee of this student?")
            if y:
                r = messagebox.showinfo("", "Student fee saved successfully!")
                if r:
                    menupg()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def on_scroll(*args):
        date_amt_box.yview(*args)

    def menupg():
        win.destroy()
        menu.dashboard()

    def fill_current_date(event):
        current_date = datetime.datetime.now().strftime("%Y/%m/%d")
        Monthentry.delete(0, END)
        Monthentry.insert(0, current_date)

    win = tk.Tk()
    win.resizable(0, 0)
    win.title("STUDENT FEE")

    window_width = 535
    window_height = 710

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    S_Id = Label(win, text="S-ID :")
    S_Id.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    S_Id_entry = Entry(win)
    S_Id_entry.grid(row=0, column=1, padx=10, pady=10)

    Firstname = Label(win, text="First Name :")
    Firstname.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    Firstnameentry = Entry(win)
    Firstnameentry.grid(row=1, column=1, padx=10, pady=10)

    Middlename = Label(win, text="Middle Name :")
    Middlename.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    Middlenameentry = Entry(win)
    Middlenameentry.grid(row=2, column=1, padx=10, pady=10)

    Lastname = Label(win, text="Last Name :")
    Lastname.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    Lastnameentry = Entry(win)
    Lastnameentry.grid(row=3, column=1, padx=10, pady=10)

    phone = Label(win, text="Phone Number:")
    phone.grid(row=4, column=0, sticky="w", padx=10, pady=10)

    phoneentry = Entry(win)
    phoneentry.grid(row=4, column=1)

    Roomnumber = Label(win, text="Room Number :")
    Roomnumber.grid(row=5, column=0, sticky="w", padx=10, pady=10)

    Roomnumberentry = Entry(win)
    Roomnumberentry.grid(row=5, column=1, padx=10, pady=10)

    roomtype = Label(win, text="Beds:")
    roomtype.grid(row=6, column=0, sticky="w", padx=10, pady=10)

    roomtypeentry = Entry(win)
    roomtypeentry.grid(row=6, column=1)

    Month = Label(win, text="Date of payment received:")
    Month.grid(row=7, column=0, sticky="w", padx=10, pady=10)

    Monthentry = Entry(win)
    Monthentry.grid(row=7, column=1, padx=10, pady=10)

    Monthentry.bind("<Button-1>", fill_current_date)
    Monthentry.bind("<ButtonRelease-1>", fill_current_date)

    AmountPaid = Label(win, text="FEE Received:")
    AmountPaid.grid(row=8, column=0, sticky="w", padx=10, pady=10)

    AmountPaidentry = Entry(win)
    AmountPaidentry.grid(row=8, column=1, padx=10, pady=10)

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))
    search_icon = ImageTk.PhotoImage(icon_image)

    search_button = Button(win, text="Search", bg="#00C8D8", fg="white", image=search_icon, borderless=1,
                           compound="left", command=search_student)
    search_button.grid(row=0, column=3, pady=10, padx=10, sticky='w')

    save_btn = Button(win, text="Save", bg="#FF7F24", font="verdana 14 bold", borderless=1,
                      command=save_fee_record)
    save_btn.place(x=20, y=440)

    back_btn = Button(win, text="Back", bg="#DA00D6", font="verdana 14 bold", borderless=1, command=menupg)
    back_btn.place(x=145, y=440)

    date_amt_box = ttk.Treeview(win)
    date_amt_box['columns'] = ("Date", "Amount")
    date_amt_box.column("#0", width=0, stretch=NO)
    date_amt_box.column("Date", anchor=CENTER, width=200, minwidth=200)
    date_amt_box.column("Amount", anchor=CENTER, width=200, minwidth=200)

    date_amt_box.heading("#0", text="", anchor=CENTER)
    date_amt_box.heading("Date", text="Date", anchor=CENTER)
    date_amt_box.heading("Amount", text="Amount", anchor=CENTER)

    date_amt_box.grid(row=9, column=0, columnspan=4, pady=60, sticky="nsew")

    scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=on_scroll)
    scrollbar.grid(row=9, column=3, sticky="nse", pady=85, rowspan=100)
    date_amt_box.configure(yscrollcommand=scrollbar.set)

    win.mainloop()

if __name__ == "__main__":
    feespg()
