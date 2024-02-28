from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import messagebox
import homepage
import sqlite3

def new_acc():

    def create_table():
        try:
            conn = sqlite3.connect('hostel.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS adminLogin
                        (username TEXT PRIMARY KEY, password TEXT)''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error occurred while creating table:", e)

    create_table()

    def insert_user(username, password):
        try:
            conn = sqlite3.connect('hostel.db')
            c = conn.cursor()
            c.execute("INSERT INTO adminLogin (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error occurred:", e)

    def validate_login(username, password):
        conn = sqlite3.connect('hostel.db')
        c = conn.cursor()
        c.execute("SELECT * FROM adminLogin WHERE username = ? AND password = ?", (username, password))
        result = c.fetchone()
        conn.close()
        return result is not None
    
    def validate_sigin():
        username = username_name.get()
        password = password_name.get()
        confirm = comform_password.get()
        
        # Check if any field is empty
        if username==default_username_text or password ==default_password_text or comform_password==default_comform_text:
            messagebox.showerror("Error", "Please fill all the Entries.")
        else:
            if password != confirm:
                messagebox.showerror("Error", "Password and Confirm Password do not match.")
            else:
                # Check if username already exists
                if validate_existing_username(username):
                    messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                    return
                # Call insert_user() to insert new user data into the database
                insert_user(username, password)
                messagebox.showinfo("Success", "Account created successfully!")
                # Redirect to home page
                home()

    def validate_existing_username(username):
        conn = sqlite3.connect('hostel.db')
        c = conn.cursor()
        c.execute("SELECT * FROM adminLogin WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        return result is not None
    

    
    def home():
        window.destroy()
        homepage.main()

    def validate_sigin():
        username = username_name.get()
        password = password_name.get()
        confirm=comform_password.get()
        if username == default_username_text or password == default_password_text or confirm ==default_comform_text:
            messagebox.showerror("Error", "Please fill all the Entries.")

        else:
            if password != confirm:
                messagebox.showerror("Error", "Password and Confirm Password do not match.")
            else:
                # Check if username already exists
                if validate_existing_username(username):
                    messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                    return
                # Call insert_user() to insert new user data into the database
                insert_user(username, password)
                messagebox.showinfo("Success", "Account created successfully!")
                # Redirect to home page
                home()
    

    def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def on_focus_out(event, entry_widget, default_text):
        if not entry_widget.get():
            entry_widget.insert(0, default_text)
            entry_widget.config(fg="black")

    window = tk.Tk()
    window.title("REGISTER")
    window.resizable(0, 0)
    window.configure(bg="purple")
    window_width = 600
    window_height = 430

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    
    # Load the images
    # User logo
    user_icon = Image.open("user_logo.png")
    user_icon = user_icon.resize((30, 30), Image.BICUBIC)  
    user_icon = ImageTk.PhotoImage(user_icon)

    # lock logo
    lock_icon = Image.open("locked.png")
    lock_icon = lock_icon.resize((30, 30), Image.BICUBIC) 
    lock_icon = ImageTk.PhotoImage(lock_icon)

    # Hostel Image
    img = Image.open("hostel_logo.jpg")
    img = img.resize((210, 210), Image.BICUBIC)  
    new_logo = ImageTk.PhotoImage(img)
    image = Label(image=new_logo, border=0)
    image.grid(row=0, column=0, sticky="w", padx=40, pady=110)

    # Create Labels to display icons
    user_icon_label = Label(window, image=user_icon, border=0)
    user_icon_label.place(x=320, y=120)

    lock_icon_label = Label(window, image=lock_icon, border=0)
    lock_icon_label.place(x=320, y=190)

    default_username_text = "Create Username"
    default_password_text = "Create Password"
    default_comform_text="Confirm Password"

    # Create Entry widgets
    username_name = Entry(window, width=15, bg="#D9D9D9", fg="black", font=("verdana", 16), insertbackground="black",
                        insertwidth=2)
    username_name.insert(0,default_username_text)
    username_name.bind("<FocusIn>", lambda event: on_entry_click(event, username_name, default_username_text))
    username_name.bind("<FocusOut>", lambda event: on_focus_out(event, username_name, default_username_text))
    username_name.place(x=360, y=120)


    password_name = Entry(window, width=15, bg="#D9D9D9", fg="black", font=("verdana", 16), insertbackground="black",
                        insertwidth=2)
    password_name.insert(0, default_password_text)
    password_name.bind("<FocusIn>", lambda event: on_entry_click(event, password_name, default_password_text))
    password_name.bind("<FocusOut>", lambda event: on_focus_out(event, password_name, default_password_text))
    password_name.place(x=360, y=190)

    comform_password=Entry(window, width=15, bg="#D9D9D9", fg="black", font=("verdana", 16), insertbackground="black",
                        insertwidth=2)
    comform_password.insert(0,default_comform_text)
    comform_password.bind("<FocusIn>", lambda event: on_entry_click(event, comform_password, default_comform_text))
    comform_password.bind("<FocusOut>", lambda event: on_focus_out(event, comform_password, default_comform_text))
    comform_password.place(x=360, y=250)

    create_btn = Button(window, text="Create", width=100, height=30, bg="#00C412", fg="black", font=("verdana 15"),borderless=1,command=validate_sigin)  
    create_btn.place(x=325,y=330)

    back_btn = Button(window, text="Back", width=100, height=30, bg="#F33400", fg="black", font=("verdana 15"),borderless=1,command=home)  
    back_btn.place(x=440,y=330)

    window.mainloop()


if  __name__ == "__main__":
    new_acc()