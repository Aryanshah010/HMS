from tkinter import *
import tkinter as tk
from tkmacosx import Button
import std_menu

def myinfopg():

    def stdmenupage():
        win.destroy()
        std_menu.std_menupg()

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

    date_label=Label(win,text="Date of Admission:")
    date_label.grid(row=1,column=0,sticky="w",padx=10,pady=10)

    date_value = Entry(win)
    date_value.grid(row=1, column=1)

    std_first=Label(win,text="First Name:")
    std_first.grid(row=2,column=0,sticky="w",padx=10,pady=10)


    std_first_entry=Entry(win)
    std_first_entry.grid(row=2,column=1)

    std_middle=Label(win,text="Middle Name:")
    std_middle.grid(row=3,column=0,sticky="w",padx=10,pady=10)

    std_middle_entry=Entry(win)
    std_middle_entry.grid(row=3,column=1)

    std_last=Label(win,text="Last Name:")
    std_last.grid(row=4,column=0,sticky="w",padx=10,pady=10)

    std_last_entry=Entry(win)
    std_last_entry.grid(row=4,column=1)

    std_phone=Label(win,text="Phone Number:")
    std_phone.grid(row=5,column=0,sticky="w",padx=10,pady=10)

    std_phone_entry=Entry(win)
    std_phone_entry.grid(row=5,column=1)

    std_address=Label(win,text="Address:")
    std_address.grid(row=6,column=0,sticky="w",padx=10,pady=10)

    std_address_entry=Entry(win)
    std_address_entry.grid(row=6,column=1)

    building_label=Label(win,text="Building:")
    building_label.grid(row=7,column=0,sticky="w",padx=10,pady=10)

    building_entry=Entry(win)
    building_entry.grid(row=7,column=1)

    room_num=Label(win,text="Room Number:")
    room_num.grid(row=8,column=0,sticky="w",padx=10,pady=10)

    room_num_entry=Entry(win)
    room_num_entry.grid(row=8,column=1)

    room_price=Label(win,text="Total Fees:")
    room_price.grid(row=9,column=0,sticky="w",padx=10,pady=10)

    room_price_entry=Entry(win)
    room_price_entry.grid(row=9,column=1)

    guardian_first=Label(win,text="G First Name:")
    guardian_first.grid(row=10,column=0,sticky="w",padx=10,pady=10)

    guardian_first_entry=Entry(win)
    guardian_first_entry.grid(row=10,column=1)

    guardian_middle=Label(win,text="G Middle Name:")
    guardian_middle.grid(row=11,column=0,sticky="w",padx=10,pady=10)

    guardian_middle_entry=Entry(win)
    guardian_middle_entry.grid(row=11,column=1)

    guardian_last=Label(win,text="G Last Name:")
    guardian_last.grid(row=12,column=0,sticky="w",padx=10,pady=10)

    guardian_last_entry=Entry(win)
    guardian_last_entry.grid(row=12,column=1)

    guardian_phone=Label(win,text="G Phone Number:")
    guardian_phone.grid(row=13,column=0,sticky="w",padx=10,pady=10)

    guardian_phone_entry=Entry(win)
    guardian_phone_entry.grid(row=13,column=1)

    guardian_address=Label(win,text="G Address:")
    guardian_address.grid(row=14,column=0,sticky="w",padx=10,pady=10)

    guardian_address_entry=Entry(win)
    guardian_address_entry.grid(row=14,column=1)

    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 15 bold",borderless=1,command=stdmenupage)
    back_btn.place(x=10,y=650)
    

    win.mainloop()


   
if __name__=="__main__":
    myinfopg()

































