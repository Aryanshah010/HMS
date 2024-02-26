from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk,ImageFilter
from tkmacosx import Button
from tkinter import messagebox
import homepage
import sqlite3


def std_mainpg():
  
    def home():
        window.destroy()
        homepage.main()

    def validate_signin():
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()

            # Retrieve student ID and phone number from the entry widgets
            phone_number = username_name.get()
            std_id = password_name.get()

            # Query the Students table for the provided credentials
            cursor.execute("SELECT * FROM Students WHERE Phone_Number=? AND std_id=?", (phone_number, std_id))
            student_data = cursor.fetchone()

            conn.close()

            if student_data:
                window.destroy()
                std_menupg(student_data[0])
            else:
                messagebox.showerror("Login Error", "Invalid phone number or student ID.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def on_focus_out(event, entry_widget, default_text):
        if not entry_widget.get():
            entry_widget.insert(0, default_text)
            entry_widget.config(fg="black")

    window = tk.Tk()
    window.title("STUDENT LOGIN")
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


    default_username_text = "Phone Number"
    default_password_text = "Student ID"

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

    sign_btn = Button(window, text="Sign In", width=100, height=30, bg="#00C412", fg="black", font=('verdana', 15),
                    borderless=1,command=validate_signin)  
    sign_btn.place(x=320,y=275)

    back_btn = Button(window, text="Back", width=100, height=30, bg="#F33400", fg="black", font=("verdana 15"),borderless=1,command=home)
    back_btn.place(x=435,y=275)
    
    window.mainloop()



def std_menupg(student_id): 

    def homepg():
        y=messagebox.askyesno("","DO YOU WANT TO LOGOUT?")
        if y:
            window.destroy()
            homepage.main()
            
    def ck_fee(student_id):
        window.destroy()
        fees(student_id)

    def infopg(student_id):
        window.destroy()
        myinfopg(student_id)

    def fm(student_id):
        window.destroy()
        foodM(student_id)

    window = tk.Tk()
    window.title("MENU")
    window.resizable(0,0)
    window_width = 730
    window_height = 310
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Function to blur the image and resize it
    def blur_and_resize_image(image_path, blur_radius, size):
        image = Image.open(image_path)
        # Resize the image
        image = image.resize(size)
        # Apply Gaussian blur
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
        return blurred_image

    # Blur the image and set its size
    background_image = blur_and_resize_image("hostelBuilding.jpg", blur_radius=4,size=(580,590))

    # Convert the image to a Tkinter PhotoImage using ImageTk
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = ttk.Label(window, image=background_photo)
    background_label.place(x=198, y=0, relwidth=1, relheight=1)

    menu_frame=tk.Frame(window,bg="#00D4FF",width=115)
    menu_frame.grid(row=0,column=0,sticky="w")

    menu_label=tk.Label(menu_frame,text="DASHBOARD",fg="#D76500",bg="#00D4FF",font="verdana 20 bold underline")
    menu_label.grid(row=0,column=0,sticky="w",padx=14,pady=5)

    fees_btn=Button(menu_frame,width=200,height=70,text="Check Fees",bg="#00B203",font="verdana 15 bold",borderless=1,command=lambda: ck_fee(student_id))
    fees_btn.grid(row=1,column=0,pady=10)

    std_info_btn=Button(menu_frame,width=200,height=70,text="My Info",bg="#00B203",font="verdana 15 bold",borderless=1,command=lambda: infopg(student_id))
    std_info_btn.grid(row=2,column=0,pady=10)

    food_btn=Button(menu_frame,width=200,height=70,text="Food Menu",bg="#00B203",font="verdana 15 bold",borderless=1,command=lambda: fm(student_id))
    food_btn.grid(row=3,column=0,pady=10)


    logout_btn=Button(window,text="Logout",bg="red",font="verdana 15 bold",borderless=1,command=homepg)
    logout_btn.place(x=610,y=270)


    window.mainloop()



def fees(student_id):

    def fetch_fee_records(student_id):
        try:
            conn = sqlite3.connect('hostel.db')
            cursor = conn.cursor()
            cursor.execute("SELECT date_paid, amount_paid FROM Payments WHERE student_id=?", (student_id,))
            fee_records = cursor.fetchall()
            conn.close()
            return fee_records
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching fee records: {str(e)}")
            return []
     
    def on_scroll(*args):
        date_amt_box.yview(*args)

    def stdmenupg(student_id):
        window.destroy()
        std_menupg(student_id)

    window = tk.Tk()
    window.title("FEE RECORD")
    window.resizable(0,0)
    window_width = 500
    window_height = 260
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(window)
    frame.pack(pady=5)

    # scroll bar
    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)


    date_amt_box = ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set)
    ver_scroll_bar.config(command=date_amt_box.yview)

    # defining columns
    date_amt_box['columns'] = ("Date", "Amount")
    date_amt_box.column("#0", width=0, minwidth=0)  
    date_amt_box.column("Date", anchor=CENTER, width=250, minwidth=250)
    date_amt_box.column("Amount", anchor=CENTER, width=250, minwidth=250)
    
    date_amt_box.heading("#0", text="", anchor=CENTER)
    date_amt_box.heading("Date", text="Date", anchor=CENTER)
    date_amt_box.heading("Amount", text="Amount", anchor=CENTER)
    
    date_amt_box.pack(padx=2)

    fee_records = fetch_fee_records(student_id)
    for record in fee_records:
        date_amt_box.insert("", "end", values=record)

    back_btn = Button(window, text="Back", width=100, height=30, bg="#F33400", fg="black", font=("verdana 13 bold"),borderless=1,command=lambda: stdmenupg(student_id))
    back_btn.place(x=385,y=220)

    window.mainloop()


