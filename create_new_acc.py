from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import messagebox
import homepage

def new_acc():
    
    def home():
        window.destroy()
        homepage.main()

    def validate_sigin():
        username = username_name.get()
        password = password_name.get()
        confirm=comform_password.get()
        if username == default_username_text or password == default_password_text or confirm ==default_comform_text:
            messagebox.showerror("Error", "Please fill all the Entries.")
    

    def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def on_focus_out(event, entry_widget, default_text):
        if not entry_widget.get():
            entry_widget.insert(0, default_text)
            entry_widget.config(fg="black")

    window = tk.Tk()
    window.title("LOGIN")
    window.geometry("600x430")
    window.resizable(0, 0)
    window.configure(bg="purple")
    
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