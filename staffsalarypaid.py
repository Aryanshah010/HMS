from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL  import Image , ImageTk
from tkmacosx import Button
import datetime
import menu

def salarypg():

    # def make_data():
    #     # Insert some sample data into the Treeview
    #     for i in range(1, 1000):
    #         date_amt_box.insert("", "end", values=("2024-02-" + str(i), str(i * 100)))

    def on_scroll(*args):
        date_amt_box.yview(*args)
    
    
    def menupg():
        win.destroy()
        menu.dashboard()

    def fill_current_date(event):
        current_date = datetime.datetime.now().strftime("%Y/%m/%d")
        Monthentry.delete(0, END)
        Monthentry.insert(0, current_date)


    def onclick():
        tk.messagebox.showinfo("","Staff salary payment is saved!")

    win=tk.Tk()
    win.resizable(0,0)
    win.title("STAFF Salary")

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

    search_button = Button(win, text="Search", bg="#00C8D8",fg="white",font="verdana 14",image=search_icon, borderless=1,compound="left")
    search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')

    save_btn = Button(win, text="Save", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=onclick)
    save_btn.place(x=20,y=350)

    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 14 bold",borderless=1,command=menupg)
    back_btn.place(x=143,y=350)

    style = ttk.Style()
    style.theme_use("clam")


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