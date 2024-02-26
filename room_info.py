from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkmacosx import Button
import menu
import sqlite3

def roominfopg():

    def fetch_room_info():
        conn = sqlite3.connect('hostel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT room_number, room_status, beds, building, total_fees FROM Rooms")
        room_info = cursor.fetchall()
        conn.close()
        return room_info

    def on_scroll(*args):
        roomTree.yview(*args)
    
    def menupg():
        win.destroy()
        menu.dashboard()

    win=tk.Tk()
    win.resizable(0,0)
    win.title("ALL ROOM INFO")

    window_width = 690
    window_height = 270

    # get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(win)
    frame.pack(pady=10)


    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)
   
    roomTree = ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set)

    ver_scroll_bar.config(command=roomTree.yview)
   
    roomTree['columns'] = ("Room No", "Room status","Seats","Building","Fees")
    roomTree.column("#0", width=0, minwidth=0)  
    roomTree.column("Room No", anchor=CENTER, width=140, minwidth=140)
    roomTree.column("Room status", anchor=CENTER, width=140, minwidth=140)
    roomTree.column("Seats", anchor=CENTER, width=100, minwidth=100)
    roomTree.column("Building", anchor=CENTER, width=140, minwidth=140)
    roomTree.column("Fees", anchor=CENTER, width=140, minwidth=140)

    
    roomTree.heading("#0", text="", anchor=CENTER)
    roomTree.heading("Room No", text="Room No", anchor=CENTER)
    roomTree.heading("Room status", text="Room status", anchor=CENTER)
    roomTree.heading("Seats", text="Seats", anchor=CENTER)
    roomTree.heading("Building", text="Building", anchor=CENTER)
    roomTree.heading("Fees", text="Fees", anchor=CENTER)

    roomTree.pack(padx=2)

    room_info = fetch_room_info()

    # Add room information to the Treeview
    for room in room_info:
        roomTree.insert('', 'end', values=room)
    
    
    back_btn=Button(win,text="Back",bg="#DA00D6",font="verdana 15 bold",borderless=1,command=menupg)
    back_btn.place(x=560,y=225)

    win.mainloop()

if __name__=="__main__":
    roominfopg()