def myinfopg(student_id):

    def stdmenupage(student_id):
        win.destroy()
        std_menupg(student_id)

    conn = sqlite3.connect('hostel.db')
    cursor = conn.cursor()

    # Retrieve student's information based on the provided ID
    cursor.execute("SELECT * FROM Students WHERE std_id=?", (student_id,))
    student_data = cursor.fetchone()

    conn.close()

    win=tk.Tk()
    win.title("MY INFO")
    win.resizable(0,0)

    window_width = 430
    window_height = 700

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # ALL INFO OF STUDENT

    std_id=Label(win,text="S-ID:")
    std_id.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    std_id_entry=Entry(win)
    std_id_entry.grid(row=0,column=1)
    std_id_entry.insert(0, student_data[0])

    date_label=Label(win,text="Date of Admission:")
    date_label.grid(row=1,column=0,sticky="w",padx=10,pady=10)

    date_value = Entry(win)
    date_value.grid(row=1, column=1)
    date_value.insert(0, student_data[1])

    std_first=Label(win,text="First Name:")
    std_first.grid(row=2,column=0,sticky="w",padx=10,pady=10)

    std_first_entry=Entry(win)
    std_first_entry.grid(row=2,column=1)
    std_first_entry.insert(0,student_data[2])


    std_middle=Label(win,text="Middle Name:")
    std_middle.grid(row=3,column=0,sticky="w",padx=10,pady=10)

    std_middle_entry=Entry(win)
    std_middle_entry.grid(row=3,column=1)
    std_middle_entry.insert(0, student_data[3])

    std_last=Label(win,text="Last Name:")
    std_last.grid(row=4,column=0,sticky="w",padx=10,pady=10)

    std_last_entry=Entry(win)
    std_last_entry.grid(row=4,column=1)
    std_last_entry.insert(0, student_data[4])

    std_phone=Label(win,text="Phone Number:")
    std_phone.grid(row=5,column=0,sticky="w",padx=10,pady=10)

    std_phone_entry=Entry(win)
    std_phone_entry.grid(row=5,column=1)
    std_phone_entry.insert(0, student_data[5])

    std_address=Label(win,text="Address:")
    std_address.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    std_address_entry=Entry(win)
    std_address_entry.grid(row=6,column=1)
    std_address_entry.insert(0, student_data[6])

    building_label=Label(win,text="Building:")
    building_label.grid(row=7,column=0,sticky="w",padx=10,pady=10)

    building_entry=Entry(win)
    building_entry.grid(row=7,column=1)
    building_entry.insert(0,student_data[7])

    room_num=Label(win,text="Room Number:")
    room_num.grid(row=8,column=0,sticky="w",padx=10,pady=10)

    room_num_entry=Entry(win)
    room_num_entry.grid(row=8,column=1)
    room_num_entry.insert(0,student_data[8])

    room_price=Label(win,text="Total Fees:")
    room_price.grid(row=9,column=0,sticky="w",padx=10,pady=10)

    room_price_entry=Entry(win)
    room_price_entry.grid(row=9,column=1)
    room_price_entry.insert(0,student_data[10])

    guardian_first=Label(win,text="G First Name:")
    guardian_first.grid(row=10,column=0,sticky="w",padx=10,pady=10)

    guardian_first_entry=Entry(win)
    guardian_first_entry.grid(row=10,column=1)
    guardian_first_entry.insert(0,student_data[11])

    guardian_middle=Label(win,text="G Middle Name:")
    guardian_middle.grid(row=11,column=0,sticky="w",padx=10,pady=10)

    guardian_middle_entry=Entry(win)
    guardian_middle_entry.grid(row=11,column=1)
    guardian_middle_entry.insert(0,student_data[12])

    guardian_last=Label(win,text="G Last Name:")
    guardian_last.grid(row=12,column=0,sticky="w",padx=10,pady=10)

    guardian_last_entry=Entry(win)
    guardian_last_entry.grid(row=12,column=1)
    guardian_last_entry.insert(0,student_data[13])

    guardian_phone=Label(win,text="G Phone Number:")
    guardian_phone.grid(row=13,column=0,sticky="w",padx=10,pady=10)

    guardian_phone_entry=Entry(win)
    guardian_phone_entry.grid(row=13,column=1)
    guardian_phone_entry.insert(0,student_data[14])

    guardian_address=Label(win,text="G Address:")
    guardian_address.grid(row=14,column=0,sticky="w",padx=10,pady=10)

    guardian_address_entry=Entry(win)
    guardian_address_entry.grid(row=14,column=1)
    guardian_address_entry.insert(0,student_data[15])

    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 15 bold",borderless=1,command=lambda: stdmenupage(student_id))
    back_btn.place(x=10,y=650)
    

    win.mainloop()


def foodM(student_id):

    def stdMenu(student_id):
        window.destroy()
        std_menupg(student_id)

    window = tk.Tk()
    window.title("FOOD MENU")
    window.resizable(0,0)
    window_width = 630
    window_height = 650

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    img = Image.open("foodMenu.jpg")
    img = img.resize((600, 600), Image.BICUBIC)  
    FoodMenu = ImageTk.PhotoImage(img)
    image = Label(image=FoodMenu, border=0)
    image.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

    back_btn=Button(window,text="Back",bg="#DA00D6",font="verdana 15 bold",command=lambda: stdMenu(student_id))
    back_btn.place(x=10,y=615)



    window.mainloop()


if __name__=="__main__":
    std_mainpg()