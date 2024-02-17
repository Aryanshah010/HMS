from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkmacosx import Button
import menu


def staffinfo():

    def dashpg():
        window.destroy()
        menu.dashboard()

    def on_scroll(*args):
        std_info.yview(*args)

    window = tk.Tk()
    window.title("STAFF INFO")
    window.resizable(0,0)
    window_width = 950
    window_height = 280
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(window)
    frame.pack(pady=10)

    # scroll bar
    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)

    # Treeview

    std_info=ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set)

    ver_scroll_bar.config(command=std_info.yview)

    # defining columns
    std_info["columns"]=("First Name","Middle Name","Last Name","Ph No","Address","Date of Join","Post","Salary")

    std_info.column("#0",width=0,minwidth=0)
    std_info.column("First Name",anchor=CENTER,width=100,minwidth=100)
    std_info.column("Middle Name",anchor=CENTER,width=100,minwidth=100)
    std_info.column("Last Name",anchor=CENTER,width=100,minwidth=100)
    std_info.column("Ph No",anchor=CENTER,width=105,minwidth=105)
    std_info.column("Address",anchor=CENTER,width=140,minwidth=140)
    std_info.column("Date of Join",anchor=CENTER,width=160,minwidth=160)
    std_info.column("Post",anchor=CENTER,width=100,minwidth=100)
    std_info.column("Salary",anchor=CENTER,width=100,minwidth=100)

    std_info.heading("#0",text="",anchor=CENTER)
    std_info.heading("First Name",text="First Name",anchor=CENTER)
    std_info.heading("Middle Name",text="Middle Name",anchor=CENTER)
    std_info.heading("Last Name",text="Last Name",anchor=CENTER)
    std_info.heading("Ph No",text="Ph No",anchor=CENTER)
    std_info.heading("Address",text="Address",anchor=CENTER)
    std_info.heading("Date of Join",text="Date of Join",anchor=CENTER)
    std_info.heading("Post",text="Post",anchor=CENTER)
    std_info.heading("Salary",text="Salary",anchor=CENTER)

    std_info.pack(padx=2)

    back_btn=Button(window,text="Back",width=130,bg="#DA00D6",font="verdana 14 bold",command=dashpg)
    back_btn.place(x=790,y=235)
   
    window.mainloop()

if __name__=="__main__":
    staffinfo()