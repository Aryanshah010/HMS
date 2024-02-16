from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL  import Image , ImageTk
from tkmacosx import Button
import datetime
import menu

def feespg():

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
        save=tk.messagebox.askyesno("","DO YOU WANT TO SAVE FEE OF THIS STUDENT!")
        if save:
            tk.messagebox.showinfo("","Student FEE saved successfully!")
        else:
            tk.messagebox.showinfo("","FEE Cancled!")
            

    win=tk.Tk()
    win.resizable(0,0)
    win.title("STUDENT FEE")

    window_width = 535
    window_height = 630

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    S_Id =Label(win,text="S-ID :")
    S_Id.grid(row=0,column=0,sticky="w",padx=10,pady=10)

    S_Id_entry=Entry(win)
    S_Id_entry.grid(row=0,column=1,padx=10,pady=10)


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

    Roomnumber = Label(win,text="Room Number :")
    Roomnumber.grid(row=4,column=0 ,sticky="w",padx=10,pady=10)


    Roomnumberentry =Entry(win)
    Roomnumberentry.grid(row=4,column=1,padx=10,pady=10)

    Month =Label(win,text="Date of payment received:")
    Month.grid(row=5,column=0 ,sticky="w",padx=10,pady=10)

    Monthentry =Entry(win)
    Monthentry.grid(row=5,column=1,padx=10,pady=10)

    Monthentry.bind("<Button-1>", fill_current_date)
    Monthentry.bind("<ButtonRelease-1>", fill_current_date)


    AmountPaid =Label(win,text="FEE Received:")
    AmountPaid.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    AmountPaidentry =Entry(win)
    AmountPaidentry.grid(row=6,column=1,padx=10,pady=10)

    icon_image = Image.open("searchicon.png")
    icon_image = icon_image.resize((16, 16))  
    search_icon = ImageTk.PhotoImage(icon_image)

    search_button = Button(win, text="Search", bg="#00C8D8",fg="white",image=search_icon, borderless=1,compound="left")
    search_button.grid(row=0,column=3,pady=10,padx=10, sticky='w')

    save_btn = Button(win, text="Save", bg="#FF7F24",font="verdana 14 bold",borderless=1,command=onclick)
    save_btn.place(x=20,y=350)

    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 14 bold",borderless=1,command=menupg)
    back_btn.place(x=143,y=350)
    
    # salary paid record
    date_amt_box = ttk.Treeview(win)
    # defining columns
    date_amt_box['columns'] = ("Date", "Amount")
    date_amt_box.column("#0", width=0, stretch=NO)  # Set width to 0 and stretch to NO
    date_amt_box.column("Date", anchor=CENTER, width=200, minwidth=200)
    date_amt_box.column("Amount", anchor=CENTER, width=200, minwidth=200)
    
    date_amt_box.heading("#0", text="", anchor=CENTER)
    date_amt_box.heading("Date", text="Date", anchor=CENTER)
    date_amt_box.heading("Amount", text="Amount", anchor=CENTER)
    
    # Place the salary paid record at the bottom
    date_amt_box.grid(row=7, column=0, columnspan=4, pady=60, sticky="nsew")
    
    # make_data()  # Insert sample data

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=on_scroll)
    scrollbar.grid(row=7,column=3,sticky="nse",pady=85,padx=0,rowspan=100)
    # Link the scrollbar to the Treeview widget
    date_amt_box.configure(yscrollcommand=scrollbar.set)
  

    win.mainloop()


if  __name__ == "__main__":
    feespg()