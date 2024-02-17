from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkmacosx import Button
import std_menu

def stdinfopg():

    def dashpg():
        window.destroy()
        std_menu.dashboard()

    def on_scroll(*args):
        std_info.yview(*args)

    window = tk.Tk()
    window.title("STAFF INFO")
    window.resizable(0,0)
    window_width = 1000
    window_height = 310
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(window)
    frame.pack(side=TOP,padx=10,pady=15,fill=X)

    # scroll bar
    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)

    hor_scroll_bar=ttk.Scrollbar(frame, orient=HORIZONTAL)
    hor_scroll_bar.pack(side=BOTTOM,fill=X)
    
    # Treeview

    std_info=ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set,xscrollcommand=hor_scroll_bar.set,show="headings")

    ver_scroll_bar.config(command=std_info.yview)

    hor_scroll_bar.config(command=std_info.xview)

    # defining columns
    std_info["columns"]=("First Name","Last Name","Ph No","Staff Address","Date Of Join","Post","Salary")

    std_info.column("#0",width=0,minwidth=0)
    std_info.column("First Name",anchor="w",width=100,minwidth=130)
    std_info.column("Last Name",anchor="w",width=100,minwidth=130)
    std_info.column("Ph No",anchor="w",width=105,minwidth=105)
    std_info.column("Staff Address",anchor="w",width=140,minwidth=140)
    std_info.column("Date Of Join",anchor="w",width=60,minwidth=65)
    std_info.column("Post",anchor="w",width=60,minwidth=65)
    std_info.column("Salary",anchor="w",width=75,minwidth=75)

    std_info.heading("#0",text="",anchor="w")
    std_info.heading("First Name",text="First Name",anchor="w")
    std_info.heading("Last Name",text="Last Name",anchor="w")
    std_info.heading("Ph No",text="Ph No",anchor="w")
    std_info.heading("Staff Address",text="Std Address",anchor="w")
    std_info.heading("Date Of Join",text="Date Of Join",anchor="w")
    std_info.heading("Post",text="Post",anchor="w")
    std_info.heading("Salary",text="Salary",anchor="w")

    std_info.pack(padx=2,pady=7,fill=X)

    back_btn=Button(window,text="Back",width=130,bg="#DA00D6",font="verdana 15 bold",command=dashpg)
    back_btn.place(x=785,y=275)

   
    window.mainloop()

if __name__=="__main__":
    stdinfopg()